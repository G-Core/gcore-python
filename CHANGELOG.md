# Changelog

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
