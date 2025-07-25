[![Supported Python versions](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Unit Tests](https://github.com/elastic/ecs/workflows/Tests/badge.svg)](https://github.com/elastic/ecs/actions)
[![Chat](https://img.shields.io/badge/chat-%23stack--ecs-blueviolet)](https://ela.st/slack)

# Elastic Common Schema (ECS)

The Elastic Common Schema (ECS) defines a common set of fields for
ingesting data into Elasticsearch. A common schema helps you correlate
data from sources like logs and metrics or IT operations
analytics and security analytics.

## ECS Donation to OpenTelemetry
In April 2023, OpenTelemetry and Elastic made an
[important joint announcement](https://opentelemetry.io/blog/2023/ecs-otel-semconv-convergence/).
In this announcement, we shared our intention to achieve convergence of ECS and OTel
Semantic Conventions into a single standard maintained by OpenTelemetry.

Special guidance is provided during the donation period. Please review the [contribution guide](CONTRIBUTING.md).

## Opensearch Modifications

This repositroy conatins some modifications as opposed to the original repo. 
This includes sections in the generator scripts which generate OpenSearch compatible
index templates. Due to some differences in the APIs and available field types
within OpenSearch, I adopted the build process to handle the differences and do 
some conversions. This makes it possible to get some future schema updates from the
repo easily.

Changes in field types:

| ECS => Elasticsearch | Opensearch |
|----------------------|------------|
| constant_keyword     | keyword    |
| wildcard             | keyword    |
| flattened            | object     |
| version              | keyword    |

These changes will lead to some differences in performance and search options. 

## Documentation

The ECS reference is published on the main Elastic documentation website.

Visit [the official ECS Reference Documentation](https://www.elastic.co/guide/en/ecs/current/index.html).

## Getting Started

Please review the [tooling usage guide](USAGE.md) to get started using the tools provided in this repo.

## Contributing

If you're looking to contribute to ECS, you're invited to look at our
[contribution guide](CONTRIBUTING.md). Substantial changes to ECS are completed
through our [RFC process](./rfcs/README.md).

## Generated artifacts

Various kinds of files or programs can be generated based on ECS.
You can learn more in [generated/README.md](generated)

## Releases of ECS

The main branch of this repository should never be considered an
official release of ECS. You can browse official releases of ECS
[here](https://github.com/elastic/ecs/releases).

The ECS team publishes improvements to the schema by following
[Semantic Versioning](https://semver.org/).
Generally major ECS releases are planned to be aligned with major Elastic Stack releases.

## License

This software is licensed under the Apache License, version 2 ("ALv2"), quoted below.

Copyright 2018-2021 Elasticsearch <https://www.elastic.co>

Licensed under the Apache License, Version 2.0 (the "License"); you may not
use this file except in compliance with the License. You may obtain a copy of
the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations under
the License.
