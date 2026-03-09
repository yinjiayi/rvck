# 中兴通讯 贡献画像

<div style="background-color: #FF980020; padding: 15px; border-radius: 8px; border-left: 5px solid #FF9800;">
<p><strong>📊 核心数据</strong></p>
<ul>
<li><strong>贡献提交数</strong>: 256 (占所有机构贡献的 23.0%)</li>
<li><strong>最活跃领域</strong>: 主线反合(backport) (234 个提交)</li>
<li><strong>统计周期</strong>: v6.6.127 → 3c705a33</li>
<li><strong>生成时间</strong>: 2026-03-09 21:51:52</li>
</ul>
</div>

## 📈 贡献分布

| 贡献维度 | 数量 | 占比 | 说明 |
|----------|------|------|------|
| 新功能 | 201 | ███████░░░ 78.5% | 新增功能特性 |
| 缺陷修复 | 53 | ██░░░░░░░░ 20.7% | 修复代码缺陷 |
| 代码清理 | 0 | ░░░░░░░░░░ 0.0% | 重构和优化 |
| 配置变更 | 2 | ░░░░░░░░░░ 0.8% | 配置项调整 |
| 其他贡献 | 0 | ░░░░░░░░░░ 0.0% | 未分类提交 |
| 主线反合 | 234 | █████████░ 91.4% | 同步主线代码 |
| 硬件支持 | 0 | ░░░░░░░░░░ 0.0% | 硬件平台适配 |

> 💡 **说明**: 分类标签存在交叉，同一提交可能同时属于多个分类（如 feature+backport+hardware）。
> 因此各维度数量之和可能大于总提交数（256）。

### 🔧 硬件支持详情

*暂无硬件支持数据*

## 📧 识别规则

- **邮箱后缀**: @zte.com.cn

## 📋 提交列表

| 提交哈希 | 日期 | 原始作者 | 标题 |
|----------|------|----------|------|
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

**共 256 条提交，显示 201-256**

[1](中兴通讯.md) **[2]**

[显示全部](中兴通讯_all.md) | [纯文本视图](中兴通讯_commits.txt)
## 🔙 返回

[← 返回统计主页](../index.md)

---

*本页面最后更新于 2026-03-09 21:51:52*
*数据来源: 主分支 tmp-stats@3c705a33*
