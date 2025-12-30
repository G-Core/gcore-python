# Changelog

## 0.28.0 (2025-12-30)

Full Changelog: [v0.27.0...v0.28.0](https://github.com/G-Core/gcore-python/compare/v0.27.0...v0.28.0)

### ⚠ BREAKING CHANGES

* change naming for POST, PUT, PATCH, DELETE models

### Bug Fixes

* **cloud:** fix SSH keys examples ([4e79f57](https://github.com/G-Core/gcore-python/commit/4e79f578b04fbca2126a46aded663246c449eb64))


### Chores

* change naming for POST, PUT, PATCH, DELETE models ([ae21e7c](https://github.com/G-Core/gcore-python/commit/ae21e7c61096ade39749c39a7c4c7572516980e9))

## 0.27.0 (2025-12-30)

Full Changelog: [v0.26.0...v0.27.0](https://github.com/G-Core/gcore-python/compare/v0.26.0...v0.27.0)

### Features

* **api:** manual updates ([e6fec4e](https://github.com/G-Core/gcore-python/commit/e6fec4e8c85de66bd2557833cd03f38c30b19ecd))

## 0.26.0 (2025-12-23)

Full Changelog: [v0.25.0...v0.26.0](https://github.com/G-Core/gcore-python/compare/v0.25.0...v0.26.0)

### ⚠ BREAKING CHANGES

* **cloud:** move methods to gpu_baremetal_clusters.interfaces.attach()/detach()
* **cloud:** restructure to be gpu_virtual.clusters

### Features

* **api:** aggregated API specs update ([3a272e8](https://github.com/G-Core/gcore-python/commit/3a272e8b9a0399be48094ce82cc9127e59a2867a))
* **api:** aggregated API specs update ([789277a](https://github.com/G-Core/gcore-python/commit/789277a61a3ead490d9b8b0f439e0e21100036ba))
* **cloud:** add k8s cluster pools check quotas method ([326786c](https://github.com/G-Core/gcore-python/commit/326786cd4d499fffe760f308326bbd79003e4856))


### Bug Fixes

* **cloud:** move methods to gpu_baremetal_clusters.interfaces.attach()/detach() ([053ebcf](https://github.com/G-Core/gcore-python/commit/053ebcfdf462a66c3edc929e052b75d8afd51a20))
* **cloud:** restructure to be gpu_virtual.clusters ([36b7b63](https://github.com/G-Core/gcore-python/commit/36b7b63d98a20c3927069bb396154b068304f321))
* **examples:** make code consistent with comment ([85a0331](https://github.com/G-Core/gcore-python/commit/85a03310d31fa3ac6b74897b8754a19bd905df75))
* use async_to_httpx_files in patch method ([88c4050](https://github.com/G-Core/gcore-python/commit/88c4050f59d8a55796ab553a60b1e55aaadc81ca))


### Chores

* **internal:** add missing files argument to base client ([7d81efb](https://github.com/G-Core/gcore-python/commit/7d81efb323f72cdcaed3faa59a4fc5182f0fedab))
* **internal:** codegen related update ([3c38f42](https://github.com/G-Core/gcore-python/commit/3c38f4280bc1b57f987ff984c7504c4781d74ab8))
* speedup initial import ([ff1db23](https://github.com/G-Core/gcore-python/commit/ff1db23e58ffc5e118bd1fed3585ffc0cd04855e))

## 0.25.0 (2025-12-12)

Full Changelog: [v0.24.0...v0.25.0](https://github.com/G-Core/gcore-python/compare/v0.24.0...v0.25.0)

### ⚠ BREAKING CHANGES

* **cloud:** streamline vip connected and candidate ports

### Bug Fixes

* **cloud:** fix vip examples ([f4f6c46](https://github.com/G-Core/gcore-python/commit/f4f6c46f6352fb55eae9d91a2060f24289ed4dda))
* **cloud:** streamline vip connected and candidate ports ([958b2a7](https://github.com/G-Core/gcore-python/commit/958b2a735265407c29cc2ccd4b06566f9151dd15))

## 0.24.0 (2025-12-10)

Full Changelog: [v0.23.0...v0.24.0](https://github.com/G-Core/gcore-python/compare/v0.23.0...v0.24.0)

### ⚠ BREAKING CHANGES

* **cloud:** replace PUT /cloud/v1/l7policies with PATCH
* **cdn:** streamline audit_logs naming
* **cloud:** rename load balancer pool member methods to create/delete
* streamline naming for create/replace models

### Features

* **api:** aggregated API specs update ([67dc79f](https://github.com/G-Core/gcore-python/commit/67dc79fea2b041b24b212a02e927ccbd243e4522))
* **api:** aggregated API specs update ([7656563](https://github.com/G-Core/gcore-python/commit/7656563fc5dd17e35f6818812ca099251cdda258))
* **api:** aggregated API specs update ([a1d51b8](https://github.com/G-Core/gcore-python/commit/a1d51b8ff11dc70e5f8f534cb45e87e1eba2cc14))
* **api:** aggregated API specs update ([c5159ef](https://github.com/G-Core/gcore-python/commit/c5159efb03e551f71ed83f7efd3a9b73f5017d1d))
* **api:** aggregated API specs update ([61299ed](https://github.com/G-Core/gcore-python/commit/61299edb52f077ab1cd4ac198b3ce59283fe779c))
* **api:** aggregated API specs update ([b745f43](https://github.com/G-Core/gcore-python/commit/b745f43a066be1d41dd690c0e767d60e495c4a6c))
* **dns:** enable terraform code generation for gcore_dns_network_mapping ([145f10c](https://github.com/G-Core/gcore-python/commit/145f10ce4125be5a97ec6f092e4056ff78b2f3b1))


### Bug Fixes

* **cdn:** streamline audit_logs naming ([cb075f5](https://github.com/G-Core/gcore-python/commit/cb075f51ee3bda135fbeb9eae1957ad0cda1c22a))
* **cloud:** fix types in examples ([8b73b2a](https://github.com/G-Core/gcore-python/commit/8b73b2ae7a25cd187f5eeeb8e264c8ea6b22aaa1))
* **cloud:** rename load balancer pool member methods to create/delete ([86346d4](https://github.com/G-Core/gcore-python/commit/86346d4fd0f464f120dd0ed6c1e7fb2b0107a625))
* **cloud:** replace PUT /cloud/v1/l7policies with PATCH ([310c86d](https://github.com/G-Core/gcore-python/commit/310c86dfebff83232844a7bed4b8c8094f0f38a6))
* **cloud:** use PATCH /cloud/v1/projects ([de29040](https://github.com/G-Core/gcore-python/commit/de29040774e27e8fd6ea552d6f47ca60a1992976))
* streamline naming for create/replace models ([06e1dc3](https://github.com/G-Core/gcore-python/commit/06e1dc32499533ad16b88458164ec5a9ea385cc5))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([616698d](https://github.com/G-Core/gcore-python/commit/616698d4f75cd79685904b3ff5cf7a4057525332))


### Chores

* add missing docstrings ([91761cb](https://github.com/G-Core/gcore-python/commit/91761cb4af0ee9824166a9b4eb966f981547d9ec))
* **docs:** use environment variables for authentication in code snippets ([2c2fa17](https://github.com/G-Core/gcore-python/commit/2c2fa1790799aab90409f65669bcb7f48659a7cb))
* update lockfile ([ece4535](https://github.com/G-Core/gcore-python/commit/ece45355779bfa9a8d3c68783cd3512236f83f96))

## 0.23.0 (2025-12-01)

Full Changelog: [v0.22.0...v0.23.0](https://github.com/G-Core/gcore-python/compare/v0.22.0...v0.23.0)

### ⚠ BREAKING CHANGES

* **cloud:** change *_and_poll signature types to correspond to regular methods

### Features

* **api:** aggregated API specs update ([66af572](https://github.com/G-Core/gcore-python/commit/66af57201d06fc54c6b79a59690982bcc107fbfa))
* **api:** aggregated API specs update ([8e6e84f](https://github.com/G-Core/gcore-python/commit/8e6e84f26b4dfc56558641e3996529f7552a7b9f))


### Bug Fixes

* **cloud:** change *_and_poll signature types to correspond to regular methods ([d58e9b4](https://github.com/G-Core/gcore-python/commit/d58e9b48d2aa104beef736c57b6170886bea6072))
* ensure streams are always closed ([e2716cb](https://github.com/G-Core/gcore-python/commit/e2716cbc3b7de2b3fe7eef68fa1c07dcf4014385))


### Chores

* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([7703d53](https://github.com/G-Core/gcore-python/commit/7703d534a550a9465212e391aeeef906cf589dd0))

## 0.22.0 (2025-11-25)

Full Changelog: [v0.21.0...v0.22.0](https://github.com/G-Core/gcore-python/compare/v0.21.0...v0.22.0)

### ⚠ BREAKING CHANGES

* **cloud:** k8s references from k8 to k8s
* **cloud:** updates to get/list LB l7 policy/rules models

### Features

* **api:** aggregated API specs update ([49ac2ae](https://github.com/G-Core/gcore-python/commit/49ac2ae5ff6575877adfc16d46454c1ddf9b4160))
* **api:** aggregated API specs update ([299adc0](https://github.com/G-Core/gcore-python/commit/299adc06cba63fb89bd3cd5f17d10188db08c735))
* **api:** aggregated API specs update ([fff1d1e](https://github.com/G-Core/gcore-python/commit/fff1d1e981d3c286288c77c0a9a7c3fa146abd80))
* **cloud:** updates to get/list LB l7 policy/rules models ([95a4cf1](https://github.com/G-Core/gcore-python/commit/95a4cf12132dc638e3a0994e3b5a5249b079e5ad))


### Bug Fixes

* add overloads to L7 policy polling methods to match create/replace signatures ([ecd63d8](https://github.com/G-Core/gcore-python/commit/ecd63d8704925bb86d232ea97e90bf7b45bb6e0b))
* add overloads to L7 policy polling methods to match create/replace signatures ([44d657e](https://github.com/G-Core/gcore-python/commit/44d657e515ffd4c65bdcd82a419f85db138ceeba))
* **cloud:** add overloads to L7 policy polling methods ([a639930](https://github.com/G-Core/gcore-python/commit/a639930e1d18b1a95ba4dfff4b847efc9093f5ef))
* **cloud:** k8s references from k8 to k8s ([96211ea](https://github.com/G-Core/gcore-python/commit/96211ea00c49baddd1ada6c26af994181bcd50de))
* resolve type errors in L7 policy/rule polling methods ([30e648f](https://github.com/G-Core/gcore-python/commit/30e648f9d9a5f6ed0ad7bb9b34272819d85fb594))


### Chores

* **internal:** codegen related update ([a6fbaff](https://github.com/G-Core/gcore-python/commit/a6fbaffe05cbdd3dac367525266a736d6b633ec1))

## 0.21.0 (2025-11-17)

Full Changelog: [v0.20.0...v0.21.0](https://github.com/G-Core/gcore-python/compare/v0.20.0...v0.21.0)

### Features

* **api:** aggregated API specs update ([0d13f58](https://github.com/G-Core/gcore-python/commit/0d13f58d129067316254f9907aebf3057495ca8d))

## 0.20.0 (2025-11-11)

Full Changelog: [v0.19.0...v0.20.0](https://github.com/G-Core/gcore-python/compare/v0.19.0...v0.20.0)

### Features

* **api:** aggregated API specs update ([767fdd5](https://github.com/G-Core/gcore-python/commit/767fdd5d74846369e3331efba210aff12a43e802))
* **cloud:** add support for GPU virtual clusters ([c406d97](https://github.com/G-Core/gcore-python/commit/c406d97d04db03f5c4d105f2e9761e9b8c2d96c8))


### Bug Fixes

* compat with Python 3.14 ([90bfffe](https://github.com/G-Core/gcore-python/commit/90bfffeed8b28a360e1489162d4dc6a28745b411))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([70e1cc8](https://github.com/G-Core/gcore-python/commit/70e1cc8404668e008c236881c5819eeff91725d6))


### Chores

* **package:** drop Python 3.8 support ([99955b9](https://github.com/G-Core/gcore-python/commit/99955b9208b2810fcbafbf5f8d941b5981faebbe))

## 0.19.0 (2025-11-07)

Full Changelog: [v0.18.0...v0.19.0](https://github.com/G-Core/gcore-python/compare/v0.18.0...v0.19.0)

### Features

* **api:** aggregated API specs update ([7c0231a](https://github.com/G-Core/gcore-python/commit/7c0231aa3836ea9ab69769c2c06fe3fb70ca4a7b))
* **api:** aggregated API specs update ([00be2a9](https://github.com/G-Core/gcore-python/commit/00be2a9da75503640bb2ce1383162c48170ef819))
* **api:** aggregated API specs update ([8469462](https://github.com/G-Core/gcore-python/commit/846946265537791605e00dd260d5bd1a8eb7bddf))
* **api:** aggregated API specs update ([2c780f3](https://github.com/G-Core/gcore-python/commit/2c780f329064bcabb64492d7a237f9865feffd14))

## 0.18.0 (2025-11-04)

Full Changelog: [v0.17.0...v0.18.0](https://github.com/G-Core/gcore-python/compare/v0.17.0...v0.18.0)

### Features

* **api:** aggregated API specs update ([c69f622](https://github.com/G-Core/gcore-python/commit/c69f622f4d085d5c93978edbf4deb2ecbe4279d6))
* **api:** aggregated API specs update ([e008291](https://github.com/G-Core/gcore-python/commit/e008291499f90553d12deffbcef5c4a9b6752f61))
* **api:** aggregated API specs update ([7e17f98](https://github.com/G-Core/gcore-python/commit/7e17f98624fecfb8d1ad5a53a001dcd20ca15214))
* **api:** aggregated API specs update ([01c7469](https://github.com/G-Core/gcore-python/commit/01c746977c89d813e54b97c87513960a5cba42c3))
* **api:** aggregated API specs update ([3ef8586](https://github.com/G-Core/gcore-python/commit/3ef8586481df9533a0627310458bb72b9b458d2f))
* **api:** aggregated API specs update ([af54c88](https://github.com/G-Core/gcore-python/commit/af54c886222ea41e6ef57d8683fbb64e2b688a15))
* **api:** aggregated API specs update ([4e62953](https://github.com/G-Core/gcore-python/commit/4e629534e07db80d93c46e5ccc5e3d2ba48d9eb4))
* **api:** aggregated API specs update ([18614cb](https://github.com/G-Core/gcore-python/commit/18614cb786fd3ea9020cee18c2a23c4c81f116f3))
* **api:** aggregated API specs update ([926c0dd](https://github.com/G-Core/gcore-python/commit/926c0ddfcef420ba47eca7b399ea43462a18371a))
* **cloud:** add support for postgres ([2802edf](https://github.com/G-Core/gcore-python/commit/2802edf3bbac88b644ba8ff4d5b83dc0606e4b48))


### Bug Fixes

* **client:** close streams without requiring full consumption ([cd7152c](https://github.com/G-Core/gcore-python/commit/cd7152cd959a9984e5c60edb41d16fa2db342012))
* **cloud:** members not optional in lb pools create_and_poll ([27bc07a](https://github.com/G-Core/gcore-python/commit/27bc07acab63505e03f4a5b51e21544fe84877ec))


### Chores

* **cloud:** add *_and_poll() to *WithRawResponse and *WithStreaming ([d8886ce](https://github.com/G-Core/gcore-python/commit/d8886ce4abeadd3d260c3f533e72b778d521482c))
* **internal/tests:** avoid race condition with implicit client cleanup ([67e4c77](https://github.com/G-Core/gcore-python/commit/67e4c77936fca0b2192b931ec71003dd62383c81))
* **internal:** grammar fix (it's -&gt; its) ([9bf8a18](https://github.com/G-Core/gcore-python/commit/9bf8a18f42a2122f43d9084ff3287e4d1aa7dd95))

## 0.17.0 (2025-10-21)

Full Changelog: [v0.16.0...v0.17.0](https://github.com/G-Core/gcore-python/compare/v0.16.0...v0.17.0)

### ⚠ BREAKING CHANGES

* **cloud:** rename to projects update
* **cloud:** use new PATCH files shares endpoint

### Features

* **api:** aggregated API specs update ([c9d6195](https://github.com/G-Core/gcore-python/commit/c9d6195649fd18c9c32107a978e0d40032b285be))
* **cdn:** add methods to list aws and alibaba regions ([0d1d290](https://github.com/G-Core/gcore-python/commit/0d1d290d11626ac0128329c005d048f0ab2f25dc))
* **client:** add client opt for cloud polling timeout ([bad7ecb](https://github.com/G-Core/gcore-python/commit/bad7ecbb58f0decc31e4091c5bdb0585b7471b09))
* **cloud:** add polling_timeout_seconds parameter to polling methods ([8b556ae](https://github.com/G-Core/gcore-python/commit/8b556aefc279caddaad9782747b2d6f65a523067))
* **cloud:** enable TF for placement groups ([63abaa7](https://github.com/G-Core/gcore-python/commit/63abaa7156d2a79bf27f9ba0d3fa2abb3a31aafd))
* **cloud:** support polling timeout in tasks.poll() ([3f8a419](https://github.com/G-Core/gcore-python/commit/3f8a419a48677e5f443248c963e045dd5169979a))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([e906ee6](https://github.com/G-Core/gcore-python/commit/e906ee6224833181a4618bcd63671d9a131bca94))
* **cloud:** fix file shares examples ([c5cc6fa](https://github.com/G-Core/gcore-python/commit/c5cc6fa74b5678d08d1ed750872e424edd6f5377))
* **cloud:** rename to projects update ([f3f52da](https://github.com/G-Core/gcore-python/commit/f3f52da58998f8ce2637b99d1c944fd692861b48))
* **cloud:** use new PATCH files shares endpoint ([2ac6bce](https://github.com/G-Core/gcore-python/commit/2ac6bce8afbe4783620060964359d01ab105979e))


### Refactors

* **spec:** remove CDN deprecated endpoints ([193a257](https://github.com/G-Core/gcore-python/commit/193a257bcf3e00d85179809e63fa47b021323f65))

## 0.16.0 (2025-10-17)

Full Changelog: [v0.15.0...v0.16.0](https://github.com/G-Core/gcore-python/compare/v0.15.0...v0.16.0)

### ⚠ BREAKING CHANGES

* **cloud:** remove get and update list method for billing reservations
* **cloud:** use load_balancer_id in poll methods
* **cloud:** rename to load_balancer_id path param
* **cloud:** rename inference applications deployments update method

### Features

* **api:** aggregated API specs update ([ca4cbba](https://github.com/G-Core/gcore-python/commit/ca4cbbabc6c143e6a1c54e861cafbd38f906ebda))
* **api:** aggregated API specs update ([0d92524](https://github.com/G-Core/gcore-python/commit/0d92524c16aeac6e96b0360c49de70a7912a8485))
* **api:** aggregated API specs update ([7a58cae](https://github.com/G-Core/gcore-python/commit/7a58cae302e7a3818a11e616f967719db076fd25))
* **api:** aggregated API specs update ([c62d748](https://github.com/G-Core/gcore-python/commit/c62d7487ca76b74c8919c438b7d50979e75527cf))
* **api:** aggregated API specs update ([2a0347f](https://github.com/G-Core/gcore-python/commit/2a0347fbb670a29ca3cf0418637cd843bd8d535d))
* **api:** aggregated API specs update ([1dc8993](https://github.com/G-Core/gcore-python/commit/1dc8993163988b192d1f7bcedd2b4df4259f60d0))
* **api:** aggregated API specs update ([555824b](https://github.com/G-Core/gcore-python/commit/555824be97e936b2a20077870dfd50a186446e40))
* **api:** aggregated API specs update ([c8e06a9](https://github.com/G-Core/gcore-python/commit/c8e06a9c4db67838c190b7f985fa99e2ee1bc9f4))
* **api:** aggregated API specs update ([8eedd02](https://github.com/G-Core/gcore-python/commit/8eedd0251f0519932ccc9034383e56bbf385d4a4))
* **cloude:** remove cloud_lbmember name ([0c3df8e](https://github.com/G-Core/gcore-python/commit/0c3df8e1330f518b13457f5a3db8e7fcf963ea42))
* **cloud:** remove get and update list method for billing reservations ([b030ed6](https://github.com/G-Core/gcore-python/commit/b030ed6e7f2b26e396ebd2852df3e915b425a761))


### Bug Fixes

* **cloud:** rename to load_balancer_id path param ([ab273aa](https://github.com/G-Core/gcore-python/commit/ab273aadd364dc22a1fc8538c8b39c916fd002df))
* **cloud:** use load_balancer_id in poll methods ([6b55df9](https://github.com/G-Core/gcore-python/commit/6b55df953a0695b0047b947ab898063df9cba044))
* **examples:** suppress deprecation warnings for file shares update method ([#104](https://github.com/G-Core/gcore-python/issues/104)) ([0b3c21b](https://github.com/G-Core/gcore-python/commit/0b3c21b3f1f971a9d22623ae03c136e3aad84611))


### Chores

* add pull request template ([2e2997b](https://github.com/G-Core/gcore-python/commit/2e2997b1591f489581b6568c7adf9a4d39d5501c))
* **ci:** add fossa ([289bea8](https://github.com/G-Core/gcore-python/commit/289bea8c56d1b1e185dc1374628115b708aedcfa))
* **cloud:** rename inference applications deployments update method ([c672843](https://github.com/G-Core/gcore-python/commit/c6728438a3bba4d47de59bbdf30fe4d1c82a3d97))
* **internal:** detect missing future annotations with ruff ([9b55e6e](https://github.com/G-Core/gcore-python/commit/9b55e6e072e0f4210545e5fb91d5b628a8512cf8))

## 0.15.0 (2025-10-02)

Full Changelog: [v0.14.0...v0.15.0](https://github.com/G-Core/gcore-python/compare/v0.14.0...v0.15.0)

### Features

* **api:** Add missing reserved_fixed_ips update method ([b7b8db0](https://github.com/G-Core/gcore-python/commit/b7b8db03bd75a4889601a6da2fd5aa2e8004a141))
* **api:** aggregated API specs update ([8c59ffa](https://github.com/G-Core/gcore-python/commit/8c59ffa34fe9d77a585d53b9243fb0ec752de5c4))
* **api:** aggregated API specs update ([6281066](https://github.com/G-Core/gcore-python/commit/6281066df4e5cc479f7f53f731e4ecd59f41e7a4))
* **api:** aggregated API specs update ([0a2f63b](https://github.com/G-Core/gcore-python/commit/0a2f63b1a5dd2dfc26cfa9b3e5ad4e4e997e4988))


### Bug Fixes

* **examples:** remove unnecessary None checks in quota examples ([#97](https://github.com/G-Core/gcore-python/issues/97)) ([ff71c83](https://github.com/G-Core/gcore-python/commit/ff71c83bb97e5fabf25efc32e0e2f6b60addbe64))

## 0.14.0 (2025-09-30)

Full Changelog: [v0.13.0...v0.14.0](https://github.com/G-Core/gcore-python/compare/v0.13.0...v0.14.0)

### Features

* **api:** aggregated API specs update ([0e7967b](https://github.com/G-Core/gcore-python/commit/0e7967b1f6be77cac807f5a1e3d3483c9151902b))
* **api:** aggregated API specs update ([0199b8c](https://github.com/G-Core/gcore-python/commit/0199b8ccce3fc74ba60586b9cbe6411b29bf9ece))
* **api:** aggregated API specs update ([0784cf9](https://github.com/G-Core/gcore-python/commit/0784cf918ef8d820a7a5ecfd9dc5b185829041a1))
* **api:** aggregated API specs update ([f1ff659](https://github.com/G-Core/gcore-python/commit/f1ff65992ff4992554d00f10b1b17794155cc129))
* **api:** aggregated API specs update ([fc88cbd](https://github.com/G-Core/gcore-python/commit/fc88cbd66531167d50927d4a87c53d5f05fbdce1))
* **cdn:** add API support ([e07d4e7](https://github.com/G-Core/gcore-python/commit/e07d4e7427042c2996c6dae86f70f0cc86a8d6d5))
* **cloud:** enable TF for floating IPs ([634f34b](https://github.com/G-Core/gcore-python/commit/634f34b96fb7e74f7566493af8716f90d85016b9))


### Bug Fixes

* **client:** correctly generate K8sClusterSlurmAddonV2Serializers ([e5961ca](https://github.com/G-Core/gcore-python/commit/e5961ca7683a89bf6e551bd4bedd82c1b76e4052))


### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([9482c47](https://github.com/G-Core/gcore-python/commit/9482c4755e629b9411290d189efc5f1de4bbbec1))
* improve example values ([2560541](https://github.com/G-Core/gcore-python/commit/25605419cf1878d28e77251f44246b68212efb8a))
* **internal:** update pydantic dependency ([adf8df6](https://github.com/G-Core/gcore-python/commit/adf8df69810c6e978395aefe12b4ba6f88772d16))
* **types:** change optional parameter type from NotGiven to Omit ([24bebe1](https://github.com/G-Core/gcore-python/commit/24bebe1a809b38732c6b960f5cc6703fa2d6d1be))
* use Omit in more places ([2a4abf1](https://github.com/G-Core/gcore-python/commit/2a4abf1aa6f07c9c9f8d16150caed76e8e35a146))

## 0.13.0 (2025-09-16)

Full Changelog: [v0.12.0...v0.13.0](https://github.com/G-Core/gcore-python/compare/v0.12.0...v0.13.0)

### ⚠ BREAKING CHANGES

* **waap:** model references

### Features

* **api:** aggregated API specs update ([2954990](https://github.com/G-Core/gcore-python/commit/295499000a8e2b1ef24ae497cb34fafbf38f2149))
* **api:** aggregated API specs update ([09db4dd](https://github.com/G-Core/gcore-python/commit/09db4dde07cbec7bb8e94348c6ef78578c3022d3))
* **api:** aggregated API specs update ([a2de60c](https://github.com/G-Core/gcore-python/commit/a2de60c773c01aeb6223001a0d8bff5463fa82ef))
* **api:** aggregated API specs update ([ccf4739](https://github.com/G-Core/gcore-python/commit/ccf4739750f27e01ece2ff147458dd7fe9305437))
* **api:** aggregated API specs update ([484ee11](https://github.com/G-Core/gcore-python/commit/484ee1144558b56f40d5bc41b9613370dc74c42e))
* **cloud:** support floating IPs update ([28a8882](https://github.com/G-Core/gcore-python/commit/28a888260878577e697004da02077ef96a8616ad))
* **dns:** replace post with get in check delegation status ([ddd12bd](https://github.com/G-Core/gcore-python/commit/ddd12bd4782b8883d82b97a45d043ad3970ee31a))


### Bug Fixes

* **cloud:** floating ips examples ([bf8a5dd](https://github.com/G-Core/gcore-python/commit/bf8a5ddff3e777441db47163dc03b73052d99ecd))
* **waap:** model references ([4f69e7e](https://github.com/G-Core/gcore-python/commit/4f69e7e5aa778cf82357d7d097e874100bfa9e0d))

## 0.12.0 (2025-09-11)

Full Changelog: [v0.11.0...v0.12.0](https://github.com/G-Core/gcore-python/compare/v0.11.0...v0.12.0)

### Features

* **api:** aggregated API specs update ([3fbc8f1](https://github.com/G-Core/gcore-python/commit/3fbc8f1a6126f4cb6d9e6a0aff7f35f67f77ec6f))
* **cloud:** add create_and_poll() and delete_and_poll() to reserved fixed ips ([6e6efc0](https://github.com/G-Core/gcore-python/commit/6e6efc03de62b895199a043e0cf1b396aefb0d01))
* **cloud:** add polling methods to volumes ([3537e8c](https://github.com/G-Core/gcore-python/commit/3537e8c5b6ebd0500868dfc2b14bfeba735fe1f5))


### Refactors

* **storage:** use v2 endpoint ([4a00499](https://github.com/G-Core/gcore-python/commit/4a00499c3bc80a6f06e476bd1c0d544bd1c46cef))

## 0.11.0 (2025-09-09)

Full Changelog: [v0.10.0...v0.11.0](https://github.com/G-Core/gcore-python/compare/v0.10.0...v0.11.0)

### ⚠ BREAKING CHANGES

* **cloud:** update polling methods signatures
* **cloud:** migrate baremetal gpu cluster from v1 to v3
* **cloud:** support inference applications

### Features

* **api:** aggregated API specs update ([931c594](https://github.com/G-Core/gcore-python/commit/931c5941afceba9f8cc84e0bfccd727f5d40bd78))
* **api:** aggregated API specs update ([f6d4e0b](https://github.com/G-Core/gcore-python/commit/f6d4e0b2f721b6dfa531e6246fb7f4ea270df75e))
* **api:** aggregated API specs update ([86b63d4](https://github.com/G-Core/gcore-python/commit/86b63d43a1197c77ae6d6df4f92d32a78db5f211))
* **api:** aggregated API specs update ([09eeb95](https://github.com/G-Core/gcore-python/commit/09eeb95a33f70d79cab833c0e1c599fa13599e69))
* **api:** aggregated API specs update ([72414c5](https://github.com/G-Core/gcore-python/commit/72414c5f92c2af4a7fbc01871271900b5a69ac88))
* **api:** aggregated API specs update ([ac889a3](https://github.com/G-Core/gcore-python/commit/ac889a31107fb2c9525a8a3e9c889bdf718b2b8b))
* **api:** aggregated API specs update ([98f84bc](https://github.com/G-Core/gcore-python/commit/98f84bce3cba455432f94aa21de179c385dc2e19))
* **api:** aggregated API specs update ([86d8c4f](https://github.com/G-Core/gcore-python/commit/86d8c4fdc885691c89c385f275c5fc389d81c349))
* **api:** aggregated API specs update ([ba76405](https://github.com/G-Core/gcore-python/commit/ba76405912b3514cd9836c49d41b564ca911e8f5))
* **api:** aggregated API specs update ([d14eac7](https://github.com/G-Core/gcore-python/commit/d14eac7b754be27c008f44462cc965292ab99e95))
* **api:** aggregated API specs update ([6a790b7](https://github.com/G-Core/gcore-python/commit/6a790b71e6dbd81e33aba81612c305240624062d))
* **api:** aggregated API specs update ([e7e2da7](https://github.com/G-Core/gcore-python/commit/e7e2da79cf39dc75aa4178267b7ee5a4c31189ae))
* **api:** aggregated API specs update ([165290f](https://github.com/G-Core/gcore-python/commit/165290f51e1c0913b9b324e03472e4134f9c7a31))
* **api:** aggregated API specs update ([a56f7d1](https://github.com/G-Core/gcore-python/commit/a56f7d17b74d5c4489024edf5f3eb26eef802ee1))
* **api:** aggregated API specs update ([12bae5a](https://github.com/G-Core/gcore-python/commit/12bae5ae6cbdf0d73da465fd7b1382c36ff0d00a))
* **api:** aggregated API specs update ([2576f9c](https://github.com/G-Core/gcore-python/commit/2576f9cc8143fae02367e94e693cafd8954209c4))
* **api:** aggregated API specs update ([5de1f95](https://github.com/G-Core/gcore-python/commit/5de1f95503f39a215839a6d86d9f692904ee0267))
* **api:** api update ([602ef7d](https://github.com/G-Core/gcore-python/commit/602ef7daaecd2c5af65a73adba4055e4a74c8c24))
* **api:** manual updates ([fca7094](https://github.com/G-Core/gcore-python/commit/fca709450327ddeaaa6d9bc70a15f4ac3f46d30c))
* **api:** manual upload of aggregated API specs ([45843a3](https://github.com/G-Core/gcore-python/commit/45843a39873202bec9e0874526379cce0beb5f4e))
* **api:** manual upload of aggregated API specs ([aad5c71](https://github.com/G-Core/gcore-python/commit/aad5c71696d2940cd3f443208c02acc55d5224e3))
* **api:** update field_value type ([2095ccc](https://github.com/G-Core/gcore-python/commit/2095ccc238b559e5e048bc86ddd8e93ba372f88c))
* **cloud:** add create_and_poll() and delete_and_poll() for floating ips ([e645a83](https://github.com/G-Core/gcore-python/commit/e645a83cde29fe50dfed87d1a9210134ec4b8e7b))
* **cloud:** add create_and_poll() for subnets ([d537d4e](https://github.com/G-Core/gcore-python/commit/d537d4ed2dfda9d051d327a9bf55726f04f35104))
* **cloud:** add managed k8s ([9b88526](https://github.com/G-Core/gcore-python/commit/9b885262b12c18f0f7ac17accebbb7e8d4ad4d48))
* **cloud:** add new_and_poll() and delete_and_poll() for networks ([fda3191](https://github.com/G-Core/gcore-python/commit/fda3191c4680f62d2eb089db258e6c9e084303ed))
* **cloud:** add polling for instance action and interfaces attach/detach ([ee59347](https://github.com/G-Core/gcore-python/commit/ee593474fe8f788d09b40e46995af7f993a32dcd))
* **cloud:** fetch client_id from iam in cloud quotas examples ([daaf5e1](https://github.com/G-Core/gcore-python/commit/daaf5e10afe359e74d93fb9ac96061a38be107e0))
* **cloud:** migrate baremetal gpu cluster from v1 to v3 ([064b2a1](https://github.com/G-Core/gcore-python/commit/064b2a1b4d56ff3ab8a1ed34e2dca64c9713d0b6))
* **cloud:** remove inference model examples ([958a08e](https://github.com/G-Core/gcore-python/commit/958a08e51577f6e5d95fee19500e8f96bd552c95))
* **cloud:** support inference applications ([dcf34ac](https://github.com/G-Core/gcore-python/commit/dcf34acdce70518d2bf119d7ca5ae50bec1521bd))
* **cloud:** use PATCH /v2/lbpools ([6da421d](https://github.com/G-Core/gcore-python/commit/6da421dc9d1d3206b5e2275a84432cd0ce1b9d3b))
* improve future compat with pydantic v3 ([cc3a79f](https://github.com/G-Core/gcore-python/commit/cc3a79f2268c3ced2cd0c3634844d01f2657c69d))
* **s3:** add object storage ([7e1ed77](https://github.com/G-Core/gcore-python/commit/7e1ed7740b7a41454bc2779a0937f0c5ca5d4349))
* **storage:** make list storage locations paginated ([eeef646](https://github.com/G-Core/gcore-python/commit/eeef64689a62cb5cc0546a616097f35e85492803))
* **types:** replace List[str] with SequenceNotStr in params ([be5d331](https://github.com/G-Core/gcore-python/commit/be5d331430334b7e779510f99a4b6a0cddbb1859))


### Bug Fixes

* avoid newer type syntax ([adc20b7](https://github.com/G-Core/gcore-python/commit/adc20b7bc65b75be4d105cf05a886f7db299b2c4))
* **cloud:** update polling methods signatures ([a5ecf6a](https://github.com/G-Core/gcore-python/commit/a5ecf6ac3957532628de955bd12b9f8c688861c4))
* **dns:** fix dns methods ([58f23c0](https://github.com/G-Core/gcore-python/commit/58f23c07ac519f9ba1c181bce131a140e2151001))
* **types:** add missing types to method arguments ([bec1dff](https://github.com/G-Core/gcore-python/commit/bec1dff935fa6f933c7ac3118e0e4e5cb463da72))
* **waap:** fix component name ([fabb616](https://github.com/G-Core/gcore-python/commit/fabb616f3fe3c61a262275d7e359c7eafc324c8c))


### Chores

* formatting ([d739b03](https://github.com/G-Core/gcore-python/commit/d739b037fdfdee9dd86a283434b4d8c2e2c9b53b))
* **internal:** add Sequence related utils ([daed5dc](https://github.com/G-Core/gcore-python/commit/daed5dc7a9f6bd8472da9bcad00bf4521f13efe8))
* **internal:** change ci workflow machines ([cf13b4e](https://github.com/G-Core/gcore-python/commit/cf13b4e5b16ce2f6921e65fd780d780e83e95ff5))
* **internal:** codegen related update ([0c6db9d](https://github.com/G-Core/gcore-python/commit/0c6db9d80d32327c271a81355319dea0c01b3836))
* **internal:** codegen related update ([835fc54](https://github.com/G-Core/gcore-python/commit/835fc543e274454f92ee81b2af8ff5a203a14571))
* **internal:** codegen related update ([04ce18a](https://github.com/G-Core/gcore-python/commit/04ce18ae770a17fe93fdec4c594d8e1ff03b0b4a))
* **internal:** detect breaking changes when removing endpoints ([1fdb544](https://github.com/G-Core/gcore-python/commit/1fdb544c80140e5133cc272d5b1c1f2de897ce0f))
* **internal:** improve breaking change detection ([cf699e9](https://github.com/G-Core/gcore-python/commit/cf699e9bc204256be2984ed0d6bb42ec168d0f79))
* **internal:** minor formatting change ([48573ba](https://github.com/G-Core/gcore-python/commit/48573ba1f69b104a005f35595b8f7829790c75bc))
* **internal:** move mypy configurations to `pyproject.toml` file ([1961ffc](https://github.com/G-Core/gcore-python/commit/1961ffc1434500cf47ef776b947d5eff18307502))
* **internal:** update comment in script ([e11594e](https://github.com/G-Core/gcore-python/commit/e11594e226edc21949a7e319434a6032271f7119))
* **internal:** update pyright exclude list ([5b2e640](https://github.com/G-Core/gcore-python/commit/5b2e640a05b46321c6d0438a89a39b5f3e0f2678))
* **tests:** simplify `get_platform` test ([ebdb1e8](https://github.com/G-Core/gcore-python/commit/ebdb1e8ed0ab19745e41cd354196368cff14ef20))
* **tests:** unskip tests failing due to wrong Prism routing ([6d24ccb](https://github.com/G-Core/gcore-python/commit/6d24ccb1b2927f54e4ca795a484c9c924c2f50d4))
* update @stainless-api/prism-cli to v5.15.0 ([bed3f36](https://github.com/G-Core/gcore-python/commit/bed3f36e6b0ec73ae01f595e45ffad0052721df2))
* update github action ([13f7cfd](https://github.com/G-Core/gcore-python/commit/13f7cfdd9e914d9b65bd3758b812f08a8a6f24cb))

## 0.10.0 (2025-08-07)

Full Changelog: [v0.9.0...v0.10.0](https://github.com/G-Core/gcore-python/compare/v0.9.0...v0.10.0)

### ⚠ BREAKING CHANGES

* **security:** rename bgp_announces change() to toggle()
* **waap:** refactor WAAP models

### Features

* add example snippet to invite user and assign cloud role ([4baccef](https://github.com/G-Core/gcore-python/commit/4baccef0422ea20f5abbfc9808f447cc0df02e30))
* **api:** aggregated API specs update ([70ea19b](https://github.com/G-Core/gcore-python/commit/70ea19b8c9cd53810565c71dba1fc62e03a81090))
* **api:** aggregated API specs update ([163edcb](https://github.com/G-Core/gcore-python/commit/163edcb6b3ed69edf0e7c6711217433a73564e10))


### Bug Fixes

* **security:** rename bgp_announces change() to toggle() ([070f06a](https://github.com/G-Core/gcore-python/commit/070f06ad558afb0d608c4de45e4ce8e7d118dccd))


### Chores

* **internal:** fix ruff target version ([c91b1b3](https://github.com/G-Core/gcore-python/commit/c91b1b38e01a3a65b3b82e01bf6babd6a73ac233))


### Refactors

* **waap:** refactor WAAP models ([fb20add](https://github.com/G-Core/gcore-python/commit/fb20add86c0b2d8e122afe9216d5b84bcd59fb11))

## 0.9.0 (2025-07-31)

Full Changelog: [v0.8.0...v0.9.0](https://github.com/G-Core/gcore-python/compare/v0.8.0...v0.9.0)

### Features

* **api:** aggregated API specs update ([bf2d683](https://github.com/G-Core/gcore-python/commit/bf2d683bf679eb9412ebd278f9ca4eceb2f4ba6e))
* **api:** aggregated API specs update ([95d8011](https://github.com/G-Core/gcore-python/commit/95d8011132b86e8bf5311c14d43aea7a416d778c))
* **client:** support file upload requests ([980b86d](https://github.com/G-Core/gcore-python/commit/980b86dfcc7697fcc2e856bf030c971c54a509f1))
* **fastedge:** add binaries create method ([04bd754](https://github.com/G-Core/gcore-python/commit/04bd754a175b1d3e3bfcef2abdd1c96081c535df))
* **security:** add security api ([7e85df3](https://github.com/G-Core/gcore-python/commit/7e85df337055265317c988f67f6b0a4831dbdf73))

## 0.8.0 (2025-07-29)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/G-Core/gcore-python/compare/v0.7.0...v0.8.0)

### Features

* **api:** aggregated API specs update ([7296a44](https://github.com/G-Core/gcore-python/commit/7296a445ea8d692bcc212a91f1e6f2ea7c100789))
* **api:** aggregated API specs update ([bdd85b5](https://github.com/G-Core/gcore-python/commit/bdd85b5413ad87e01c6fca896c7160f6ee854491))


### Bug Fixes

* **iam:** remove obsolete pagination scheme ([85723b3](https://github.com/G-Core/gcore-python/commit/85723b333ed196f3501fdf84d7a7155bf0f700b7))
* **iam:** user model path ([e5429bb](https://github.com/G-Core/gcore-python/commit/e5429bb95df2710c7937e1125af25a268e8428e0))

## 0.7.0 (2025-07-25)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/G-Core/gcore-python/compare/v0.6.0...v0.7.0)

### Features

* **api:** aggregated API specs update ([56f5995](https://github.com/G-Core/gcore-python/commit/56f5995eafb29076d88fc586a2a05954399b6a30))
* **api:** aggregated API specs update ([7c593d2](https://github.com/G-Core/gcore-python/commit/7c593d2e5a95b1b67182535dc7510c602f5d2108))
* **api:** aggregated API specs update ([fdc5efd](https://github.com/G-Core/gcore-python/commit/fdc5efd0654c53fdfd29aba3a22072f001b0296e))
* **cloud:** add cost and usage reports ([bd8f648](https://github.com/G-Core/gcore-python/commit/bd8f648c6f97121eede374cdd4aea754317f718b))
* **streaming:** add streaming api ([025ee94](https://github.com/G-Core/gcore-python/commit/025ee94a20aed69abac1ffd608950f88dd6b4cda))


### Bug Fixes

* **parsing:** ignore empty metadata ([b64a2b6](https://github.com/G-Core/gcore-python/commit/b64a2b6bef89b3ec2075fa4f0ed3545a52cec0c9))
* **parsing:** parse extra field types ([fc9c2a6](https://github.com/G-Core/gcore-python/commit/fc9c2a6795202626e23f5303d0d2617b41ed9557))


### Chores

* **project:** add settings file for vscode ([e1a685b](https://github.com/G-Core/gcore-python/commit/e1a685b1719cb6d856fb088e56d7a384e7eca795))


### Refactors

* **cloud:** ignore deprecation warn in gpu baremetal polling methods ([6d8ae98](https://github.com/G-Core/gcore-python/commit/6d8ae9830f788b0b9fa49d9ef41ab9e06cd8485d))

## 0.6.0 (2025-07-18)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/G-Core/gcore-python/compare/v0.5.0...v0.6.0)

### Features

* **api:** aggregated API specs update ([ce31169](https://github.com/G-Core/gcore-python/commit/ce311695bbea628175adc51f9f1a2545eb213d01))
* clean up environment call outs ([2842d39](https://github.com/G-Core/gcore-python/commit/2842d3970f535d9095065ca681eaad809ea792e1))
* **cloud:** add audit logs ([2b0fe4c](https://github.com/G-Core/gcore-python/commit/2b0fe4cd8e7e125958c2784fb1a8f26209457e2d))
* **cloud:** add baremetal examples ([1193361](https://github.com/G-Core/gcore-python/commit/1193361f59f54de3ba454c4d23bb16c9ea87ac4b))
* **cloud:** add inference api_keys subresource ([4857d4e](https://github.com/G-Core/gcore-python/commit/4857d4eae79e51969c80e28309a4b452e4a8a597))

## 0.5.0 (2025-07-14)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/G-Core/gcore-python/compare/v0.4.0...v0.5.0)

### ⚠ BREAKING CHANGES

* **cloud:** refactor cloud inference models

### Features

* **api:** aggregated API specs update ([d1ae8cd](https://github.com/G-Core/gcore-python/commit/d1ae8cd01bc978e9afc8cefaae2799178a3c1e35))
* **api:** aggregated API specs update ([a182213](https://github.com/G-Core/gcore-python/commit/a182213096bdf7338261105c95c8b1e399d0f408))
* **api:** manual updates ([3ba0065](https://github.com/G-Core/gcore-python/commit/3ba0065f84e200ad4ae981e4189ae68a9cf3fff6))
* **api:** manual upload of aggregated API specs ([354a103](https://github.com/G-Core/gcore-python/commit/354a103447e5a3e9c69b11b871e9dec0e9ee7dc8))
* **cloud:** add inference examples ([2fe1536](https://github.com/G-Core/gcore-python/commit/2fe153665d086ee5c80ae99935b4d222065525a1))
* **cloud:** update secrets examples with pagination ([2909ae2](https://github.com/G-Core/gcore-python/commit/2909ae2e9d352fa07c70fdf64346db76d379f10e))
* **fastedge:** add api ([bec64b0](https://github.com/G-Core/gcore-python/commit/bec64b0db3ac113a875908ab5cb5041f4b1ed4aa))


### Bug Fixes

* **client:** don't send Content-Type header on GET requests ([1640b0b](https://github.com/G-Core/gcore-python/commit/1640b0b861aaf560c09b1cc651e3e1ffbb9b0095))
* **cloud:** update polling signatures after refactor ([1ee9ef9](https://github.com/G-Core/gcore-python/commit/1ee9ef98c604959f724c5c72317893089674debc))
* **parsing:** correctly handle nested discriminated unions ([3d16223](https://github.com/G-Core/gcore-python/commit/3d16223c06ee81a46657f37fb43621d095d4d9e5))


### Chores

* **client:** set default timeout to be 2 mins ([17159a0](https://github.com/G-Core/gcore-python/commit/17159a03ed71b64f03fde8cbf85d92ec0db29b31))
* **internal:** bump pinned h11 dep ([d0da186](https://github.com/G-Core/gcore-python/commit/d0da186d6203a09c7aec841287c02455b9c3b6df))
* **package:** mark python 3.13 as supported ([1440f43](https://github.com/G-Core/gcore-python/commit/1440f43464c3f5cbfb68df908792ab503656c63b))
* **readme:** fix version rendering on pypi ([8a8281c](https://github.com/G-Core/gcore-python/commit/8a8281c749792394c73b4d38f89d43fd0b6b1573))


### Refactors

* **cloud:** refactor cloud inference models ([3886c6d](https://github.com/G-Core/gcore-python/commit/3886c6d8244c58424cf09eb4514441e7e0afa7a1))

## 0.4.0 (2025-07-04)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/G-Core/gcore-python/compare/v0.3.0...v0.4.0)

### ⚠ BREAKING CHANGES

* **cloud:** remove list suitable from bm flavors
* remove list suitable and list for resize from instance flavors

### Features

* **api:** aggregated API specs update ([7395880](https://github.com/G-Core/gcore-python/commit/7395880c1291632db977714b43de1ab7061c23ed))
* **api:** aggregated API specs update ([dd87a63](https://github.com/G-Core/gcore-python/commit/dd87a630497b9dd478330bb190920da41fc6b6da))
* **api:** aggregated API specs update ([d4b4f22](https://github.com/G-Core/gcore-python/commit/d4b4f221489c1047b8e92752a1da014f1af59af9))
* **api:** aggregated API specs update ([a942886](https://github.com/G-Core/gcore-python/commit/a9428867b76afd4e3e0adb5892c007c3b8922fca))
* **api:** aggregated API specs update ([8b5d094](https://github.com/G-Core/gcore-python/commit/8b5d094f732e0c5f236f8bfc32fe069a6fd412ed))
* **api:** aggregated API specs update ([c86820e](https://github.com/G-Core/gcore-python/commit/c86820e1ca68185902d8e5e3cb911fca6d4dc10b))
* **api:** aggregated API specs update ([26b81bd](https://github.com/G-Core/gcore-python/commit/26b81bdeb1d84c2bc72a34e046db8fb1b1e5fcd1))
* **api:** update via SDK Studio ([96a27dd](https://github.com/G-Core/gcore-python/commit/96a27dd845f5fe9128b111171feb6c065f0c2916))
* **api:** update via SDK Studio ([1da4aa3](https://github.com/G-Core/gcore-python/commit/1da4aa370b1e633b002e1be99b7c5f3cf785ebc7))
* **client:** add support for aiohttp ([a983aee](https://github.com/G-Core/gcore-python/commit/a983aee8dd4ddf7d111f4798c89cfd3f341568d4))
* **cloud:** add floating IPs examples ([9010134](https://github.com/G-Core/gcore-python/commit/90101344d7fdf1ba0c8f55bc290ffe7839cb6af0))
* **cloud:** add instances examples ([a38f100](https://github.com/G-Core/gcore-python/commit/a38f10024534ab8c65ff72e96f49100bfaeb17a1))
* **cloud:** add load balancers examples ([#50](https://github.com/G-Core/gcore-python/issues/50)) ([c73f5d1](https://github.com/G-Core/gcore-python/commit/c73f5d1b84dbd2c96c9383100a93c89c8cf5e498))
* **cloud:** add networks examples ([5f32d6f](https://github.com/G-Core/gcore-python/commit/5f32d6f75aec5a7ff33729c65984f8b171910f8b))
* **cloud:** add reserved fixed ips examples ([a42b974](https://github.com/G-Core/gcore-python/commit/a42b974dde0d61edd9efa8f5929c0cbd967eebf8))
* **cloud:** add routers examples ([aba1f63](https://github.com/G-Core/gcore-python/commit/aba1f6343d40a6c6181929923b80a31d0bae332c))
* **cloud:** add security groups examples ([5c4f2a5](https://github.com/G-Core/gcore-python/commit/5c4f2a57603a5940c13220770e363c1e597ec48d))
* **cloud:** add volumes examples ([57ddcba](https://github.com/G-Core/gcore-python/commit/57ddcba83e1664b765c1c16e9ee314f6af74c38b))
* **iam:** add IAM ([1507ac3](https://github.com/G-Core/gcore-python/commit/1507ac37f5d588a999880cf5f51c94293f65b039))
* **images:** add instance images examples ([ecc8d91](https://github.com/G-Core/gcore-python/commit/ecc8d91c94df8c09ab4aeb5f89c966f03924caed))


### Bug Fixes

* **ci:** correct conditional ([b8d8b92](https://github.com/G-Core/gcore-python/commit/b8d8b9275a3c0d0864cfbd0d396a68cfd07c0b7b))
* **ci:** release-doctor — report correct token name ([0bf3b18](https://github.com/G-Core/gcore-python/commit/0bf3b1850e85aa8d9b635dcee9aeaf416f35df6c))
* **cloud:** linting on load balancer examples ([3534bea](https://github.com/G-Core/gcore-python/commit/3534beaed71a9fb5fe61df6a8b9aa76b9c3913c8))
* **cloud:** update tags type for gpu baremetal clusters and images, instances, load balancers ([6634a74](https://github.com/G-Core/gcore-python/commit/6634a74d3106f25476bd6bce98d12249f07dd8a6))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([3d88ae5](https://github.com/G-Core/gcore-python/commit/3d88ae5a7df41b7e9e88d0520a9586c1240da54c))
* **waap:** remove duplicate method for acct overview ([85766ca](https://github.com/G-Core/gcore-python/commit/85766ca7a1a3848cf6e252a55d7cc7ef384a4f94))


### Chores

* **ci:** change upload type ([960a44b](https://github.com/G-Core/gcore-python/commit/960a44ba2f255ad2bf8f571de381b06e5f1fffbd))
* **ci:** only run for pushes and fork pull requests ([7df32ec](https://github.com/G-Core/gcore-python/commit/7df32eca9f58a777487a2d00e2bfd41ccdd6a518))
* **cloud:** reorder ([0441c52](https://github.com/G-Core/gcore-python/commit/0441c52c6407e2ae427b70fdd22881bde8ea8191))
* **cloud:** reorder example functions ([7c3a568](https://github.com/G-Core/gcore-python/commit/7c3a5683c8482ca7398e6863c77fdae350b3e711))
* **cloud:** skip load balancer test statuses ([8dd7ccb](https://github.com/G-Core/gcore-python/commit/8dd7ccb677a41455d0c3ee6407e21271485669aa))
* **cloud:** streamline envs in examples ([e26746f](https://github.com/G-Core/gcore-python/commit/e26746fd50a2fee2157c88244b737352f07dd55c))
* **cloud:** unify examples format ([32446c4](https://github.com/G-Core/gcore-python/commit/32446c4e9bb385f68b0a24637f731ff93ee0eb5a))
* format ([fbe3508](https://github.com/G-Core/gcore-python/commit/fbe3508482950455f4ccd02b6941bb0273b2fdf6))
* **internal:** updates ([2377589](https://github.com/G-Core/gcore-python/commit/237758929ed119a1780c5a0cf9d60c72f6c70b8a))
* **internal:** updates ([054c374](https://github.com/G-Core/gcore-python/commit/054c374d0b02ec85d6702ecfded1362e827cf655))
* **readme:** update badges ([6ba343d](https://github.com/G-Core/gcore-python/commit/6ba343d802d353c4df42e4e7f6cc4f693fe9734a))
* **tests:** skip some failing tests on the latest python versions ([4b45142](https://github.com/G-Core/gcore-python/commit/4b45142d7fe138a5f0a030bdd27f9de26df533b9))
* **tests:** skip some failing tests on the latest python versions ([272ce51](https://github.com/G-Core/gcore-python/commit/272ce51ed26d568e181dee26205448d35184e015))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([1f4c28f](https://github.com/G-Core/gcore-python/commit/1f4c28f252df42a703a60ed2901391167296ecc7))


### Refactors

* **cloud:** remove list suitable from bm flavors ([2626938](https://github.com/G-Core/gcore-python/commit/262693876592601fa5a07dd088033037c7eae9b6))
* remove list suitable and list for resize from instance flavors ([24b00fe](https://github.com/G-Core/gcore-python/commit/24b00fec390f141457c98334b302dab5a8b1d480))

## 0.3.0 (2025-06-17)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/G-Core/gcore-python/compare/v0.2.0...v0.3.0)

### Features

* **api:** aggregated API specs update ([cc09f05](https://github.com/G-Core/gcore-python/commit/cc09f0514d7fdaf4be53bc0a9c6c83bc51d15c8e))
* **api:** aggregated API specs update ([bb1cd39](https://github.com/G-Core/gcore-python/commit/bb1cd39ca5b0fe5fdcaa27cc7c4010652ec63bd7))
* **api:** manual upload of aggregated API specs ([5cc5748](https://github.com/G-Core/gcore-python/commit/5cc5748cd293cf9fc82b869300942ebc185acba4))
* **api:** manual upload of aggregated API specs ([bcb9528](https://github.com/G-Core/gcore-python/commit/bcb9528ac00d87793c1482fbae29ccad530d98d1))
* **client:** add follow_redirects request option ([5e174cd](https://github.com/G-Core/gcore-python/commit/5e174cd6d8b9ff289e41470876e6fa606b577d9d))
* **cloud:** add file shares examples ([861ee72](https://github.com/G-Core/gcore-python/commit/861ee72d59ab0a6b5ce30fb3d3d1c1e8827c3dc8))
* **cloud:** add quotas examples ([353fe46](https://github.com/G-Core/gcore-python/commit/353fe4673252ae21c30d35217b2a8431ff23f1dc))
* **waap:** add domain analytics, api_paths, insights and insight_silences; and ip_info ([5bf944d](https://github.com/G-Core/gcore-python/commit/5bf944dcb78eb969dc6d0cca2fcec60cf8ad29d4))
* **waap:** add domain custom, firewall and advanced rules; custom page sets, advanced rules and tags ([c87c991](https://github.com/G-Core/gcore-python/commit/c87c99120593ce8fbc4ad6c17cdafee26980261b))


### Bug Fixes

* **client:** correctly parse binary response | stream ([4266555](https://github.com/G-Core/gcore-python/commit/42665557859017c7978aa9bae5e0e9f4f86369f9))


### Chores

* **change-detection:** filter newly generated files ([6afae28](https://github.com/G-Core/gcore-python/commit/6afae286af9d73e8c709761bcdb204aecf0b1fd8))
* **ci:** enable for pull requests ([dc1b8d6](https://github.com/G-Core/gcore-python/commit/dc1b8d60856032734dbd4fc398de8dacdc0d1005))
* **cloud:** fix lint ([47beba7](https://github.com/G-Core/gcore-python/commit/47beba75971064ab94d8741f4d1c676850700021))
* **docs:** remove reference to rye shell ([46c6ddf](https://github.com/G-Core/gcore-python/commit/46c6ddf669a7e9ee58e6629455c3d83029bee626))
* **internal:** update conftest.py ([dc9134b](https://github.com/G-Core/gcore-python/commit/dc9134b3ea02980aea2cdcde0775c0ad19101ef5))
* **tests:** add tests for httpx client instantiation & proxies ([d5913dd](https://github.com/G-Core/gcore-python/commit/d5913dde70db8a76542e48af5bcc62a14c2c52a4))
* **tests:** run tests in parallel ([b73e6f9](https://github.com/G-Core/gcore-python/commit/b73e6f906e21e58993645e7060dead8edaf2b6cd))

## 0.2.0 (2025-05-30)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/G-Core/gcore-python/compare/v0.1.0...v0.2.0)

### Features

* **api:** aggregated API specs update ([8396748](https://github.com/G-Core/gcore-python/commit/83967485975f181b79166c5ab6ae6533a77ff414))
* **api:** aggregated API specs update ([f3e527b](https://github.com/G-Core/gcore-python/commit/f3e527bba66b98a5e3d58b604bff1a7d772fd504))
* **api:** aggregated API specs update ([8f63298](https://github.com/G-Core/gcore-python/commit/8f63298756d8de3df98788b640c33dbf9cbd4c0c))
* **api:** aggregated API specs update ([ec4a6bd](https://github.com/G-Core/gcore-python/commit/ec4a6bdd8cce948d0b3bb279b42a020d20b3fceb))
* **api:** aggregated API specs update ([e270005](https://github.com/G-Core/gcore-python/commit/e27000533d742531397c34435a60a9f816c5d559))


### Bug Fixes

* **ci:** do not always skip breaking change detection ([018e357](https://github.com/G-Core/gcore-python/commit/018e357a11cfd863973fbd29f1f1867d3851b342))
* **inference:** make poll method consistent with latest api changes ([0ea64f9](https://github.com/G-Core/gcore-python/commit/0ea64f92b47e914d980ba0fd2208dd44e1119903))
* **instances,baremetal,loadbalancers,inference,gpu_cloud:** don't fail if nr tasks gt 1 ([760226e](https://github.com/G-Core/gcore-python/commit/760226eddee2cf1c66ab5dfcca86ea7130de382b))


### Chores

* **api:** mark some methods as deprecated ([726ef80](https://github.com/G-Core/gcore-python/commit/726ef8008d1bc67aea4884dcc48718fd94d738c3))
* **docs:** grammar improvements ([cd7a162](https://github.com/G-Core/gcore-python/commit/cd7a16205cad089539ab3d7f6871d564691e3f40))
* **internal:** codegen related update ([fb451ad](https://github.com/G-Core/gcore-python/commit/fb451ada041dce34bd134274969b29c474c6d094))
* **internal:** version bump ([69cc570](https://github.com/G-Core/gcore-python/commit/69cc570d3cd366763c4506990ae886abe3a3d734))


### Refactors

* **loadbalancers:** change oas schema names ([422d5c2](https://github.com/G-Core/gcore-python/commit/422d5c2c03155b9d136f15ddd087e175a4af00aa))
* **loadbalancers:** use correct schema for loadbalancer pool ([6a285dd](https://github.com/G-Core/gcore-python/commit/6a285dd1683f30f8aee24ddd20ec5b1684ace304))

## 0.1.0 (2025-05-20)

Full Changelog: [v0.1.0-alpha.2...v0.1.0](https://github.com/G-Core/gcore-python/compare/v0.1.0-alpha.2...v0.1.0)

### Features

* **api:** aggregated API specs update ([8173c1e](https://github.com/G-Core/gcore-python/commit/8173c1ea495b7b27876fa8b777070e3a28407f0d))
* **api:** aggregated API specs update ([22e6e90](https://github.com/G-Core/gcore-python/commit/22e6e90558ebaa7e4d5b50000ef0a8706037ab3f))
* **baremetal:** add polling methods ([#38](https://github.com/G-Core/gcore-python/issues/38)) ([0423186](https://github.com/G-Core/gcore-python/commit/0423186035ceb14e772adf585ec3664755c4902f))
* **gpu_cloud:** add polling methods ([#40](https://github.com/G-Core/gcore-python/issues/40)) ([b209a4d](https://github.com/G-Core/gcore-python/commit/b209a4d6bf565559503462a4d28a8d6ed45c18b8))
* **instances:** add polling methods ([#36](https://github.com/G-Core/gcore-python/issues/36)) ([64ec95d](https://github.com/G-Core/gcore-python/commit/64ec95d62a0ee4ca69ad7df78ef875eb3dd81ecf))
* **load_balancers, inference, gpu_cloud, instances:** add polling methods ([#44](https://github.com/G-Core/gcore-python/issues/44)) ([ba106ad](https://github.com/G-Core/gcore-python/commit/ba106adf1b54b9109574da93e9617e777f6890cc))
* **loadbalancers,inference:** add polling methods ([#39](https://github.com/G-Core/gcore-python/issues/39)) ([55bbc2f](https://github.com/G-Core/gcore-python/commit/55bbc2f56049f10b6360e53fcaed25ec343ce6fa))


### Bug Fixes

* **package:** support direct resource imports ([74d6f0d](https://github.com/G-Core/gcore-python/commit/74d6f0d5763de81c2017943d3a39633f32ee20c4))


### Chores

* **ci:** fix installation instructions ([8dc3dcf](https://github.com/G-Core/gcore-python/commit/8dc3dcf9beda9745d64f906a2d386d930e04bbe2))
* **ci:** upload sdks to package manager ([370efcf](https://github.com/G-Core/gcore-python/commit/370efcfd392562b1fbc28ef9b87dc9c65ba8363c))
* **internal:** avoid errors for isinstance checks on proxies ([6ccc750](https://github.com/G-Core/gcore-python/commit/6ccc7507b9882b0c9eb5b0ac2d5ec57035d6f959))
* **internal:** codegen related update ([67c1836](https://github.com/G-Core/gcore-python/commit/67c183613a3c3ac4ecc6a7c2a17ca09b80838a8e))


### Documentation

* remove or fix invalid readme examples ([457d409](https://github.com/G-Core/gcore-python/commit/457d4091f05eee8bd4862c262cce7bef5c071e7e))

## 0.1.0-alpha.2 (2025-05-06)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/G-Core/gcore-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Documentation

* enable pypi publishing ([6fd398f](https://github.com/G-Core/gcore-python/commit/6fd398f307673c521d41acef7ee6833977d8b108))

## 0.1.0-alpha.1 (2025-05-06)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/G-Core/gcore-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** add nested_params readme example ([6ee8d52](https://github.com/G-Core/gcore-python/commit/6ee8d52fb55f54a07380696b27e5db42298dd39f))
* **api:** aggregated API specs update ([2813f87](https://github.com/G-Core/gcore-python/commit/2813f879dd9276506139471c7c12d8160f159924))
* **api:** aggregated API specs update ([2469a5f](https://github.com/G-Core/gcore-python/commit/2469a5f97c5e07cd9b74a3af2688a9fbb963b86a))
* **api:** aggregated API specs update ([84eac69](https://github.com/G-Core/gcore-python/commit/84eac69a9ba19fece92100b53864252d183d20df))
* **api:** aggregated API specs update ([d3569ad](https://github.com/G-Core/gcore-python/commit/d3569add7e2dff9f3580bc4557ae65095bedf39b))
* **api:** aggregated API specs update ([f3cf87c](https://github.com/G-Core/gcore-python/commit/f3cf87cb01ae9ff0f92ea85ceab2133a69017827))
* **api:** aggregated API specs update ([1e9b9c8](https://github.com/G-Core/gcore-python/commit/1e9b9c8a2504eceefdaf666be1bec98874e322e7))
* **api:** aggregated API specs update ([0006431](https://github.com/G-Core/gcore-python/commit/00064311320c0fe23330cebe0879099d7819b4eb))
* **api:** aggregated API specs update ([a342c37](https://github.com/G-Core/gcore-python/commit/a342c37d2882dc47109c6b8aead1e72b3a1a6188))
* **api:** aggregated API specs update ([f09d378](https://github.com/G-Core/gcore-python/commit/f09d378224a50075ae24e2a70212a20a3631ee11))
* **api:** aggregated API specs update ([0357ef7](https://github.com/G-Core/gcore-python/commit/0357ef75d82cdf567492fe02ca688aecdb9836d2))
* **api:** aggregated API specs update ([5e1e67a](https://github.com/G-Core/gcore-python/commit/5e1e67a95ac08931d14a1a29a85262eb6df1c4ee))
* **api:** aggregated API specs update ([7fc187b](https://github.com/G-Core/gcore-python/commit/7fc187ba11c0ef604da22f70ade6aacd4c5ce090))
* **api:** aggregated API specs update ([1963fee](https://github.com/G-Core/gcore-python/commit/1963fee15dd6877e69584758595dbd160ae696f8))
* **api:** aggregated API specs update ([4f397d1](https://github.com/G-Core/gcore-python/commit/4f397d124fc6da07bd03e7c8b539e6db284d39b4))
* **api:** Config update for algis-dumbris/cloud-quotas ([38d5cd6](https://github.com/G-Core/gcore-python/commit/38d5cd68ec8dee8d00a7327e5231520aa00403d8))
* **api:** manual updates ([4815004](https://github.com/G-Core/gcore-python/commit/481500416f100dee03be8e7d884ca232eb6fa5fc))
* **api:** manual updates ([9828118](https://github.com/G-Core/gcore-python/commit/9828118404382abefbaeba2553d0e799781d425d))
* **api:** manual updates ([4d67833](https://github.com/G-Core/gcore-python/commit/4d67833a7f4b88bec825841bf89c88a461a8f1e8))
* **api:** manual upload of aggregated API specs ([19202b1](https://github.com/G-Core/gcore-python/commit/19202b1ceccbc317d3b6d15c4403370141340037))
* **api:** remove duplicates ([3ed9f67](https://github.com/G-Core/gcore-python/commit/3ed9f6797b48ccc326cb536ddb2487848e22bcbd))
* **api:** remove quotas ([ff784b5](https://github.com/G-Core/gcore-python/commit/ff784b5ef5dad16dceee3ab70dd8a59c2e379ccd))
* **api:** rename regions.retrieve() to rregions.get() ([5823e81](https://github.com/G-Core/gcore-python/commit/5823e8121bd2ce949f16e1ec1c24fb71e6766d1f))
* **api:** simplify env vars ([161e7c4](https://github.com/G-Core/gcore-python/commit/161e7c48c4d7923f6c263558c239a0d6d99be980))
* **api:** trigger codegen ([c66f1ab](https://github.com/G-Core/gcore-python/commit/c66f1ab7645b8deee2d2fc10fbcfc76254855549))
* changes for loadbalancers-renaming ([4785701](https://github.com/G-Core/gcore-python/commit/47857019e5ca8b21efd41157175c7ee349ecf3ea))
* **oas:** update to v14.150.0 ([c0fdf81](https://github.com/G-Core/gcore-python/commit/c0fdf81d61fe9054d0dd0524560c6019e27a70f7))
* **opts:** polling interval in secs ([9abb721](https://github.com/G-Core/gcore-python/commit/9abb72182049081ba16fbd5f2b4fd371ccb61ec4))
* **projects:** add cloud projects ([#1](https://github.com/G-Core/gcore-python/issues/1)) ([abc2b1c](https://github.com/G-Core/gcore-python/commit/abc2b1c600ae63694604a8ed9ca3564577618e39))
* **tasks:** make polling interval in secs ([#34](https://github.com/G-Core/gcore-python/issues/34)) ([b29fe33](https://github.com/G-Core/gcore-python/commit/b29fe3359588dfb7f3226cb6c37709aa9aa5db3a))


### Bug Fixes

* **api:** update regions.retrieve() to regions.get() in async and sync examples ([#33](https://github.com/G-Core/gcore-python/issues/33)) ([8f14234](https://github.com/G-Core/gcore-python/commit/8f142340a731a19666917e5d7e30cf0e2e0c76b9))
* **client:** correct path param return type ([3436e9d](https://github.com/G-Core/gcore-python/commit/3436e9d5fc453ee21b68a32781e51846fece99a0))
* **cloud:** move and/or rename models ([1022e65](https://github.com/G-Core/gcore-python/commit/1022e65d85e9398d993edfc86f1a5af0a483ea07))
* **cloud:** remove workaround ([70c3bd0](https://github.com/G-Core/gcore-python/commit/70c3bd0c6b77083df0a3e0f1fa897caf585f80a3))
* **examples:** client opts rename ([#30](https://github.com/G-Core/gcore-python/issues/30)) ([7d62a64](https://github.com/G-Core/gcore-python/commit/7d62a6403b357c3298bf8b37c2167e05b38671f0))
* **examples:** update examples after model rename ([#21](https://github.com/G-Core/gcore-python/issues/21)) ([2000922](https://github.com/G-Core/gcore-python/commit/2000922b4e6c99e6bdbffcaf8e102256bfcc1413))
* **floating_ips:** workaround ([4517d6e](https://github.com/G-Core/gcore-python/commit/4517d6e7c0564dc20d40ae1c5ba37514d360645f))
* **ipranges:** add examples ([#14](https://github.com/G-Core/gcore-python/issues/14)) ([a77b150](https://github.com/G-Core/gcore-python/commit/a77b15074507bdf8d39cfbe21b71c2b1533be49e))
* **perf:** optimize some hot paths ([dfdb2cb](https://github.com/G-Core/gcore-python/commit/dfdb2cbdaa75f45a760680d65a5540c1aae2ccc5))
* **perf:** skip traversing types for NotGiven values ([c8beef9](https://github.com/G-Core/gcore-python/commit/c8beef965db0c8eac4f68d32fe5dccf356227140))
* **pydantic v1:** more robust ModelField.annotation check ([d2feb9f](https://github.com/G-Core/gcore-python/commit/d2feb9f7dff5092550811bbe8fc8252b85da68cd))
* **ssh_keys:** add examples ([#13](https://github.com/G-Core/gcore-python/issues/13)) ([7c19fc6](https://github.com/G-Core/gcore-python/commit/7c19fc6b1e7cf3eec829e622f01e473d10041848))
* **tests:** unset region env var during tests ([#10](https://github.com/G-Core/gcore-python/issues/10)) ([194ef5c](https://github.com/G-Core/gcore-python/commit/194ef5cd7af25a2278460e747502b2d637d896df))


### Chores

* broadly detect json family of content-type headers ([f78af6d](https://github.com/G-Core/gcore-python/commit/f78af6db49a301121dd1bb28cdb88119cc169081))
* **ci:** add timeout thresholds for CI jobs ([aabedbd](https://github.com/G-Core/gcore-python/commit/aabedbd9886425f15eca1c5a83e23e234abb97ed))
* **ci:** fix formatting for debug mode ([376ed6b](https://github.com/G-Core/gcore-python/commit/376ed6bb4302a92efc5290b93bfc2a223c1299ac))
* **ci:** only use depot for staging repos ([12782f0](https://github.com/G-Core/gcore-python/commit/12782f034862557585dcaed07ecd073da6b91996))
* **client:** minor internal fixes ([c605c1c](https://github.com/G-Core/gcore-python/commit/c605c1c816d74d4a01ec8dc0689ea7f226892e0e))
* configure new SDK language ([5559374](https://github.com/G-Core/gcore-python/commit/5559374feffdb8eca7f20f0bcc4af83ad1bf49eb))
* **internal:** base client updates ([c3782cc](https://github.com/G-Core/gcore-python/commit/c3782cc4660beaaa8eed7560118e2bbe60ab6506))
* **internal:** bump pyright version ([a59f39b](https://github.com/G-Core/gcore-python/commit/a59f39b5393e9a0af05e9c520b3a40e06b3708c6))
* **internal:** codegen related update ([1e5e4a4](https://github.com/G-Core/gcore-python/commit/1e5e4a43c02d64079c771c05171e159a5a70a9e7))
* **internal:** expand CI branch coverage ([832a5a0](https://github.com/G-Core/gcore-python/commit/832a5a0ebf1bd13aae23ce31212d374199779661))
* **internal:** fix list file params ([f9dbece](https://github.com/G-Core/gcore-python/commit/f9dbecefee3db3d903f1eb43a8f96dac4571f013))
* **internal:** import reformatting ([a160ca4](https://github.com/G-Core/gcore-python/commit/a160ca4084342039946258c36f163ede88afe4ec))
* **internal:** minor formatting changes ([c7958d2](https://github.com/G-Core/gcore-python/commit/c7958d278347c0294fdd08d5315597d9885d9d89))
* **internal:** reduce CI branch coverage ([e4e582c](https://github.com/G-Core/gcore-python/commit/e4e582c604e3bea37bf53f530c162b978e427a29))
* **internal:** refactor retries to not use recursion ([b1b2600](https://github.com/G-Core/gcore-python/commit/b1b26009317ab59938990bb3604677007f58f0fe))
* **internal:** slight transform perf improvement ([c826d0d](https://github.com/G-Core/gcore-python/commit/c826d0d042c55b034a488eb76fb23ae42a927349))
* **internal:** update models test ([e3550d8](https://github.com/G-Core/gcore-python/commit/e3550d80dc73520576ce16cc0c7259b7a4d7ffac))
* **internal:** update pyright settings ([3c14296](https://github.com/G-Core/gcore-python/commit/3c142960c5b7b0bb81919e8337c8bb6428676e1d))
* **tests:** improve enum examples ([a10cbfa](https://github.com/G-Core/gcore-python/commit/a10cbfa870a42cae4f75beae90f185ce068c14fa))
* update SDK settings ([81d0161](https://github.com/G-Core/gcore-python/commit/81d0161b6651e00fe9be43faef815c31a17361b1))
* update SDK settings ([0f4877e](https://github.com/G-Core/gcore-python/commit/0f4877e87435d053c2038dd11590caad6ad90700))


### Documentation

* update links ([edb2a76](https://github.com/G-Core/gcore-python/commit/edb2a766f451b9dfa798e620d01bb7ba5299e33d))


### Refactors

* **tasks:** rename retrieve methods to get to fix polling ([#16](https://github.com/G-Core/gcore-python/issues/16)) ([61fc9a9](https://github.com/G-Core/gcore-python/commit/61fc9a9e0ab9f998c9fd303ff6cea3ff6e03a345))
