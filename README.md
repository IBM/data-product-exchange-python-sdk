# ⚠️ DEPRECATED - Data Product Hub Python SDK Version 1.7.1

> **DEPRECATION NOTICE**: This repository has been deprecated and is no longer maintained.
>
> **Please use the new repository**: [IBM Data Intelligence SDK](https://github.com/IBM/data-intelligence-sdk)
>
> All future development, bug fixes, and updates will be made in the new repository. Please migrate your applications to use the new SDK as soon as possible.

---

Python client library to interact with various Data Product Hub Service APIs.

Disclaimer: this SDK is being released initially as a **pre-release** version.
Changes might occur which impact applications that use this SDK.

## Table of Contents

<!--
  The TOC below is generated using the `markdown-toc` node package.

      https://github.com/jonschlinkert/markdown-toc

  You should regenerate the TOC after making changes to this file.

      npx markdown-toc -i README.md
  -->

<!-- toc -->

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Using the SDK](#using-the-sdk)
- [Questions](#questions)
- [Issues](#issues)
- [Open source @ IBM](#open-source--ibm)
- [Contributing](#contributing)
- [License](#license)

<!-- tocstop -->

## Overview

The IBM Cloud dph_services Python SDK allows developers to programmatically interact with the following service:

Service Name | Module Name | Imported Class Name
--- | --- | ---
[Data Product Hub](https://cloud.ibm.com/apidocs/dataproducts) | data_product_hub_api_service_v1 | DataProductHubApiServiceV1

## Prerequisites

[ibm-cloud-onboarding]: https://cloud.ibm.com/registration

* An [IBM Cloud][ibm-cloud-onboarding] account.
* An IAM API key to allow the SDK to access your account. Create one [here](https://cloud.ibm.com/iam/apikeys).
* Python 3.9 or above.

## Installation

To install, use `pip`:

```bash
pip install --upgrade dph-services
```

Then in your code, you can import the appropriate service like this:
```
from dph_services.<service-module-name> import *
```
where `<service-module-name>` is the service's module name from the table above

## Using the SDK
For general SDK usage information, please see [this link](https://github.com/IBM/ibm-cloud-sdk-common/blob/main/README.md)

## Questions

If you are having difficulties using this SDK or have a question about the IBM Cloud services,
please ask a question at
[Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-cloud).

## Issues
**This repository is deprecated.** Please report any issues in the new repository:
[IBM Data Intelligence SDK Issues](https://github.com/IBM/data-intelligence-sdk/issues)

## Open source @ IBM
Find more open source projects on the [IBM Github Page](http://ibm.github.io/)

## Contributing
**This repository is deprecated and no longer accepts contributions.** Please contribute to the new repository:
[IBM Data Intelligence SDK](https://github.com/IBM/data-intelligence-sdk)

## Migration Guide

To migrate to the new SDK:

1. Uninstall the old package:
   ```bash
   pip uninstall dph-services
   ```

2. Install the new package:
   ```bash
   pip install ibm-data-intelligence-sdk
   ```

3. Update your imports and code to use the new SDK. See the [migration documentation](https://github.com/IBM/data-intelligence-sdk) for details.

## License

This SDK is released under the Apache 2.0 license.
The license's full text can be found in [LICENSE](LICENSE).
