# coding: utf-8
# Copyright 2019, 2020 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
DEPRECATED: Python client library for the DPH Services

This package is deprecated and no longer maintained.
Please migrate to: ibm-data-intelligence-sdk
Repository: https://github.com/IBM/data-intelligence-sdk
"""

import warnings

# Issue deprecation warning when package is imported
warnings.warn(
    "\n" + "="*80 + "\n"
    "DeprecationWarning: The 'dph_services' package is DEPRECATED.\n"
    "\n"
    "This package is no longer maintained. Please migrate to:\n"
    "  pip install ibm-data-intelligence-sdk\n"
    "\n"
    "New repository: https://github.com/IBM/data-intelligence-sdk\n"
    + "="*80,
    DeprecationWarning,
    stacklevel=2
)

from ibm_cloud_sdk_core import IAMTokenManager, DetailedResponse, BaseService, ApiException

from .common import get_sdk_headers
from .version import __version__
from .dph_v1 import DphV1
