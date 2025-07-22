# Changelog

## [1.6.0](https://www.github.com/snakemake/mastodon-release-post-action/compare/v1.5.0...v1.6.0) (2025-07-22)


### Features

* accounting for multiple link cases ([c2803bb](https://www.github.com/snakemake/mastodon-release-post-action/commit/c2803bbbbbca29d2d058312faf08a4dbc6d7a07c))
* added pyproject toml file ([18e5f53](https://www.github.com/snakemake/mastodon-release-post-action/commit/18e5f534423b4c1642856dd4840c41f1bd939ade))
* added test suite test.py file ([837521f](https://www.github.com/snakemake/mastodon-release-post-action/commit/837521f2dca47799cbbb0e8ed39cb65281094b7b))
* added test suite test.py file ([c468f96](https://www.github.com/snakemake/mastodon-release-post-action/commit/c468f962c9214109bce17255a9f27958057ca587))


### Bug Fixes

* attempt to fix CI pipeline ([cf3ee5b](https://www.github.com/snakemake/mastodon-release-post-action/commit/cf3ee5b5a817ee5749e693d4c9bbf22c45644dcd))
* formatting ([c736b46](https://www.github.com/snakemake/mastodon-release-post-action/commit/c736b4664deecbb30959726aa750482b5b709907))
* gnarf ([8a5978b](https://www.github.com/snakemake/mastodon-release-post-action/commit/8a5978bcec38d81cec7bf41f5597dbb29366a9f3))
* hopefully filtering out links, now ([6a0ee66](https://www.github.com/snakemake/mastodon-release-post-action/commit/6a0ee66c187536523befe38e4b7512c75f74071d))
* python version and missing poetry ([24884bb](https://www.github.com/snakemake/mastodon-release-post-action/commit/24884bb7bf8a66a63ffae8632866cbf5950afc21))
* removed code and moved it to ci.yml ([223b3cf](https://www.github.com/snakemake/mastodon-release-post-action/commit/223b3cf815f6fce075da193b164205ae8c3e4f58))
* syntax ([332c3f9](https://www.github.com/snakemake/mastodon-release-post-action/commit/332c3f9400755f5da1c7dea4f59a1142b2e9d25e))
* trigger ([dfb2bed](https://www.github.com/snakemake/mastodon-release-post-action/commit/dfb2bed7be542550c03b28ee2b597303fee8365f))

## [1.5.0](https://www.github.com/snakemake/mastodon-release-post-action/compare/v1.4.1...v1.5.0) (2025-06-13)


### Features

* improved formatting of changelog texts ([25c6161](https://www.github.com/snakemake/mastodon-release-post-action/commit/25c616168690c1cb5c0212c90a5742808b75451c))

### [1.4.1](https://www.github.com/snakemake/mastodon-release-post-action/compare/v1.4.0...v1.4.1) (2025-05-25)


### Bug Fixes

* typo in variable ([9e81a21](https://www.github.com/snakemake/mastodon-release-post-action/commit/9e81a21a387a63487c7d0e6e4a559a7ef27bc656))

## [1.4.0](https://www.github.com/snakemake/mastodon-release-post-action/compare/v1.3.0...v1.4.0) (2025-05-18)


### Features

* extracting release nodes from changelog file ([34e9ac9](https://www.github.com/snakemake/mastodon-release-post-action/commit/34e9ac925676a19c4cc7293a8e63d2244b5048dc))
* own detectin of CHANGELOG and producing release notes ([370551d](https://www.github.com/snakemake/mastodon-release-post-action/commit/370551d04c03120fdb01b1f5449e42275480f7eb))


### Bug Fixes

* blacked ([eecd8fd](https://www.github.com/snakemake/mastodon-release-post-action/commit/eecd8fdb4d6ea2689cdf74defec07e98c31c64e4))
* removed ill-placed exit ([e61ba93](https://www.github.com/snakemake/mastodon-release-post-action/commit/e61ba93a303482c0a229df64cc938adc7e5eb3e4))
* warning for unfound changelog placed correctly ([7b434f6](https://www.github.com/snakemake/mastodon-release-post-action/commit/7b434f6f5ead577d837ead2913cba490725307a2))

## [1.3.0](https://www.github.com/snakemake/mastodon-release-post-action/compare/v1.2.3...v1.3.0) (2025-05-16)


### Features

* implemented tolerant argument parsing ([0bb63cf](https://www.github.com/snakemake/mastodon-release-post-action/commit/0bb63cf0358c30a84256d1234a7336ef42c31499))

### [1.2.3](https://www.github.com/snakemake/mastodon-release-post-action/compare/v1.2.2...v1.2.3) (2025-05-16)


### Bug Fixes

* duplicated command directive ([8df339e](https://www.github.com/snakemake/mastodon-release-post-action/commit/8df339ea7d3718d6caeba59f89d771baffda213a))

### [1.2.2](https://www.github.com/snakemake/mastodon-release-post-action/compare/v1.2.1...v1.2.2) (2025-05-16)


### Bug Fixes

* added empty last line ([8fbff55](https://www.github.com/snakemake/mastodon-release-post-action/commit/8fbff552642559eac25bffffa6d5949775cf046b))
* protecting base url flag with if statement ([79b95ac](https://www.github.com/snakemake/mastodon-release-post-action/commit/79b95acaa4992612f3d745134c6aa0445e2b34ba))

### [1.2.1](https://www.github.com/snakemake/mastodon-release-post-action/compare/v1.2.0...v1.2.1) (2025-05-16)


### Bug Fixes

* bugfix for dangling backslash, if no base-url is given ([b5b602b](https://www.github.com/snakemake/mastodon-release-post-action/commit/b5b602b5cdd882a3de89690bf0342c1585497d55))

## [1.2.0](https://www.github.com/snakemake/mastodon-release-post-action/compare/v1.1.1...v1.2.0) (2025-05-15)


### Features

* added option to include a base-url, differing from fediscience ([89ece3c](https://www.github.com/snakemake/mastodon-release-post-action/commit/89ece3c37c37fd73d43de2f699166533fe74df2b))
* the base url is only set, if given ([a341c43](https://www.github.com/snakemake/mastodon-release-post-action/commit/a341c4359b9564476ea71982ae395500fe5b1cf1))


### Bug Fixes

* hopefully better inner workings ([302c37f](https://www.github.com/snakemake/mastodon-release-post-action/commit/302c37f10ac428f7c053d447c3406703df046753))
* working now ([8973533](https://www.github.com/snakemake/mastodon-release-post-action/commit/8973533836e8114b9aeece59eadbc60f7b47795f))

### [1.1.1](https://www.github.com/snakemake/mastodon-release-post-action/compare/v1.1.0...v1.1.1) (2025-05-13)


### Bug Fixes

* added pr-title to allowed inputs ([da3b5c3](https://www.github.com/snakemake/mastodon-release-post-action/commit/da3b5c390cb035a4fe5affb6bfed33c8df257dd2))

## [1.1.0](https://www.github.com/snakemake/mastodon-release-post-action/compare/v1.0.8...v1.1.0) (2025-05-13)


### Features

* added argument parsing for pr title ([1678071](https://www.github.com/snakemake/mastodon-release-post-action/commit/1678071a6a01c3d93f90523c46dd10f8f84d73fd))


### Bug Fixes

* added pr title as input ([8c53fe5](https://www.github.com/snakemake/mastodon-release-post-action/commit/8c53fe55379a8cb6ee6a40a5af745b1d303c1f79))

### [1.0.8](https://www.github.com/snakemake/mastodon-release-post-action/compare/v1.0.7...v1.0.8) (2025-05-13)


### Bug Fixes

* another attempt ([63f2dcd](https://www.github.com/snakemake/mastodon-release-post-action/commit/63f2dcdd93c5850782e914a0cfa0205265a404b9))

### [1.0.7](https://www.github.com/snakemake/mastodon-release-post-action/compare/v1.0.6...v1.0.7) (2025-05-13)


### Bug Fixes

* not using path variable any longer ([06e08b4](https://www.github.com/snakemake/mastodon-release-post-action/commit/06e08b4377a0e11965f29a81493b73d00a9e9bd7))

### [1.0.6](https://www.github.com/snakemake/mastodon-release-post-action/compare/v1.0.5...v1.0.6) (2025-05-13)


### Bug Fixes

* deleted 'shell' directive, apparently not allowed here ([c9327ed](https://www.github.com/snakemake/mastodon-release-post-action/commit/c9327ed254eef2f9d6b57bdd741fe61223260065))

### [1.0.5](https://www.github.com/snakemake/mastodon-release-post-action/compare/v1.0.4...v1.0.5) (2025-05-12)


### Bug Fixes

* attempting to hand over message and access token as inputs ([c53fc32](https://www.github.com/snakemake/mastodon-release-post-action/commit/c53fc32d176782e72350c0a61ac4c9f492f4ef5a))

### [1.0.4](https://www.github.com/snakemake/mastodon-release-post-action/compare/v1.0.3...v1.0.4) (2025-05-12)


### Bug Fixes

* removing secrets - only to be tried in the workflow, not the action ([e8ea4f8](https://www.github.com/snakemake/mastodon-release-post-action/commit/e8ea4f8c4c1cb2cc3a40f57206208bd483b2089d))

### [1.0.3](https://www.github.com/snakemake/mastodon-release-post-action/compare/v1.0.2...v1.0.3) (2025-05-11)


### Bug Fixes

* another attempt ([ada3d5f](https://www.github.com/snakemake/mastodon-release-post-action/commit/ada3d5fdc2a366da251e78268bd59b290de0cb69))

### [1.0.2](https://www.github.com/snakemake/mastodon-release-post-action/compare/v1.0.1...v1.0.2) (2025-05-11)


### Bug Fixes

* syntax ([3eec9c2](https://www.github.com/snakemake/mastodon-release-post-action/commit/3eec9c27d04d21843854359ee5e72dd5b9998d2d))

### [1.0.1](https://www.github.com/snakemake/mastodon-release-post-action/compare/v1.0.0...v1.0.1) (2025-04-10)


### Bug Fixes

* correct naming and hopefully corrected export ([aee189f](https://www.github.com/snakemake/mastodon-release-post-action/commit/aee189fced57b2761ee0b82773ef9bf7c017df66))

## 1.0.0 (2025-03-12)


### Features

* added hastag info ([75f6d27](https://www.github.com/snakemake/mastodon-release-post-action/commit/75f6d27b60bf3f4f4ccb9de9e94a023bfd02509a))
* added post_to_mastodon.yml ([6fbaa72](https://www.github.com/snakemake/mastodon-release-post-action/commit/6fbaa72d67fc75e1bb4778f041c591b0a604f65f))
* allowing for generic mastodon access token and non-default server ([2a566dc](https://www.github.com/snakemake/mastodon-release-post-action/commit/2a566dcefe09a65289da61be4ce6c19de9b42f90))
* better support to infer the repository url ([3bdbe28](https://www.github.com/snakemake/mastodon-release-post-action/commit/3bdbe2850222e26736b13de5c138dfaacad09e35))
* first action version ([831f752](https://www.github.com/snakemake/mastodon-release-post-action/commit/831f752cb635ee5960fa191b147a8ec747698ec2))
* first workflow scripts ([75fac16](https://www.github.com/snakemake/mastodon-release-post-action/commit/75fac160d6c20a7b59fb7a7187bc1b55b96b6634))
* get issue url ([d6be529](https://www.github.com/snakemake/mastodon-release-post-action/commit/d6be5299c1845639d0f1db462c96a49b3293d3c2))
* improved hints for multiline messages ([cb65206](https://www.github.com/snakemake/mastodon-release-post-action/commit/cb652066a3d7b51b0362ae19ba5e1f4d9a190036))
* improved readme template ([1030f10](https://www.github.com/snakemake/mastodon-release-post-action/commit/1030f1030c1a6a68fbd5844de922b3a72dfec00b))
* included the variable handline ([0036a43](https://www.github.com/snakemake/mastodon-release-post-action/commit/0036a43fd4c981c55eedbea01164e5c767f9d282))
* robust way to retrieve changelog file ([d27169c](https://www.github.com/snakemake/mastodon-release-post-action/commit/d27169c2f3774464788dd299e7c98a9f2e34049d))


### Bug Fixes

* removed permission and branch statements ([e034ff8](https://www.github.com/snakemake/mastodon-release-post-action/commit/e034ff88253ef5718c41538efa042d4b39899bba))
* removed post_to_mastodon.sh - outdated ([0e03983](https://www.github.com/snakemake/mastodon-release-post-action/commit/0e0398327d8ee57da812b3dd01d96e8413e4cd97))
* renamed post script to action.yml ([da73b4e](https://www.github.com/snakemake/mastodon-release-post-action/commit/da73b4e65e203a0996c2b00e51c6851e3568a205))
* set default post lengtht for our robot to 1500 ([78046f4](https://www.github.com/snakemake/mastodon-release-post-action/commit/78046f4807082feb529459f73182ee1e7db8754b))
* syntax ([bcba25a](https://www.github.com/snakemake/mastodon-release-post-action/commit/bcba25af2a8137c22946345f3ba9c7a200eec4db))
* synthesis of coderabbit and me ([e39b5ad](https://www.github.com/snakemake/mastodon-release-post-action/commit/e39b5ad8953c93195dc0cbd1427798bf0de47c7d))
