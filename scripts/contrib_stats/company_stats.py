#!/usr/bin/env python3
"""
贡献统计脚本
运行在 contrib-stats 分支，从主开发分支 rvck-6.6 获取数据进行分析
默认数据统计范围是最新提交至向后找到的第一个 tag 节点
"""

import subprocess
import re
import os
import sys
import json
import argparse
import tempfile
import urllib.parse
import shutil
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path

def beijing_timestamp():
    """返回北京时间字符串"""

    # 获取当前UTC时间
    utc_now = datetime.utcnow()
    # 转换为北京时间
    bj_time = utc_now + timedelta(hours=8)
    return bj_time.strftime("%Y-%m-%d %H:%M:%S")

class ContribStats:
    def __init__(self, main_branch="rvck-6.6", stats_branch="contrib-stats", remote_url=None):
        self.main_branch = main_branch
        self.stats_branch = stats_branch
        self.remote_url = remote_url or f"https://github.com/{os.environ.get('GITHUB_REPOSITORY', '')}.git"
        self.repo_path = Path(".").absolute()

        # 配置参数
        self.clone_depth = 3000  # 默认克隆深度，rvck 贡献量超过该数值时需要更新
        self.fallback_count = 1000  # 未找到 tag 时的默认统计数量

        # 机构配置
        self.companies = {
            "超睿科技": {
                "suffixes": ["@ultrarisc.com"],
                "specific_emails": [],
                "color": "#4CAF50"
            },
            "进迭时空": {
                "suffixes": ["@spacemit.com", "@linux.spacemit.com"],
                "specific_emails": [],
                "color": "#2196F3"
            },
            "中兴通讯": {
                "suffixes": ["@zte.com.cn"],
                "specific_emails": [],
                "color": "#FF9800"
            },
            "阿里达摩院": {
                "suffixes": ["@linux.alibaba.com"],
                "specific_emails": [],
                "color": "#F44336"
            },
            "算能": {
                "suffixes": ["@sophgo.com"],
                "specific_emails": [],
                "color": "#9C27B0"
            },
            "软件所": {
                "suffixes": ["@iscas.ac.cn", "@isrc.iscas.ac.cn"],
                "specific_emails": ["Weihao Li <ieiao@outlook.com>"],
                "color": "#FF9800"
            }
        }

        # 输出目录
        self.docs_dir = self.repo_path / "docs"
        self.companies_dir = self.docs_dir / "companies"
        self.data_dir = self.docs_dir / "data"

        # 创建目录
        self.docs_dir.mkdir(parents=True, exist_ok=True)
        self.companies_dir.mkdir(parents=True, exist_ok=True)
        self.data_dir.mkdir(parents=True, exist_ok=True)

        # 时间戳
        self.timestamp = beijing_timestamp()

        # 主分支信息
        self.main_commit = self.get_main_branch_commit()

    def run_git(self, cmd, cwd=None, check_error=True):
        """运行git命令"""
        if cwd is None:
            cwd = self.repo_path

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )

        if check_error and result.returncode != 0:
            print(f"Git命令失败: {cmd}")
            print(f"错误输出: {result.stderr}")

        return result.stdout.strip(), result.stderr.strip(), result.returncode

    def get_main_branch_commit(self):
        """获取主分支的最新提交哈希"""

        # 获取主开发分支的最新提交
        stdout, stderr, code = self.run_git(f"git ls-remote {self.remote_url} {self.main_branch}")
        if code == 0 and stdout:
            parts = stdout.split()
            if len(parts) >= 1:
                return parts[0][:8]

        return "unknown"

    def clone_shallow_repo(self, tmp_dir, branch=None):
        """创建浅克隆仓库，返回凭证文件路径以便后续清理

        Args:
            tmp_dir: 临时目录
            branch: 指定要克隆的分支，默认为空（使用默认分支）
        """

        branch_arg = f"--branch {branch} --single-branch" if branch else ""
        print(f"创建浅克隆（深度: {self.clone_depth}，分支: {branch or '默认'}）...")

        # 1. 访问原始 URL（可能适用于公共仓库）
        clone_cmd = (
            f"git clone --bare --filter=blob:none "
            f"--depth={self.clone_depth} "
            f"{branch_arg} "
            f"{self.remote_url} "
            f"{tmp_dir}"
        ).strip()

        stdout, stderr, code = self.run_git(clone_cmd, check_error=False)

        if code == 0:
            print(f"✓ 浅克隆创建完成（原始 URL）")
            return True, None  # 成功，没有凭证文件

        # 2. 原始 URL 失败，尝试使用GitHub Token
        github_token = os.environ.get('GITHUB_TOKEN', '')
        if not github_token:
            print(f"❌ 原始URL克隆失败且无GITHUB_TOKEN: {stderr[:100]}")
            return False, None

        print("原始 URL 克隆失败，尝试使用 GitHub Token...")

        # 清理目标目录
        if os.path.exists(tmp_dir):
            print(f"清理目录以进行Token认证尝试: {tmp_dir}")
            shutil.rmtree(tmp_dir, ignore_errors=True)

        # 创建临时凭据文件
        parsed_url = urllib.parse.urlparse(self.remote_url)
        cred_content = f"https://x-access-token:{github_token}@{parsed_url.netloc}"
        cred_file = f"{tmp_dir}.git-credentials"

        try:
            with open(cred_file, 'w') as f:
                f.write(cred_content)

            # 配置git使用凭据文件
            self.run_git(f"git config --global credential.helper 'store --file={cred_file}'", check_error=False)

            # 再次尝试克隆
            stdout, stderr, code = self.run_git(clone_cmd, check_error=False)

            if code == 0:
                print(f"✓ 浅克隆创建完成（使用Token）")
                return True, cred_file
            else:
                print(f"❌ Token认证也失败: {stderr[:200]}")
                return False, cred_file

        except Exception as e:
            print(f"❌ 设置凭据失败: {e}")
            return False, None

    def cleanup_credentials(self, cred_file):
        """清理凭证文件"""

        try:
            if cred_file and os.path.exists(cred_file):
                os.remove(cred_file)
            self.run_git("git config --global --unset credential.helper", check_error=False)
            print("✓ 凭证已清理")
        except Exception as e:
            print(f"⚠️ 清理凭据时出错: {e}")

    def find_tag_in_clone(self, tmp_dir):
        """在克隆的仓库中查找tag"""

        print("在克隆中查找tag...")

        # 获取提交日志，查找tag
        log_cmd = f"git log --oneline --decorate -n {self.clone_depth}"
        stdout, stderr, code = self.run_git(log_cmd, cwd=tmp_dir)

        if code != 0:
            print(f"获取日志失败: {stderr}")
            return None

        # 查找包含tag的行
        for line in stdout.split('\n'):
            if 'tag:' in line:
                # 提取tag名称
                # 示例: "abc1234 (tag: v6.6.112) commit message"
                tag_match = re.search(r'tag:\s*([^,\s)]+)', line)
                if tag_match:
                    tag = tag_match.group(1)
                    print(f"找到tag: {tag}")
                    return tag

        print(f"在最近{self.clone_depth}个提交中未找到tag")
        return None

    def get_commits_from_clone(self, tmp_dir, tag):
        """从克隆中获取提交列表"""

        # 确定统计范围
        if tag:
            range_spec = f"{tag}..HEAD"
            log_cmd = f"git log {range_spec} --no-merges --format='%H|%an|%ae|%ad|%s' --date=iso"
            print(f"统计范围: {tag}..HEAD")
        else:
            range_spec = f"-{self.fallback_count}"
            log_cmd = f"git log {range_spec} --no-merges --format='%H|%an|%ae|%ad|%s' --date=iso"
            print(f"统计范围: 最近{self.fallback_count}个提交")

        stdout, stderr, code = self.run_git(log_cmd, cwd=tmp_dir)

        if code != 0:
            print(f"获取提交失败: {stderr}")
            return None

        # 解析提交数据
        commits = []
        for line in stdout.split('\n'):
            if '|' not in line:
                continue
            parts = line.split('|', 4)
            if len(parts) == 5:
                commits.append({
                    'hash': parts[0],
                    'author_name': parts[1],
                    'author_email': parts[2],
                    'date': parts[3],
                    'subject': parts[4]
                })

        print(f"获取到 {len(commits)} 个提交")
        return commits

    def get_commit_signatures(self, tmp_dir, commit_hash):
        """从克隆中获取提交的签名信息和完整body"""

        show_cmd = f"git show --no-patch --format=%B {commit_hash}"
        stdout, stderr, code = self.run_git(show_cmd, cwd=tmp_dir)

        if code != 0:
            return [], ""

        signatures = []
        for line in stdout.split('\n'):
            if line.strip().lower().startswith('signed-off-by:'):
                signatures.append(line.strip())

        return signatures, stdout

    def get_company_by_email(self, email):
        """根据邮箱判断机构归属"""

        if not email:
            return None

        email_lower = email.lower()

        for company, info in self.companies.items():
            # 检查邮箱后缀
            for suffix in info["suffixes"]:
                if suffix.lower() in email_lower:
                    return company

            # 检查特定邮箱
            for specific_email in info["specific_emails"]:
                email_match = re.search(r'<([^>]+)>', specific_email)
                if email_match:
                    specific_email_addr = email_match.group(1).lower()
                    if specific_email_addr in email_lower:
                        return company

        return None

    def fetch_github_stats(self):
        """获取 GitHub Issue 和 PR 统计数据"""
        import urllib.request
        import urllib.error

        token = os.environ.get('GITHUB_TOKEN')
        if not token:
            print("警告: 未设置 GITHUB_TOKEN，跳过 GitHub 统计")
            return None

        repo = os.environ.get('GITHUB_REPOSITORY', 'RVCK-Project/rvck')
        base_url = f"https://api.github.com/repos/{repo}"
        headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }

        stats = {}
        try:
            # 使用 GitHub API 获取仓库基本信息（包含 open issues 计数）
            req = urllib.request.Request(f"{base_url}", headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                import json
                repo_info = json.loads(resp.read().decode('utf-8'))
                stats['open_issues'] = repo_info.get('open_issues_count', 0)

            # 使用 search API 获取 closed issues 数量
            # GitHub issues 端点会同时返回 PRs，需要用 search API 过滤
            for state in ['open', 'closed']:
                req = urllib.request.Request(
                    f"https://api.github.com/search/issues?q=repo:{repo.replace('/', '%2F')}+is:issue+state:{state}",
                    headers=headers
                )
                with urllib.request.urlopen(req, timeout=10) as resp:
                    import json
                    result = json.loads(resp.read().decode('utf-8'))
                    count = result.get('total_count', 0)
                    if state == 'open':
                        stats['open_issues'] = count  # 覆盖之前的值，更精确
                    else:
                        stats['closed_issues'] = count

            # PRs - 使用 pulls 端点
            for state, key in [('open', 'open_prs'), ('closed', 'closed_prs')]:
                req = urllib.request.Request(
                    f"{base_url}/pulls?state={state}&per_page=100",
                    headers=headers
                )
                with urllib.request.urlopen(req, timeout=10) as resp:
                    import json
                    pulls = json.loads(resp.read().decode('utf-8'))
                    stats[key] = len(pulls)

            return stats
        except Exception as e:
            print(f"获取 GitHub 统计失败: {e}")
            return None

    def parse_commit_categories(self, commit_body):
        """解析提交中的分类标签

        返回: {
            'category': str or None,  # feature/bugfix/cleanup/config
            'is_backport': bool,      # mainline inclusion
            'hardware': str or None   # 硬件平台或 None
        }
        """
        result = {
            'category': None,
            'is_backport': False,
            'hardware': None
        }

        # 获取分割线以上的内容
        parts = commit_body.split('--------------------------------', 1)
        header = parts[0] if parts else commit_body

        # 解析 category: xxx
        cat_match = re.search(r'^category:[ \t]*(\w+)', header, re.MULTILINE | re.IGNORECASE)
        if cat_match:
            result['category'] = cat_match.group(1).lower()

        # 解析 mainline inclusion (backport)
        if re.search(r'^mainline inclusion', header, re.MULTILINE | re.IGNORECASE):
            result['is_backport'] = True

        # 解析 hardware: xxx
        hw_match = re.search(r'^hardware:[ \t]*(\w+)', header, re.MULTILINE | re.IGNORECASE)
        if hw_match:
            result['hardware'] = hw_match.group(1).lower()

        return result

    def get_commit_stats(self, clone_dir, commit_hash):
        """获取提交的代码修改统计（insert/delete行数）"""
        cmd = f"git -C {clone_dir} show --stat --format='' {commit_hash} | tail -1"
        stdout, stderr, returncode = self.run_git(cmd, check_error=False)

        if returncode != 0 or not stdout:
            return {'insertions': 0, 'deletions': 0}

        line = stdout
        insertions = 0
        deletions = 0

        insert_match = re.search(r'(\d+) insertion', line)
        if insert_match:
            insertions = int(insert_match.group(1))

        delete_match = re.search(r'(\d+) deletion', line)
        if delete_match:
            deletions = int(delete_match.group(1))

        # 调试：如需查看大改动提交，设置环境变量 DEBUG_LARGE_COMMITS=1
        if os.environ.get('DEBUG_LARGE_COMMITS') == '1':
            total = insertions + deletions
            if total > 10000:
                print(f"  [DEBUG] 大改动提交 {commit_hash[:8]}: +{insertions}/-{deletions}")

        return {'insertions': insertions, 'deletions': deletions}

    def analyze_commits(self):
        """分析提交数据"""

        print("开始分析提交...")

        with tempfile.TemporaryDirectory() as tmp_dir:
            cred_file = None
            try:
                # 1. 创建浅克隆（指定分支）
                clone_success, cred_file = self.clone_shallow_repo(tmp_dir, branch=self.main_branch)
                if not clone_success:
                    return None

                # 2. 查找tag
                start_tag = self.find_tag_in_clone(tmp_dir)

                # 3. 获取提交列表
                commits = self.get_commits_from_clone(tmp_dir, start_tag)
                if not commits:
                    return None

                # 4. 初始化统计数据结构
                stats = {
                    'total_commits': len(commits),
                    'commits_with_company': 0,
                    'total_insertions': 0,
                    'total_deletions': 0,
                    'companies': {company: {'count': 0, 'insertions': 0, 'deletions': 0, 'commits': [],
                                            'categories': {'feature': 0, 'bugfix': 0, 'cleanup': 0, 'config': 0, 'other': 0},
                                            'backports': 0, 'hardware': {}} for company in self.companies},
                    'no_company_commits': [],
                    'categories': {'feature': 0, 'bugfix': 0, 'cleanup': 0, 'config': 0, 'other': 0},
                    'backports': 0,
                    'hardware': {},
                    'generated_at': self.timestamp,
                    'main_branch': self.main_branch,
                    'main_commit': self.main_commit,
                    'start_tag': start_tag or f'最近{self.fallback_count}个提交'
                }

                # 5. 分析每个提交
                for i, commit in enumerate(commits):
                    if (i + 1) % 50 == 0:
                        print(f"已分析 {i + 1}/{len(commits)} 个提交")

                    # 调试：如需查看特定提交归属，设置 DEBUG_COMMIT_SUBJECT="关键字"
                    debug_subject = os.environ.get('DEBUG_COMMIT_SUBJECT')
                    if debug_subject and debug_subject in commit['subject']:
                        print(f"\n[DEBUG] 找到目标提交: {commit['hash'][:8]} - {commit['subject'][:60]}")
                        print(f"[DEBUG]   Author: {commit['author_name']} <{commit['author_email']}>")

                    # 获取代码修改统计
                    commit_stats = self.get_commit_stats(tmp_dir, commit['hash'])
                    commit['insertions'] = commit_stats['insertions']
                    commit['deletions'] = commit_stats['deletions']

                    # 累加到总体统计
                    stats['total_insertions'] += commit_stats['insertions']
                    stats['total_deletions'] += commit_stats['deletions']

                    # 获取签名信息和提交body
                    signatures, commit_body = self.get_commit_signatures(tmp_dir, commit['hash'])
                    commit['signatures'] = signatures

                    # 解析分类标签
                    categories = self.parse_commit_categories(commit_body)
                    commit['categories'] = categories

                    # 确定提交所属机构
                    author_company = self.get_company_by_email(commit['author_email'])

                    # 更新总体分类统计
                    cat = categories.get('category', 'other') or 'other'
                    stats['categories'][cat] = stats['categories'].get(cat, 0) + 1
                    if categories.get('is_backport'):
                        stats['backports'] += 1
                    if categories.get('hardware'):
                        hw = categories['hardware']
                        stats['hardware'][hw] = stats['hardware'].get(hw, 0) + 1

                    if author_company:
                        # Author属于某个机构，只统计该机构
                        stats['companies'][author_company]['count'] += 1
                        stats['companies'][author_company]['insertions'] += commit_stats['insertions']
                        stats['companies'][author_company]['deletions'] += commit_stats['deletions']
                        stats['companies'][author_company]['commits'].append(commit)
                        # 更新机构分类统计
                        stats['companies'][author_company]['categories'][cat] = stats['companies'][author_company]['categories'].get(cat, 0) + 1
                        if categories.get('is_backport'):
                            stats['companies'][author_company]['backports'] += 1
                        if categories.get('hardware'):
                            stats['companies'][author_company]['hardware'][hw] = stats['companies'][author_company]['hardware'].get(hw, 0) + 1
                        stats['commits_with_company'] += 1
                        if debug_subject and debug_subject in commit['subject']:
                            print(f"[DEBUG]   归属(Author): {author_company}\n")
                    else:
                        # Author不属于任何机构，检查签名中的机构
                        signature_companies = set()
                        for sig in signatures:
                            # 从签名中提取邮箱
                            email_match = re.search(r'<([^>]+)>', sig)
                            if email_match:
                                email = email_match.group(1)
                                company = self.get_company_by_email(email)
                                if company:
                                    signature_companies.add(company)

                        if signature_companies:
                            # 统计所有出现的机构
                            stats['commits_with_company'] += 1
                            for company in signature_companies:
                                stats['companies'][company]['count'] += 1
                                stats['companies'][company]['insertions'] += commit_stats['insertions']
                                stats['companies'][company]['deletions'] += commit_stats['deletions']
                                stats['companies'][company]['commits'].append(commit)
                                # 更新机构分类统计
                                stats['companies'][company]['categories'][cat] = stats['companies'][company]['categories'].get(cat, 0) + 1
                                if categories.get('is_backport'):
                                    stats['companies'][company]['backports'] += 1
                                if categories.get('hardware'):
                                    hw = categories['hardware']
                                    stats['companies'][company]['hardware'][hw] = stats['companies'][company]['hardware'].get(hw, 0) + 1
                            if debug_subject and debug_subject in commit['subject']:
                                print(f"[DEBUG]   归属(Signed-off-by): {', '.join(signature_companies)}\n")
                        else:
                            # 没有机构相关签名
                            stats['no_company_commits'].append(commit)
                            if debug_subject and debug_subject in commit['subject']:
                                print(f"[DEBUG]   归属: 未匹配到任何机构\n")

                return stats

            finally:
                # 确保凭证被清理
                self.cleanup_credentials(cred_file)

    def _format_hardware_stats(self, hardware_stats):
        """格式化硬件平台统计"""
        if not hardware_stats:
            return "暂无硬件平台数据"
        lines = []
        for hw, count in sorted(hardware_stats.items(), key=lambda x: x[1], reverse=True):
            lines.append(f"- {hw}: {count}")
        return '\n'.join(lines)

    def _format_github_stats(self, github_stats):
        """格式化 GitHub 统计数据"""
        if not github_stats:
            return "未获取到 GitHub 统计数据（需要设置 GITHUB_TOKEN）"
        return f"""| 项目 | 数量 |
|------|------|
| Open Issues | {github_stats.get('open_issues', 'N/A')} |
| Closed Issues | {github_stats.get('closed_issues', 'N/A')} |
| Open PRs | {github_stats.get('open_prs', 'N/A')} |
| Closed PRs | {github_stats.get('closed_prs', 'N/A')} |"""

    def _generate_cross_matrix(self, stats):
        """生成交叉矩阵表格（机构 x 分类）"""
        categories = ['feature', 'bugfix', 'cleanup', 'config', 'other']
        category_labels = {
            'feature': '新功能',
            'bugfix': '缺陷修复',
            'cleanup': '代码清理',
            'config': '配置变更',
            'other': '其他'
        }

        # 过滤有贡献的机构
        active_companies = [(c, stats['companies'][c]) for c in self.companies
                         if stats['companies'][c]['count'] > 0]
        if not active_companies:
            return "暂无机构贡献数据"

        lines = ["### 📊 各机构贡献分类矩阵"]
        lines.append("")
        lines.append("| 机构 | " + " | ".join(category_labels[cat] for cat in categories) + " | backport | hardware | 总计 |")
        lines.append("|------|" + "|".join("--------" for _ in categories) + "|----------|----------|------|")

        for company, company_stat in active_companies:
            row = [company]
            cat_stats = company_stat.get('categories', {})
            for cat in categories:
                row.append(str(cat_stats.get(cat, 0)))
            row.append(str(company_stat.get('backports', 0)))
            row.append(str(sum(company_stat.get('hardware', {}).values())))
            row.append(str(company_stat['count']))
            lines.append("| " + " | ".join(row) + " |")

        return "\n".join(lines)

    def _generate_category_leaderboards(self, stats):
        """生成各分类独立排行榜"""
        categories = [
            ('feature', '新功能', '🚀'),
            ('bugfix', '缺陷修复', '🐛'),
            ('cleanup', '代码清理', '🧹'),
            ('config', '配置变更', '⚙️'),
            ('other', '其他贡献', '📝')
        ]

        lines = ["### 🏆 各分类贡献排行"]
        lines.append("")

        for cat_key, cat_name, emoji in categories:
            lines.append(f"#### {emoji} {cat_name} (Top 3)")
            lines.append("")

            # 收集各机构该分类的数量
            rankings = []
            total_cat = stats['categories'].get(cat_key, 0)
            for company in self.companies:
                company_stat = stats['companies'][company]
                count = company_stat.get('categories', {}).get(cat_key, 0)
                if count > 0:
                    percentage = (count / total_cat * 100) if total_cat > 0 else 0
                    rankings.append((company, count, percentage))

            rankings.sort(key=lambda x: x[1], reverse=True)

            if rankings:
                lines.append("| 排名 | 机构 | 数量 | 占比 |")
                lines.append("|------|------|------|------|")
                medals = ['🥇', '🥈', '🥉']
                for i, (company, count, pct) in enumerate(rankings[:3]):
                    medal = medals[i] if i < 3 else f"{i+1}."
                    lines.append(f"| {medal} | {company} | {count} | {pct:.1f}% |")
            else:
                lines.append("*暂无数据*")
            lines.append("")

        # Backport 和 Hardware 单独展示
        lines.append("#### 🔄 Backport (主线反合)")
        lines.append("")
        backport_rankings = []
        total_backport = stats.get('backports', 0)
        for company in self.companies:
            count = stats['companies'][company].get('backports', 0)
            if count > 0:
                percentage = (count / total_backport * 100) if total_backport > 0 else 0
                backport_rankings.append((company, count, percentage))
        backport_rankings.sort(key=lambda x: x[1], reverse=True)

        if backport_rankings:
            lines.append("| 排名 | 机构 | 数量 | 占比 |")
            lines.append("|------|------|------|------|")
            medals = ['🥇', '🥈', '🥉']
            for i, (company, count, pct) in enumerate(backport_rankings[:3]):
                medal = medals[i] if i < 3 else f"{i+1}."
                lines.append(f"| {medal} | {company} | {count} | {pct:.1f}% |")
        else:
            lines.append("*暂无数据*")
        lines.append("")

        # Hardware 排行
        lines.append("#### 🔧 Hardware Support (硬件支持)")
        lines.append("")
        hw_rankings = []
        total_hw = sum(stats.get('hardware', {}).values())
        for company in self.companies:
            count = sum(stats['companies'][company].get('hardware', {}).values())
            if count > 0:
                percentage = (count / total_hw * 100) if total_hw > 0 else 0
                hw_rankings.append((company, count, percentage))
        hw_rankings.sort(key=lambda x: x[1], reverse=True)

        if hw_rankings:
            lines.append("| 排名 | 机构 | 数量 | 占比 |")
            lines.append("|------|------|------|------|")
            medals = ['🥇', '🥈', '🥉']
            for i, (company, count, pct) in enumerate(hw_rankings[:3]):
                medal = medals[i] if i < 3 else f"{i+1}."
                lines.append(f"| {medal} | {company} | {count} | {pct:.1f}% |")
        else:
            lines.append("*暂无数据*")

        return "\n".join(lines)

    def generate_main_page(self, stats):
        """生成统计主页"""
        # 按贡献数排序
        sorted_companies = sorted(
            [(company, stats['companies'][company]['count']) for company in self.companies],
            key=lambda x: x[1],
            reverse=True
        )

        # 生成概览段落中的机构列表
        company_details = []
        for company, count in sorted_companies:
            if count > 0 and stats['total_commits'] > 0:
                percentage = (count / stats['total_commits'] * 100)
                company_details.append(f"{company} {count} 个提交 ({percentage:.1f}%)")

        overview_text = "，".join(company_details) if company_details else "暂无机构贡献数据"

        # 生成Markdown内容
        content = f"""# 📊 内核贡献统计报告

**最后更新时间**: {stats['generated_at']}
**主分支**: `{stats['main_branch']}`
**主分支提交**: {stats['main_commit']}
**统计起始点**: `{stats['start_tag']}`

---

## 总体统计

| 项目 | 数量 |
|------|------|
| 总提交数 | {stats['total_commits']} |
| 有机构贡献的提交 | {stats['commits_with_company']} |
| 无机构贡献的提交 | {len(stats['no_company_commits'])} |

### 📌 累计贡献概览

目前 RVCK 基于统计起始点 `{stats['start_tag']}`，已累计合入 {stats['total_commits']} 个补丁（截至 {stats['generated_at'][:10]}），其中，{overview_text}。

### 📊 代码修改统计

RVCK 累计合入的补丁涉及代码修改：insert 🟢 +{stats.get('total_insertions', 0)} delete 🔴 -{stats.get('total_deletions', 0)}

### 📁 补丁分类统计

| 类别 | 数量 | 说明 |
|------|------|------|
| feature | {stats['categories'].get('feature', 0)} | 新功能 |
| bugfix | {stats['categories'].get('bugfix', 0)} | 缺陷修复 |
| backport | {stats.get('backports', 0)} | 主线反合 |
| hardware support | {sum(stats.get('hardware', {}).values())} | 硬件支持 |

**硬件平台分布**:
{self._format_hardware_stats(stats.get('hardware', {}))}

{self._generate_cross_matrix(stats)}

{self._generate_category_leaderboards(stats)}

### 📊 GitHub 仓库统计

{self._format_github_stats(stats.get('github_stats'))}

## 各机构贡献统计

| 机构 | 提交数 | 占比 | 可视化占比 | 代码修改行数 |
|------|--------|------|------------|--------------|
"""

        for company, count in sorted_companies:
            company_stat = stats['companies'][company]
            insertions = company_stat.get('insertions', 0)
            deletions = company_stat.get('deletions', 0)
            total_lines = insertions + deletions
            if stats['total_commits'] > 0:
                percentage = (count / stats['total_commits'] * 100)
                # 生成简单的进度条
                bar_length = int(percentage / 2)  # 50个字符对应100%
                bar = "█" * bar_length + "░" * (50 - bar_length)
                content += f"| [{company}](companies/{company}.md) | {count} | {percentage:.1f}% | `{bar}` | +{insertions}/-{deletions} ({total_lines}) |\n"
            else:
                content += f"| [{company}](companies/{company}.md) | {count} | 0.0% | `░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░` | +{insertions}/-{deletions} ({total_lines}) |\n"

        content += f"""
## 📈 可视化图表

```mermaid
pie title 各机构贡献占比
"""

        # 添加Mermaid饼图数据
        for company, count in sorted_companies:
            if count > 0 and stats['total_commits'] > 0:
                # 计算百分比
                percentage = (count / stats['total_commits'] * 100)
                content += f'    "{company} ({count}, {percentage:.1f}%)" : {count}\n'

        # 添加无机构贡献的部分
        if len(stats['no_company_commits']) > 0 and stats['total_commits'] > 0:
            no_company_percentage = (len(stats['no_company_commits']) / stats['total_commits'] * 100)
            content += f'    "其他 ({len(stats["no_company_commits"])}, {no_company_percentage:.1f}%)" : {len(stats["no_company_commits"])}\n'

        content += """```

## 📋 统计规则说明

### 1. 机构识别规则
"""

        for company, info in self.companies.items():
            content += f"- **{company}**: {', '.join(info['suffixes'])}"
            if info['specific_emails']:
                content += f"，特定签名：{', '.join(info['specific_emails'])}"
            content += "\n"

        content += f"""
### 2. 提交归属规则

贡献统计目前只面向对 RVCK 仓库有贡献的参与机构，因此在对主线补丁反合至 RVCK
等工作中，原补丁作者所属机构暂不计入该统计。

在 RVCK 贡献机构范围中，提交归属统计基于以下规则：

1. **优先原则**: 如果提交的 Author 邮箱属于某机构，则该提交只计入该机构
2. **签名统计**: 如果 Author 不属于任何机构，则统计签名中出现的所有机构
3. **去重规则**: 每个提交对每个机构最多计1次

### 3. 统计范围
- 主分支: `{stats['main_branch']}`
- 起始点: {stats['start_tag']}
- 结束点: 统计时的最新提交

---

## 🔧 技术说明

- **统计分支**: `contrib-stats`
- **统计脚本**: [scripts/contrib_stats/](scripts/contrib_stats/)
- **更新方式**: 手动/定时触发，脚本更新时自动触发
- **原始数据**: [data/latest.json](data/latest.json)

---

*最后更新: {stats['generated_at']}*
*生成自主分支提交: {stats['main_commit']}*
"""

        return content

    def _generate_page_header(self, company, info, stats):
        """生成页面头部（公共部分）- 画像式展示"""
        company_stats = stats['companies'][company]
        total_count = company_stats['count']

        if total_count == 0:
            return f"""# {company} 贡献详情

<div style="background-color: {info['color']}20; padding: 15px; border-radius: 8px; border-left: 5px solid {info['color']};">
<p><strong>📊 统计信息</strong></p>
<ul>
<li><strong>贡献提交数</strong>: {total_count}</li>
<li><strong>统计时间</strong>: {stats['generated_at']}</li>
<li><strong>主分支</strong>: {stats['main_branch']}</li>
<li><strong>起始标签</strong>: {stats['start_tag']}</li>
</ul>
</div>

*该机构暂无贡献数据*

## 📧 识别规则

- **邮箱后缀**: {', '.join(info['suffixes'])}
"""

        cat_stats = company_stats.get('categories', {})
        backport_count = company_stats.get('backports', 0)
        hw_count = sum(company_stats.get('hardware', {}).values())

        # 找出最活跃的领域
        all_categories = {
            '新功能(feature)': cat_stats.get('feature', 0),
            '缺陷修复(bugfix)': cat_stats.get('bugfix', 0),
            '代码清理(cleanup)': cat_stats.get('cleanup', 0),
            '配置变更(config)': cat_stats.get('config', 0),
            '其他(other)': cat_stats.get('other', 0),
            '主线反合(backport)': backport_count,
            '硬件支持(hardware)': hw_count
        }
        top_category = max(all_categories.items(), key=lambda x: x[1])
        top_name, top_count = top_category

        # 计算总体占比（相对于所有机构总提交）
        total_org_commits = stats.get('commits_with_company', 1)
        overall_percentage = (total_count / total_org_commits * 100) if total_org_commits > 0 else 0

        # 生成贡献画像表格
        profile_lines = []
        profile_lines.append("| 贡献维度 | 数量 | 占比 | 说明 |")
        profile_lines.append("|----------|------|------|------|")

        dimensions = [
            ('新功能', 'feature', '新增功能特性'),
            ('缺陷修复', 'bugfix', '修复代码缺陷'),
            ('代码清理', 'cleanup', '重构和优化'),
            ('配置变更', 'config', '配置项调整'),
            ('其他贡献', 'other', '未分类提交'),
            ('主线反合', 'backport', '同步主线代码'),
            ('硬件支持', 'hardware', '硬件平台适配'),
        ]

        for label, key, desc in dimensions:
            if key == 'backport':
                count = backport_count
            elif key == 'hardware':
                count = hw_count
            else:
                count = cat_stats.get(key, 0)

            pct = (count / total_count * 100) if total_count > 0 else 0
            bar = "█" * int(pct / 10) + "░" * (10 - int(pct / 10))
            profile_lines.append(f"| {label} | {count} | {bar} {pct:.1f}% | {desc} |")

        # 硬件平台明细
        hw_stats = company_stats.get('hardware', {})
        hw_detail_lines = []
        if hw_stats:
            hw_detail_lines.append("**支持的硬件平台**:")
            for hw, count in sorted(hw_stats.items(), key=lambda x: x[1], reverse=True):
                pct = (count / hw_count * 100) if hw_count > 0 else 0
                hw_detail_lines.append(f"- {hw}: {count} ({pct:.1f}%)")
        else:
            hw_detail_lines.append("*暂无硬件支持数据*")

        content = f"""# {company} 贡献画像

<div style="background-color: {info['color']}20; padding: 15px; border-radius: 8px; border-left: 5px solid {info['color']};">
<p><strong>📊 核心数据</strong></p>
<ul>
<li><strong>贡献提交数</strong>: {total_count} (占所有机构贡献的 {overall_percentage:.1f}%)</li>
<li><strong>最活跃领域</strong>: {top_name} ({top_count} 个提交)</li>
<li><strong>统计周期</strong>: {stats['start_tag']} → {stats['main_commit'][:8]}</li>
<li><strong>生成时间</strong>: {stats['generated_at']}</li>
</ul>
</div>

## 📈 贡献分布

{chr(10).join(profile_lines)}

### 🔧 硬件支持详情

{chr(10).join(hw_detail_lines)}

## 📧 识别规则

- **邮箱后缀**: {', '.join(info['suffixes'])}
"""
        if info['specific_emails']:
            content += f"- **特定签名**: {', '.join(info['specific_emails'])}\n"

        return content

    def _generate_commits_table(self, company, commits, repo):
        """生成 Markdown 格式的提交表格"""
        lines = ["| 提交哈希 | 日期 | 原始作者 | 标题 |", "|----------|------|----------|------|"]

        for commit in commits:
            date_short = commit['date'][:10] if 'T' in commit['date'] else commit['date'][:10]
            subject = commit['subject'][:80] + "..." if len(commit['subject']) > 80 else commit['subject']
            subject = subject.replace('|', '\\|').replace('<', '\\<').replace('>', '\\>')
            author = commit['author_name'].replace('|', '\\|')
            lines.append(f"| [{commit['hash'][:8]}](https://github.com/{repo}/commit/{commit['hash']}) | {date_short} | {author} | {subject} |")

        return '\n'.join(lines)

    def _generate_pagination_nav(self, company, current_page, total_pages, total_commits, page_size, is_all=False):
        """生成分页导航"""
        nav_lines = []
        nav_lines.append("")
        nav_lines.append("---")
        nav_lines.append("")

        if is_all:
            nav_lines.append(f"**共 {total_commits} 条提交（显示全部）**")
            nav_lines.append("")
            nav_lines.append(f"[分页显示]({company}.md) | [纯文本视图]({company}_commits.txt)")
        else:
            start_idx = (current_page - 1) * page_size + 1
            end_idx = min(current_page * page_size, total_commits)
            nav_lines.append(f"**共 {total_commits} 条提交，显示 {start_idx}-{end_idx}**")
            nav_lines.append("")

            # 页码链接
            page_links = []
            for i in range(1, total_pages + 1):
                if i == current_page:
                    page_links.append(f"**[{i}]**")
                elif i == 1:
                    page_links.append(f"[{i}]({company}.md)")
                else:
                    page_links.append(f"[{i}]({company}_page{i}.md)")

            nav_lines.append(" ".join(page_links))
            nav_lines.append("")
            nav_lines.append(f"[显示全部]({company}_all.md) | [纯文本视图]({company}_commits.txt)")

        return '\n'.join(nav_lines)

    def _generate_page_footer(self, stats):
        """生成页面底部"""
        return f"""
## 🔙 返回

[← 返回统计主页](../index.md)

---

*本页面最后更新于 {stats['generated_at']}*
*数据来源: 主分支 {stats['main_branch']}@{stats['main_commit']}*
"""

    def generate_company_page(self, company, info, stats, page=1, is_all=False):
        """生成单个机构的详情页（分页版本）"""

        company_stats = stats['companies'][company]
        commits = company_stats['commits']
        total = len(commits)
        page_size = 200
        repo = os.environ.get('GITHUB_REPOSITORY', 'your/repo')

        # 计算总页数
        total_pages = (total + page_size - 1) // page_size if total > 0 else 1

        # 确定要显示的提交
        if is_all:
            display_commits = commits
        else:
            start = (page - 1) * page_size
            end = start + page_size
            display_commits = commits[start:end]

        # 组装页面内容
        content = self._generate_page_header(company, info, stats)
        content += "\n## 📋 提交列表\n\n"
        content += self._generate_commits_table(company, display_commits, repo)
        content += self._generate_pagination_nav(company, page, total_pages, total, page_size, is_all)
        content += self._generate_page_footer(stats)

        return content

    def generate_company_text_view(self, company, stats):
        """生成纯文本视图文件"""

        company_stats = stats['companies'][company]
        commits = company_stats['commits']

        lines = [
            f"# {company} 提交列表（纯文本视图）",
            f"# 共 {len(commits)} 个提交",
            f"# 生成时间: {stats['generated_at']}",
            "#",
            "# 格式: 提交哈希 | 日期 | 原始作者 | 标题",
            "-" * 120,
        ]

        for commit in commits:
            date_short = commit['date'][:10] if 'T' in commit['date'] else commit['date'][:10]
            subject = commit['subject']
            lines.append(f"{commit['hash'][:8]} | {date_short} | {commit['author_name']} | {subject}")

        return "\n".join(lines)

    def save_statistics(self, stats):
        """保存所有统计数据"""

        print("正在保存统计数据...")
        # 1. 保存原始数据
        latest_file = self.data_dir / "latest.json"
        timestamp_file = self.data_dir / f"stats_{beijing_timestamp().replace('-', '').replace(' ', '_').replace(':', '')}.json"

        with open(latest_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)

        with open(timestamp_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)

        print(f"✓ 原始数据已保存: {latest_file}")

        # 2. 生成并保存主页面
        main_page = self.generate_main_page(stats)
        main_page_file = self.docs_dir / "index.md"

        with open(main_page_file, 'w', encoding='utf-8') as f:
            f.write(main_page)

        print(f"✓ 统计主页已生成: {main_page_file}")

        # 3. 生成并保存各机构页面
        for company, info in self.companies.items():
            count = stats['companies'][company]['count']
            if count > 0:
                page_size = 200
                total_pages = (count + page_size - 1) // page_size

                # 生成分页文件
                for page in range(1, total_pages + 1):
                    company_page = self.generate_company_page(company, info, stats, page=page)
                    if page == 1:
                        company_file = self.companies_dir / f"{company}.md"
                    else:
                        company_file = self.companies_dir / f"{company}_page{page}.md"

                    with open(company_file, 'w', encoding='utf-8') as f:
                        f.write(company_page)

                    print(f"✓ 机构页面已生成: {company_file}")

                # 生成"显示全部"页面
                if total_pages > 1:
                    all_page = self.generate_company_page(company, info, stats, is_all=True)
                    all_file = self.companies_dir / f"{company}_all.md"

                    with open(all_file, 'w', encoding='utf-8') as f:
                        f.write(all_page)

                    print(f"✓ 全部提交页面已生成: {all_file}")

                # 生成纯文本视图
                text_view = self.generate_company_text_view(company, stats)
                text_file = self.companies_dir / f"{company}_commits.txt"

                with open(text_file, 'w', encoding='utf-8') as f:
                    f.write(text_view)

                print(f"✓ 纯文本视图已生成: {text_file}")

        # 4. 生成分支README
        branch_readme = self.generate_branch_readme(stats)
        with open(self.repo_path / "README.md", 'w', encoding='utf-8') as f:
            f.write(branch_readme)

        print("✓ 分支README已更新")

        return True

    def generate_branch_readme(self, stats):
        """生成统计分支的README"""

        # 按贡献数排序
        sorted_companies = sorted(
            [(company, stats['companies'][company]['count']) for company in self.companies],
            key=lambda x: x[1],
            reverse=True
        )

        rank_content = ""
        for i, (company, count) in enumerate(sorted_companies, 1):
            if count > 0:
                rank_content += f"{i}. **{company}**: {count} 个提交\n"

        return f"""# 贡献统计分支

该分支专门用于存储内核贡献统计数据，独立于 RVCK 主开发分支(rvck-6.6)。

## 📊 最新统计摘要

**统计时间**: {stats['generated_at']}
**主分支**: `{stats['main_branch']}`
**统计起始点**: `{stats['start_tag']}`

| 项目 | 数量 |
|------|------|
| 总提交数 | {stats['total_commits']} |
| 有机构贡献的提交 | {stats['commits_with_company']} |

**贡献排名**:
{rank_content}
## 📁 目录结构

```
contrib-stats/
├── .github/workflows/          # GitHub Actions 工作流
├── scripts/contrib_stats/      # 统计脚本
├── docs/                       # 统计报告
│   ├── index.md               # 统计主页
│   ├── companies/             # 各机构详情
│   └── data/                  # 原始数据
└── README.md                  # 本文件
```

## 🔗 查看报告

- 📊 [完整统计报告](docs/index.md)
- 📁 [原始数据](docs/data/latest.json)

## ⚙️ 使用说明

### 手动更新统计
1. 进入 GitHub Actions 页面
2. 选择 "Update Contribution Stats"
3. 点击 "Run workflow"

### 自动触发
- 当统计脚本更新时自动触发
- 主分支有变更时需手动触发

### 本地查看
```bash
# 切换到统计分支
git checkout contrib-stats

# 查看统计报告
# 用浏览器打开 docs/index.md
```

## 📄 许可证

统计脚本和报告遵循与主项目相同的许可证。

---

*本分支最后更新于 {stats['generated_at']}*
"""

    def run(self):
        """运行完整统计流程"""

        print("=" * 60)
        print("贡献统计系统")
        print("=" * 60)
        print(f"主分支: {self.main_branch}")
        print(f"统计分支: {self.stats_branch}")
        print(f"远程仓库: {self.remote_url}")
        print(f"克隆深度: {self.clone_depth}")
        print()

        # 分析提交数据
        stats = self.analyze_commits()
        if not stats:
            return False

        # 获取 GitHub 统计
        print("\n获取 GitHub 统计数据...")
        github_stats = self.fetch_github_stats()
        if github_stats:
            stats['github_stats'] = github_stats
            print("✓ GitHub 统计获取成功")
        else:
            stats['github_stats'] = None
            print("⚠ GitHub 统计获取失败，继续生成报告")

        print(f"\n统计完成:")
        print(f"- 总提交数: {stats['total_commits']}")
        print(f"- 有机构贡献的提交: {stats['commits_with_company']}")
        print(f"- 无机构贡献的提交: {len(stats['no_company_commits'])}")

        # 输出各机构统计
        print(f"\n各机构贡献:")
        for company in self.companies:
            count = stats['companies'][company]['count']
            if count > 0:
                print(f"  - {company}: {count} 个提交")

        # 保存统计数据
        success = self.save_statistics(stats)

        if success:
            print(f"\n✓ 统计报告已生成:")
            print(f"  - 统计主页: docs/index.md")
            print(f"  - 机构详情: docs/companies/")
            print(f"  - 原始数据: docs/data/")
            print(f"  - 分支说明: README.md")

        return success

def main():
    parser = argparse.ArgumentParser(description='贡献统计')
    parser.add_argument('--main-branch', default='rvck-6.6', help='主开发分支')
    parser.add_argument('--stats-branch', default='contrib-stats', help='统计分支')
    parser.add_argument('--remote-url', help='远程仓库URL')

    args = parser.parse_args()

    print("开始贡献统计...")
    print("注意: 此脚本运行在统计分支，从远程仓库获取数据进行分析")
    print()

    stats = ContribStats(
        main_branch=args.main_branch,
        stats_branch=args.stats_branch,
        remote_url=args.remote_url
    )

    success = stats.run()

    if success:
        print("\n" + "=" * 60)
        print("✓ 统计流程成功完成!")
        print("=" * 60)
        return 0
    else:
        print("\n✗ 统计流程失败!")
        return 1

if __name__ == "__main__":
    sys.exit(main())
