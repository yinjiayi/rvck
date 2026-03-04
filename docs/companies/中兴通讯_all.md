# 中兴通讯 贡献画像

<div style="background-color: #FF980020; padding: 15px; border-radius: 8px; border-left: 5px solid #FF9800;">
<p><strong>📊 核心数据</strong></p>
<ul>
<li><strong>贡献提交数</strong>: 252 (占所有机构贡献的 22.8%)</li>
<li><strong>最活跃领域</strong>: 主线反合(backport) (230 个提交)</li>
<li><strong>统计周期</strong>: v6.6.127 → ce238702</li>
<li><strong>生成时间</strong>: 2026-03-04 22:05:14</li>
</ul>
</div>

## 📈 贡献分布

| 贡献维度 | 数量 | 占比 | 说明 |
|----------|------|------|------|
| 新功能 | 197 | ███████░░░ 78.2% | 新增功能特性 |
| 缺陷修复 | 53 | ██░░░░░░░░ 21.0% | 修复代码缺陷 |
| 代码清理 | 0 | ░░░░░░░░░░ 0.0% | 重构和优化 |
| 配置变更 | 2 | ░░░░░░░░░░ 0.8% | 配置项调整 |
| 其他贡献 | 0 | ░░░░░░░░░░ 0.0% | 未分类提交 |
| 主线反合 | 230 | █████████░ 91.3% | 同步主线代码 |
| 硬件支持 | 0 | ░░░░░░░░░░ 0.0% | 硬件平台适配 |

### 🔧 硬件支持详情

*暂无硬件支持数据*

## 📧 识别规则

- **邮箱后缀**: @zte.com.cn

## 📋 提交列表

| 提交哈希 | 日期 | 原始作者 | 标题 |
|----------|------|----------|------|
| [ce238702](https://github.com/RVCK-Project/rvck/commit/ce238702010b888c6b3fb62129a19b122c909fb1) | 2026-02-05 | shenlin | perf vendor events riscv: fix lrw core PMU event mapping |
| [9b184121](https://github.com/RVCK-Project/rvck/commit/9b184121b2529b212c8c4ccc49d770871b2c4087) | 2024-06-05 | Björn Töpel | riscv: Enable DAX VMEMMAP optimization |
| [4d1b8cb1](https://github.com/RVCK-Project/rvck/commit/4d1b8cb120f611576cc62ccd9a0c0bf1bd776fd7) | 2024-06-05 | Björn Töpel | riscv: mm: Add support for ZONE_DEVICE |
| [02e77a7b](https://github.com/RVCK-Project/rvck/commit/02e77a7b270a584542ab8fac95fc975cff47c3a1) | 2024-06-05 | Björn Töpel | virtio-mem: Enable virtio-mem for RISC-V |
| [fb7803cb](https://github.com/RVCK-Project/rvck/commit/fb7803cbce4cc438bb84462e3b10b486e6e23b36) | 2024-06-05 | Björn Töpel | riscv: Enable memory hotplugging for RISC-V |
| [f34c4e6b](https://github.com/RVCK-Project/rvck/commit/f34c4e6be2b8ccfcccc129bee578bebc6b7c301b) | 2024-06-05 | Björn Töpel | riscv: mm: Take memory hotplug read-lock during kernel page table dump |
| [b07b70f6](https://github.com/RVCK-Project/rvck/commit/b07b70f696315f4d3bd1e11af372b317fa91feb0) | 2024-06-05 | Björn Töpel | riscv: mm: Add memory hotplugging support |
| [9fa0a32f](https://github.com/RVCK-Project/rvck/commit/9fa0a32f28678c5fffba11ae288f900637534662) | 2024-06-05 | Björn Töpel | riscv: mm: Add pfn_to_kaddr() implementation |
| [8f8748c9](https://github.com/RVCK-Project/rvck/commit/8f8748c952a36b9db23bc4f552547be238969a0e) | 2024-06-05 | Björn Töpel | riscv: mm: Refactor create_linear_mapping_range() for memory hot add |
| [94396bdd](https://github.com/RVCK-Project/rvck/commit/94396bdd90d1da0846b933c4820924717d1e8818) | 2024-06-05 | Björn Töpel | riscv: mm: Change attribute from __init to __meminit for page functions |
| [e27f9f50](https://github.com/RVCK-Project/rvck/commit/e27f9f50b520e2386ae8f896387c63a696fcda53) | 2024-06-05 | Björn Töpel | riscv: mm: Pre-allocate vmemmap/direct map/kasan PGD entries |
| [7ee29f06](https://github.com/RVCK-Project/rvck/commit/7ee29f06ea15201e5fe3b9cce076d805e0064cee) | 2024-06-05 | Björn Töpel | riscv: mm: Properly forward vmemmap_populate() altmap parameter |
| [93fe47b1](https://github.com/RVCK-Project/rvck/commit/93fe47b1d141a54a41cd544311730cc9777a031e) | 2023-12-14 | Alexandre Ghiti | riscv: Use hugepage mappings for vmemmap |
| [e1f957f8](https://github.com/RVCK-Project/rvck/commit/e1f957f8d2c6bf88f34ee657f6b29988dd08695a) | 2023-11-06 | Evan Green | RISC-V: Probe misaligned access speed in parallel |
| [5753b821](https://github.com/RVCK-Project/rvck/commit/5753b821f4db866e3e2bed94aceaaa2d127a7ece) | 2023-11-06 | Evan Green | RISC-V: Remove __init on unaligned_emulation_finish() |
| [c9972b0e](https://github.com/RVCK-Project/rvck/commit/c9972b0eb5b694222003c3788ca95dc7fcc863dc) | 2023-10-04 | Clément Léger | riscv: add support for PR_SET_UNALIGN and PR_GET_UNALIGN |
| [d6dafd76](https://github.com/RVCK-Project/rvck/commit/d6dafd7671f43a13e70a49bd0ef68bcad92737eb) | 2023-10-04 | Clément Léger | riscv: report misaligned accesses emulation to hwprobe |
| [633b8adc](https://github.com/RVCK-Project/rvck/commit/633b8adc2175962f4a1bb6c504efbf28eab93c57) | 2023-10-04 | Clément Léger | riscv: add support for sysctl unaligned_enabled control |
| [9149ab3b](https://github.com/RVCK-Project/rvck/commit/9149ab3ba2575d6d709b7a53f67706d789c41342) | 2023-10-04 | Clément Léger | riscv: add floating point insn support to misaligned access emulation |
| [9eed1d4b](https://github.com/RVCK-Project/rvck/commit/9eed1d4b1a61f821666c24e86fde0592826af166) | 2023-10-04 | Clément Léger | riscv: report perf event for misaligned fault |
| [045fa236](https://github.com/RVCK-Project/rvck/commit/045fa236cb8a89c08ba604814dc98174bd13d44e) | 2023-10-04 | Clément Léger | riscv: add support for misaligned trap handling in S-mode |
| [ee055a97](https://github.com/RVCK-Project/rvck/commit/ee055a9799977ef2e1c947f8db040243ab19b4b1) | 2026-01-17 | Lu Peng | riscv: defconfig: Enable more ACPI_APEI configs |
| [af861a24](https://github.com/RVCK-Project/rvck/commit/af861a2464797b08f698ee19c61829c2835a4137) | 2025-07-23 | Ignacio Encinas | riscv: introduce asm/swab.h |
| [dfd898b8](https://github.com/RVCK-Project/rvck/commit/dfd898b8a65626e469f2103dd30b2e08f228f513) | 2026-01-07 | hu.yuye | riscv:defconfig:Enable PCIE_EDR |
| [a08e4c60](https://github.com/RVCK-Project/rvck/commit/a08e4c601e8f69d03b530a1974112498cdfe36c0) | 2025-12-31 | Yunhui Cui | arch_topology: move parse_acpi_topology() to common code |
| [26a8cbe3](https://github.com/RVCK-Project/rvck/commit/26a8cbe38be700b910695690bd8735c9474ecf99) | 2025-12-31 | Yicong Yang | arm64: topology: Support SMT control on ACPI based system |
| [5d69c37c](https://github.com/RVCK-Project/rvck/commit/5d69c37c3b04bbff4e225bd3cc273be3a4d4e7e3) | 2025-12-31 | Yicong Yang | arch_topology: Support SMT control for OF based system |
| [e83dfb5e](https://github.com/RVCK-Project/rvck/commit/e83dfb5e9b3a5ef550435b6a647c94d44ade28d8) | 2025-12-31 | Yicong Yang | cpu/SMT: Provide a default topology_is_primary_thread() |
| [06bdacd0](https://github.com/RVCK-Project/rvck/commit/06bdacd0e86208522e4a655aba5eee316dcbfb19) | 2025-01-24 | Andy Shevchenko | serial: 8250_core: Remove unneeded -\>iotype assignment |
| [1e582822](https://github.com/RVCK-Project/rvck/commit/1e582822b20fad58b88563094095e8723a5045ed) | 2025-12-30 | hu.yuye | Revert "mango pci hack:broadcast when no MSI source known" |
| [304a271b](https://github.com/RVCK-Project/rvck/commit/304a271b8ea126023fe3edd58a98cf1fa7b1e9fc) | 2025-12-22 | Clément Léger | riscv: uaccess: do not do misaligned accesses in get/put_user() |
| [f5f84ab9](https://github.com/RVCK-Project/rvck/commit/f5f84ab944c0510b5fa2032fad43de3f84eb5d5f) | 2025-12-22 | Alexandre Ghiti | riscv: make unsafe user copy routines use existing assembly routines |
| [f1bb63e1](https://github.com/RVCK-Project/rvck/commit/f1bb63e1ea1051a1ca0c4d02f33fa356604e1bb6) | 2025-12-22 | Jisheng Zhang | riscv: uaccess: use 'asm_goto_output' for get_user() |
| [d125cd77](https://github.com/RVCK-Project/rvck/commit/d125cd77affbcf66598f0be8085861008f0e904b) | 2025-12-22 | Jisheng Zhang | riscv: uaccess: use 'asm goto' for put_user() |
| [d2ca193e](https://github.com/RVCK-Project/rvck/commit/d2ca193e7156f1bfd59afd1655c16f2543db7c0c) | 2025-12-22 | Jisheng Zhang | riscv: uaccess: use input constraints for ptr of __put_user() |
| [e7cfba83](https://github.com/RVCK-Project/rvck/commit/e7cfba8382aca573ad3b67ab49765606b2c3160a) | 2025-12-22 | Jisheng Zhang | riscv: implement user_access_begin() and families |
| [947bc0be](https://github.com/RVCK-Project/rvck/commit/947bc0beb0d5880930eba6de7833829febae1fdb) | 2025-12-22 | Ben Dooks | riscv: save the SR_SUM status over switches |
| [a300afc6](https://github.com/RVCK-Project/rvck/commit/a300afc60e7bd43d031541fc0dbc5a772f5d2bdc) | 2011-12-08 | Tejun Heo | Revert "mm: Modify __find_max_addr for memory hole" |
| [73b6ac4a](https://github.com/RVCK-Project/rvck/commit/73b6ac4abfb5b53fb1a06a21b2ff1064e23b3170) | 2021-12-06 | Alexandre Ghiti | Revert "riscv: mm: Clear compilation warning about last_cpupid" |
| [3fb4f3ab](https://github.com/RVCK-Project/rvck/commit/3fb4f3ab3e71b85a6fc3a998ed4a3613d32d382e) | 2025-11-12 | shenlin | perf vendor events riscv: add lrw core JSON file with metric support |
| [71b98d85](https://github.com/RVCK-Project/rvck/commit/71b98d85e56a23458a5dd5be004cb85c0cf0c7ac) | 2025-11-11 | Fei Liu | i2c: Add driver for the LRW I2C |
| [e22fd587](https://github.com/RVCK-Project/rvck/commit/e22fd587cd482821ae71eb7074bbc2b936305f6b) | 2025-09-29 | Fei Liu | dt-bindings: i2c: Add binding for LRW I2C |
| [85e1efa1](https://github.com/RVCK-Project/rvck/commit/85e1efa152973fa10e9c7f91eea0d7c1b397e63f) | 2025-11-12 | Jie Feng | drivers/perf: add LRW DDR PMU support |
| [d9a397b0](https://github.com/RVCK-Project/rvck/commit/d9a397b004259a595d020aeb79bfdb14ba050097) | 2025-09-04 | Wenhong Liu | serial: Add driver for the LRW UART |
| [48811d37](https://github.com/RVCK-Project/rvck/commit/48811d370be5392f5ca12b54ceda0defde773a4b) | 2025-09-04 | Wenhong Liu | dt-bindings: serial: Add binding for LRW UART |
| [6a721419](https://github.com/RVCK-Project/rvck/commit/6a72141998e7f68126710c0c9e42433c50a6ac39) | 2025-10-16 | Wenhong Liu | riscv: defconfig: remove CONFIG_CMDLINE and CONFIG_CMDLINE_EXTEND as mainline do... |
| [00756dcf](https://github.com/RVCK-Project/rvck/commit/00756dcf455753d67a95e4d681a0e4414575279f) | 2025-08-27 | Himanshu Chauhan | riscv: Enable APEI and NMI safe cmpxchg options required for RAS |
| [f4df60c6](https://github.com/RVCK-Project/rvck/commit/f4df60c64c4a51129ba8f0564a9d2deb0a9e8641) | 2025-08-27 | Himanshu Chauhan | riscv: Add config option to enable APEI SSE handler |
| [0240ae22](https://github.com/RVCK-Project/rvck/commit/0240ae22c25a3b46ec7d3896a860a10ff56396ed) | 2025-08-27 | Himanshu Chauhan | riscv: Introduce HEST SSE notification handlers |
| [24dd2207](https://github.com/RVCK-Project/rvck/commit/24dd2207c48fef991764c64c1f55ae2521e62c6d) | 2025-08-27 | Himanshu Chauhan | riscv: Add RISC-V entries in processor type and ISA strings |
| [1b13a6c2](https://github.com/RVCK-Project/rvck/commit/1b13a6c2a41af596a4ad3b9bf2e3184b3cbd1510) | 2025-08-27 | Himanshu Chauhan | riscv: Add functions to register ghes having SSE notification |
| [48db3e03](https://github.com/RVCK-Project/rvck/commit/48db3e03daf41ce4e5c406b92dc6a8eaedad65cf) | 2025-08-27 | Himanshu Chauhan | riscv: conditionally compile GHES NMI spool function |
| [94dcf83e](https://github.com/RVCK-Project/rvck/commit/94dcf83e13460228928f73267127b1e7bdf571ed) | 2025-08-27 | Himanshu Chauhan | riscv: Add fixmap indices for GHES IRQ and SSE contexts |
| [57196cd7](https://github.com/RVCK-Project/rvck/commit/57196cd728ea20f5689cee434e665d69017d14d1) | 2025-08-27 | Himanshu Chauhan | acpi: Introduce SSE in HEST notification types |
| [92eadae2](https://github.com/RVCK-Project/rvck/commit/92eadae2e1838dc3a961fd5603632240afc86b2f) | 2025-08-27 | Himanshu Chauhan | riscv: Define arch_apei_get_mem_attribute for RISC-V |
| [6d1c3284](https://github.com/RVCK-Project/rvck/commit/6d1c3284e323c0bc063dca04ecfc4add9c6f9785) | 2025-08-27 | Himanshu Chauhan | riscv: Define ioremap_cache for RISC-V |
| [b439ab9c](https://github.com/RVCK-Project/rvck/commit/b439ab9c48cefc513bc2d6342cf41a4516270d2a) | 2025-08-27 | Clément Léger | selftests/riscv: add SSE test module |
| [9f7d30e7](https://github.com/RVCK-Project/rvck/commit/9f7d30e716ab5cfac7837551933760fc4d181b58) | 2025-08-27 | Clément Léger | perf: RISC-V: add support for SSE event |
| [f9bb4e16](https://github.com/RVCK-Project/rvck/commit/f9bb4e161700d5d1711297a227c828e8c426e319) | 2025-08-27 | Clément Léger | drivers: firmware: add riscv SSE support |
| [2e6a1d4a](https://github.com/RVCK-Project/rvck/commit/2e6a1d4a241c8b830ec3d71368e84c10b7cc65a5) | 2025-08-27 | Clément Léger | riscv: add support for SBI Supervisor Software Events extension |
| [e1dfb50e](https://github.com/RVCK-Project/rvck/commit/e1dfb50e0ae37fe9e89e67af86c57a985fef5795) | 2025-08-08 | Clément Léger | riscv: add SBI SSE extension definitions |
| [7bc5030f](https://github.com/RVCK-Project/rvck/commit/7bc5030f0320b5fd5af652496309cb614ea3d055) | 2025-10-14 | Sunil V L | iommu/riscv: Add ACPI support |
| [40391fc4](https://github.com/RVCK-Project/rvck/commit/40391fc48eb27e73d6513814548ad46df020be97) | 2025-10-14 | Sunil V L | ACPI: scan: Add support for RISC-V in acpi_iommu_configure_id() |
| [e88f7b28](https://github.com/RVCK-Project/rvck/commit/e88f7b28f21993a0679ae634d3c1a974bc294dfa) | 2025-10-14 | Sunil V L | ACPI: RISC-V: Add support for RIMT |
| [c9185801](https://github.com/RVCK-Project/rvck/commit/c9185801842e452d5cd04eda2b67a482e7353d4b) | 2025-10-13 | Sunil V L | ACPICA: actbl2: Add definitions for RIMT |
| [26a4fd9f](https://github.com/RVCK-Project/rvck/commit/26a4fd9f493a64c0b2ad738cbb2eea237e61d0e6) | 2025-09-20 | shenlin | perf vendor events riscv: add lrw core JSON file |
| [fa4ba9a3](https://github.com/RVCK-Project/rvck/commit/fa4ba9a38bc044d9683d0b5400019fd44ac1607c) | 2025-04-21 | Alexandre Ghiti | riscv: Add support for Zicbop |
| [a3a2217c](https://github.com/RVCK-Project/rvck/commit/a3a2217c227ddc161006757a846e0e2588e0b395) | 2025-04-21 | Alexandre Ghiti | riscv: Introduce Zicbop instructions |
| [aff8c919](https://github.com/RVCK-Project/rvck/commit/aff8c9192e3cd6288984e9f86190758feba94e36) | 2025-02-26 | Yunhui Cui | RISC-V: Enable cbo.clean/flush in usermode |
| [ed67d541](https://github.com/RVCK-Project/rvck/commit/ed67d54115f6e0bbfe9a275a9b6bab7be3ccadeb) | 2024-08-14 | Samuel Holland | riscv: Add support for per-thread envcfg CSR values |
| [4bd21721](https://github.com/RVCK-Project/rvck/commit/4bd21721ddd2eebd45fdcfe1468fba2a65be7ee4) | 2024-06-19 | Clément Léger | RISC-V: KVM: Allow Zaamo/Zalrsc extensions for Guest/VM |
| [28220b62](https://github.com/RVCK-Project/rvck/commit/28220b6221234ea91c7b6079200e7c5b91856a93) | 2024-06-19 | Clément Léger | riscv: hwprobe: export Zaamo and Zalrsc extensions |
| [13a6c7a1](https://github.com/RVCK-Project/rvck/commit/13a6c7a1856ca6324dad98896601901844398649) | 2024-06-19 | Clément Léger | riscv: add parsing for Zaamo and Zalrsc extensions |
| [9bf81ff7](https://github.com/RVCK-Project/rvck/commit/9bf81ff7b4af7823111754ceedecfc5d69db9b8a) | 2025-02-13 | Inochi Amaoto | riscv: hwprobe: export bfloat16 ISA extension |
| [e578230f](https://github.com/RVCK-Project/rvck/commit/e578230ff7700c98ac205e934fc5f4c40c94508c) | 2025-02-13 | Inochi Amaoto | riscv: add ISA extension parsing for bfloat16 ISA extension |
| [74ed7b27](https://github.com/RVCK-Project/rvck/commit/74ed7b27803b0943acbbbdb47bcd59b7408713c0) | 2024-05-24 | Xiao Wang | riscv, bpf: Introduce shift add helper with Zba optimization |
| [1e435833](https://github.com/RVCK-Project/rvck/commit/1e435833ac8f8be1f9a962e4050f2d68b5af87ab) | 2024-05-16 | Xiao Wang | riscv, bpf: Optimize zextw insn with Zba extension |
| [98c89309](https://github.com/RVCK-Project/rvck/commit/98c893098bbce8aff4564c06eab8aed06e24c89a) | 2024-01-15 | Pu Lehui | riscv, bpf: Optimize bswap insns with Zbb support |
| [6f2b0ecc](https://github.com/RVCK-Project/rvck/commit/6f2b0ecc601d0d4bc252d6ac87fbbe56b41329f4) | 2024-01-15 | Pu Lehui | riscv, bpf: Optimize sign-extention mov insns with Zbb support |
| [22f80a47](https://github.com/RVCK-Project/rvck/commit/22f80a478e30772f8a09e8886e9d141ad4624aee) | 2024-01-15 | Pu Lehui | riscv, bpf: Add necessary Zbb instructions |
| [5509679f](https://github.com/RVCK-Project/rvck/commit/5509679f25602979df5ed353a81451441dde7880) | 2024-01-15 | Pu Lehui | riscv, bpf: Simplify sext and zext logics in branch instructions |
| [7881cc3d](https://github.com/RVCK-Project/rvck/commit/7881cc3dd73ddb4e3a3ff30b94f160132c2745f0) | 2024-01-15 | Pu Lehui | riscv, bpf: Unify 32-bit zero-extension to emit_zextw |
| [20cb6f43](https://github.com/RVCK-Project/rvck/commit/20cb6f432d8d53f115d9c4691341552f63709617) | 2024-01-15 | Pu Lehui | riscv, bpf: Unify 32-bit sign-extension to emit_sextw |
| [4959df05](https://github.com/RVCK-Project/rvck/commit/4959df05529e46116fc3b1ec46e0586d66184873) | 2025-03-12 | Robin Murphy | iommu: Don't warn prematurely about dodgy probes |
| [618c0e07](https://github.com/RVCK-Project/rvck/commit/618c0e07b1cf5d8838dfc430c37f4aa057fbb590) | 2024-10-09 | Lu Baolu | iommu: Remove iommu_domain_alloc() |
| [05330e05](https://github.com/RVCK-Project/rvck/commit/05330e057d5c8ea269198c7ec69e0a536729a05b) | 2024-10-09 | Lu Baolu | iommu: Remove iommu_present() |
| [6c062551](https://github.com/RVCK-Project/rvck/commit/6c06255166f192fe36ee2d46ee2d5a73f36fc7fd) | 2024-09-02 | Lu Baolu | drm/tegra: Use iommu_paging_domain_alloc() |
| [e6672556](https://github.com/RVCK-Project/rvck/commit/e6672556865401b4188cd4c20a6eebd0a24514f0) | 2024-09-02 | Lu Baolu | drm/rockchip: Use iommu_paging_domain_alloc() |
| [6fd53ea6](https://github.com/RVCK-Project/rvck/commit/6fd53ea69f3a7caeb696c88e7d9d65e445974f92) | 2024-06-10 | Lu Baolu | RDMA/usnic: Use iommu_paging_domain_alloc() |
| [643435d3](https://github.com/RVCK-Project/rvck/commit/643435d3538450b9433eed796c797b65928ebc80) | 2024-08-12 | Lu Baolu | soc: fsl: qbman: Use iommu_paging_domain_alloc() |
| [6b22ab3f](https://github.com/RVCK-Project/rvck/commit/6b22ab3fef8151f73a31ba8068404fc84b8dc1be) | 2024-08-12 | Lu Baolu | remoteproc: Use iommu_paging_domain_alloc() |
| [263c59ab](https://github.com/RVCK-Project/rvck/commit/263c59abcbe06e88008c6fe0f167333ff1033972) | 2024-08-12 | Lu Baolu | media: venus: firmware: Use iommu_paging_domain_alloc() |
| [1ae90dbb](https://github.com/RVCK-Project/rvck/commit/1ae90dbb769a1a138949f3e08f609bad6c570dc3) | 2024-08-12 | Lu Baolu | media: nvidia: tegra: Use iommu_paging_domain_alloc() |
| [1fae1a2a](https://github.com/RVCK-Project/rvck/commit/1fae1a2a1308fe6b29345d82075136e55ad6ce7e) | 2024-08-12 | Lu Baolu | gpu: host1x: Use iommu_paging_domain_alloc() |
| [c986ae13](https://github.com/RVCK-Project/rvck/commit/c986ae1349504fa5e05d93d12bb906e8f1952997) | 2024-09-02 | Lu Baolu | drm/nouveau/tegra: Use iommu_paging_domain_alloc() |
| [4a38e575](https://github.com/RVCK-Project/rvck/commit/4a38e575aa72ea0cf5b9339d63d7e3db6f2ccbb5) | 2024-06-10 | Lu Baolu | wifi: ath11k: Use iommu_paging_domain_alloc() |
| [f77d974a](https://github.com/RVCK-Project/rvck/commit/f77d974a58730e1f1d7767ec20dcfc921d86cbae) | 2024-06-10 | Lu Baolu | wifi: ath10k: Use iommu_paging_domain_alloc() |
| [df832a4f](https://github.com/RVCK-Project/rvck/commit/df832a4f704bd262b38c1a33dbfc01c9654b6071) | 2024-06-10 | Lu Baolu | drm/msm: Use iommu_paging_domain_alloc() |
| [760f3744](https://github.com/RVCK-Project/rvck/commit/760f3744695ae5260c188e841908113f6c371c12) | 2024-06-10 | Lu Baolu | vhost-vdpa: Use iommu_paging_domain_alloc() |
| [911788c6](https://github.com/RVCK-Project/rvck/commit/911788c684806e39f34f597b86819b990a073e4d) | 2024-06-10 | Lu Baolu | vfio/type1: Use iommu_paging_domain_alloc() |
| [1df3dd04](https://github.com/RVCK-Project/rvck/commit/1df3dd04cc5e00603465837e652c43f68459a4f5) | 2024-06-10 | Lu Baolu | iommufd: Use iommu_paging_domain_alloc() |
| [272621c8](https://github.com/RVCK-Project/rvck/commit/272621c8fed76039bc897b3be90b884b96bab29d) | 2024-06-10 | Lu Baolu | iommu: Add iommu_paging_domain_alloc() interface |
| [67bc8b41](https://github.com/RVCK-Project/rvck/commit/67bc8b410e4904482e82d7719bdc7f13cf7e30a0) | 2025-02-28 | Robin Murphy | iommu: Get DT/ACPI parsing into the proper probe path |
| [6b5a1375](https://github.com/RVCK-Project/rvck/commit/6b5a137569339da13b72bfce66e6a3927c6b35c2) | 2025-02-28 | Robin Murphy | iommu: Keep dev-\>iommu state consistent |
| [edd45ea6](https://github.com/RVCK-Project/rvck/commit/edd45ea6ee01e7d01d86a2947865c9db7b5fb13c) | 2025-02-28 | Robin Murphy | iommu: Resolve ops in iommu_init_device() |
| [fbd1e5a0](https://github.com/RVCK-Project/rvck/commit/fbd1e5a0218b27d5d6750aa936c5078606e52bd1) | 2025-02-28 | Robin Murphy | iommu: Handle race with default domain setup |
| [0cca36a7](https://github.com/RVCK-Project/rvck/commit/0cca36a764b69e37e51dc5459c3b8476dd44e58f) | 2025-02-27 | Robin Murphy | iommu: Unexport iommu_fwspec_free() |
| [d281086a](https://github.com/RVCK-Project/rvck/commit/d281086af1072de24017c9bca000b0e7eafc9ec7) | 2024-07-02 | Robin Murphy | iommu: Remove iommu_fwspec ops |
| [d2931cdd](https://github.com/RVCK-Project/rvck/commit/d2931cdd41f21a9a1b2acf8a7fc9bfb8f94a9781) | 2024-07-02 | Robin Murphy | OF: Simplify of_iommu_configure() |
| [54d49e62](https://github.com/RVCK-Project/rvck/commit/54d49e62702cc14dfcb5071d03f5e5ceb1fa9fd4) | 2024-07-02 | Robin Murphy | ACPI: Retire acpi_iommu_fwspec_ops() |
| [c814140c](https://github.com/RVCK-Project/rvck/commit/c814140c81351f2c746dd4d07b393304dbf24dbe) | 2024-07-02 | Robin Murphy | iommu: Resolve fwspec ops automatically |
| [5436cde2](https://github.com/RVCK-Project/rvck/commit/5436cde2f13286d0f89f6d09de226eeebcf8c8f4) | 2023-12-07 | Jason Gunthorpe | acpi: Do not return struct iommu_ops from acpi_iommu_configure_id() |
| [1887a950](https://github.com/RVCK-Project/rvck/commit/1887a950662d1e659052a0725416a87a2db2e509) | 2023-12-07 | Jason Gunthorpe | iommu: Mark dev_iommu_priv_set() with a lockdep |
| [bef8f4b4](https://github.com/RVCK-Project/rvck/commit/bef8f4b4b9df94888bb036ec9c2d2aeab94365b7) | 2023-12-07 | Jason Gunthorpe | iommu: Mark dev_iommu_get() with lockdep |
| [1b76d057](https://github.com/RVCK-Project/rvck/commit/1b76d057f229063f65d2a8682ea9652cd48b2f00) | 2023-12-07 | Jason Gunthorpe | iommu/of: Use -ENODEV consistently in of_iommu_configure() |
| [c27b0a9d](https://github.com/RVCK-Project/rvck/commit/c27b0a9dbcf85e12d1dc50797cac5638f48aa75e) | 2023-12-07 | Jason Gunthorpe | iommmu/of: Do not return struct iommu_ops from of_iommu_configure() |
| [38d06d99](https://github.com/RVCK-Project/rvck/commit/38d06d99e5418f031aafe8399c583a18636e8a54) | 2023-12-07 | Jason Gunthorpe | iommu: Remove struct iommu_ops *iommu from arch_setup_dma_ops() |
| [bd9d0b31](https://github.com/RVCK-Project/rvck/commit/bd9d0b31e6a8e883a8308a44c365b9838b2e72dc) | 2023-11-21 | Robin Murphy | iommu: Clean up open-coded ownership checks |
| [412d33cf](https://github.com/RVCK-Project/rvck/commit/412d33cf86af35e65a38184079fe78d03a0aabf3) | 2023-11-21 | Robin Murphy | iommu: Retire bus ops |
| [e9c37a8e](https://github.com/RVCK-Project/rvck/commit/e9c37a8e7468adeb98e4ccd60821c4e5e2d263fd) | 2023-11-21 | Robin Murphy | iommu: Decouple iommu_domain_alloc() from bus ops |
| [6f7062b4](https://github.com/RVCK-Project/rvck/commit/6f7062b4d01ad135f15efaa60321c90eb1d233de) | 2023-11-21 | Robin Murphy | iommu: Validate that devices match domains |
| [d500f16c](https://github.com/RVCK-Project/rvck/commit/d500f16c7b507b3e643fc4b2bbd3bf3edca43707) | 2023-11-21 | Robin Murphy | iommu: Decouple iommu_present() from bus ops |
| [497975e1](https://github.com/RVCK-Project/rvck/commit/497975e1ddf440e38ee3f3dfc59f0cbc3b7eb83e) | 2023-11-21 | Robin Murphy | iommu: Factor out some helpers |
| [a452aec4](https://github.com/RVCK-Project/rvck/commit/a452aec421270ed8757c9bf076affa9e972b7378) | 2024-03-13 | Xiao Wang | riscv: uaccess: Relax the threshold for fast path |
| [c1e3b5b0](https://github.com/RVCK-Project/rvck/commit/c1e3b5b0cba6b589905721b735b769b2efec2b33) | 2024-03-13 | Xiao Wang | riscv: uaccess: Allow the last potential unrolled copy |
| [513dfb89](https://github.com/RVCK-Project/rvck/commit/513dfb891bb5cee5041ff7d6ca394fffa74bfcfc) | 2024-12-24 | Atish Patra | RISC-V: KVM: Add new exit statstics for redirected traps |
| [6947bb98](https://github.com/RVCK-Project/rvck/commit/6947bb9872f8f3ad05b45cc2fb4fdbd227f76ba9) | 2024-12-24 | Atish Patra | RISC-V: KVM: Update firmware counters for various events |
| [a0306303](https://github.com/RVCK-Project/rvck/commit/a0306303ac8b2c8b5e8f7eca21ea76bdcb31c1a0) | 2024-04-29 | Yu-Wei Hsu | RISC-V: KVM: Redirect AMO load/store access fault traps to guest |
| [9a1e8da0](https://github.com/RVCK-Project/rvck/commit/9a1e8da0e7e2208bfb5ebdb7c2b45d313b8b9ade) | 2025-08-20 | XianLiang Huang | iommu/riscv: prevent NULL deref in iova_to_phys |
| [5014139d](https://github.com/RVCK-Project/rvck/commit/5014139d610c80dbf889a79014094a387966a6f1) | 2025-01-03 | Xu Lu | iommu/riscv: Add shutdown function for iommu driver |
| [4805540b](https://github.com/RVCK-Project/rvck/commit/4805540bdb39cc6366c76ab486e6eb4e04e61311) | 2025-01-03 | Xu Lu | iommu/riscv: Empty iommu queue before enabling it |
| [38b89563](https://github.com/RVCK-Project/rvck/commit/38b89563e236227a874b5304b6b11abd45f20716) | 2024-11-12 | Andrew Jones | iommu/riscv: Add support for platform msi |
| [f37b04f7](https://github.com/RVCK-Project/rvck/commit/f37b04f70187e5dd1689902042419fbd54831195) | 2024-10-15 | Tomasz Jeznach | iommu/riscv: Paging domain support |
| [de8c663e](https://github.com/RVCK-Project/rvck/commit/de8c663ed44350c87786360475584919a20daa76) | 2024-10-15 | Tomasz Jeznach | iommu/riscv: Command and fault queue support |
| [1f05e12c](https://github.com/RVCK-Project/rvck/commit/1f05e12ce68195735f6ce13382693aed5205ab6f) | 2024-10-15 | Tomasz Jeznach | iommu/riscv: Device directory management. |
| [2330eb69](https://github.com/RVCK-Project/rvck/commit/2330eb69e623080d03be7c3a54d492b6fefb0996) | 2024-10-15 | Tomasz Jeznach | iommu/riscv: Enable IOMMU registration and device probe. |
| [140f04e8](https://github.com/RVCK-Project/rvck/commit/140f04e8b67c5f8778967ed1c8e9e860577abb3f) | 2024-10-15 | Tomasz Jeznach | iommu/riscv: Add RISC-V IOMMU PCIe device driver |
| [371885a5](https://github.com/RVCK-Project/rvck/commit/371885a535850bd24ce49c96aec655b74e087841) | 2024-10-15 | Tomasz Jeznach | iommu/riscv: Add RISC-V IOMMU platform device driver |
| [83a2aa31](https://github.com/RVCK-Project/rvck/commit/83a2aa3164e87d37cbadebc085b936f000e66672) | 2024-10-15 | Tomasz Jeznach | dt-bindings: iommu: riscv: Add bindings for RISC-V IOMMU |
| [0b8f7b9f](https://github.com/RVCK-Project/rvck/commit/0b8f7b9f21ff2950fee556b8aa1e0ae9e985d8e6) | 2024-04-13 | Pasha Tatashin | iommu/vt-d: add wrapper functions for page allocations |
| [e136b0b2](https://github.com/RVCK-Project/rvck/commit/e136b0b2da1d30355babd4cc6aefce44a3239e6e) | 2024-02-16 | Krzysztof Kozlowski | iommu: constify of_phandle_args in xlate |
| [5334472e](https://github.com/RVCK-Project/rvck/commit/5334472ea2783f61bdf32dcaf6a3372894fb15b7) | 2023-11-22 | Matt Coster | sizes.h: Add entries between SZ_32G and SZ_64T |
| [f3b94a29](https://github.com/RVCK-Project/rvck/commit/f3b94a291a449cc7c1d011e7fc8f182f0d85fe5c) | 2024-03-05 | Lu Baolu | iommu: Add static iommu_ops-\>release_domain |
| [e74efb07](https://github.com/RVCK-Project/rvck/commit/e74efb073c4a286598646d91f838ad6b4487d0ad) | 2023-09-27 | Jason Gunthorpe | iommufd: Convert to alloc_domain_paging() |
| [aec8b750](https://github.com/RVCK-Project/rvck/commit/aec8b750c320b161528a0f3d1074c7db9a8c832a) | 2024-04-13 | Pasha Tatashin | iommu: Move IOMMU_DOMAIN_BLOCKED global statics to ops-\>blocked_domain |
| [c7fcd287](https://github.com/RVCK-Project/rvck/commit/c7fcd2875105364a3f929a4cd8a63e2db3be3e91) | 2024-07-17 | Alexandre Ghiti | riscv: Stop emitting preventive sfence.vma for new userspace mappings with Svvpt... |
| [c22d57c9](https://github.com/RVCK-Project/rvck/commit/c22d57c96169879cedfd2266be9c855e9905b256) | 2024-07-17 | Alexandre Ghiti | riscv: Stop emitting preventive sfence.vma for new vmalloc mappings |
| [8d607de9](https://github.com/RVCK-Project/rvck/commit/8d607de92255b5b5b6dcfb41c01c984d4cb13e12) | 2023-10-20 | Anup Patel | KVM: riscv: selftests: Add SBI DBCN extension to get-reg-list test |
| [70d741e3](https://github.com/RVCK-Project/rvck/commit/70d741e3b1c6f71f594c721cacf6b2cc1e314c32) | 2022-07-22 | Anup Patel | RISC-V: KVM: Forward SBI DBCN extension to user-space |
| [7d270be2](https://github.com/RVCK-Project/rvck/commit/7d270be230c5aa5158e08003e93a0853e9e25166) | 2023-10-11 | Anup Patel | RISC-V: KVM: Allow some SBI extensions to be disabled by default |
| [7ba4154d](https://github.com/RVCK-Project/rvck/commit/7ba4154d6c4b495b8b797f7a25fa0cc656fc8db9) | 2023-10-10 | Anup Patel | RISC-V: KVM: Change the SBI specification version to v2.0 |
| [9c79d743](https://github.com/RVCK-Project/rvck/commit/9c79d7439269da65ff8d2b93d7fc9bdcf9e7003f) | 2022-07-22 | Anup Patel | RISC-V: Add defines for SBI debug console extension |
| [5dfe7d28](https://github.com/RVCK-Project/rvck/commit/5dfe7d281d9c4387d95df9c0f9a3f2f9a2becd33) | 2023-11-24 | Anup Patel | RISC-V: Enable SBI based earlycon support |
| [b8d69a60](https://github.com/RVCK-Project/rvck/commit/b8d69a60b681b4900f913ff03e2dad8cd8cd3c86) | 2023-11-24 | Atish Patra | tty: Add SBI debug console support to HVC SBI driver |
| [b7380373](https://github.com/RVCK-Project/rvck/commit/b73803739767e94f332c0b37c5fcf2b4579df33c) | 2023-11-24 | Anup Patel | tty/serial: Add RISC-V SBI debug console based earlycon |
| [5d1a6ad5](https://github.com/RVCK-Project/rvck/commit/5d1a6ad52eeb54ced86df125b43333b28d10a642) | 2023-11-24 | Anup Patel | RISC-V: Add SBI debug console helper routines |
| [71a08673](https://github.com/RVCK-Project/rvck/commit/71a086734a627c184ab156973caf10cba441901b) | 2023-11-24 | Anup Patel | RISC-V: Add stubs for sbi_console_putchar/getchar() |
| [43571df2](https://github.com/RVCK-Project/rvck/commit/43571df256de09f8274444375a251b826be897df) | 2024-04-03 | Björn Töpel | riscv: Fix vector state restore in rt_sigreturn() |
| [28eee47d](https://github.com/RVCK-Project/rvck/commit/28eee47d9e5b9ada2cd48cb7dc9afcadd19f9853) | 2024-01-15 | Andy Chiu | riscv: vector: allow kernel-mode Vector with preemption |
| [1fcc7cd6](https://github.com/RVCK-Project/rvck/commit/1fcc7cd61b23e41dc7b2cb3293a61f21045db291) | 2024-01-15 | Andy Chiu | riscv: vector: use kmem_cache to manage vector context |
| [c4a233f2](https://github.com/RVCK-Project/rvck/commit/c4a233f2841d7292d7770d104466bdc7e117a0ec) | 2024-01-15 | Andy Chiu | riscv: vector: use a mask to write vstate_ctrl |
| [ede73720](https://github.com/RVCK-Project/rvck/commit/ede7372084db1db6f96dc778ba41dad6e8d42284) | 2024-01-15 | Andy Chiu | riscv: vector: do not pass task_struct into riscv_v_vstate_{save,restore}() |
| [b4c30ccf](https://github.com/RVCK-Project/rvck/commit/b4c30ccf7d428c0e4a39ca4b0c58772232284b38) | 2024-01-15 | Andy Chiu | riscv: fpu: drop SR_SD bit checking |
| [8fc95662](https://github.com/RVCK-Project/rvck/commit/8fc95662176884ed2145e5a00f143cdb82674188) | 2024-01-15 | Andy Chiu | riscv: lib: vectorize copy_to_user/copy_from_user |
| [1b5d0d67](https://github.com/RVCK-Project/rvck/commit/1b5d0d675cec0ccc653672e4f5a418140f47c442) | 2024-01-15 | Andy Chiu | riscv: sched: defer restoring Vector context for user |
| [708651d2](https://github.com/RVCK-Project/rvck/commit/708651d2cb7759fcd84853db504672527dc1d272) | 2024-01-15 | Greentime Hu | riscv: Add vector extension XOR implementation |
| [7955960e](https://github.com/RVCK-Project/rvck/commit/7955960e9129e64ac7f5990e43f567b232cf2b20) | 2024-01-15 | Andy Chiu | riscv: vector: make Vector always available for softirq context |
| [8616e8a8](https://github.com/RVCK-Project/rvck/commit/8616e8a8a7a267e7cda225dd3b81ef1eaaec548e) | 2024-01-15 | Greentime Hu | riscv: Add support for kernel mode vector |
| [752319f8](https://github.com/RVCK-Project/rvck/commit/752319f8625400c7cdd8e57434a51fd028ec6adb) | 2023-10-24 | Clément Léger | riscv: kernel: Use correct SYM_DATA_*() macro for data |
| [6c27f625](https://github.com/RVCK-Project/rvck/commit/6c27f6254c8b518024f23197f8f4f00d9a20e925) | 2023-10-24 | Clément Léger | riscv: Use SYM_*() assembly macros instead of deprecated ones |
| [e1bdf9ff](https://github.com/RVCK-Project/rvck/commit/e1bdf9ff5ae446f3511410c43a7c51d5659cc4ca) | 2023-10-24 | Clément Léger | riscv: use ".L" local labels in assembly when applicable |
| [f7119539](https://github.com/RVCK-Project/rvck/commit/f7119539fd6e66bc787ce13c419330f2671f7eed) | 2024-11-03 | Alexandre Ghiti | riscv: Add qspinlock support |
| [17addce4](https://github.com/RVCK-Project/rvck/commit/17addce4d9ab140e272fa3d0e22c67f409431317) | 2024-11-03 | Alexandre Ghiti | riscv: Implement xchg8/16() using Zabha |
| [d557cc05](https://github.com/RVCK-Project/rvck/commit/d557cc058166d02c8de6cac40fe72d401963c754) | 2024-11-03 | Alexandre Ghiti | riscv: Implement arch_cmpxchg128() using Zacas |
| [2e552f68](https://github.com/RVCK-Project/rvck/commit/2e552f685523ce4539a8a0bb002327e33aad2e54) | 2024-11-03 | Alexandre Ghiti | riscv: Improve zacas fully-ordered cmpxchg() |
| [be972722](https://github.com/RVCK-Project/rvck/commit/be9727224486548e7c4c956923ea8016f6ab7886) | 2024-07-26 | Yong-Xuan Wang | RISC-V: KVM: Add Svade and Svadu Extensions Support for Guest/VM |
| [a73e82cb](https://github.com/RVCK-Project/rvck/commit/a73e82cb4ac175532e45f2c1e583ccc0811a7186) | 2024-10-16 | Samuel Holland | RISC-V: KVM: Allow Smnpm and Ssnpm extensions for guests |
| [dda2841e](https://github.com/RVCK-Project/rvck/commit/dda2841edfce6abb19dd500e240e69c8ba74a0f3) | 2024-04-26 | Andrew Jones | KVM: riscv: Support guest wrs.nto |
| [9bbce6b3](https://github.com/RVCK-Project/rvck/commit/9bbce6b3bf657eff4884da15f9e7409fa6276763) | 2024-06-19 | Clément Léger | RISC-V: KVM: Allow Zcmop extension for Guest/VM |
| [e33e8b52](https://github.com/RVCK-Project/rvck/commit/e33e8b524fb040a3545ab79cef135723ef3963dd) | 2024-06-19 | Clément Léger | RISC-V: KVM: Allow Zca, Zcf, Zcd and Zcb extensions for Guest/VM |
| [9f7cabca](https://github.com/RVCK-Project/rvck/commit/9f7cabcac913b7afa19357778dc9fdce144a3213) | 2024-06-19 | Clément Léger | RISC-V: KVM: Allow Zimop extension for Guest/VM |
| [47667ab4](https://github.com/RVCK-Project/rvck/commit/47667ab4da9c256b76611664c0fe1fce5ae654a6) | 2024-02-13 | Anup Patel | RISC-V: KVM: Allow Zacas extension for Guest/VM |
| [0e826968](https://github.com/RVCK-Project/rvck/commit/0e826968c8007a8d85dcc2670fe2d38e4527dd55) | 2024-02-13 | Anup Patel | RISC-V: KVM: Allow Ztso extension for Guest/VM |
| [6fb4c4de](https://github.com/RVCK-Project/rvck/commit/6fb4c4de3c73f0a87037eba06e2b1bbf2c437abd) | 2024-02-13 | Anup Patel | RISC-V: KVM: Forward SEED CSR access to user space |
| [642fcc2b](https://github.com/RVCK-Project/rvck/commit/642fcc2b86436153982edbea78d92e48632feac8) | 2023-11-27 | Anup Patel | RISC-V: KVM: Allow Zfa extension for Guest/VM |
| [dab51aa2](https://github.com/RVCK-Project/rvck/commit/dab51aa28424278b680ffbf1ee2afee818ff0288) | 2023-11-27 | Anup Patel | RISC-V: KVM: Allow Zvfh[min] extensions for Guest/VM |
| [120b4cbc](https://github.com/RVCK-Project/rvck/commit/120b4cbcd6695f20088fb4c403aa6a476af784c2) | 2023-11-27 | Anup Patel | RISC-V: KVM: Allow Zihintntl extension for Guest/VM |
| [ac953c40](https://github.com/RVCK-Project/rvck/commit/ac953c40e42af8feced272f594e06c618adc2452) | 2023-11-27 | Anup Patel | RISC-V: KVM: Allow Zfh[min] extensions for Guest/VM |
| [aa243d17](https://github.com/RVCK-Project/rvck/commit/aa243d17ba4175323d6c59bd930d0161ef21f234) | 2023-11-27 | Anup Patel | RISC-V: KVM: Allow vector crypto extensions for Guest/VM |
| [90848373](https://github.com/RVCK-Project/rvck/commit/90848373c9bc9fecf142707103f2e2f002ac1a1b) | 2023-11-27 | Anup Patel | RISC-V: KVM: Allow scalar crypto extensions for Guest/VM |
| [d8b722f0](https://github.com/RVCK-Project/rvck/commit/d8b722f07c706b7b70c2bdbc1796266274584066) | 2023-11-27 | Anup Patel | RISC-V: KVM: Allow Zbc extension for Guest/VM |
| [92825f08](https://github.com/RVCK-Project/rvck/commit/92825f088595c5cf3619ad5c3ce14fd0bd9875f5) | 2023-09-15 | Anup Patel | RISC-V: KVM: Allow Zicond extension for Guest/VM |
| [3aa576fa](https://github.com/RVCK-Project/rvck/commit/3aa576faeaf0834aeb29eb829ea465ca9422cff9) | 2023-11-12 | Xiao Wang | riscv: Optimize hweight API with Zbb extension |
| [310a7436](https://github.com/RVCK-Project/rvck/commit/310a7436ec91580f83b0a65a6d98b1fc71b3a68f) | 2023-10-31 | Xiao Wang | riscv: Optimize bitops with Zbb extension |
| [69555ab5](https://github.com/RVCK-Project/rvck/commit/69555ab57080bf5de040d9940e83445a27835f04) | 2024-06-21 | Xiao Wang | riscv: Optimize crc32 with Zbc extension |
| [cbb95eba](https://github.com/RVCK-Project/rvck/commit/cbb95ebaf45ddec71e26f83a2f7ff9cd66128b90) | 2025-02-28 | Robin Murphy | iommu: Handle race with default domain setup |
| [fa04c8e4](https://github.com/RVCK-Project/rvck/commit/fa04c8e48602e5e405fbb419c9d7bc6aa739fbe8) | 2023-10-03 | Jason Gunthorpe | iommu: Do not use IOMMU_DOMAIN_DMA if CONFIG_IOMMU_DMA is not enabled |
| [c1c46c34](https://github.com/RVCK-Project/rvck/commit/c1c46c349ce80a022aa17695ce3fbc44c31d3bfd) | 2023-09-13 | Jason Gunthorpe | iommu: Convert remaining simple drivers to domain_alloc_paging() |
| [af94d2d8](https://github.com/RVCK-Project/rvck/commit/af94d2d8f42d4a5812eb58dde7c48110c3e290dd) | 2023-09-13 | Jason Gunthorpe | iommu: Convert simple drivers with DOMAIN_DMA to domain_alloc_paging() |
| [8bf778e3](https://github.com/RVCK-Project/rvck/commit/8bf778e3cb05ca652c351798bbb526e7465b3231) | 2023-09-13 | Jason Gunthorpe | iommu: Add ops-\>domain_alloc_paging() |
| [c30c0226](https://github.com/RVCK-Project/rvck/commit/c30c022616af1a3cfe8d3ed1da2fabe7dc14ebdc) | 2023-09-13 | Jason Gunthorpe | iommu: Add __iommu_group_domain_alloc() |
| [d93cd234](https://github.com/RVCK-Project/rvck/commit/d93cd2347934e36e7c2eba3a47757f1c24d6ff9c) | 2023-09-13 | Jason Gunthorpe | iommu: Require a default_domain for all iommu drivers |
| [6d5fd48a](https://github.com/RVCK-Project/rvck/commit/6d5fd48a0c0b4a99f2031ccfe92553d709ca1542) | 2023-09-13 | Jason Gunthorpe | iommu/sun50i: Add an IOMMU_IDENTITIY_DOMAIN |
| [6d081da8](https://github.com/RVCK-Project/rvck/commit/6d081da81efcfd2ed668a8820481d4280700c520) | 2023-09-13 | Jason Gunthorpe | iommu/mtk_iommu: Add an IOMMU_IDENTITIY_DOMAIN |
| [7484af74](https://github.com/RVCK-Project/rvck/commit/7484af745226180a685f7aec83a1c54e871d0368) | 2023-09-13 | Jason Gunthorpe | iommu/ipmmu: Add an IOMMU_IDENTITIY_DOMAIN |
| [eee82f8c](https://github.com/RVCK-Project/rvck/commit/eee82f8c8538474879a7f46dd0ca01e231fec145) | 2023-09-13 | Jason Gunthorpe | iommu/qcom_iommu: Add an IOMMU_IDENTITIY_DOMAIN |
| [8cf3452a](https://github.com/RVCK-Project/rvck/commit/8cf3452a50c1b59b6559f8276264207692a1ec3b) | 2023-09-13 | Jason Gunthorpe | iommu: Remove ops-\>set_platform_dma_ops() |
| [229841c2](https://github.com/RVCK-Project/rvck/commit/229841c2a010646b8e3c4129b62b47476b8762d5) | 2023-09-13 | Jason Gunthorpe | iommu/msm: Implement an IDENTITY domain |
| [4c198e33](https://github.com/RVCK-Project/rvck/commit/4c198e335d4e1d311cee444c7e3da93f3aa7388a) | 2023-09-13 | Jason Gunthorpe | iommu/omap: Implement an IDENTITY domain |
| [0c793e4c](https://github.com/RVCK-Project/rvck/commit/0c793e4cae7946a3376366e1aa72e27a81ecbd91) | 2023-09-13 | Jason Gunthorpe | iommu/tegra-smmu: Support DMA domains in tegra |
| [29c1afa3](https://github.com/RVCK-Project/rvck/commit/29c1afa3fec1ccb74cb2b8fcfc4863995d940b48) | 2023-09-13 | Jason Gunthorpe | iommu/tegra-smmu: Implement an IDENTITY domain |
| [122be213](https://github.com/RVCK-Project/rvck/commit/122be2134bd4d593ca2d14f311a638c78be1670e) | 2023-09-13 | Jason Gunthorpe | iommu/exynos: Implement an IDENTITY domain |
| [caa7465e](https://github.com/RVCK-Project/rvck/commit/caa7465edb5da18d9a88b6a39174ef0c9b51c941) | 2023-09-13 | Jason Gunthorpe | iommu: Allow an IDENTITY domain as the default_domain in ARM32 |
| [65c072e1](https://github.com/RVCK-Project/rvck/commit/65c072e124a792a636ea8e63b7816d23f9a4a0ab) | 2023-09-13 | Jason Gunthorpe | iommu: Reorganize iommu_get_default_domain_type() to respect def_domain_type() |
| [5a59c96a](https://github.com/RVCK-Project/rvck/commit/5a59c96a71aaede6f4508c5eeecac5fe1c056825) | 2023-09-13 | Jason Gunthorpe | iommu/mtk_iommu_v1: Implement an IDENTITY domain |
| [812ffa04](https://github.com/RVCK-Project/rvck/commit/812ffa047ad55b7fe8f345ddf132a38967eb9074) | 2023-09-13 | Jason Gunthorpe | iommu/fsl_pamu: Implement a PLATFORM domain |
| [8033c612](https://github.com/RVCK-Project/rvck/commit/8033c6127cde051d14597072bbafb337bd9a180f) | 2023-09-13 | Jason Gunthorpe | iommu: Add IOMMU_DOMAIN_PLATFORM for S390 |
| [ed2ca1b2](https://github.com/RVCK-Project/rvck/commit/ed2ca1b2bbe53dd2433a20deb62dcaaf85fa9d1c) | 2023-09-13 | Jason Gunthorpe | iommu: Add IOMMU_DOMAIN_PLATFORM |
| [8a8ff74e](https://github.com/RVCK-Project/rvck/commit/8a8ff74ec2c21ec2d8d0d19be416ef9586ba7f82) | 2023-09-13 | Jason Gunthorpe | iommu: Add iommu_ops-\>identity_domain |
| [8fd04863](https://github.com/RVCK-Project/rvck/commit/8fd04863002bb35d47b61aa59e5b6016b70de23a) | 2025-07-29 | gaorui | Revert "iommu: Handle race with default domain setup" |
| [ae7f8e6c](https://github.com/RVCK-Project/rvck/commit/ae7f8e6c76b28e6562b9bb2835aa10c64487cf2c) | 2024-04-09 | Baoquan He | kexec: fix the unexpected kexec_dprintk() macro |
| [295bdb0e](https://github.com/RVCK-Project/rvck/commit/295bdb0edf45d2f89733b77c3cda500aa954ccd1) | 2024-07-30 | Sunil V L | kexec_file, parisc: print out debugging message if required |
| [fe98710e](https://github.com/RVCK-Project/rvck/commit/fe98710e063acc321e98527141b3bd9a1e9315c9) | 2023-12-13 | Baoquan He | kexec_file, power: print out debugging message if required |
| [6abc778a](https://github.com/RVCK-Project/rvck/commit/6abc778a6e3d241d0e562859c1413c4ff8d32804) | 2023-12-13 | Baoquan He | kexec_file, riscv: print out debugging message if required |
| [b930395b](https://github.com/RVCK-Project/rvck/commit/b930395bafab62ffe1c783ddbbe8bd8116dfe4b9) | 2023-12-13 | Baoquan He | kexec_file, arm64: print out debugging message if required |
| [e33defdb](https://github.com/RVCK-Project/rvck/commit/e33defdb16476db3b90fd8d2f821b1733b5d97f9) | 2023-12-13 | Baoquan He | kexec_file, x86: print out debugging message if required |
| [71c55262](https://github.com/RVCK-Project/rvck/commit/71c5526234a27f88faeb884bac12bf25b6e91ce1) | 2023-12-13 | Baoquan He | kexec_file: print out debugging message if required |
| [58d7ffef](https://github.com/RVCK-Project/rvck/commit/58d7ffefe96cafb8a794d3494007ed984381983d) | 2023-12-13 | Baoquan He | kexec_file: add kexec_file flag to control debug printing |
| [f276ac65](https://github.com/RVCK-Project/rvck/commit/f276ac65f11a15ab8fe77897c889b2658c66ef24) | 2025-04-03 | Radim Krčmář | KVM: RISC-V: reset smstateen CSRs |
| [aa984da6](https://github.com/RVCK-Project/rvck/commit/aa984da63cecc731d9d0b8010d5b0f64683cd185) | 2023-12-24 | Anup Patel | RISC-V: KVM: Fix indentation in kvm_riscv_vcpu_set_reg_csr() |
| [8febb0b2](https://github.com/RVCK-Project/rvck/commit/8febb0b290d8b24b132a77c93c5f2f625e2f9ab0) | 2023-09-13 | Mayuresh Chitale | RISCV: KVM: Add sstateen0 to ONE_REG |
| [fe47c8ab](https://github.com/RVCK-Project/rvck/commit/fe47c8ab2a9b8ef4d83941820217d31ae72c8a22) | 2023-09-13 | Mayuresh Chitale | RISCV: KVM: Add sstateen0 context save/restore |
| [643db4be](https://github.com/RVCK-Project/rvck/commit/643db4befc7b74ca3511f600365834934bc485ec) | 2023-09-13 | Mayuresh Chitale | RISCV: KVM: Add senvcfg context save/restore |
| [b630a41f](https://github.com/RVCK-Project/rvck/commit/b630a41f7f47e17d874a00710338d1f8a9779c1b) | 2023-09-13 | Mayuresh Chitale | RISC-V: KVM: Enable Smstateen accesses |
| [d47b59fd](https://github.com/RVCK-Project/rvck/commit/d47b59fdc6dbb2479931cbf32232475a73e06884) | 2023-09-13 | Mayuresh Chitale | RISC-V: KVM: Add kvm_vcpu_config |
| [95c4746d](https://github.com/RVCK-Project/rvck/commit/95c4746df30ba40c4decb943ed18418979232610) | 2024-07-30 | Sunil V L | serial: 8250_platform: Enable generic 16550A platform devices |
| [6cac92e6](https://github.com/RVCK-Project/rvck/commit/6cac92e6583b11c091ce3d08fea2ba6c5e4117ac) | 2025-04-09 | Song Shuai | riscv: kexec_file: Support loading Image binary file |
| [79b3ed64](https://github.com/RVCK-Project/rvck/commit/79b3ed64c2277868aded8ecf118c295cf0adbf7d) | 2025-07-25 | gaorui | riscv: kexec_file: Split the loading of kernel and others |
| [e1418880](https://github.com/RVCK-Project/rvck/commit/e14188804dd30bbf50a1d63e43e989035bcf5986) | 2025-07-25 | gaorui | Revert "riscv: kexec: Add image loader for kexec file" |
| [a52c0a61](https://github.com/RVCK-Project/rvck/commit/a52c0a6163daa3b224742d55bca6d9a62e70e61c) | 2023-11-30 | Samuel Ortiz | RISC-V: Implement archrandom when Zkr is available |
| [ea0ffc5c](https://github.com/RVCK-Project/rvck/commit/ea0ffc5ccb36e563c9d35eebf7a860c685b1d954) | 2024-02-08 | Sunil V L | cpufreq: Move CPPC configs to common Kconfig and add RISC-V |
| [8baa79e4](https://github.com/RVCK-Project/rvck/commit/8baa79e4df1f35b15b985727e7213ec0ebd37f8b) | 2024-02-08 | Sunil V L | ACPI: RISC-V: Add CPPC driver |
| [bc871db4](https://github.com/RVCK-Project/rvck/commit/bc871db43b1d34261e5666ace978bd9d5573e6bf) | 2024-06-17 | Yunhui Cui | RISC-V: Select ACPI PPTT drivers |
| [87e976b7](https://github.com/RVCK-Project/rvck/commit/87e976b7077cefd87038ce690bcf71eb3d53e523) | 2024-05-02 | Sia Jee Heng | RISC-V: ACPI: Enable SPCR table for console output on RISC-V |
| [64378cdd](https://github.com/RVCK-Project/rvck/commit/64378cddac362b0c8b9bed7f3e94057d7772fffe) | 2024-07-18 | Ryo Takakura | RISC-V: Enable IPI CPU Backtrace |
| [9adb6ce6](https://github.com/RVCK-Project/rvck/commit/9adb6ce6acc36ebc7a7fad64ec74d678dafeeb73) | 2024-06-13 | Haibo Xu | riscv: dmi: Add SMBIOS/DMI support |
| [878af5df](https://github.com/RVCK-Project/rvck/commit/878af5df025cf7b215dfd95258948e6d01a69cbc) | 2024-06-13 | Haibo Xu | ACPI: NUMA: replace pr_info with pr_debug in arch_acpi_numa_init |
| [0b66c7ce](https://github.com/RVCK-Project/rvck/commit/0b66c7cead28e8badd88892ab0bb242835c4a066) | 2025-04-25 | gaorui | ACPI: NUMA: change the ACPI_NUMA to a hidden option |
| [da676eab](https://github.com/RVCK-Project/rvck/commit/da676eab24b0fabfd9412c88e69820b72331b3f9) | 2025-04-25 | gaorui | ACPI: NUMA: Make some NUMA-related functions available for RISC-V |
| [564a70dd](https://github.com/RVCK-Project/rvck/commit/564a70ddfd4caf7ce94097ad256483d4c2f5ef70) | 2024-06-13 | Haibo Xu | ACPI: NUMA: Add handler for SRAT RINTC affinity structure |
| [9b283892](https://github.com/RVCK-Project/rvck/commit/9b2838923537051d7d1618df5183dbd792e58e78) | 2024-06-13 | Haibo Xu | ACPI: RISCV: Add NUMA support based on SRAT and SLIT |
| [aadb0bee](https://github.com/RVCK-Project/rvck/commit/aadb0bee7df8cddd8169e8025218753e59b2bc8e) | 2024-01-17 | Haibo Xu | ACPICA: SRAT: Add RISC-V RINTC affinity structure |
---

**共 252 条提交（显示全部）**

[分页显示](中兴通讯.md) | [纯文本视图](中兴通讯_commits.txt)
## 🔙 返回

[← 返回统计主页](../index.md)

---

*本页面最后更新于 2026-03-04 22:05:14*
*数据来源: 主分支 tmp-stats@ce238702*
