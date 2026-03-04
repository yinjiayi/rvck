# 软件所 贡献详情

<div style="background-color: #FF980020; padding: 15px; border-radius: 8px; border-left: 5px solid #FF9800;">
<p><strong>📊 统计信息</strong></p>
<ul>
<li><strong>贡献提交数</strong>: 252</li>
<li><strong>backport提交数</strong>: 133</li>
<li><strong>统计时间</strong>: 2026-03-04 21:03:03</li>
<li><strong>主分支</strong>: tmp-stats</li>
<li><strong>起始标签</strong>: v6.6.127</li>
</ul>
</div>

## 📁 补丁分类统计

- feature: 202
- bugfix: 44
- cleanup: 5
- other: 1

### 硬件支持分布

- th1520: 55
- sg2042: 2

## 📧 识别规则

- **邮箱后缀**: @iscas.ac.cn, @isrc.iscas.ac.cn
- **特定签名**: Weihao Li <ieiao@outlook.com>

## 📋 提交列表

| 提交哈希 | 日期 | 原始作者 | 标题 |
|----------|------|----------|------|
| [a8fb171e](https://github.com/RVCK-Project/rvck/commit/a8fb171ea894a69a2ccf925defe52fb25fa42c21) | 2025-12-11 | Mingzheng Xing | th1520-i2s: Fix kernel panic when reading sysfs registers |
| [02d50086](https://github.com/RVCK-Project/rvck/commit/02d500867b4c309a436507e5cf5a29b0bc8f2cc9) | 2025-02-26 | Yunhui Cui | RISC-V: hwprobe: Expose Zicbom extension and its block size |
| [6bc34119](https://github.com/RVCK-Project/rvck/commit/6bc34119ae68f563fa1aa2cd83c373fbdb6f4585) | 2024-09-13 | Miquel Sabaté Solà | riscv: hwprobe: export Zicntr and Zihpm extensions |
| [e101b4b3](https://github.com/RVCK-Project/rvck/commit/e101b4b3d3e0aa09591b51abca204f724e816b27) | 2024-12-24 | Quan Zhou | RISC-V: KVM: Redirect instruction access fault trap to guest |
| [b0b16d0e](https://github.com/RVCK-Project/rvck/commit/b0b16d0e664cdf90041cc48265d05a885737ccd6) | 2023-10-05 | Benjamin Tissoires | selftests/hid: force using our compiled libbpf headers |
| [964d10c3](https://github.com/RVCK-Project/rvck/commit/964d10c3fef27bbb2289e75ecf8c3d6528cfb0df) | 2023-10-05 | Benjamin Tissoires | selftests/hid: do not manually call headers_install |
| [c9fd1c72](https://github.com/RVCK-Project/rvck/commit/c9fd1c72770976675de452be1837f74022ac5447) | 2023-10-05 | Benjamin Tissoires | selftests/hid: ensure we can compile the tests on kernels pre-6.3 |
| [dfe5729e](https://github.com/RVCK-Project/rvck/commit/dfe5729ea9391c50d6d8c40d3c93c296cbff30cd) | 2024-12-02 | Quan Zhou | RISC-V: KVM: Allow Ziccrse extension for Guest/VM |
| [1f51f7be](https://github.com/RVCK-Project/rvck/commit/1f51f7be23c48368a387d2245ae7e0a8b811d402) | 2024-12-02 | Quan Zhou | RISC-V: KVM: Allow Zabha extension for Guest/VM |
| [7df8d155](https://github.com/RVCK-Project/rvck/commit/7df8d155902e8510d853a0b71559beffbeba3c9d) | 2024-12-02 | Quan Zhou | RISC-V: KVM: Allow Svvptc extension for Guest/VM |
| [eef4ae99](https://github.com/RVCK-Project/rvck/commit/eef4ae9918676a792b9a322b164ee79b01bdf038) | 2023-10-12 | Björn Töpel | riscv, qemu_fw_cfg: Add support for RISC-V architecture |
| [63fd6635](https://github.com/RVCK-Project/rvck/commit/63fd66353753f85a630b38a90e4baa979a8655a9) | 2025-08-19 | Yafen Fang | xuantie: nna: select SYNC_FILE |
| [d82ab91d](https://github.com/RVCK-Project/rvck/commit/d82ab91d51526fe307303292f15078fbec4255e8) | 2024-02-22 | Yu Chien Peter Lin | riscv: errata: Rename defines for Andes |
| [f8599ba5](https://github.com/RVCK-Project/rvck/commit/f8599ba5b21095abae92de8da546a7302a793691) | 2024-11-03 | Alexandre Ghiti | riscv: Move cpufeature.h macros into their own header |
| [5d36b008](https://github.com/RVCK-Project/rvck/commit/5d36b008d69a3297c42de7ea2d809e6b4368aeed) | 2024-07-19 | Charlie Jenkins | riscv: cpufeature: Extract common elements from extension checking |
| [544ceb83](https://github.com/RVCK-Project/rvck/commit/544ceb83065b5036935708becdbb3deb3fa36dc5) | 2024-07-19 | Charlie Jenkins | riscv: Introduce vendor variants of extension helpers |
| [5d8ab77d](https://github.com/RVCK-Project/rvck/commit/5d8ab77d739d58f96e39f4f41294d3dd7c24316e) | 2024-07-17 | Conor Dooley | RISC-V: hwprobe: sort EXT_KEY()s in hwprobe_isa_ext0() alphabetically |
| [a63ff926](https://github.com/RVCK-Project/rvck/commit/a63ff926b33e125414e2bad2c6d52a2310450e58) | 2024-10-16 | Samuel Holland | riscv: hwprobe: Export the Supm ISA extension |
| [8214dc1f](https://github.com/RVCK-Project/rvck/commit/8214dc1ff2a1d6cfe8de6f851879935ed5359144) | 2024-07-02 | Palmer Dabbelt | RISC-V: Provide the frequency of time CSR via hwprobe |
| [722884d7](https://github.com/RVCK-Project/rvck/commit/722884d73102a833e5f32c7bb0e1c0f0a0231a72) | 2024-04-26 | Andrew Jones | riscv: hwprobe: export Zawrs ISA extension |
| [5200eace](https://github.com/RVCK-Project/rvck/commit/5200eacea2ee3a47f072d701847f638c43a5b224) | 2024-04-10 | Clément Léger | riscv: hwprobe: export highest virtual userspace address |
| [fd4292df](https://github.com/RVCK-Project/rvck/commit/fd4292dfea0c61a5a4afdc85a24d7168a8efbdd3) | 2024-06-19 | Clément Léger | riscv: hwprobe: export Zcmop ISA extension |
| [bc96f196](https://github.com/RVCK-Project/rvck/commit/bc96f196485bb4298c778e34fb2a7c424cd89345) | 2024-06-19 | Clément Léger | riscv: hwprobe: export Zca, Zcf, Zcd and Zcb ISA extensions |
| [eed69c1b](https://github.com/RVCK-Project/rvck/commit/eed69c1b56879d522b09c9b405c56b54796391b7) | 2024-06-19 | Clément Léger | riscv: hwprobe: export Zimop ISA extension |
| [926178ae](https://github.com/RVCK-Project/rvck/commit/926178aef770fec18ef67bac6a8fc6c1750c66a8) | 2024-05-10 | Andy Chiu | riscv: hwprobe: add zve Vector subextensions into hwprobe interface |
| [91374f60](https://github.com/RVCK-Project/rvck/commit/91374f60b66aefd407527aa6fe0d3fabc405d6ab) | 2024-02-21 | Clément Léger | riscv: hwprobe: export Zihintpause ISA extension |
| [40cb79dd](https://github.com/RVCK-Project/rvck/commit/40cb79ddc32115b9cb4d10519e6335545f2f4bcf) | 2023-11-22 | Andrew Jones | RISC-V: Move the hwprobe syscall to its own file |
| [f5a7d2a0](https://github.com/RVCK-Project/rvck/commit/f5a7d2a073c525705df6971f540a632f8fffbe4c) | 2024-04-09 | Clément Léger | riscv: hwprobe: fix invalid sign extension for RISCV_HWPROBE_EXT_ZVFHMIN |
| [48c8e35e](https://github.com/RVCK-Project/rvck/commit/48c8e35e143203615522809c3bf5659277f25bf0) | 2023-12-20 | Clément Léger | riscv: hwprobe: export Zicond extension |
| [f041beba](https://github.com/RVCK-Project/rvck/commit/f041beba35737c58a5cb9349197618e985e230bb) | 2023-12-20 | Clément Léger | riscv: hwprobe: export Zacas ISA extension |
| [063ab482](https://github.com/RVCK-Project/rvck/commit/063ab482697d6a5119a9b23264afcdd64467e99b) | 2023-12-20 | Clément Léger | riscv: hwprobe: export Ztso ISA extension |
| [20e7208c](https://github.com/RVCK-Project/rvck/commit/20e7208c5f4212f9e5211e07797f54da143e4a94) | 2023-11-22 | Andrew Jones | RISC-V: hwprobe: Introduce which-cpus flag |
| [64ae5bee](https://github.com/RVCK-Project/rvck/commit/64ae5beef33a3a853d4bad3bdda735355d94d634) | 2023-11-22 | Andrew Jones | RISC-V: hwprobe: Clarify cpus size parameter |
| [d4ee9485](https://github.com/RVCK-Project/rvck/commit/d4ee9485a4ab2a3859d587c41607d8241e0cb2b3) | 2023-09-18 | Andrew Jones | RISC-V: selftests: Add CBO tests |
| [05d31cd3](https://github.com/RVCK-Project/rvck/commit/05d31cd34c480f2e50d4efa0ada937f661872a92) | 2023-09-18 | Andrew Jones | RISC-V: selftests: Convert hwprobe test to kselftest API |
| [4cdcf47c](https://github.com/RVCK-Project/rvck/commit/4cdcf47ca413da94b865f8e3d28b5c67cde35ce0) | 2023-09-18 | Andrew Jones | RISC-V: selftests: Statically link hwprobe test |
| [2c86d384](https://github.com/RVCK-Project/rvck/commit/2c86d384ab5e083ffa429e4e2863cc765190e4fb) | 2023-11-14 | Clément Léger | riscv: hwprobe: export Zfa ISA extension |
| [0cfae608](https://github.com/RVCK-Project/rvck/commit/0cfae608eff7cc3c176f43ad06931b21cfa4ddf9) | 2023-11-14 | Clément Léger | riscv: hwprobe: export Zvfh[min] ISA extensions |
| [c8b4844b](https://github.com/RVCK-Project/rvck/commit/c8b4844bf6370274a13977bf9f976010a14bf665) | 2023-11-14 | Clément Léger | riscv: hwprobe: export Zhintntl ISA extension |
| [2fd3a955](https://github.com/RVCK-Project/rvck/commit/2fd3a95524adfc2387175574393a349f89c74db2) | 2023-11-14 | Clément Léger | riscv: hwprobe: export Zfh[min] ISA extensions |
| [7a4beb08](https://github.com/RVCK-Project/rvck/commit/7a4beb085a64f94e8669508f1d26f1cea028c3e4) | 2023-11-14 | Clément Léger | riscv: hwprobe: export vector crypto ISA extensions |
| [f78e3afd](https://github.com/RVCK-Project/rvck/commit/f78e3afdc6c328e2c5dba993a49f96c7e5cd7adf) | 2023-11-14 | Clément Léger | riscv: hwprobe: add support for scalar crypto ISA extensions |
| [8f3fabb9](https://github.com/RVCK-Project/rvck/commit/8f3fabb90c491126a7587d541f262cac0466ea99) | 2023-11-14 | Clément Léger | riscv: hwprobe: export missing Zbc ISA extension |
| [1ded924c](https://github.com/RVCK-Project/rvck/commit/1ded924c0b4aa60a500edd16a37c9cee6ee2fc59) | 2023-09-30 | Costa Shulyupin | docs: move riscv under arch |
| [592f1789](https://github.com/RVCK-Project/rvck/commit/592f178903d5ae9c3f01ca6dc0e93b8df35dcf78) | 2023-09-18 | Andrew Jones | RISC-V: hwprobe: Expose Zicboz extension and its block size |
| [ae6b444f](https://github.com/RVCK-Project/rvck/commit/ae6b444fb5d2d503daf421c4c869700fc5f83c9e) | 2024-07-26 | Yong-Xuan Wang | RISC-V: Add Svade and Svadu Extensions Support |
| [d009160d](https://github.com/RVCK-Project/rvck/commit/d009160d4ad3eac638c9870e5689cf5d6955f029) | 2024-11-03 | Alexandre Ghiti | riscv: Add ISA extension parsing for Ziccrse |
| [d1a144e8](https://github.com/RVCK-Project/rvck/commit/d1a144e8e46a41d6555b7c234fc1d29bfad3f4d8) | 2024-11-03 | Alexandre Ghiti | riscv: Implement cmpxchg8/16() using Zabha |
| [2e5659bf](https://github.com/RVCK-Project/rvck/commit/2e5659bfb91a7d34b02aef40c9361213484d628c) | 2024-11-03 | Alexandre Ghiti | riscv: Implement cmpxchg32/64() using Zacas |
| [7eeec773](https://github.com/RVCK-Project/rvck/commit/7eeec77390878d484c8e645e2f66c25d637a284a) | 2024-11-03 | Alexandre Ghiti | riscv: Do not fail to build on byte/halfword operations with Zawrs |
| [b64c3b23](https://github.com/RVCK-Project/rvck/commit/b64c3b23b44a5785535e27f3e71b0c51f2cd8bf0) | 2024-10-16 | Samuel Holland | riscv: Add ISA extension parsing for pointer masking |
| [3d6b9b3f](https://github.com/RVCK-Project/rvck/commit/3d6b9b3f444ae8d083626ffe5acc6a5d93808da1) | 2024-08-14 | Samuel Holland | riscv: Call riscv_user_isa_enable() only on the boot hart |
| [04bac914](https://github.com/RVCK-Project/rvck/commit/04bac91455dafb2f1e67cd435c7158b0c76bca87) | 2024-08-14 | Samuel Holland | riscv: Enable cbo.zero only when all harts support Zicboz |
| [722e777c](https://github.com/RVCK-Project/rvck/commit/722e777c794509081a2fc8f7045f3eb083621cc8) | 2024-03-12 | Samuel Holland | riscv: Do not save the scratch CSR during suspend |
| [67c7a3ea](https://github.com/RVCK-Project/rvck/commit/67c7a3ea2b378dd605d0b942962c4e272859e69a) | 2024-01-18 | Sunil V L | cpuidle: RISC-V: Move few functions to arch/riscv |
| [0e4f5486](https://github.com/RVCK-Project/rvck/commit/0e4f54869474a8927dbb1781bb92940f6e92bf50) | 2024-02-27 | Samuel Holland | riscv: Save/restore envcfg CSR during CPU suspend |
| [a2d36684](https://github.com/RVCK-Project/rvck/commit/a2d36684c6a81e52b2cbb782cd78415f88200e92) | 2024-07-17 | Alexandre Ghiti | riscv: Add ISA extension parsing for Svvptc |
| [d433ef9f](https://github.com/RVCK-Project/rvck/commit/d433ef9fde42c1b8adbc5400bd6ac5fae9fe8cee) | 2024-07-18 | Samuel Holland | riscv: cpufeature: Do not drop Linux-internal extensions |
| [99692919](https://github.com/RVCK-Project/rvck/commit/9969291936e1e50161d9896e29a4388f06b78d5d) | 2024-07-19 | Charlie Jenkins | riscv: Extend cpufeature.c to detect vendor extensions |
| [249dab92](https://github.com/RVCK-Project/rvck/commit/249dab9215b840c3429d75f162abb9935d251bd6) | 2024-04-26 | Andrew Jones | riscv: Provide a definition for 'pause' |
| [41cc3116](https://github.com/RVCK-Project/rvck/commit/41cc311679207995744cee5a7bff5a2f2328caea) | 2024-04-26 | Christoph Müllner | riscv: Add Zawrs support for spinlocks |
| [96ea2d94](https://github.com/RVCK-Project/rvck/commit/96ea2d94f65ac0d90e68a727a51d368b2780ef75) | 2024-05-30 | Alexandre Ghiti | riscv: Fix fully ordered LR/SC xchg[8\|16]() implementations |
| [0e781959](https://github.com/RVCK-Project/rvck/commit/0e781959758e8c2127c527a7129c278dcbbc2780) | 2024-03-25 | Jisheng Zhang | riscv: cmpxchg: implement arch_cmpxchg64_{relaxed\|acquire\|release} |
| [0463019f](https://github.com/RVCK-Project/rvck/commit/0463019feb0fe3300c1ba70b5ab30041b2084494) | 2024-01-03 | Leonardo Bras | riscv/cmpxchg: Implement xchg for variables of size 1 and 2 |
| [3b2a376c](https://github.com/RVCK-Project/rvck/commit/3b2a376c68dcd4d2fbc68ddae60171e7b127ea6a) | 2024-01-03 | Leonardo Bras | riscv/cmpxchg: Implement cmpxchg for variables of size 1 and 2 |
| [58da0efb](https://github.com/RVCK-Project/rvck/commit/58da0efb0e05cfc71020601163097684547dc70f) | 2024-01-03 | Leonardo Bras | riscv/cmpxchg: Deduplicate cmpxchg() asm and macros |
| [61975e3a](https://github.com/RVCK-Project/rvck/commit/61975e3a8ff81a28475732609b1c2dfdda632c74) | 2024-01-03 | Leonardo Bras | riscv/cmpxchg: Deduplicate xchg() asm functions |
| [aa8440ed](https://github.com/RVCK-Project/rvck/commit/aa8440edad0096b84a21d6e5986deae6a2e5a7c8) | 2024-02-17 | Eric Chan | riscv/barrier: Consolidate fence definitions |
| [b3254c6d](https://github.com/RVCK-Project/rvck/commit/b3254c6d51c903f29e5abd947f21633f823f3652) | 2024-02-17 | Eric Chan | riscv/barrier: Define RISCV_FULL_BARRIER |
| [493bad42](https://github.com/RVCK-Project/rvck/commit/493bad422699afb0d279c0907a6c2a84eb1dc55c) | 2024-06-19 | Clément Léger | riscv: add ISA extension parsing for Zcmop |
| [25b9fea0](https://github.com/RVCK-Project/rvck/commit/25b9fea07cda97e0ce97ab3311056026c8d2762e) | 2024-06-19 | Clément Léger | riscv: add ISA parsing for Zca, Zcf, Zcd and Zcb |
| [85a8fc95](https://github.com/RVCK-Project/rvck/commit/85a8fc956d7caaf73ad4fc3924036edb0dec38b7) | 2024-06-19 | Clément Léger | riscv: add ISA extensions validation callback |
| [a9534048](https://github.com/RVCK-Project/rvck/commit/a9534048d2b4c006f8862448ae798bcffed28b00) | 2024-06-19 | Clément Léger | riscv: add ISA extension parsing for Zimop |
| [2ee2cdce](https://github.com/RVCK-Project/rvck/commit/2ee2cdce5e5ab03e47b1c655a72c0e5c176740da) | 2024-05-10 | Andy Chiu | riscv: vector: adjust minimum Vector requirement to ZVE32X |
| [c9bceaee](https://github.com/RVCK-Project/rvck/commit/c9bceaeec79bae5755976b4adbbd5ee8ad09ec5d) | 2024-05-10 | Andy Chiu | riscv: cpufeature: add zve32[xf] and zve64[xfd] isa detection |
| [02522af4](https://github.com/RVCK-Project/rvck/commit/02522af4c96687fc49aaa6e7c8e6e40e9c076c19) | 2024-02-22 | Yu Chien Peter Lin | perf: RISC-V: Introduce Andes PMU to support perf event sampling |
| [8d7d0d9b](https://github.com/RVCK-Project/rvck/commit/8d7d0d9b55571fa105cd5b6b5c4be70a44ca9b0e) | 2024-02-22 | Yu Chien Peter Lin | perf: RISC-V: Eliminate redundant interrupt enable/disable operations |
| [eaae15b3](https://github.com/RVCK-Project/rvck/commit/eaae15b3aadaee8391efacd975113672ed51f32f) | 2024-05-10 | Andy Chiu | riscv: cpufeature: call match_isa_ext() for single-letter extensions |
| [0ee64ab9](https://github.com/RVCK-Project/rvck/commit/0ee64ab9ffb78275a3f7d22e64bef33de38d7f8b) | 2024-05-10 | Andy Chiu | riscv: vector: add a comment when calling riscv_setup_vsize() |
| [46730f81](https://github.com/RVCK-Project/rvck/commit/46730f8133ca46454a26a0961bae93034d6d4208) | 2024-05-02 | Charlie Jenkins | riscv: cpufeature: Fix extension subset checking |
| [2cd54147](https://github.com/RVCK-Project/rvck/commit/2cd54147ae396b46251e19201c8dbf3c8ed2da0a) | 2024-02-27 | Samuel Holland | riscv: Add a custom ISA extension for the [ms]envcfg CSR |
| [f18a9b46](https://github.com/RVCK-Project/rvck/commit/f18a9b461e8a78bb2f5fffc694e293a31c0fcfeb) | 2023-12-20 | Clément Léger | riscv: add ISA extension parsing for Zacas |
| [90b0cc26](https://github.com/RVCK-Project/rvck/commit/90b0cc2660674bf25162aecb47b57a36e22a388b) | 2023-12-20 | Clément Léger | riscv: add ISA extension parsing for Ztso |
| [d411e983](https://github.com/RVCK-Project/rvck/commit/d411e983fc1dcd92c34b180e021a1d798d8859de) | 2023-11-10 | Palmer Dabbelt | RISC-V: Remove the removed single-letter extensions |
| [18dd676f](https://github.com/RVCK-Project/rvck/commit/18dd676f17b1f29e9a76a7b15401d5d1c48f04e6) | 2023-11-14 | Clément Léger | riscv: add ISA extension parsing for Zfa |
| [6bacaa5a](https://github.com/RVCK-Project/rvck/commit/6bacaa5a292410eb43514a0dffde913a533dfe4f) | 2023-11-14 | Clément Léger | riscv: add ISA extension parsing for Zvfh[min] |
| [3ca323b1](https://github.com/RVCK-Project/rvck/commit/3ca323b1040a3f02c12a61d4c4c9a348e0c1b041) | 2023-11-14 | Clément Léger | riscv: add ISA extension parsing for Zihintntl |
| [414b1995](https://github.com/RVCK-Project/rvck/commit/414b19958142ca9136c223eb7bac7a639361864e) | 2023-11-14 | Clément Léger | riscv: add ISA extension parsing for Zfh/Zfh[min] |
| [e363321e](https://github.com/RVCK-Project/rvck/commit/e363321e882b2dd4e659d2212228d96a6a6e4da7) | 2023-11-14 | Clément Léger | riscv: add ISA extension parsing for vector crypto |
| [edeea415](https://github.com/RVCK-Project/rvck/commit/edeea4153f3e2d8c210c8107653ca377414aff7f) | 2023-11-14 | Evan Green | riscv: add ISA extension parsing for scalar crypto |
| [157cff04](https://github.com/RVCK-Project/rvck/commit/157cff049999dc078686a0defcdb6254ce225f31) | 2023-10-04 | Clément Léger | riscv: annotate check_unaligned_access_boot_cpu() with __init |
| [6735fa2a](https://github.com/RVCK-Project/rvck/commit/6735fa2a082d00b46e8e4458dd50f9e1ec67caa8) | 2023-07-26 | Tsukasa OI | RISC-V: clarify the QEMU workaround in ISA parser |
| [abe2c5dd](https://github.com/RVCK-Project/rvck/commit/abe2c5dd713d8e02a250908bef87a31c3f471cc3) | 2023-10-31 | Xiao Wang | riscv: Rearrange hwcap.h and cpufeature.h |
| [b6d7f92a](https://github.com/RVCK-Project/rvck/commit/b6d7f92ae39ee6edea5da3addd23625590d8d3e3) | 2023-11-14 | Clément Léger | riscv: add ISA extension parsing for Zbc |
| [f83cbcb1](https://github.com/RVCK-Project/rvck/commit/f83cbcb1398f0ea6861cdd7298db3b9e0fc4d653) | 2023-09-15 | Anup Patel | RISC-V: Detect Zicond from ISA string |
| [19495e96](https://github.com/RVCK-Project/rvck/commit/19495e96d64cd8f4bdd49ec023692be83954d0d4) | 2024-11-13 | Mingzheng Xing | th1520: npu: fix build error |
| [3b00e984](https://github.com/RVCK-Project/rvck/commit/3b00e984b81d43578480d88411936aadc7a4145b) | 2024-04-11 | Anup Patel | RISC-V: KVM: Use IMSIC guest files when available |
| [9fad4667](https://github.com/RVCK-Project/rvck/commit/9fad4667504e191506d114e370fc21b2659f2f1d) | 2024-04-11 | Anup Patel | RISC-V: KVM: Share APLIC and IMSIC defines with irqchip drivers |
| [42531cfb](https://github.com/RVCK-Project/rvck/commit/42531cfb516d05cb8250c1cb0e6a3480954d7d33) | 2025-02-12 | Mingzheng Xing | riscv: Kconfig: Enable amdkfd driver config |
| [57a36cd9](https://github.com/RVCK-Project/rvck/commit/57a36cd9362029d67dd85bbd71b40abeefbfac53) | 2025-01-10 | Mingzheng Xing | kconfig: fix kernel-mode FPU support |
| [f6491c2f](https://github.com/RVCK-Project/rvck/commit/f6491c2f0f984ce6bf90916ee6e7065315987480) | 2024-03-07 | Anup Patel | MAINTAINERS: Add entry for RISC-V AIA drivers |
| [1c757df1](https://github.com/RVCK-Project/rvck/commit/1c757df1b2a96364ad90e3f99c5d90f9ac730744) | 2024-03-07 | Anup Patel | RISC-V: Select APLIC and IMSIC drivers |
| [3f37b137](https://github.com/RVCK-Project/rvck/commit/3f37b1378664d551b252c3ecdd33b213626d86c4) | 2024-11-14 | Samuel Holland | irqchip/riscv-aplic: Prevent crash when MSI domain is missing |
| [7ce26304](https://github.com/RVCK-Project/rvck/commit/7ce263046bec105ecb45f08e2f5bfc9bb8dbbf27) | 2024-08-09 | Yong-Xuan Wang | irqchip/riscv-aplic: Retrigger MSI interrupt on source configuration |
| [9bb378b2](https://github.com/RVCK-Project/rvck/commit/9bb378b24f3be5c769371502131bd10565764e16) | 2024-06-03 | Jinjie Ruan | irqchip/riscv-aplic: Simplify the initialization code |
| [54042a37](https://github.com/RVCK-Project/rvck/commit/54042a37d91113eb7d5495858046df419e52ef7f) | 2024-04-16 | Dawei Li | irqchip/riscv-aplic-direct: Avoid explicit cpumask allocation on stack |
| [56e812b7](https://github.com/RVCK-Project/rvck/commit/56e812b7a504beb81405a134625dc027a9a5843f) | 2024-04-16 | Dawei Li | cpumask: Introduce cpumask_first_and_and() |
| [1034afab](https://github.com/RVCK-Project/rvck/commit/1034afab2ef73511d9289e36f338b0a403579cb5) | 2024-03-07 | Anup Patel | irqchip/riscv-aplic: Add support for MSI-mode |
| [d9e8e38d](https://github.com/RVCK-Project/rvck/commit/d9e8e38d6a75772a266c6ae05f221cbc70b8e8ce) | 2024-08-20 | Dan Carpenter | irqchip/riscv-aplic: Fix an IS_ERR() vs NULL bug in probe() |
| [9f00c08b](https://github.com/RVCK-Project/rvck/commit/9f00c08ba4d9765ab005d8ab822e753da6713d06) | 2024-03-07 | Anup Patel | irqchip: Add RISC-V advanced PLIC driver for direct-mode |
| [79a25343](https://github.com/RVCK-Project/rvck/commit/79a253439a26ef734a400c7a99ad7fd83ad47ca5) | 2024-03-07 | Anup Patel | dt-bindings: interrupt-controller: Add RISC-V advanced PLIC |
| [cc1dfdff](https://github.com/RVCK-Project/rvck/commit/cc1dfdff3e93a762b64feb198f3636d8fdf4ace6) | 2024-03-07 | Anup Patel | irqchip/riscv-imsic: Add device MSI domain support for PCI devices |
| [4e6fde4b](https://github.com/RVCK-Project/rvck/commit/4e6fde4bd5335b6653c33bc2e8ea27b8a9784661) | 2024-09-09 | Andrew Jones | irqchip/riscv-imsic: Fix output text of base address |
| [c8614b9a](https://github.com/RVCK-Project/rvck/commit/c8614b9a35d3cdc3f69b1e2e4c4f8b93122ab88d) | 2024-04-13 | Anup Patel | irqchip/riscv-imsic: Fix boot time update effective affinity warning |
| [993ee18f](https://github.com/RVCK-Project/rvck/commit/993ee18fe58cf9feb185f906380bfdf40da0b8a9) | 2024-03-07 | Anup Patel | irqchip/riscv-imsic: Add device MSI domain support for platform devices |
| [859354b3](https://github.com/RVCK-Project/rvck/commit/859354b35917bc61b5fca60d20c3a1f7227d7d92) | 2024-03-07 | Anup Patel | irqchip: Add RISC-V incoming MSI controller early driver |
| [0c6648ec](https://github.com/RVCK-Project/rvck/commit/0c6648ec758116e2e2767ca4ffa251f5b862fe85) | 2024-03-07 | Anup Patel | dt-bindings: interrupt-controller: Add RISC-V incoming MSI controller |
| [c8c1910d](https://github.com/RVCK-Project/rvck/commit/c8c1910df71dfc831b17d28c379ef5d6b94b499c) | 2024-02-22 | Björn Töpel | genirq/matrix: Dynamic bitmap allocation |
| [ef5b4424](https://github.com/RVCK-Project/rvck/commit/ef5b442406b5cca1a36663c158f07eee492e6a70) | 2024-03-12 | Samuel Holland | irqchip/riscv-intc: Fix use of AIA interrupts 32-63 on riscv32 |
| [11a905d3](https://github.com/RVCK-Project/rvck/commit/11a905d3afe2c0f65a1cb4aa1a9265604a2cccec) | 2024-02-26 | Anup Patel | irqchip/riscv-intc: Fix low-level interrupt handler setup for AIA |
| [ceb96b43](https://github.com/RVCK-Project/rvck/commit/ceb96b434b21f0148b334b30ad3b2f034bcb5a7d) | 2024-02-22 | Anup Patel | irqchip/riscv-intc: Add support for RISC-V AIA |
| [2dfa910d](https://github.com/RVCK-Project/rvck/commit/2dfa910dfa89661755ed215436a318e879aec35f) | 2023-12-20 | Jisheng Zhang | riscv: enable HAVE_FAST_GUP if MMU |
| [21b0c46c](https://github.com/RVCK-Project/rvck/commit/21b0c46c22e34041fa3698d1d2d80753350a4cda) | 2023-12-20 | Jisheng Zhang | riscv: enable MMU_GATHER_RCU_TABLE_FREE for SMP && MMU |
| [8b52110d](https://github.com/RVCK-Project/rvck/commit/8b52110dd99fd0195c15f7634ac5179f167c15ff) | 2023-12-20 | Jisheng Zhang | riscv: tlb: convert __p*d_free_tlb() to inline functions |
| [bcd0454d](https://github.com/RVCK-Project/rvck/commit/bcd0454d45a9dfa0a382732270727104a1f497ea) | 2023-12-20 | Jisheng Zhang | riscv: tlb: fix __p*d_free_tlb() |
| [96ec5524](https://github.com/RVCK-Project/rvck/commit/96ec552446e20da549acb52ba8c30a28c995c395) | 2023-09-13 | Mayuresh Chitale | dt-bindings: riscv: Add smstateen entry |
| [cabfc801](https://github.com/RVCK-Project/rvck/commit/cabfc80113f591a9ce286d6294d6ffe78934490d) | 2023-09-13 | Mayuresh Chitale | RISC-V: Detect Smstateen extension |
| [93d68daa](https://github.com/RVCK-Project/rvck/commit/93d68daa5e2b85a5d91e8db9b393173547f21ff0) | 2024-01-27 | Thomas Gleixner | genirq/msi: Provide MSI_FLAG_PARENT_PM_DEV |
| [aa5f5bab](https://github.com/RVCK-Project/rvck/commit/aa5f5babc1cf17c77502cdba53cd5b1da35e6319) | 2024-01-27 | Thomas Gleixner | genirq/irqdomain: Reroute device MSI create_mapping |
| [e7b00f72](https://github.com/RVCK-Project/rvck/commit/e7b00f72b77827729bf61b8c306c0ffaf1816849) | 2024-01-27 | Thomas Gleixner | genirq/msi: Provide allocation/free functions for "wired" MSI interrupts |
| [5f1c6999](https://github.com/RVCK-Project/rvck/commit/5f1c69994094f377c0b7d0eb1d03c65089080dd8) | 2024-01-27 | Thomas Gleixner | genirq/msi: Optionally use dev-\>fwnode for device domain |
| [4cbac34f](https://github.com/RVCK-Project/rvck/commit/4cbac34fd2af7be32ac93057e39bbcae6327a9ae) | 2024-01-27 | Thomas Gleixner | genirq/msi: Provide DOMAIN_BUS_WIRED_TO_MSI |
| [dcf85ecf](https://github.com/RVCK-Project/rvck/commit/dcf85ecf1c283f637a6e9b2f8275c3d4a087d8ca) | 2024-01-27 | Thomas Gleixner | genirq/msi: Split msi_domain_alloc_irq_at() |
| [3aa04747](https://github.com/RVCK-Project/rvck/commit/3aa04747c0e19cf00731c60e00a6b4b5b73649a6) | 2024-02-20 | Marc Zyngier | genirq/irqdomain: Don't call ops-\>select for DOMAIN_BUS_ANY tokens |
| [64fdb5b2](https://github.com/RVCK-Project/rvck/commit/64fdb5b2f64dc33b857275e35a32c72e2a011a7b) | 2024-01-27 | Thomas Gleixner | genirq/msi: Provide optional translation op |
| [31c411b9](https://github.com/RVCK-Project/rvck/commit/31c411b93b995e7dd7c56be239de7122784c2b9f) | 2024-02-15 | Thomas Gleixner | platform-msi: Remove unused interfaces |
| [45f80dca](https://github.com/RVCK-Project/rvck/commit/45f80dca27404f1905e596254cbd09bf838eec57) | 2024-01-27 | Thomas Gleixner | irqchip: Convert all platform MSI users to the new API |
| [bcb7e0a0](https://github.com/RVCK-Project/rvck/commit/bcb7e0a00e36bcfcc1f5bee633f7fe8ceab1fcf0) | 2024-01-27 | Thomas Gleixner | platform-msi: Prepare for real per device domains |
| [7ae2c00e](https://github.com/RVCK-Project/rvck/commit/7ae2c00e1d6ed922a872f98b816347698c5ddde5) | 2024-01-27 | Thomas Gleixner | genirq/irqdomain: Add DOMAIN_BUS_DEVICE_MSI |
| [570486c5](https://github.com/RVCK-Project/rvck/commit/570486c556a3429255418994edc3ea730f06d040) | 2024-01-27 | Thomas Gleixner | genirq/msi: Extend msi_parent_ops |
| [007e94c3](https://github.com/RVCK-Project/rvck/commit/007e94c37d4673f878fb4bc2cb47bb8a9eb6b3cd) | 2024-01-27 | Thomas Gleixner | genirq/irqdomain: Remove the param count restriction from select() |
| [40092f25](https://github.com/RVCK-Project/rvck/commit/40092f256e740fdc4f10ea7300a123494ae58d19) | 2024-12-10 | Yafen Fang | fix: Error: unrecognized opcode cbo.clean (a0) |
| [9f28a749](https://github.com/RVCK-Project/rvck/commit/9f28a7499b2cfa10c4233f56faeec898ca56479b) | 2024-03-27 | Han Gao | riscv: sophgo: mango: add xtheadvector for mango-cpus-socket0&1 |
| [5e23702b](https://github.com/RVCK-Project/rvck/commit/5e23702bce51e46ee3d7594051354330181c6f99) | 2024-09-27 | Han Gao | driver: video-memory: reorganize the code structure |
| [e4400dae](https://github.com/RVCK-Project/rvck/commit/e4400dae52ef18e823da1d19bc4b9c1b837a5927) | 2024-09-21 | Han Gao | fix: gpu: fix device tree matching img,gpu |
| [7be5139d](https://github.com/RVCK-Project/rvck/commit/7be5139d5622ddac843ae292961c6ee7d4e2e319) | 2024-09-21 | Han Gao | ci: cleanup forced setting of thread number |
| [f3e9cf1c](https://github.com/RVCK-Project/rvck/commit/f3e9cf1c4a4cdfbf364d227e9c8051ad4228dbf9) | 2024-09-21 | Han Gao | debian: linux-image provide wireguard-modules |
| [dd372b41](https://github.com/RVCK-Project/rvck/commit/dd372b41889d30430c47f9579da9f744faf7005a) | 2024-09-21 | Han Gao | config: cleanup unused option |
| [c74bb90b](https://github.com/RVCK-Project/rvck/commit/c74bb90b6bf93c346038e8cecbf1fae0d12c5307) | 2024-09-21 | Han Gao | fix: disable CONFIG_PCI for pvrsrvkm build error |
| [1da8dbf1](https://github.com/RVCK-Project/rvck/commit/1da8dbf1824388a133419d652ca33077270600d1) | 2024-09-21 | Han Gao | dts: lpi4a: remove mipi screen |
| [0a044bc2](https://github.com/RVCK-Project/rvck/commit/0a044bc2f4ff5a02cfdbcec1231da9fe2ffe783d) | 2024-09-19 | Han Gao | sync: xuantie: vpu-vc8000e SDK v2.0.2 code |
| [57e23bb3](https://github.com/RVCK-Project/rvck/commit/57e23bb3350dfd08548394e6272891545fd157f4) | 2024-09-19 | Han Gao | sync: xuantie: vpu-vc8000d SDK v2.0.2 code |
| [4ab033da](https://github.com/RVCK-Project/rvck/commit/4ab033da34cd38dbdac2bbedf6e9abd697f1e77d) | 2024-08-07 | Han Gao | symbol: gpl: export pud_offset/p4d_offset symbol |
| [0ade10ae](https://github.com/RVCK-Project/rvck/commit/0ade10aedc53f7801577b04986d88f599df41366) | 2024-09-19 | Han Gao | sync: xuantie: video_memory SDK v2.0.2 code |
| [fb687ff0](https://github.com/RVCK-Project/rvck/commit/fb687ff0b522b4cba6f4a785691ff886ad6758f9) | 2024-09-19 | Han Gao | sync: img: npu-ax3386: sync SDK V2.0.2 code |
| [a3e12e90](https://github.com/RVCK-Project/rvck/commit/a3e12e90083f519834928cffde7d36b905a0bd8e) | 2024-09-16 | Han Gao | ci: kernel auto build on native |
| [c8491ce8](https://github.com/RVCK-Project/rvck/commit/c8491ce83de6d7ccc724e80da51399a11bf94291) | 2024-03-28 | Icenowy Zheng | drm/verisilicon: add format_mod_supported to plane |
| [6041ef4d](https://github.com/RVCK-Project/rvck/commit/6041ef4da8c2b4a6a21f171d938e08863a956b1f) | 2023-12-28 | Icenowy Zheng | drm/verisilicon: bias fb address for dual-head offset |
| [8b8b3593](https://github.com/RVCK-Project/rvck/commit/8b8b359396d5220ac485e6ee2dca1b09a88d3dbe) | 2023-12-27 | Icenowy Zheng | drm/verisilicon: finally fix the cursor position |
| [63e091f3](https://github.com/RVCK-Project/rvck/commit/63e091f394e1a6fd6c576083192376b4a0efac1a) | 2023-12-05 | Icenowy Zheng | drm/verisilicon: fix cursor position |
| [5f357711](https://github.com/RVCK-Project/rvck/commit/5f357711ac43040b51e2808badabfd875cef46be) | 2023-05-08 | Icenowy Zheng | drm: verisilicon: fix fbcon |
| [400bd518](https://github.com/RVCK-Project/rvck/commit/400bd518a9ff50708cacd2d0aac2cf31baeb43a2) | 2022-09-14 | Icenowy Zheng | drm/dc8200: disable gamma lut now |
| [4360faf2](https://github.com/RVCK-Project/rvck/commit/4360faf29e99a89d8c3ad55d66f1fef580323310) | 2024-09-14 | Drew Fustini | cpufreq: th1520-cpufreq: fix cpu_pll1 already disabled warning |
| [2056faea](https://github.com/RVCK-Project/rvck/commit/2056faeace8050754e7ca4ace1def976fde88d03) | 2024-09-13 | Icenowy Zheng | th1520: use etnaviv gpu |
| [ddc2460a](https://github.com/RVCK-Project/rvck/commit/ddc2460a9b8a50198b73669d1cd499d0dd492c3c) | 2024-09-13 | Han Gao | config: enable configs for TH1520 |
| [8d9057a6](https://github.com/RVCK-Project/rvck/commit/8d9057a68312a37c4c6dcb25d24151dbb61c3420) | 2024-09-13 | Han Gao | config: enable ARCH_XUANTIE |
| [74f7b84f](https://github.com/RVCK-Project/rvck/commit/74f7b84f1f5b20b147b089fcec85d2543dec6840) | 2024-09-13 | Han Gao | config: mmc_block & ext4 builtin |
| [7e54fdcd](https://github.com/RVCK-Project/rvck/commit/7e54fdcd8faed30e0bb206cff305145cea7b9e99) | 2024-09-13 | Han Gao | config: init revyos defconfig |
| [4ab159d7](https://github.com/RVCK-Project/rvck/commit/4ab159d703a52a62ca872d33047d309a8d8804ef) | 2024-09-01 | Han Gao | configs: enable img rogue gpu |
| [a02ce3e9](https://github.com/RVCK-Project/rvck/commit/a02ce3e91cbd765d58728847bfe2dc8c9a5ee626) | 2024-09-01 | Mingzheng Xing | th1520: gpu: Add driver for PowerVR Rogue GPU |
| [279f2175](https://github.com/RVCK-Project/rvck/commit/279f21751fdd0098c94e7845d8244185a2b12f65) | 2024-09-01 | Han Gao | fix: dts: remove duplicate node |
| [1a62a6f6](https://github.com/RVCK-Project/rvck/commit/1a62a6f69047f389d004dbbc2cc1c2d58b84662b) | 2024-09-01 | Han Gao | Solve problem of hdmi-edid reading |
| [c5125722](https://github.com/RVCK-Project/rvck/commit/c512572264ad1049e6db3e3b72075617b044666b) | 2024-09-01 | Han Gao | riscv:uprobe: fix flush_icache to ensure that instructions are refreshed when sw... |
| [48a0a686](https://github.com/RVCK-Project/rvck/commit/48a0a6860c034af5b0f0a6c44fa649cb728d5e1c) | 2024-09-01 | Han Gao | HDMI: fix bug of not being able to light up the external monitor |
| [0d67288b](https://github.com/RVCK-Project/rvck/commit/0d67288b76cfbc2b285a0c479e02810d055a81f1) | 2024-09-01 | Han Gao | Fix panel-jadard-jd9365da panel driver problem |
| [ac114c72](https://github.com/RVCK-Project/rvck/commit/ac114c72450935b54dfa6f2ea48aed8092eb52c6) | 2024-09-01 | Han Gao | Fix panel-jadard-jd9365da panel driver problem |
| [0ddeff68](https://github.com/RVCK-Project/rvck/commit/0ddeff689c337ec158ad0384445ffed60fb5ccaa) | 2024-09-01 | Han Gao | sensor: fix bug of channel 1 and channel 2 of video2 failed to run |
| [f64212e8](https://github.com/RVCK-Project/rvck/commit/f64212e8d7c3f7f5a33f883e484a5842a8c52f0b) | 2024-09-01 | Han Gao | Expand cma size from 512MB to 768MB to meet the FBO video frame buffer requireme... |
| [95d6676c](https://github.com/RVCK-Project/rvck/commit/95d6676cdd9b9d67d607e5d3b93b478e6ed6abac) | 2024-09-01 | Han Gao | defconfig: th1520: to fix the problem of perf test fail |
| [e61296f7](https://github.com/RVCK-Project/rvck/commit/e61296f7cf4e1d5946ecc898097dac474b8ec63a) | 2024-09-01 | Han Gao | Fix: Repair rvbook hall sensor functionality and optimize codebase |
| [f000ea27](https://github.com/RVCK-Project/rvck/commit/f000ea279bd74c594194f1e8760ecd99d172ac73) | 2024-09-01 | Han Gao | riscv:vector: Check datap status in __switch_to_vector |
| [b2d266f0](https://github.com/RVCK-Project/rvck/commit/b2d266f0b3c6b1fe6c51e50e1cf5a15b8de8dbb2) | 2024-09-01 | Han Gao | th1520_defconfig:Enable lowpower settings |
| [5f9142fc](https://github.com/RVCK-Project/rvck/commit/5f9142fc42191d0e9ca0f87627e5172a6d24d244) | 2024-09-01 | Han Gao | th1520_defconfig:Enable ebpf settings |
| [72702d15](https://github.com/RVCK-Project/rvck/commit/72702d1522e222ab5cd9fd212eb682e9714fd4b3) | 2024-09-01 | Han Gao | dts: th1520: sd card not try sdio cmds |
| [c6ae7c43](https://github.com/RVCK-Project/rvck/commit/c6ae7c435ed5ed5b0d2190a4869a18444150b03b) | 2024-09-01 | Han Gao | fix rv_book str |
| [97e32d91](https://github.com/RVCK-Project/rvck/commit/97e32d9131247d46440f85838f113aff77e3c218) | 2024-09-01 | Han Gao | driver usb: optimize pm resume time, do resume in runtime_resume |
| [e53d4351](https://github.com/RVCK-Project/rvck/commit/e53d4351a67d6ca822cca8b613a920c6029d4162) | 2024-09-01 | Han Gao | Solve problem of DSI transfer command failure when hotplug hdmi |
| [206bcd0f](https://github.com/RVCK-Project/rvck/commit/206bcd0fb4cd51a0a2173dddd74087717f9504f7) | 2024-09-01 | Han Gao | dts: bt: support rtl8822cs |
| [b7a9500e](https://github.com/RVCK-Project/rvck/commit/b7a9500e2796de1eae2acf6bbae7c33c73b5ec7d) | 2024-09-01 | Han Gao | dts: wifi: support rtl8822cs |
| [a6f89ddc](https://github.com/RVCK-Project/rvck/commit/a6f89ddcbb4fcc3482fca148c14b3049da7eec9a) | 2024-09-01 | Han Gao | defconfig: wifi : add rtl8822cs(for rvbook) |
| [6126533b](https://github.com/RVCK-Project/rvck/commit/6126533b30d2ad15f22ead0e2e7fdfb0fda47a48) | 2024-09-01 | Han Gao | riscv:kdump: Fix gen /proc/vmcore |
| [6856371d](https://github.com/RVCK-Project/rvck/commit/6856371d5c102882eea5a220f8d927c04c8a7a23) | 2024-09-01 | Han Gao | driver:tee:add tee_driver_pm_ops |
| [8801099c](https://github.com/RVCK-Project/rvck/commit/8801099c1b05121cefbb60a98d374a347e25b48b) | 2024-09-01 | Han Gao | driver:tee:Allow to freeze when tee supplicant is freezed |
| [e69d8c13](https://github.com/RVCK-Project/rvck/commit/e69d8c135b49420c9b063a0c55de332811d2b4b5) | 2024-09-01 | Han Gao | usb: dwc3: th1520.dtsi: bugfix: fix usb str xhci error |
| [16e0fa06](https://github.com/RVCK-Project/rvck/commit/16e0fa0636eb3ad9972b0b136ffd24deaf8cc70e) | 2024-09-01 | Han Gao | drivers: support virtio_vdmabuf |
| [8efc86a0](https://github.com/RVCK-Project/rvck/commit/8efc86a0d8f02b03ea4a85b9ba91b78b06d2c96a) | 2024-09-01 | Han Gao | perf:test:fix PERF_RECORD_* events & perf_sample fields in yocto linux |
| [cbad68f4](https://github.com/RVCK-Project/rvck/commit/cbad68f4529b89c668cffcb90c2f91ce8af9bcc7) | 2024-09-01 | Han Gao | move the place of dts "audio-text-memory-region" property |
| [c230bebf](https://github.com/RVCK-Project/rvck/commit/c230bebf67a5e5fd2d0a196eb18ac2e5692bff38) | 2024-09-01 | Han Gao | defconfig: bt: add hid support |
| [8a1d0695](https://github.com/RVCK-Project/rvck/commit/8a1d0695e514b54d3cb42acc60035e3523e87706) | 2024-09-01 | Han Gao | defconfig: bt : add rtl8723ds |
| [581eaf8f](https://github.com/RVCK-Project/rvck/commit/581eaf8fe5c777a4631cc272f6490ef7f5705f41) | 2024-09-01 | Han Gao | driver: bt : Compatible with RTL8723ds'h5 protocol |
| [5a68ee35](https://github.com/RVCK-Project/rvck/commit/5a68ee35e0d27d73f855c2efdc8a501247a8896a) | 2024-09-01 | Han Gao | driver: bt: add rtl8723ds h5 protocol |
| [66b71dc5](https://github.com/RVCK-Project/rvck/commit/66b71dc5ebac2d9c559cd15a5bb37026a90f0663) | 2024-09-01 | Han Gao | add audio hibernation ops |
| [28768584](https://github.com/RVCK-Project/rvck/commit/287685846d979a5cafc0116b97d3dbaf964eb05a) | 2024-09-01 | Han Gao | DPU: remove panel unprepare process in disable dsi process |
| [68371710](https://github.com/RVCK-Project/rvck/commit/6837171099595d2e367df9258b057ffff3438cc2) | 2024-09-01 | Han Gao | remove dts "audio_mem" node and add mbox 910r channel |
| [260a0648](https://github.com/RVCK-Project/rvck/commit/260a0648a3044c600e020d34c78cdd24968f66d9) | 2024-09-01 | Han Gao | usb: dwc3-thead: fix usb gadget support |
| [7c08f3c5](https://github.com/RVCK-Project/rvck/commit/7c08f3c545bab2edb82e2b9dcaddcada1209d219) | 2024-09-01 | Han Gao | dts: th1520-lichee-pi-4a: update usb hub |
| [7115dddb](https://github.com/RVCK-Project/rvck/commit/7115dddb2b7bc01b54b485a569bb3f163fb3f339) | 2024-09-01 | Han Gao | dts: add th1520-lpi4a-dsi0.dts and th1520-lpi4a-hx8279.dts |
| [87be70e7](https://github.com/RVCK-Project/rvck/commit/87be70e706ca272bd3ae56121114459748e3ee8d) | 2024-09-01 | Han Gao | dts: add display support for dsi0&dsi1 and dsi0&hdmi |
| [e951e020](https://github.com/RVCK-Project/rvck/commit/e951e020c7bdb5786e308125d28d716f900d90ee) | 2024-09-01 | Han Gao | dw-axi-dma : dma_chan_prep_dma_memcpy func add chan-\>direction = DMA_MEM_TO_MEM |
| [9ecb69c0](https://github.com/RVCK-Project/rvck/commit/9ecb69c0b02ec1a85ad9cd2a4bd47e46dc86e9ac) | 2024-09-01 | Han Gao | DPU: support DSI/HDMI driver for light-a-val |
| [ecb7ec45](https://github.com/RVCK-Project/rvck/commit/ecb7ec4591899e81147721f396fcf21ef5a8781e) | 2024-09-01 | Han Gao | driver : rfkill : Delete unnecessary code |
| [5ee7790b](https://github.com/RVCK-Project/rvck/commit/5ee7790b293f6b2b6157c7c9de6ba3687215d860) | 2024-09-01 | Han Gao | dts: rfkill: Delete unnecessary nodes |
| [54929a7f](https://github.com/RVCK-Project/rvck/commit/54929a7f1189d35d1a8a65f1c922d23c5e2098b0) | 2024-09-01 | Han Gao | RISC-V laptop: Add new drivers for specific hardware components |
| [dc14a89e](https://github.com/RVCK-Project/rvck/commit/dc14a89ef78581e703479cfe3d8556ddcf597eac) | 2024-09-01 | Han Gao | rvbook: add th1520-rvbook.dts |
| [c9452552](https://github.com/RVCK-Project/rvck/commit/c94525520271b8e3bec254dd461d12d7d4f64e53) | 2024-09-01 | Han Gao | Add kernel boot rvbook_defconfig |
| [b31b4cbc](https://github.com/RVCK-Project/rvck/commit/b31b4cbc35323c873f9701c1c30c09c62ea95611) | 2024-09-01 | Han Gao | dts: add GPU device node |
| [9252fd8e](https://github.com/RVCK-Project/rvck/commit/9252fd8e68e19483fc033e42df8bc054e7bcd507) | 2024-09-01 | Han Gao | perf vendor events riscv: Add PMU event JSON files for TH1520 DDRC PMU |
| [853878cb](https://github.com/RVCK-Project/rvck/commit/853878cb7bbd089111dcbb86871c4d69e795d0a0) | 2024-09-01 | Han Gao | dts: rfkill: Resolving Insmod Failure Issues |
| [53e77c39](https://github.com/RVCK-Project/rvck/commit/53e77c3902964bae3a41e49a0d63e1ee38db0847) | 2024-09-01 | Han Gao | dts: th1520: add g2d device node |
| [87f2735d](https://github.com/RVCK-Project/rvck/commit/87f2735d72918be152fda9d5149b9f239b2c3864) | 2024-08-31 | Han Gao | aic8800: Add AIC8800's config to th1520_defconfig, as well as resolve known issu... |
| [9fb74c6d](https://github.com/RVCK-Project/rvck/commit/9fb74c6d75adc223c22feb5758c470497376c0c6) | 2024-08-31 | Han Gao | uart: Fix the UART problem |
| [4614ddf3](https://github.com/RVCK-Project/rvck/commit/4614ddf3b63dc0ebd975b70c3b50c0462400ef7e) | 2024-08-31 | Han Gao | rfkill: add aic8800 rfkill support for gpio control of aic8800 wifi/bt |
| [d54d768e](https://github.com/RVCK-Project/rvck/commit/d54d768e634f7872930f155d694eafb2bb4b6703) | 2024-08-31 | Han Gao | th1520-lichee-pi-4a.dts: change dts for aic8800 wifi Support aic8800 wifi |
| [cab7136b](https://github.com/RVCK-Project/rvck/commit/cab7136be3aff6ea8177f35bcd816b7ed251bed3) | 2024-08-31 | Han Gao | th1520-lichee-pi-4a.dts: change dts for aic8800 bt Support aic8800 bt |
| [035f700a](https://github.com/RVCK-Project/rvck/commit/035f700a1dbcaae2d75c27e8ff8411a2c20d6bca) | 2024-08-27 | Han Gao | fix: riscv: xtheadvector: fix setup_v_vsize |
| [59ecb579](https://github.com/RVCK-Project/rvck/commit/59ecb57957ea85768c79aac3c2abe0da1138af7d) | 2024-07-05 | Han Gao | configs: enable rtw88 for 8723ds |
| [73cc5ec2](https://github.com/RVCK-Project/rvck/commit/73cc5ec22eaa2a088a7a7dd819b1d9a0260a5aa9) | 2024-06-10 | Han Gao | xtheadvector: fix it used as v-ext when hwprobe is used |
| [e1cc1f0b](https://github.com/RVCK-Project/rvck/commit/e1cc1f0b9a9badad48e534f93c99c95d3dcfb7d7) | 2024-03-30 | Han Gao | dts: th1520: add xtheadvector |
| [f157d56e](https://github.com/RVCK-Project/rvck/commit/f157d56e9169e8e020b511c5d3238e2898053c57) | 2024-03-29 | Han Gao | fix: use has_vector instead of judge ELF_HWCAP |
| [1139a8ef](https://github.com/RVCK-Project/rvck/commit/1139a8ef8577747b199207cde5377783a0d08f00) | 2024-03-27 | Han Gao | riscv: xtheadvector: enable vector function |
| [1949c9bc](https://github.com/RVCK-Project/rvck/commit/1949c9bc25ed5f15c57d3fc85e8007a1d3fe2458) | 2024-07-03 | Han Gao | configs: init th1520 config |
| [2a2e5817](https://github.com/RVCK-Project/rvck/commit/2a2e5817cf622e21cd4741ac98c6619cea8c4fe0) | 2024-07-05 | Han Gao | riscv: dts: lpi4a 16g support |
| [00dc7159](https://github.com/RVCK-Project/rvck/commit/00dc71595fcf3dc723c6290110e37d890873365e) | 2024-07-02 | Han Gao | chore: use thead instead of xuantie |
| [28606207](https://github.com/RVCK-Project/rvck/commit/28606207b23033a8e92a389e75aea45d6fd8dbbb) | 2024-07-02 | Han Gao | chore: use xuantie instead of thead |
| [10cc3485](https://github.com/RVCK-Project/rvck/commit/10cc34858c40449ec28671d45734a188e294a4d3) | 2024-01-12 | Han Gao | chore: dtb_install in /boot |
| [c4000ca6](https://github.com/RVCK-Project/rvck/commit/c4000ca6e79549fe54053a3bbdcac1b5f371434d) | 2023-09-21 | Han Gao | remove compression for riscv Image |
| [ec3dee88](https://github.com/RVCK-Project/rvck/commit/ec3dee886cd2692efc19e09e55dd938413d07674) | 2023-12-06 | Drew Fustini | riscv: dts: thead: Enable LicheePi 4A eMMC and microSD |
| [1c4289f2](https://github.com/RVCK-Project/rvck/commit/1c4289f281b4d13509b1b64c62bc455a7bf24983) | 2023-12-06 | Drew Fustini | riscv: dts: thead: Enable BeagleV Ahead eMMC and microSD |
| [f50f655b](https://github.com/RVCK-Project/rvck/commit/f50f655b17e3f39a6e9ff5570b061fa6c1a5697b) | 2023-12-06 | Drew Fustini | riscv: dts: thead: Add TH1520 mmc controllers and sdhci clock |
| [5eb52624](https://github.com/RVCK-Project/rvck/commit/5eb52624e0446e5b48317ffaa6635d0770f77045) | 2023-12-06 | Drew Fustini | riscv: defconfig: Enable mmc and dma drivers for T-Head TH1520 |
| [10bff1f2](https://github.com/RVCK-Project/rvck/commit/10bff1f2b5ea3ec2388866b7f75b91c01284a1c4) | 2023-11-14 | Drew Fustini | mmc: sdhci-of-dwcmshc: Add support for T-Head TH1520 |
| [76e9bd3e](https://github.com/RVCK-Project/rvck/commit/76e9bd3eddd9056f39dece9aaf6fd6702219f2cd) | 2023-11-14 | Drew Fustini | mmc: sdhci: add __sdhci_execute_tuning() to header |
| [1a67f455](https://github.com/RVCK-Project/rvck/commit/1a67f45557db72bbd67cdd68a7b9f97d1a41389b) | 2023-11-14 | Drew Fustini | dt-bindings: mmc: sdhci-of-dwcmhsc: Add T-Head TH1520 support |
| [2a5db116](https://github.com/RVCK-Project/rvck/commit/2a5db11611681ccbe6b2f488fb6aecf297988765) | 2024-04-25 | Han Gao | fix: remove linux/array_size.h for pinctrl-th1520 |
| [1ac38318](https://github.com/RVCK-Project/rvck/commit/1ac38318ea77b53405eabefd4a100111c93aba1b) | 2024-01-03 | Emil Renner Berthing | riscv: dtb: thead: Add BeagleV Ahead LEDs |
| [51b6f8a3](https://github.com/RVCK-Project/rvck/commit/51b6f8a33e01e7f089d5fd6a1b061ff129fa54f7) | 2024-01-03 | Emil Renner Berthing | riscv: dts: thead: Add TH1520 pinctrl settings for UART0 |
| [1b907adc](https://github.com/RVCK-Project/rvck/commit/1b907adc30c5742140d76588f08fbd8d200386d7) | 2024-01-03 | Emil Renner Berthing | riscv: dts: thead: Add Lichee Pi 4M GPIO line names |
| [f4e58a66](https://github.com/RVCK-Project/rvck/commit/f4e58a6656199a61950231e9686dc7554689442e) | 2024-01-03 | Emil Renner Berthing | riscv: dts: thead: Adjust TH1520 GPIO labels |
| [a5f5ce81](https://github.com/RVCK-Project/rvck/commit/a5f5ce81559bab0fc99e1af26c05a263e3021571) | 2024-01-03 | Emil Renner Berthing | riscv: dts: thead: Add TH1520 GPIO ranges |
| [08c3ff05](https://github.com/RVCK-Project/rvck/commit/08c3ff05861a6f2d2a87754a3c9aac11772436fa) | 2024-01-03 | Emil Renner Berthing | riscv: dts: thead: Add TH1520 pin control nodes |
| [6134204c](https://github.com/RVCK-Project/rvck/commit/6134204c548cb713745a260223a2f32e096e1a37) | 2024-01-03 | Emil Renner Berthing | pinctrl: Add driver for the T-Head TH1520 SoC |
| [d71037e9](https://github.com/RVCK-Project/rvck/commit/d71037e906ff09fb314391e4d2f1072ec1ee7012) | 2024-01-03 | Emil Renner Berthing | dt-bindings: pinctrl: Add thead,th1520-pinctrl bindings |
---

**共 252 条提交（显示全部）**

[分页显示](软件所.md) | [纯文本视图](软件所_commits.txt)
## 🔙 返回

[← 返回统计主页](../index.md)

---

*本页面最后更新于 2026-03-04 21:03:03*
*数据来源: 主分支 tmp-stats@ce238702*
