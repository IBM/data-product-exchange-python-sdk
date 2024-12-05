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
This module provides common constants for use across all service modules.
"""

# Dph Api Paths
URL_GET_INITIALIZE_STATUS = '/data_product_exchange/v1/configuration/initialize/status'
URL_GET_SERVICEID_CREDENTIALS = '/data_product_exchange/v1/configuration/credentials'
URL_INITIALIZE = '/data_product_exchange/v1/configuration/initialize'
URL_MANAGE_APIKEYS = '/data_product_exchange/v1/configuration/rotate_credentials'
URL_LIST_DATA_PRODUCTS = '/data_product_exchange/v1/data_products'
URL_CREATE_DATA_PRODUCT = '/data_product_exchange/v1/data_products'
URL_GET_DATA_PRODUCT = '/data_product_exchange/v1/data_products/{data_product_id}'
URL_COMPLETE_DRAFT_CONTRACT_TERMS_DOCUMENT = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/contract_terms/{contract_terms_id}/documents/{document_id}/complete'
URL_LIST_DATA_PRODUCT_DRAFTS = '/data_product_exchange/v1/data_products/{data_product_id}/drafts'
URL_CREATE_DATA_PRODUCT_DRAFT = '/data_product_exchange/v1/data_products/{data_product_id}/drafts'
URL_CREATE_DRAFT_CONTRACT_TERMS_DOCUMENT = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/contract_terms/{contract_terms_id}/documents'
URL_GET_DATA_PRODUCT_DRAFT = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}'
URL_GET_DRAFT_CONTRACT_TERMS_DOCUMENT = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/contract_terms/{contract_terms_id}/documents/{document_id}'
URL_PUBLISH_DATA_PRODUCT_DRAFT = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/publish'
URL_GET_DATA_PRODUCT_RELEASE = '/data_product_exchange/v1/data_products/{data_product_id}/releases/{release_id}'
URL_UPDATE_DATA_PRODUCT_RELEASE = '/data_product_exchange/v1/data_products/{data_product_id}/releases/{release_id}'
URL_GET_RELEASE_CONTRACT_TERMS_DOCUMENT = '/data_product_exchange/v1/data_products/{data_product_id}/releases/{release_id}/contract_terms/{contract_terms_id}/documents/{document_id}'
URL_LIST_DATA_PRODUCT_RELEASES = '/data_product_exchange/v1/data_products/{data_product_id}/releases'
URL_RETIRE_DATA_PRODUCT_RELEASE = (
    '/data_product_exchange/v1/data_products/{data_product_id}/releases/{release_id}/retire'
)

# Dph Api Headers
CONTENT_TYPE_JSON = 'application/json'
CONTENT_TYPE_PATCH_JSON = 'application/json-patch+json'

SERVICE_NAME = 'data_product_hub_api_service'
SERVICE_VERSION = 'V1'
