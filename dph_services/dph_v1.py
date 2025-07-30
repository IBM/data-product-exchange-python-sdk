# coding: utf-8

# (C) Copyright IBM Corp. 2025.
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

# IBM OpenAPI SDK Code Generator Version: 3.96.0-d6dec9d7-20241008-212902

"""
Data Product Hub API Service

API Version: 1
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_list, convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers
from .common_constants import *

##############################################################################
# Service
##############################################################################


class DphV1(BaseService):
    """The DPH V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.dataplatform.dev.cloud.ibm.com/'
    DEFAULT_SERVICE_NAME = SERVICE_NAME

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'DphV1':
        """
        Return a new client for the DPH service using the specified parameters and
               external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(
        self,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the DPH service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)

    #########################
    # Configuration
    #########################

    def get_initialize_status(
        self,
        *,
        container_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get resource initialization status.

        Use this API to get the status of resource initialization in Data Product
        Hub.<br/><br/>If the data product catalog exists but has never been initialized,
        the status will be "not_started".<br/><br/>If the data product catalog exists and
        has been or is being initialized, the response will contain the status of the last
        or current initialization. If the initialization failed, the "errors" and "trace"
        fields will contain the error(s) encountered during the initialization, including
        the ID to trace the error(s).<br/><br/>If the data product catalog doesn't exist,
        an HTTP 404 response is returned.

        :param str container_id: (optional) Container ID of the data product
               catalog. If not supplied, the data product catalog is looked up by using
               the uid of the default data product catalog.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `InitializeResource` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_initialize_status',
        )
        headers.update(sdk_headers)

        params = {
            'container.id': container_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/data_product_exchange/v1/configuration/initialize/status'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_service_id_credentials(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get service id credentials.

        Use this API to get the information of service id credentials in Data Product Hub.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServiceIdCredentials` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_service_id_credentials',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/data_product_exchange/v1/configuration/credentials'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def initialize(
        self,
        *,
        container: Optional['ContainerReference'] = None,
        include: Optional[List[str]] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Initialize resources.

        Use this API to initialize default assets for data product hub. <br/><br/>You can
        initialize: <br/><ul><li>`delivery_methods` - Methods through which data product
        parts can be delivered to consumers of the data product
        hub</li><li>`domains_multi_industry` - Taxonomy of domains and use cases
        applicable to multiple industries</li><li>`data_product_samples` - Sample data
        products used to illustrate capabilities of the data product
        hub</li><li>`workflows` - Workflows to enable restricted data
        products</li><li>`project` - A default project for exporting data assets to
        files</li><li>`catalog_configurations` - Catalog configurations for the default
        data product catalog</li></ul><br/><br/>If a resource depends on resources that
        are not specified in the request, these dependent resources will be automatically
        initialized. E.g., initializing `data_product_samples` will also initialize
        `domains_multi_industry` and `delivery_methods` even if they are not specified in
        the request because it depends on them.<br/><br/>If initializing the data product
        hub for the first time, do not specify a container. The default data product
        catalog will be created.<br/>For first time initialization, it is recommended that
        at least `delivery_methods` and `domains_multi_industry` is included in the
        initialize operation.<br/><br/>If the data product hub has already been
        initialized, you may call this API again to initialize new resources, such as new
        delivery methods. In this case, specify the default data product catalog container
        information.

        :param ContainerReference container: (optional) Container reference.
        :param List[str] include: (optional) List of configuration options to
               (re-)initialize.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `InitializeResource` object
        """

        if container is not None:
            container = convert_model(container)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='initialize',
        )
        headers.update(sdk_headers)

        data = {
            'container': container,
            'include': include,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/data_product_exchange/v1/configuration/initialize'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def manage_api_keys(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Rotate credentials for a Data Product Hub instance.

        Use this API to rotate credentials for a Data Product Hub instance.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='manage_api_keys',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        url = '/data_product_exchange/v1/configuration/rotate_credentials'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Data Asset Visualization
    #########################

    def create_data_asset_visualization(
        self,
        *,
        assets: Optional[List['DataAssetRelationship']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create visualization asset and initialize profiling for the provided data assets.

        Use this API to create visualization asset and initialize profiling for the
        provided data assets<br/><br/>Provide the below required fields<br/><br/>Required
        fields:<br/><br/>- catalog_id<br/>- Collection of assetId with it's related asset
        id<br/><br/>.

        :param List[DataAssetRelationship] assets: (optional) Data product hub
               asset and it's related part asset.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataAssetVisualizationRes` object
        """

        if assets is not None:
            assets = [convert_model(x) for x in assets]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_data_asset_visualization',
        )
        headers.update(sdk_headers)

        data = {
            'assets': assets,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/data_product_exchange/v1/data_asset/visualization'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def reinitiate_data_asset_visualization(
        self,
        *,
        assets: Optional[List['DataAssetRelationship']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Reinitiate visualization for an asset.

        Use this API to Reinitiate visualization for an asset which is in below
        scenarios<br/><br/>- Previous bucket got deleted and new bucket is created.<br/>-
        Data visualization attachment is missing in asset details.<br/>- Visualization
        asset reference is missing in related asset details.<br/><br/>.

        :param List[DataAssetRelationship] assets: (optional) Data product hub
               asset and it's related part asset.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataAssetVisualizationRes` object
        """

        if assets is not None:
            assets = [convert_model(x) for x in assets]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='reinitiate_data_asset_visualization',
        )
        headers.update(sdk_headers)

        data = {
            'assets': assets,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/data_product_exchange/v1/data_asset/visualization/reinitiate'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Data Products
    #########################

    def list_data_products(
        self,
        *,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a list of data products.

        Retrieve a list of data products.

        :param int limit: (optional) Limit the number of data products in the
               results. The maximum limit is 200.
        :param str start: (optional) Start token for pagination.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductCollection` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_data_products',
        )
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'start': start,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/data_product_exchange/v1/data_products'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_data_product(
        self,
        drafts: List['DataProductDraftPrototype'],
        *,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a new data product.

        Use this API to create a new data product.<br/><br/>Provide the initial draft of
        the data product.<br/><br/>Required fields:<br/><br/>- name<br/>-
        container<br/><br/>If `version` is not specified, the default version **1.0.0**
        will be used.<br/><br/>The `domain` is optional.

        :param List[DataProductDraftPrototype] drafts: Collection of data products
               drafts to add to data product.
        :param int limit: (optional) Limit the number of data products in the
               results. The maximum limit is 200.
        :param str start: (optional) Start token for pagination.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProduct` object
        """

        if drafts is None:
            raise ValueError('drafts must be provided')
        drafts = [convert_model(x) for x in drafts]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_data_product',
        )
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'start': start,
        }

        data = {
            'drafts': drafts,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/data_product_exchange/v1/data_products'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_data_product(
        self,
        data_product_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a data product identified by id.

        Retrieve a data product identified by id.

        :param str data_product_id: Data product ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProduct` object
        """

        if not data_product_id:
            raise ValueError('data_product_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_data_product',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['data_product_id']
        path_param_values = self.encode_path_vars(data_product_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Data Product Drafts
    #########################

    def complete_draft_contract_terms_document(
        self,
        data_product_id: str,
        draft_id: str,
        contract_terms_id: str,
        document_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Complete a contract document upload operation.

        After uploading a file to the provided signed URL, call this endpoint to mark the
        upload as complete. After the upload operation is marked as complete, the file is
        available to download. Use '-' for the `data_product_id` to skip specifying the
        data product ID explicitly.
        - After the upload is marked as complete, the returned URL is displayed in the
        "url" field. The signed URL is used to download the document.
        - Calling complete on referential documents results in an error.
        - Calling complete on attachment documents for which the file has not been
        uploaded will result in an error.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str draft_id: Data product draft id.
        :param str contract_terms_id: Contract terms id.
        :param str document_id: Document id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ContractTermsDocument` object
        """

        if not data_product_id:
            raise ValueError('data_product_id must be provided')
        if not draft_id:
            raise ValueError('draft_id must be provided')
        if not contract_terms_id:
            raise ValueError('contract_terms_id must be provided')
        if not document_id:
            raise ValueError('document_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='complete_draft_contract_terms_document',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['data_product_id', 'draft_id', 'contract_terms_id', 'document_id']
        path_param_values = self.encode_path_vars(data_product_id, draft_id, contract_terms_id, document_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/contract_terms/{contract_terms_id}/documents/{document_id}/complete'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def list_data_product_drafts(
        self,
        data_product_id: str,
        *,
        asset_container_id: Optional[str] = None,
        version: Optional[str] = None,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a list of data product drafts.

        Retrieve a list of data product drafts. Use '-' for the `data_product_id` to skip
        specifying the data product ID explicitly.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str asset_container_id: (optional) Filter the list of data product
               drafts by container id.
        :param str version: (optional) Filter the list of data product drafts by
               version number.
        :param int limit: (optional) Limit the number of data product drafts in the
               results. The maximum limit is 200.
        :param str start: (optional) Start token for pagination.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductDraftCollection` object
        """

        if not data_product_id:
            raise ValueError('data_product_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_data_product_drafts',
        )
        headers.update(sdk_headers)

        params = {
            'asset.container.id': asset_container_id,
            'version': version,
            'limit': limit,
            'start': start,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['data_product_id']
        path_param_values = self.encode_path_vars(data_product_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}/drafts'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_data_product_draft(
        self,
        data_product_id: str,
        asset: 'AssetPrototype',
        *,
        version: Optional[str] = None,
        state: Optional[str] = None,
        data_product: Optional['DataProductIdentity'] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
        use_cases: Optional[List['UseCase']] = None,
        types: Optional[List[str]] = None,
        contract_terms: Optional[List['ContractTerms']] = None,
        domain: Optional['Domain'] = None,
        parts_out: Optional[List['DataProductPart']] = None,
        workflows: Optional['DataProductWorkflows'] = None,
        dataview_enabled: Optional[bool] = None,
        comments: Optional[str] = None,
        access_control: Optional['AssetListAccessControl'] = None,
        last_updated_at: Optional[datetime] = None,
        is_restricted: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a new draft of an existing data product.

        Create a new draft of an existing data product.

        :param str data_product_id: Data product ID.
        :param AssetPrototype asset: New asset input properties.
        :param str version: (optional) The data product version number.
        :param str state: (optional) The state of the data product version. If not
               specified, the data product version will be created in `draft` state.
        :param DataProductIdentity data_product: (optional) Data product
               identifier.
        :param str name: (optional) The name that refers to the new data product
               version. If this is a new data product, this value must be specified. If
               this is a new version of an existing data product, the name will default to
               the name of the previous data product version. A name can contain letters,
               numbers, understores, dashes, spaces or periods. A name must contain at
               least one non-space character.
        :param str description: (optional) Description of the data product version.
               If this is a new version of an existing data product, the description will
               default to the description of the previous version of the data product.
        :param List[str] tags: (optional) Tags on the data product.
        :param List[UseCase] use_cases: (optional) A list of use cases associated
               with the data product version.
        :param List[str] types: (optional) Types of parts on the data product.
        :param List[ContractTerms] contract_terms: (optional) Contract terms
               binding various aspects of the data product.
        :param Domain domain: (optional) Domain that the data product version
               belongs to. If this is the first version of a data product, this field is
               required. If this is a new version of an existing data product, the domain
               will default to the domain of the previous version of the data product.
        :param List[DataProductPart] parts_out: (optional) The outgoing parts of
               this data product version to be delivered to consumers. If this is the
               first version of a data product, this field defaults to an empty list. If
               this is a new version of an existing data product, the data product parts
               will default to the parts list from the previous version of the data
               product.
        :param DataProductWorkflows workflows: (optional) The workflows associated
               with the data product version.
        :param bool dataview_enabled: (optional) Indicates whether the dataView has
               enabled for data product.
        :param str comments: (optional) Comments by a producer that are provided
               either at the time of data product version creation or retiring.
        :param AssetListAccessControl access_control: (optional) Access control
               object.
        :param datetime last_updated_at: (optional) Timestamp of last asset update.
        :param bool is_restricted: (optional) Indicates whether the data product is
               restricted or not. A restricted data product indicates that orders of the
               data product requires explicit approval before data is delivered.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductDraft` object
        """

        if not data_product_id:
            raise ValueError('data_product_id must be provided')
        if asset is None:
            raise ValueError('asset must be provided')
        asset = convert_model(asset)
        if data_product is not None:
            data_product = convert_model(data_product)
        if use_cases is not None:
            use_cases = [convert_model(x) for x in use_cases]
        if contract_terms is not None:
            contract_terms = [convert_model(x) for x in contract_terms]
        if domain is not None:
            domain = convert_model(domain)
        if parts_out is not None:
            parts_out = [convert_model(x) for x in parts_out]
        if workflows is not None:
            workflows = convert_model(workflows)
        if access_control is not None:
            access_control = convert_model(access_control)
        if last_updated_at is not None:
            last_updated_at = datetime_to_string(last_updated_at)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_data_product_draft',
        )
        headers.update(sdk_headers)

        data = {
            'asset': asset,
            'version': version,
            'state': state,
            'data_product': data_product,
            'name': name,
            'description': description,
            'tags': tags,
            'use_cases': use_cases,
            'types': types,
            'contract_terms': contract_terms,
            'domain': domain,
            'parts_out': parts_out,
            'workflows': workflows,
            'dataview_enabled': dataview_enabled,
            'comments': comments,
            'access_control': access_control,
            'last_updated_at': last_updated_at,
            'is_restricted': is_restricted,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['data_product_id']
        path_param_values = self.encode_path_vars(data_product_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}/drafts'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def create_draft_contract_terms_document(
        self,
        data_product_id: str,
        draft_id: str,
        contract_terms_id: str,
        type: str,
        name: str,
        *,
        url: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Upload a contract document to the data product draft contract terms.

        Upload a contract document to the data product draft identified by draft_id. Use
        '-' for the `data_product_id` to skip specifying the data product ID explicitly.
        - If the request object contains a "url" parameter, a referential document is
        created to store the provided url.
        - If the request object does not contain a "url" parameter, an attachment document
        is created, and a signed url will be returned in an "upload_url" parameter. The
        data product producer can upload the document using the provided "upload_url".
        After the upload is completed, call "complete_contract_terms_document" for the
        given document needs to be called to mark the upload as completed. After
        completion of the upload, "get_contract_terms_document" for the given document
        returns a signed "url" parameter that can be used to download the attachment
        document.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str draft_id: Data product draft id.
        :param str contract_terms_id: Contract terms id.
        :param str type: Type of the contract document.
        :param str name: Name of the contract document.
        :param str url: (optional) URL that can be used to retrieve the contract
               document.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ContractTermsDocument` object
        """

        if not data_product_id:
            raise ValueError('data_product_id must be provided')
        if not draft_id:
            raise ValueError('draft_id must be provided')
        if not contract_terms_id:
            raise ValueError('contract_terms_id must be provided')
        if type is None:
            raise ValueError('type must be provided')
        if name is None:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_draft_contract_terms_document',
        )
        headers.update(sdk_headers)

        data = {
            'type': type,
            'name': name,
            'url': url,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['data_product_id', 'draft_id', 'contract_terms_id']
        path_param_values = self.encode_path_vars(data_product_id, draft_id, contract_terms_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/contract_terms/{contract_terms_id}/documents'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_data_product_draft(
        self,
        data_product_id: str,
        draft_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a draft of an existing data product.

        Get a draft of an existing data product. Use '-' for the `data_product_id` to skip
        specifying the data product ID explicitly.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str draft_id: Data product draft id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductDraft` object
        """

        if not data_product_id:
            raise ValueError('data_product_id must be provided')
        if not draft_id:
            raise ValueError('draft_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_data_product_draft',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['data_product_id', 'draft_id']
        path_param_values = self.encode_path_vars(data_product_id, draft_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_data_product_draft(
        self,
        data_product_id: str,
        draft_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a data product draft identified by ID.

        Delete a data product draft identified by a valid ID. Use '-' for the
        `data_product_id` to skip specifying the data product ID explicitly.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str draft_id: Data product draft id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not data_product_id:
            raise ValueError('data_product_id must be provided')
        if not draft_id:
            raise ValueError('draft_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_data_product_draft',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['data_product_id', 'draft_id']
        path_param_values = self.encode_path_vars(data_product_id, draft_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_data_product_draft(
        self,
        data_product_id: str,
        draft_id: str,
        json_patch_instructions: List['JsonPatchOperation'],
        **kwargs,
    ) -> DetailedResponse:
        """
        Update the data product draft identified by ID.

        Use this API to update the properties of a data product draft identified by a
        valid ID. Use '-' for the `data_product_id` to skip specifying the data product ID
        explicitly.<br/><br/>Specify patch operations using http://jsonpatch.com/
        syntax.<br/><br/>Supported patch operations include:<br/><br/>- Update the
        properties of a data product<br/><br/>- Add/Remove parts from a data product (up
        to 20 parts)<br/><br/>- Add/Remove use cases from a data product<br/><br/>- Update
        the data product state<br/><br/>.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str draft_id: Data product draft id.
        :param List[JsonPatchOperation] json_patch_instructions: A set of patch
               operations as defined in RFC 6902. See http://jsonpatch.com/ for more
               information.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductDraft` object
        """

        if not data_product_id:
            raise ValueError('data_product_id must be provided')
        if not draft_id:
            raise ValueError('draft_id must be provided')
        if json_patch_instructions is None:
            raise ValueError('json_patch_instructions must be provided')
        json_patch_instructions = [convert_model(x) for x in json_patch_instructions]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_data_product_draft',
        )
        headers.update(sdk_headers)

        data = json.dumps(json_patch_instructions)
        headers['content-type'] = 'application/json-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['data_product_id', 'draft_id']
        path_param_values = self.encode_path_vars(data_product_id, draft_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_draft_contract_terms_document(
        self,
        data_product_id: str,
        draft_id: str,
        contract_terms_id: str,
        document_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a contract document.

        If a document has a completed attachment, the response contains the `url` which
        can be used to download the attachment. If a document does not have a completed
        attachment, the response contains the `url` which was submitted at document
        creation. If a document has an attachment that is incomplete, an error is returned
        to prompt the user to upload the document file and complete it. Use '-' for the
        `data_product_id` to skip specifying the data product ID explicitly.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str draft_id: Data product draft id.
        :param str contract_terms_id: Contract terms id.
        :param str document_id: Document id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ContractTermsDocument` object
        """

        if not data_product_id:
            raise ValueError('data_product_id must be provided')
        if not draft_id:
            raise ValueError('draft_id must be provided')
        if not contract_terms_id:
            raise ValueError('contract_terms_id must be provided')
        if not document_id:
            raise ValueError('document_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_draft_contract_terms_document',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['data_product_id', 'draft_id', 'contract_terms_id', 'document_id']
        path_param_values = self.encode_path_vars(data_product_id, draft_id, contract_terms_id, document_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/contract_terms/{contract_terms_id}/documents/{document_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_draft_contract_terms_document(
        self,
        data_product_id: str,
        draft_id: str,
        contract_terms_id: str,
        document_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a contract document.

        Delete an existing contract document.
        Contract documents can only be deleted for data product versions that are in DRAFT
        state. Use '-' for the `data_product_id` to skip specifying the data product ID
        explicitly.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str draft_id: Data product draft id.
        :param str contract_terms_id: Contract terms id.
        :param str document_id: Document id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not data_product_id:
            raise ValueError('data_product_id must be provided')
        if not draft_id:
            raise ValueError('draft_id must be provided')
        if not contract_terms_id:
            raise ValueError('contract_terms_id must be provided')
        if not document_id:
            raise ValueError('document_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_draft_contract_terms_document',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['data_product_id', 'draft_id', 'contract_terms_id', 'document_id']
        path_param_values = self.encode_path_vars(data_product_id, draft_id, contract_terms_id, document_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/contract_terms/{contract_terms_id}/documents/{document_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_draft_contract_terms_document(
        self,
        data_product_id: str,
        draft_id: str,
        contract_terms_id: str,
        document_id: str,
        json_patch_instructions: List['JsonPatchOperation'],
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a contract document.

        Use this API to update the properties of a contract document that is identified by
        a valid ID.
        Specify patch operations using http://jsonpatch.com/ syntax.
        Supported patch operations include:
        - Update the url of document if it does not have an attachment.
        - Update the type of the document.
        <br/><br/>Contract terms documents can only be updated if the associated data
        product version is in DRAFT state. Use '-' for the `data_product_id` to skip
        specifying the data product ID explicitly.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str draft_id: Data product draft id.
        :param str contract_terms_id: Contract terms id.
        :param str document_id: Document id.
        :param List[JsonPatchOperation] json_patch_instructions: A set of patch
               operations as defined in RFC 6902. See http://jsonpatch.com/ for more
               information.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ContractTermsDocument` object
        """

        if not data_product_id:
            raise ValueError('data_product_id must be provided')
        if not draft_id:
            raise ValueError('draft_id must be provided')
        if not contract_terms_id:
            raise ValueError('contract_terms_id must be provided')
        if not document_id:
            raise ValueError('document_id must be provided')
        if json_patch_instructions is None:
            raise ValueError('json_patch_instructions must be provided')
        json_patch_instructions = [convert_model(x) for x in json_patch_instructions]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_draft_contract_terms_document',
        )
        headers.update(sdk_headers)

        data = json.dumps(json_patch_instructions)
        headers['content-type'] = 'application/json-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['data_product_id', 'draft_id', 'contract_terms_id', 'document_id']
        path_param_values = self.encode_path_vars(data_product_id, draft_id, contract_terms_id, document_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/contract_terms/{contract_terms_id}/documents/{document_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_data_product_draft_contract_terms(
        self,
        data_product_id: str,
        draft_id: str,
        contract_terms_id: str,
        *,
        accept: Optional[str] = None,
        include_contract_documents: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a data product contract terms identified by id.

        Retrieve a data product contract terms identified by id.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str draft_id: Data product draft id.
        :param str contract_terms_id: Contract terms id.
        :param str accept: (optional) The type of the response:
               application/odcs+yaml or application/json.
        :param bool include_contract_documents: (optional) Set to false to exclude
               external contract documents (e.g., Terms and Conditions URLs) from the
               response. By default, these are included.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if not data_product_id:
            raise ValueError('data_product_id must be provided')
        if not draft_id:
            raise ValueError('draft_id must be provided')
        if not contract_terms_id:
            raise ValueError('contract_terms_id must be provided')
        headers = {
            'Accept': accept,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_data_product_draft_contract_terms',
        )
        headers.update(sdk_headers)

        params = {
            'include_contract_documents': include_contract_documents,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['data_product_id', 'draft_id', 'contract_terms_id']
        path_param_values = self.encode_path_vars(data_product_id, draft_id, contract_terms_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/contract_terms/{contract_terms_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_data_product_draft_contract_terms(
        self,
        data_product_id: str,
        draft_id: str,
        contract_terms_id: str,
        *,
        asset: Optional['AssetReference'] = None,
        id: Optional[str] = None,
        documents: Optional[List['ContractTermsDocument']] = None,
        error_msg: Optional[str] = None,
        overview: Optional['Overview'] = None,
        description: Optional['Description'] = None,
        organization: Optional[List['ContractTemplateOrganization']] = None,
        roles: Optional[List['Roles']] = None,
        price: Optional['Pricing'] = None,
        sla: Optional[List['ContractTemplateSLA']] = None,
        support_and_communication: Optional[List['ContractTemplateSupportAndCommunication']] = None,
        custom_properties: Optional[List['ContractTemplateCustomProperty']] = None,
        contract_test: Optional['ContractTest'] = None,
        schema: Optional[List['ContractSchema']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a data product contract terms identified by id.

        Update a data product contract terms identified by id.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str draft_id: Data product draft id.
        :param str contract_terms_id: Contract terms id.
        :param AssetReference asset: (optional) The reference schema for a asset in
               a container.
        :param str id: (optional) ID of the contract terms.
        :param List[ContractTermsDocument] documents: (optional) Collection of
               contract terms documents.
        :param str error_msg: (optional) An error message, if existing, relating to
               the contract terms.
        :param Overview overview: (optional) Overview details of a data contract.
        :param Description description: (optional) Description details of a data
               contract.
        :param List[ContractTemplateOrganization] organization: (optional) List of
               sub domains to be added within a domain.
        :param List[Roles] roles: (optional) List of roles associated with the
               contract.
        :param Pricing price: (optional) Represents the pricing details of the
               contract.
        :param List[ContractTemplateSLA] sla: (optional) Service Level Agreement
               details.
        :param List[ContractTemplateSupportAndCommunication]
               support_and_communication: (optional) Support and communication details for
               the contract.
        :param List[ContractTemplateCustomProperty] custom_properties: (optional)
               Custom properties that are not part of the standard contract.
        :param ContractTest contract_test: (optional) Contains the contract test
               status and related metadata.
        :param List[ContractSchema] schema: (optional) Schema details of the data
               asset.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ContractTerms` object
        """

        if not data_product_id:
            raise ValueError('data_product_id must be provided')
        if not draft_id:
            raise ValueError('draft_id must be provided')
        if not contract_terms_id:
            raise ValueError('contract_terms_id must be provided')
        if asset is not None:
            asset = convert_model(asset)
        if documents is not None:
            documents = [convert_model(x) for x in documents]
        if overview is not None:
            overview = convert_model(overview)
        if description is not None:
            description = convert_model(description)
        if organization is not None:
            organization = [convert_model(x) for x in organization]
        if roles is not None:
            roles = [convert_model(x) for x in roles]
        if price is not None:
            price = convert_model(price)
        if sla is not None:
            sla = [convert_model(x) for x in sla]
        if support_and_communication is not None:
            support_and_communication = [convert_model(x) for x in support_and_communication]
        if custom_properties is not None:
            custom_properties = [convert_model(x) for x in custom_properties]
        if contract_test is not None:
            contract_test = convert_model(contract_test)
        if schema is not None:
            schema = [convert_model(x) for x in schema]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='replace_data_product_draft_contract_terms',
        )
        headers.update(sdk_headers)

        data = {
            'asset': asset,
            'id': id,
            'documents': documents,
            'error_msg': error_msg,
            'overview': overview,
            'description': description,
            'organization': organization,
            'roles': roles,
            'price': price,
            'sla': sla,
            'support_and_communication': support_and_communication,
            'custom_properties': custom_properties,
            'contract_test': contract_test,
            'schema': schema,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['data_product_id', 'draft_id', 'contract_terms_id']
        path_param_values = self.encode_path_vars(data_product_id, draft_id, contract_terms_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/contract_terms/{contract_terms_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def update_data_product_draft_contract_terms(
        self,
        data_product_id: str,
        draft_id: str,
        contract_terms_id: str,
        json_patch_instructions: List['JsonPatchOperation'],
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a contract terms property.

        Use this API to update the properties of a contract terms that is identified by a
        valid ID.
        Specify patch operations using http://jsonpatch.com/ syntax.
        Supported patch operations include:
        - Update the contract terms properties.
        <br/><br/>Contract terms can only be updated if the associated data product
        version is in DRAFT state.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str draft_id: Data product draft id.
        :param str contract_terms_id: Contract terms id.
        :param List[JsonPatchOperation] json_patch_instructions: A set of patch
               operations as defined in RFC 6902. See http://jsonpatch.com/ for more
               information.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ContractTerms` object
        """

        if not data_product_id:
            raise ValueError('data_product_id must be provided')
        if not draft_id:
            raise ValueError('draft_id must be provided')
        if not contract_terms_id:
            raise ValueError('contract_terms_id must be provided')
        if json_patch_instructions is None:
            raise ValueError('json_patch_instructions must be provided')
        json_patch_instructions = [convert_model(x) for x in json_patch_instructions]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_data_product_draft_contract_terms',
        )
        headers.update(sdk_headers)

        data = json.dumps(json_patch_instructions)
        headers['content-type'] = 'application/json-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['data_product_id', 'draft_id', 'contract_terms_id']
        path_param_values = self.encode_path_vars(data_product_id, draft_id, contract_terms_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/contract_terms/{contract_terms_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def publish_data_product_draft(
        self,
        data_product_id: str,
        draft_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Publish a draft of an existing data product.

        Publish a draft of an existing data product. Use '-' for the `data_product_id` to
        skip specifying the data product ID explicitly.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str draft_id: Data product draft id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductRelease` object
        """

        if not data_product_id:
            raise ValueError('data_product_id must be provided')
        if not draft_id:
            raise ValueError('draft_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='publish_data_product_draft',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['data_product_id', 'draft_id']
        path_param_values = self.encode_path_vars(data_product_id, draft_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/publish'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Data Product Releases
    #########################

    def get_data_product_release(
        self,
        data_product_id: str,
        release_id: str,
        *,
        check_caller_approval: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a release of an existing data product.

        Get a release of an existing data product. Use '-' for the `data_product_id` to
        skip specifying the data product ID explicitly.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str release_id: Data product release id.
        :param bool check_caller_approval: (optional) If the value is true, then it
               will be verfied whether the caller is present in the data access request
               pre-approved user list.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductRelease` object
        """

        if not data_product_id:
            raise ValueError('data_product_id must be provided')
        if not release_id:
            raise ValueError('release_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_data_product_release',
        )
        headers.update(sdk_headers)

        params = {
            'check_caller_approval': check_caller_approval,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['data_product_id', 'release_id']
        path_param_values = self.encode_path_vars(data_product_id, release_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}/releases/{release_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_data_product_release(
        self,
        data_product_id: str,
        release_id: str,
        json_patch_instructions: List['JsonPatchOperation'],
        **kwargs,
    ) -> DetailedResponse:
        """
        Update the data product release identified by ID.

        Use this API to update the properties of a data product release identified by a
        valid ID. Use '-' for the `data_product_id` to skip specifying the data product ID
        explicitly.<br/><br/>Specify patch operations using http://jsonpatch.com/
        syntax.<br/><br/>Supported patch operations include:<br/><br/>- Update the
        properties of a data product<br/><br/>- Add/remove parts from a data product (up
        to 20 parts)<br/><br/>- Add/remove use cases from a data product<br/><br/>.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str release_id: Data product release id.
        :param List[JsonPatchOperation] json_patch_instructions: A set of patch
               operations as defined in RFC 6902. See http://jsonpatch.com/ for more
               information.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductRelease` object
        """

        if not data_product_id:
            raise ValueError('data_product_id must be provided')
        if not release_id:
            raise ValueError('release_id must be provided')
        if json_patch_instructions is None:
            raise ValueError('json_patch_instructions must be provided')
        json_patch_instructions = [convert_model(x) for x in json_patch_instructions]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_data_product_release',
        )
        headers.update(sdk_headers)

        data = json.dumps(json_patch_instructions)
        headers['content-type'] = 'application/json-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['data_product_id', 'release_id']
        path_param_values = self.encode_path_vars(data_product_id, release_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}/releases/{release_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_release_contract_terms_document(
        self,
        data_product_id: str,
        release_id: str,
        contract_terms_id: str,
        document_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a contract document.

        If the document has a completed attachment, the response contains the `url` to
        download the attachment.<br/><br/> If the document does not have an attachment,
        the response contains the `url` which was submitted at document
        creation.<br/><br/> If the document has an incomplete attachment, an error is
        returned to prompt the user to upload the document file to complete the
        attachment. Use '-' for the `data_product_id` to skip specifying the data product
        ID explicitly.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str release_id: Data product release id.
        :param str contract_terms_id: Contract terms id.
        :param str document_id: Document id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ContractTermsDocument` object
        """

        if not data_product_id:
            raise ValueError('data_product_id must be provided')
        if not release_id:
            raise ValueError('release_id must be provided')
        if not contract_terms_id:
            raise ValueError('contract_terms_id must be provided')
        if not document_id:
            raise ValueError('document_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_release_contract_terms_document',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['data_product_id', 'release_id', 'contract_terms_id', 'document_id']
        path_param_values = self.encode_path_vars(data_product_id, release_id, contract_terms_id, document_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}/releases/{release_id}/contract_terms/{contract_terms_id}/documents/{document_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def list_data_product_releases(
        self,
        data_product_id: str,
        *,
        asset_container_id: Optional[str] = None,
        state: Optional[List[str]] = None,
        version: Optional[str] = None,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a list of data product releases.

        Retrieve a list of data product releases. Use '-' for the `data_product_id` to
        skip specifying the data product ID explicitly.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str asset_container_id: (optional) Filter the list of data product
               releases by container id.
        :param List[str] state: (optional) Filter the list of data product versions
               by state. States are: available and retired. Default is
               "available","retired".
        :param str version: (optional) Filter the list of data product releases by
               version number.
        :param int limit: (optional) Limit the number of data product releases in
               the results. The maximum is 200.
        :param str start: (optional) Start token for pagination.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductReleaseCollection` object
        """

        if not data_product_id:
            raise ValueError('data_product_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_data_product_releases',
        )
        headers.update(sdk_headers)

        params = {
            'asset.container.id': asset_container_id,
            'state': convert_list(state),
            'version': version,
            'limit': limit,
            'start': start,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['data_product_id']
        path_param_values = self.encode_path_vars(data_product_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}/releases'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def retire_data_product_release(
        self,
        data_product_id: str,
        release_id: str,
        *,
        revoke_access: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retire a release of an existing data product.

        Retire a release of an existing data product. Use '-' for the `data_product_id` to
        skip specifying the data product ID explicitly.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str release_id: Data product release id.
        :param bool revoke_access: (optional) Revoke's Access from all the
               Subscriptions of the Data Product. No user's can able to see the subscribed
               assets anymore.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductRelease` object
        """

        if not data_product_id:
            raise ValueError('data_product_id must be provided')
        if not release_id:
            raise ValueError('release_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='retire_data_product_release',
        )
        headers.update(sdk_headers)

        params = {
            'revoke_access': revoke_access,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['data_product_id', 'release_id']
        path_param_values = self.encode_path_vars(data_product_id, release_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}/releases/{release_id}/retire'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Data Product Contract Templates
    #########################

    def list_data_product_contract_template(
        self,
        *,
        container_id: Optional[str] = None,
        contract_template_name: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a list of data product contract templates.

        Retrieve a list of data product contract templates.

        :param str container_id: (optional) Container ID of the data product
               catalog. If not supplied, the data product catalog is looked up by using
               the uid of the default data product catalog.
        :param str contract_template_name: (optional) Name of the data product
               contract template. If not supplied, the data product templates within the
               catalog will returned.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductContractTemplateCollection` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_data_product_contract_template',
        )
        headers.update(sdk_headers)

        params = {
            'container.id': container_id,
            'contract_template.name': contract_template_name,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/data_product_exchange/v1/contract_templates'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_contract_template(
        self,
        container: 'ContainerReference',
        *,
        id: Optional[str] = None,
        name: Optional[str] = None,
        error: Optional['ErrorMessage'] = None,
        contract_terms: Optional['ContractTerms'] = None,
        container_id: Optional[str] = None,
        contract_template_name: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create new data product contract template.

        Create new data product contract template.

        :param ContainerReference container: Container reference.
        :param str id: (optional) The identifier of the data product contract
               template.
        :param str name: (optional) The name of the contract template.
        :param ErrorMessage error: (optional) Contains the code and details.
        :param ContractTerms contract_terms: (optional) Defines the complete
               structure of a contract terms.
        :param str container_id: (optional) Container ID of the data product
               catalog. If not supplied, the data product catalog is looked up by using
               the uid of the default data product catalog.
        :param str contract_template_name: (optional) Name of the data product
               contract template. If not supplied, the data product templates within the
               catalog will returned.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductContractTemplate` object
        """

        if container is None:
            raise ValueError('container must be provided')
        container = convert_model(container)
        if error is not None:
            error = convert_model(error)
        if contract_terms is not None:
            contract_terms = convert_model(contract_terms)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_contract_template',
        )
        headers.update(sdk_headers)

        params = {
            'container.id': container_id,
            'contract_template.name': contract_template_name,
        }

        data = {
            'container': container,
            'id': id,
            'name': name,
            'error': error,
            'contract_terms': contract_terms,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/data_product_exchange/v1/contract_templates'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_contract_template(
        self,
        contract_template_id: str,
        container_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a data product contract template identified by id.

        Retrieve a data product contract template identified by id.

        :param str contract_template_id: Data Product Contract Template id.
        :param str container_id: Container ID of the data product catalog.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductContractTemplate` object
        """

        if not contract_template_id:
            raise ValueError('contract_template_id must be provided')
        if not container_id:
            raise ValueError('container_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_contract_template',
        )
        headers.update(sdk_headers)

        params = {
            'container.id': container_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['contract_template_id']
        path_param_values = self.encode_path_vars(contract_template_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/contract_templates/{contract_template_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_data_product_contract_template(
        self,
        contract_template_id: str,
        container_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a data product contract template identified by id.

        Delete a data product contract template identified by id.

        :param str contract_template_id: Data Product Contract Template id.
        :param str container_id: Container ID of the data product catalog.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not contract_template_id:
            raise ValueError('contract_template_id must be provided')
        if not container_id:
            raise ValueError('container_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_data_product_contract_template',
        )
        headers.update(sdk_headers)

        params = {
            'container.id': container_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['contract_template_id']
        path_param_values = self.encode_path_vars(contract_template_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/contract_templates/{contract_template_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_data_product_contract_template(
        self,
        contract_template_id: str,
        container_id: str,
        json_patch_instructions: List['JsonPatchOperation'],
        **kwargs,
    ) -> DetailedResponse:
        """
        Update the data product contract template identified by ID.

        Use this API to update the properties of a data product contract template
        identified by a valid ID.<br/><br/>Specify patch operations using
        http://jsonpatch.com/ syntax.<br/><br/>Supported patch operations
        include:<br/><br/>- Update the name of a data product contract template<br/><br/>-
        Update the contract terms of data product contract template<br/><br/>.

        :param str contract_template_id: Data Product Contract Template id.
        :param str container_id: Container ID of the data product catalog.
        :param List[JsonPatchOperation] json_patch_instructions: A set of patch
               operations as defined in RFC 6902. See http://jsonpatch.com/ for more
               information.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductContractTemplate` object
        """

        if not contract_template_id:
            raise ValueError('contract_template_id must be provided')
        if not container_id:
            raise ValueError('container_id must be provided')
        if json_patch_instructions is None:
            raise ValueError('json_patch_instructions must be provided')
        json_patch_instructions = [convert_model(x) for x in json_patch_instructions]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_data_product_contract_template',
        )
        headers.update(sdk_headers)

        params = {
            'container.id': container_id,
        }

        data = json.dumps(json_patch_instructions)
        headers['content-type'] = 'application/json-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['contract_template_id']
        path_param_values = self.encode_path_vars(contract_template_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/contract_templates/{contract_template_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Data Product Domains
    #########################

    def list_data_product_domains(
        self,
        *,
        container_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a list of data product domains.

        Retrieve a list of data product domains.

        :param str container_id: (optional) Container ID of the data product
               catalog. If not supplied, the data product catalog is looked up by using
               the uid of the default data product catalog.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductDomainCollection` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_data_product_domains',
        )
        headers.update(sdk_headers)

        params = {
            'container.id': container_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/data_product_exchange/v1/domains'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_data_product_domain(
        self,
        container: 'ContainerReference',
        *,
        trace: Optional[str] = None,
        errors: Optional[List['ErrorModelResource']] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        member_roles: Optional['MemberRolesSchema'] = None,
        properties: Optional['PropertiesSchema'] = None,
        sub_domains: Optional[List['InitializeSubDomain']] = None,
        container_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create new data product domain.

        Create new data product domain.

        :param ContainerReference container: Container reference.
        :param str trace: (optional) The id to trace the failed domain creations.
        :param List[ErrorModelResource] errors: (optional) Set of errors on the sub
               domain creation.
        :param str name: (optional) The name of the data product domain.
        :param str description: (optional) The description of the data product
               domain.
        :param str id: (optional) The identifier of the data product domain.
        :param MemberRolesSchema member_roles: (optional) Member roles of a
               corresponding asset.
        :param PropertiesSchema properties: (optional) Properties of the
               corresponding asset.
        :param List[InitializeSubDomain] sub_domains: (optional) List of sub
               domains to be added within a domain.
        :param str container_id: (optional) Container ID of the data product
               catalog. If not supplied, the data product catalog is looked up by using
               the uid of the default data product catalog.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductDomain` object
        """

        if container is None:
            raise ValueError('container must be provided')
        container = convert_model(container)
        if errors is not None:
            errors = [convert_model(x) for x in errors]
        if member_roles is not None:
            member_roles = convert_model(member_roles)
        if properties is not None:
            properties = convert_model(properties)
        if sub_domains is not None:
            sub_domains = [convert_model(x) for x in sub_domains]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_data_product_domain',
        )
        headers.update(sdk_headers)

        params = {
            'container.id': container_id,
        }

        data = {
            'container': container,
            'trace': trace,
            'errors': errors,
            'name': name,
            'description': description,
            'id': id,
            'member_roles': member_roles,
            'properties': properties,
            'sub_domains': sub_domains,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/data_product_exchange/v1/domains'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def create_data_product_subdomain(
        self,
        domain_id: str,
        container_id: str,
        *,
        name: Optional[str] = None,
        id: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create data product subdomains for a specific domain identified by id.

        Create data product subdomains for a specific domain identified by id.

        :param str domain_id: Domain id.
        :param str container_id: Container ID of the data product catalog.
        :param str name: (optional) The name of the data product subdomain.
        :param str id: (optional) The identifier of the data product subdomain.
        :param str description: (optional) The description of the data product
               subdomain.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `InitializeSubDomain` object
        """

        if not domain_id:
            raise ValueError('domain_id must be provided')
        if not container_id:
            raise ValueError('container_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_data_product_subdomain',
        )
        headers.update(sdk_headers)

        params = {
            'container.id': container_id,
        }

        data = {
            'name': name,
            'id': id,
            'description': description,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['domain_id']
        path_param_values = self.encode_path_vars(domain_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/domains/{domain_id}/subdomains'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_domain(
        self,
        domain_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a data product domain or subdomain identified by id.

        Retrieve a data product domain or subdomain identified by id.

        :param str domain_id: Domain id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductDomain` object
        """

        if not domain_id:
            raise ValueError('domain_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_domain',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['domain_id']
        path_param_values = self.encode_path_vars(domain_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/domains/{domain_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_domain(
        self,
        domain_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a data product domain identified by id.

        Delete a data product domain identified by id.

        :param str domain_id: Domain id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not domain_id:
            raise ValueError('domain_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_domain',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['domain_id']
        path_param_values = self.encode_path_vars(domain_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/domains/{domain_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_data_product_domain(
        self,
        domain_id: str,
        container_id: str,
        json_patch_instructions: List['JsonPatchOperation'],
        **kwargs,
    ) -> DetailedResponse:
        """
        Update the data product domain identified by ID.

        Use this API to update the properties of a data product domain identified by a
        valid ID.<br/><br/>Specify patch operations using http://jsonpatch.com/
        syntax.<br/><br/>Supported patch operations include:<br/><br/>- Update the name of
        a data product domain<br/><br/>- Update the description of a data product
        domain<br/><br/>- Update the rov of a data product domain<br/><br/>.

        :param str domain_id: Domain id.
        :param str container_id: Container ID of the data product catalog.
        :param List[JsonPatchOperation] json_patch_instructions: A set of patch
               operations as defined in RFC 6902. See http://jsonpatch.com/ for more
               information.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductDomain` object
        """

        if not domain_id:
            raise ValueError('domain_id must be provided')
        if not container_id:
            raise ValueError('container_id must be provided')
        if json_patch_instructions is None:
            raise ValueError('json_patch_instructions must be provided')
        json_patch_instructions = [convert_model(x) for x in json_patch_instructions]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_data_product_domain',
        )
        headers.update(sdk_headers)

        params = {
            'container.id': container_id,
        }

        data = json.dumps(json_patch_instructions)
        headers['content-type'] = 'application/json-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['domain_id']
        path_param_values = self.encode_path_vars(domain_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/domains/{domain_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_data_product_by_domain(
        self,
        domain_id: str,
        container_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve all data products in a domain specified by id or any of it's subdomains.

        Retrieve all the data products tagged to the domain identified by id or any of
        it's subdomains.

        :param str domain_id: Domain id.
        :param str container_id: Container ID of the data product catalog.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductVersionCollection` object
        """

        if not domain_id:
            raise ValueError('domain_id must be provided')
        if not container_id:
            raise ValueError('container_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_data_product_by_domain',
        )
        headers.update(sdk_headers)

        params = {
            'container.id': container_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['domain_id']
        path_param_values = self.encode_path_vars(domain_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/domains/{domain_id}/data_products'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Bucket Services
    #########################

    def create_s3_bucket(
        self,
        is_shared: bool,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a new Bucket.

        Use this API to create a new S3 Bucket on an AWS Hosting.

        :param bool is_shared: Flag to specify whether the bucket is dedicated or
               shared.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BucketResponse` object
        """

        if is_shared is None:
            raise ValueError('is_shared must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_s3_bucket',
        )
        headers.update(sdk_headers)

        params = {
            'is_shared': is_shared,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/data_product_exchange/v1/bucket'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_s3_bucket_validation(
        self,
        bucket_name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Validate the Bucket Existence.

        Use this API to validate the bucket existence on an AWS hosting.

        :param str bucket_name: Name of the bucket to validate.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BucketValidationResponse` object
        """

        if not bucket_name:
            raise ValueError('bucket_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_s3_bucket_validation',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['bucket_name']
        path_param_values = self.encode_path_vars(bucket_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/bucket/validate/{bucket_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response


class GetDataProductDraftContractTermsEnums:
    """
    Enums for get_data_product_draft_contract_terms parameters.
    """

    class Accept(str, Enum):
        """
        The type of the response: application/odcs+yaml or application/json.
        """

        APPLICATION_ODCS_YAML = 'application/odcs+yaml'
        APPLICATION_JSON = 'application/json'


class ListDataProductReleasesEnums:
    """
    Enums for list_data_product_releases parameters.
    """

    class State(str, Enum):
        """
        Filter the list of data product versions by state. States are: available and
        retired. Default is "available","retired".
        """

        AVAILABLE = 'available'
        RETIRED = 'retired'


##############################################################################
# Models
##############################################################################


class AssetListAccessControl:
    """
    Access control object.

    :param str owner: (optional) The owner of the asset.
    """

    def __init__(
        self,
        *,
        owner: Optional[str] = None,
    ) -> None:
        """
        Initialize a AssetListAccessControl object.

        :param str owner: (optional) The owner of the asset.
        """
        self.owner = owner

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AssetListAccessControl':
        """Initialize a AssetListAccessControl object from a json dictionary."""
        args = {}
        if (owner := _dict.get('owner')) is not None:
            args['owner'] = owner
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AssetListAccessControl object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'owner') and self.owner is not None:
            _dict['owner'] = self.owner
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AssetListAccessControl object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AssetListAccessControl') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AssetListAccessControl') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AssetPartReference:
    """
    The asset represented in this part.

    :param str id: (optional) The unique identifier of the asset.
    :param str name: (optional) Asset name.
    :param ContainerReference container: Container reference.
    :param str type: (optional) The type of the asset.
    """

    def __init__(
        self,
        container: 'ContainerReference',
        *,
        id: Optional[str] = None,
        name: Optional[str] = None,
        type: Optional[str] = None,
    ) -> None:
        """
        Initialize a AssetPartReference object.

        :param ContainerReference container: Container reference.
        :param str id: (optional) The unique identifier of the asset.
        :param str name: (optional) Asset name.
        :param str type: (optional) The type of the asset.
        """
        self.id = id
        self.name = name
        self.container = container
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AssetPartReference':
        """Initialize a AssetPartReference object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (container := _dict.get('container')) is not None:
            args['container'] = ContainerReference.from_dict(container)
        else:
            raise ValueError('Required property \'container\' not present in AssetPartReference JSON')
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AssetPartReference object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'container') and self.container is not None:
            if isinstance(self.container, dict):
                _dict['container'] = self.container
            else:
                _dict['container'] = self.container.to_dict()
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AssetPartReference object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AssetPartReference') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AssetPartReference') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AssetPrototype:
    """
    New asset input properties.

    :param str id: (optional) The unique identifier of the asset.
    :param ContainerIdentity container: The identity schema for a IBM knowledge
          catalog container (catalog/project/space).
    """

    def __init__(
        self,
        container: 'ContainerIdentity',
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a AssetPrototype object.

        :param ContainerIdentity container: The identity schema for a IBM knowledge
               catalog container (catalog/project/space).
        :param str id: (optional) The unique identifier of the asset.
        """
        self.id = id
        self.container = container

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AssetPrototype':
        """Initialize a AssetPrototype object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (container := _dict.get('container')) is not None:
            args['container'] = ContainerIdentity.from_dict(container)
        else:
            raise ValueError('Required property \'container\' not present in AssetPrototype JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AssetPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'container') and self.container is not None:
            if isinstance(self.container, dict):
                _dict['container'] = self.container
            else:
                _dict['container'] = self.container.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AssetPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AssetPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AssetPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AssetReference:
    """
    The reference schema for a asset in a container.

    :param str id: (optional) The unique identifier of the asset.
    :param str name: (optional) Asset name.
    :param ContainerReference container: Container reference.
    """

    def __init__(
        self,
        container: 'ContainerReference',
        *,
        id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> None:
        """
        Initialize a AssetReference object.

        :param ContainerReference container: Container reference.
        :param str id: (optional) The unique identifier of the asset.
        :param str name: (optional) Asset name.
        """
        self.id = id
        self.name = name
        self.container = container

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AssetReference':
        """Initialize a AssetReference object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (container := _dict.get('container')) is not None:
            args['container'] = ContainerReference.from_dict(container)
        else:
            raise ValueError('Required property \'container\' not present in AssetReference JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AssetReference object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'container') and self.container is not None:
            if isinstance(self.container, dict):
                _dict['container'] = self.container
            else:
                _dict['container'] = self.container.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AssetReference object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AssetReference') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AssetReference') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BucketResponse:
    """
    BucketResponse to hold the Bucket response data.

    :param str bucket_name: (optional) Name of the Bucket.
    :param str bucket_location: (optional) Location of the Bucket stored.
    :param str role_arn: (optional) Role ARN.
    :param str bucket_type: (optional) Bucket Type.
    :param bool shared: (optional) Is Shared Bucket.
    """

    def __init__(
        self,
        *,
        bucket_name: Optional[str] = None,
        bucket_location: Optional[str] = None,
        role_arn: Optional[str] = None,
        bucket_type: Optional[str] = None,
        shared: Optional[bool] = None,
    ) -> None:
        """
        Initialize a BucketResponse object.

        :param str bucket_name: (optional) Name of the Bucket.
        :param str bucket_location: (optional) Location of the Bucket stored.
        :param str role_arn: (optional) Role ARN.
        :param str bucket_type: (optional) Bucket Type.
        :param bool shared: (optional) Is Shared Bucket.
        """
        self.bucket_name = bucket_name
        self.bucket_location = bucket_location
        self.role_arn = role_arn
        self.bucket_type = bucket_type
        self.shared = shared

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BucketResponse':
        """Initialize a BucketResponse object from a json dictionary."""
        args = {}
        if (bucket_name := _dict.get('bucket_name')) is not None:
            args['bucket_name'] = bucket_name
        if (bucket_location := _dict.get('bucket_location')) is not None:
            args['bucket_location'] = bucket_location
        if (role_arn := _dict.get('role_arn')) is not None:
            args['role_arn'] = role_arn
        if (bucket_type := _dict.get('bucket_type')) is not None:
            args['bucket_type'] = bucket_type
        if (shared := _dict.get('shared')) is not None:
            args['shared'] = shared
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BucketResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'bucket_name') and self.bucket_name is not None:
            _dict['bucket_name'] = self.bucket_name
        if hasattr(self, 'bucket_location') and self.bucket_location is not None:
            _dict['bucket_location'] = self.bucket_location
        if hasattr(self, 'role_arn') and self.role_arn is not None:
            _dict['role_arn'] = self.role_arn
        if hasattr(self, 'bucket_type') and self.bucket_type is not None:
            _dict['bucket_type'] = self.bucket_type
        if hasattr(self, 'shared') and self.shared is not None:
            _dict['shared'] = self.shared
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BucketResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BucketResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BucketResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BucketValidationResponse:
    """
    BucketValidationResponse to hold the bucket validation data.

    :param bool bucket_exists: (optional) Flag of bucket existence.
    """

    def __init__(
        self,
        *,
        bucket_exists: Optional[bool] = None,
    ) -> None:
        """
        Initialize a BucketValidationResponse object.

        :param bool bucket_exists: (optional) Flag of bucket existence.
        """
        self.bucket_exists = bucket_exists

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BucketValidationResponse':
        """Initialize a BucketValidationResponse object from a json dictionary."""
        args = {}
        if (bucket_exists := _dict.get('bucket_exists')) is not None:
            args['bucket_exists'] = bucket_exists
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BucketValidationResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'bucket_exists') and self.bucket_exists is not None:
            _dict['bucket_exists'] = self.bucket_exists
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BucketValidationResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BucketValidationResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BucketValidationResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ContainerIdentity:
    """
    The identity schema for a IBM knowledge catalog container (catalog/project/space).

    :param str id: Container identifier.
    """

    def __init__(
        self,
        id: str,
    ) -> None:
        """
        Initialize a ContainerIdentity object.

        :param str id: Container identifier.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContainerIdentity':
        """Initialize a ContainerIdentity object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in ContainerIdentity JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContainerIdentity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContainerIdentity object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ContainerIdentity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContainerIdentity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ContainerReference:
    """
    Container reference.

    :param str id: Container identifier.
    :param str type: Container type.
    """

    def __init__(
        self,
        id: str,
        type: str,
    ) -> None:
        """
        Initialize a ContainerReference object.

        :param str id: Container identifier.
        :param str type: Container type.
        """
        self.id = id
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContainerReference':
        """Initialize a ContainerReference object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in ContainerReference JSON')
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in ContainerReference JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContainerReference object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContainerReference object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ContainerReference') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContainerReference') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Container type.
        """

        CATALOG = 'catalog'
        PROJECT = 'project'



class ContractSchema:
    """
    Schema definition of the data asset.

    :param str name: (optional) Name of the schema or data asset part.
    :param str description: (optional) Description of the schema.
    :param str physical_type: (optional) MIME type or physical type.
    :param List[ContractSchemaProperty] properties: (optional) List of properties.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        physical_type: Optional[str] = None,
        properties: Optional[List['ContractSchemaProperty']] = None,
    ) -> None:
        """
        Initialize a ContractSchema object.

        :param str name: (optional) Name of the schema or data asset part.
        :param str description: (optional) Description of the schema.
        :param str physical_type: (optional) MIME type or physical type.
        :param List[ContractSchemaProperty] properties: (optional) List of
               properties.
        """
        self.name = name
        self.description = description
        self.physical_type = physical_type
        self.properties = properties

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContractSchema':
        """Initialize a ContractSchema object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (physical_type := _dict.get('physical_type')) is not None:
            args['physical_type'] = physical_type
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = [ContractSchemaProperty.from_dict(v) for v in properties]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContractSchema object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'physical_type') and self.physical_type is not None:
            _dict['physical_type'] = self.physical_type
        if hasattr(self, 'properties') and self.properties is not None:
            properties_list = []
            for v in self.properties:
                if isinstance(v, dict):
                    properties_list.append(v)
                else:
                    properties_list.append(v.to_dict())
            _dict['properties'] = properties_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContractSchema object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ContractSchema') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContractSchema') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ContractSchemaProperty:
    """
    Defines a property inside the schema.

    :param str name: Property name.
    :param ContractSchemaPropertyType type: (optional) Detailed type definition of a
          schema property.
    """

    def __init__(
        self,
        name: str,
        *,
        type: Optional['ContractSchemaPropertyType'] = None,
    ) -> None:
        """
        Initialize a ContractSchemaProperty object.

        :param str name: Property name.
        :param ContractSchemaPropertyType type: (optional) Detailed type definition
               of a schema property.
        """
        self.name = name
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContractSchemaProperty':
        """Initialize a ContractSchemaProperty object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in ContractSchemaProperty JSON')
        if (type := _dict.get('type')) is not None:
            args['type'] = ContractSchemaPropertyType.from_dict(type)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContractSchemaProperty object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            if isinstance(self.type, dict):
                _dict['type'] = self.type
            else:
                _dict['type'] = self.type.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContractSchemaProperty object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ContractSchemaProperty') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContractSchemaProperty') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ContractSchemaPropertyType:
    """
    Detailed type definition of a schema property.

    :param str type: (optional) Type of the field.
    :param str length: (optional) Length of the field as string.
    :param str scale: (optional) Scale of the field as string.
    :param str nullable: (optional) Is field nullable? true/false as string.
    :param str signed: (optional) Is field signed? true/false as string.
    :param str native_type: (optional) Native type of the field.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        length: Optional[str] = None,
        scale: Optional[str] = None,
        nullable: Optional[str] = None,
        signed: Optional[str] = None,
        native_type: Optional[str] = None,
    ) -> None:
        """
        Initialize a ContractSchemaPropertyType object.

        :param str type: (optional) Type of the field.
        :param str length: (optional) Length of the field as string.
        :param str scale: (optional) Scale of the field as string.
        :param str nullable: (optional) Is field nullable? true/false as string.
        :param str signed: (optional) Is field signed? true/false as string.
        :param str native_type: (optional) Native type of the field.
        """
        self.type = type
        self.length = length
        self.scale = scale
        self.nullable = nullable
        self.signed = signed
        self.native_type = native_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContractSchemaPropertyType':
        """Initialize a ContractSchemaPropertyType object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (length := _dict.get('length')) is not None:
            args['length'] = length
        if (scale := _dict.get('scale')) is not None:
            args['scale'] = scale
        if (nullable := _dict.get('nullable')) is not None:
            args['nullable'] = nullable
        if (signed := _dict.get('signed')) is not None:
            args['signed'] = signed
        if (native_type := _dict.get('native_type')) is not None:
            args['native_type'] = native_type
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContractSchemaPropertyType object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'length') and self.length is not None:
            _dict['length'] = self.length
        if hasattr(self, 'scale') and self.scale is not None:
            _dict['scale'] = self.scale
        if hasattr(self, 'nullable') and self.nullable is not None:
            _dict['nullable'] = self.nullable
        if hasattr(self, 'signed') and self.signed is not None:
            _dict['signed'] = self.signed
        if hasattr(self, 'native_type') and self.native_type is not None:
            _dict['native_type'] = self.native_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContractSchemaPropertyType object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ContractSchemaPropertyType') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContractSchemaPropertyType') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ContractTemplateCustomProperty:
    """
    Represents a custom property within the contract.

    :param str key: The name of the key. Names should be in camel case–the same as
          if they were permanent properties in the contract.
    :param str value: The value of the key.
    """

    def __init__(
        self,
        key: str,
        value: str,
    ) -> None:
        """
        Initialize a ContractTemplateCustomProperty object.

        :param str key: The name of the key. Names should be in camel case–the same
               as if they were permanent properties in the contract.
        :param str value: The value of the key.
        """
        self.key = key
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContractTemplateCustomProperty':
        """Initialize a ContractTemplateCustomProperty object from a json dictionary."""
        args = {}
        if (key := _dict.get('key')) is not None:
            args['key'] = key
        else:
            raise ValueError('Required property \'key\' not present in ContractTemplateCustomProperty JSON')
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        else:
            raise ValueError('Required property \'value\' not present in ContractTemplateCustomProperty JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContractTemplateCustomProperty object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContractTemplateCustomProperty object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ContractTemplateCustomProperty') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContractTemplateCustomProperty') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ContractTemplateOrganization:
    """
    Represents a user and their role in the contract.

    :param str user_id: The user ID associated with the contract.
    :param str role: The role of the user in the contract.
    """

    def __init__(
        self,
        user_id: str,
        role: str,
    ) -> None:
        """
        Initialize a ContractTemplateOrganization object.

        :param str user_id: The user ID associated with the contract.
        :param str role: The role of the user in the contract.
        """
        self.user_id = user_id
        self.role = role

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContractTemplateOrganization':
        """Initialize a ContractTemplateOrganization object from a json dictionary."""
        args = {}
        if (user_id := _dict.get('user_id')) is not None:
            args['user_id'] = user_id
        else:
            raise ValueError('Required property \'user_id\' not present in ContractTemplateOrganization JSON')
        if (role := _dict.get('role')) is not None:
            args['role'] = role
        else:
            raise ValueError('Required property \'role\' not present in ContractTemplateOrganization JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContractTemplateOrganization object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'user_id') and self.user_id is not None:
            _dict['user_id'] = self.user_id
        if hasattr(self, 'role') and self.role is not None:
            _dict['role'] = self.role
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContractTemplateOrganization object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ContractTemplateOrganization') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContractTemplateOrganization') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ContractTemplateSLA:
    """
    Represents the SLA details of the contract.

    :param str default_element: (optional) The default SLA element.
    :param List[ContractTemplateSLAProperty] properties: (optional) List of SLA
          properties and their values.
    """

    def __init__(
        self,
        *,
        default_element: Optional[str] = None,
        properties: Optional[List['ContractTemplateSLAProperty']] = None,
    ) -> None:
        """
        Initialize a ContractTemplateSLA object.

        :param str default_element: (optional) The default SLA element.
        :param List[ContractTemplateSLAProperty] properties: (optional) List of SLA
               properties and their values.
        """
        self.default_element = default_element
        self.properties = properties

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContractTemplateSLA':
        """Initialize a ContractTemplateSLA object from a json dictionary."""
        args = {}
        if (default_element := _dict.get('default_element')) is not None:
            args['default_element'] = default_element
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = [ContractTemplateSLAProperty.from_dict(v) for v in properties]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContractTemplateSLA object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'default_element') and self.default_element is not None:
            _dict['default_element'] = self.default_element
        if hasattr(self, 'properties') and self.properties is not None:
            properties_list = []
            for v in self.properties:
                if isinstance(v, dict):
                    properties_list.append(v)
                else:
                    properties_list.append(v.to_dict())
            _dict['properties'] = properties_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContractTemplateSLA object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ContractTemplateSLA') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContractTemplateSLA') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ContractTemplateSLAProperty:
    """
    Represents an SLA property and its value.

    :param str property: The SLA property name.
    :param str value: The value associated with the SLA property.
    """

    def __init__(
        self,
        property: str,
        value: str,
    ) -> None:
        """
        Initialize a ContractTemplateSLAProperty object.

        :param str property: The SLA property name.
        :param str value: The value associated with the SLA property.
        """
        self.property = property
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContractTemplateSLAProperty':
        """Initialize a ContractTemplateSLAProperty object from a json dictionary."""
        args = {}
        if (property := _dict.get('property')) is not None:
            args['property'] = property
        else:
            raise ValueError('Required property \'property\' not present in ContractTemplateSLAProperty JSON')
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        else:
            raise ValueError('Required property \'value\' not present in ContractTemplateSLAProperty JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContractTemplateSLAProperty object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'property') and self.property is not None:
            _dict['property'] = self.property
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContractTemplateSLAProperty object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ContractTemplateSLAProperty') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContractTemplateSLAProperty') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ContractTemplateSupportAndCommunication:
    """
    Represents a support and communication channel for the contract.

    :param str channel: The communication channel.
    :param str url: The URL associated with the communication channel.
    """

    def __init__(
        self,
        channel: str,
        url: str,
    ) -> None:
        """
        Initialize a ContractTemplateSupportAndCommunication object.

        :param str channel: The communication channel.
        :param str url: The URL associated with the communication channel.
        """
        self.channel = channel
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContractTemplateSupportAndCommunication':
        """Initialize a ContractTemplateSupportAndCommunication object from a json dictionary."""
        args = {}
        if (channel := _dict.get('channel')) is not None:
            args['channel'] = channel
        else:
            raise ValueError('Required property \'channel\' not present in ContractTemplateSupportAndCommunication JSON')
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        else:
            raise ValueError('Required property \'url\' not present in ContractTemplateSupportAndCommunication JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContractTemplateSupportAndCommunication object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'channel') and self.channel is not None:
            _dict['channel'] = self.channel
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContractTemplateSupportAndCommunication object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ContractTemplateSupportAndCommunication') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContractTemplateSupportAndCommunication') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ContractTerms:
    """
    Defines the complete structure of a contract terms.

    :param AssetReference asset: (optional) The reference schema for a asset in a
          container.
    :param str id: (optional) ID of the contract terms.
    :param List[ContractTermsDocument] documents: (optional) Collection of contract
          terms documents.
    :param str error_msg: (optional) An error message, if existing, relating to the
          contract terms.
    :param Overview overview: (optional) Overview details of a data contract.
    :param Description description: (optional) Description details of a data
          contract.
    :param List[ContractTemplateOrganization] organization: (optional) List of sub
          domains to be added within a domain.
    :param List[Roles] roles: (optional) List of roles associated with the contract.
    :param Pricing price: (optional) Represents the pricing details of the contract.
    :param List[ContractTemplateSLA] sla: (optional) Service Level Agreement
          details.
    :param List[ContractTemplateSupportAndCommunication] support_and_communication:
          (optional) Support and communication details for the contract.
    :param List[ContractTemplateCustomProperty] custom_properties: (optional) Custom
          properties that are not part of the standard contract.
    :param ContractTest contract_test: (optional) Contains the contract test status
          and related metadata.
    :param List[ContractSchema] schema: (optional) Schema details of the data asset.
    """

    def __init__(
        self,
        *,
        asset: Optional['AssetReference'] = None,
        id: Optional[str] = None,
        documents: Optional[List['ContractTermsDocument']] = None,
        error_msg: Optional[str] = None,
        overview: Optional['Overview'] = None,
        description: Optional['Description'] = None,
        organization: Optional[List['ContractTemplateOrganization']] = None,
        roles: Optional[List['Roles']] = None,
        price: Optional['Pricing'] = None,
        sla: Optional[List['ContractTemplateSLA']] = None,
        support_and_communication: Optional[List['ContractTemplateSupportAndCommunication']] = None,
        custom_properties: Optional[List['ContractTemplateCustomProperty']] = None,
        contract_test: Optional['ContractTest'] = None,
        schema: Optional[List['ContractSchema']] = None,
    ) -> None:
        """
        Initialize a ContractTerms object.

        :param AssetReference asset: (optional) The reference schema for a asset in
               a container.
        :param str id: (optional) ID of the contract terms.
        :param List[ContractTermsDocument] documents: (optional) Collection of
               contract terms documents.
        :param str error_msg: (optional) An error message, if existing, relating to
               the contract terms.
        :param Overview overview: (optional) Overview details of a data contract.
        :param Description description: (optional) Description details of a data
               contract.
        :param List[ContractTemplateOrganization] organization: (optional) List of
               sub domains to be added within a domain.
        :param List[Roles] roles: (optional) List of roles associated with the
               contract.
        :param Pricing price: (optional) Represents the pricing details of the
               contract.
        :param List[ContractTemplateSLA] sla: (optional) Service Level Agreement
               details.
        :param List[ContractTemplateSupportAndCommunication]
               support_and_communication: (optional) Support and communication details for
               the contract.
        :param List[ContractTemplateCustomProperty] custom_properties: (optional)
               Custom properties that are not part of the standard contract.
        :param ContractTest contract_test: (optional) Contains the contract test
               status and related metadata.
        :param List[ContractSchema] schema: (optional) Schema details of the data
               asset.
        """
        self.asset = asset
        self.id = id
        self.documents = documents
        self.error_msg = error_msg
        self.overview = overview
        self.description = description
        self.organization = organization
        self.roles = roles
        self.price = price
        self.sla = sla
        self.support_and_communication = support_and_communication
        self.custom_properties = custom_properties
        self.contract_test = contract_test
        self.schema = schema

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContractTerms':
        """Initialize a ContractTerms object from a json dictionary."""
        args = {}
        if (asset := _dict.get('asset')) is not None:
            args['asset'] = AssetReference.from_dict(asset)
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (documents := _dict.get('documents')) is not None:
            args['documents'] = [ContractTermsDocument.from_dict(v) for v in documents]
        if (error_msg := _dict.get('error_msg')) is not None:
            args['error_msg'] = error_msg
        if (overview := _dict.get('overview')) is not None:
            args['overview'] = Overview.from_dict(overview)
        if (description := _dict.get('description')) is not None:
            args['description'] = Description.from_dict(description)
        if (organization := _dict.get('organization')) is not None:
            args['organization'] = [ContractTemplateOrganization.from_dict(v) for v in organization]
        if (roles := _dict.get('roles')) is not None:
            args['roles'] = [Roles.from_dict(v) for v in roles]
        if (price := _dict.get('price')) is not None:
            args['price'] = Pricing.from_dict(price)
        if (sla := _dict.get('sla')) is not None:
            args['sla'] = [ContractTemplateSLA.from_dict(v) for v in sla]
        if (support_and_communication := _dict.get('support_and_communication')) is not None:
            args['support_and_communication'] = [ContractTemplateSupportAndCommunication.from_dict(v) for v in support_and_communication]
        if (custom_properties := _dict.get('custom_properties')) is not None:
            args['custom_properties'] = [ContractTemplateCustomProperty.from_dict(v) for v in custom_properties]
        if (contract_test := _dict.get('contract_test')) is not None:
            args['contract_test'] = ContractTest.from_dict(contract_test)
        if (schema := _dict.get('schema')) is not None:
            args['schema'] = [ContractSchema.from_dict(v) for v in schema]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContractTerms object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'asset') and self.asset is not None:
            if isinstance(self.asset, dict):
                _dict['asset'] = self.asset
            else:
                _dict['asset'] = self.asset.to_dict()
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'documents') and self.documents is not None:
            documents_list = []
            for v in self.documents:
                if isinstance(v, dict):
                    documents_list.append(v)
                else:
                    documents_list.append(v.to_dict())
            _dict['documents'] = documents_list
        if hasattr(self, 'error_msg') and self.error_msg is not None:
            _dict['error_msg'] = self.error_msg
        if hasattr(self, 'overview') and self.overview is not None:
            if isinstance(self.overview, dict):
                _dict['overview'] = self.overview
            else:
                _dict['overview'] = self.overview.to_dict()
        if hasattr(self, 'description') and self.description is not None:
            if isinstance(self.description, dict):
                _dict['description'] = self.description
            else:
                _dict['description'] = self.description.to_dict()
        if hasattr(self, 'organization') and self.organization is not None:
            organization_list = []
            for v in self.organization:
                if isinstance(v, dict):
                    organization_list.append(v)
                else:
                    organization_list.append(v.to_dict())
            _dict['organization'] = organization_list
        if hasattr(self, 'roles') and self.roles is not None:
            roles_list = []
            for v in self.roles:
                if isinstance(v, dict):
                    roles_list.append(v)
                else:
                    roles_list.append(v.to_dict())
            _dict['roles'] = roles_list
        if hasattr(self, 'price') and self.price is not None:
            if isinstance(self.price, dict):
                _dict['price'] = self.price
            else:
                _dict['price'] = self.price.to_dict()
        if hasattr(self, 'sla') and self.sla is not None:
            sla_list = []
            for v in self.sla:
                if isinstance(v, dict):
                    sla_list.append(v)
                else:
                    sla_list.append(v.to_dict())
            _dict['sla'] = sla_list
        if hasattr(self, 'support_and_communication') and self.support_and_communication is not None:
            support_and_communication_list = []
            for v in self.support_and_communication:
                if isinstance(v, dict):
                    support_and_communication_list.append(v)
                else:
                    support_and_communication_list.append(v.to_dict())
            _dict['support_and_communication'] = support_and_communication_list
        if hasattr(self, 'custom_properties') and self.custom_properties is not None:
            custom_properties_list = []
            for v in self.custom_properties:
                if isinstance(v, dict):
                    custom_properties_list.append(v)
                else:
                    custom_properties_list.append(v.to_dict())
            _dict['custom_properties'] = custom_properties_list
        if hasattr(self, 'contract_test') and self.contract_test is not None:
            if isinstance(self.contract_test, dict):
                _dict['contract_test'] = self.contract_test
            else:
                _dict['contract_test'] = self.contract_test.to_dict()
        if hasattr(self, 'schema') and self.schema is not None:
            schema_list = []
            for v in self.schema:
                if isinstance(v, dict):
                    schema_list.append(v)
                else:
                    schema_list.append(v.to_dict())
            _dict['schema'] = schema_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContractTerms object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ContractTerms') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContractTerms') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ContractTermsDocument:
    """
    Standard contract terms document, which is used for get and list contract terms
    responses.

    :param str url: (optional) URL that can be used to retrieve the contract
          document.
    :param str type: Type of the contract document.
    :param str name: Name of the contract document.
    :param str id: Id uniquely identifying this document within the contract terms
          instance.
    :param ContractTermsDocumentAttachment attachment: (optional) Attachment
          associated witht the document.
    :param str upload_url: (optional) URL which can be used to upload document file.
    """

    def __init__(
        self,
        type: str,
        name: str,
        id: str,
        *,
        url: Optional[str] = None,
        attachment: Optional['ContractTermsDocumentAttachment'] = None,
        upload_url: Optional[str] = None,
    ) -> None:
        """
        Initialize a ContractTermsDocument object.

        :param str type: Type of the contract document.
        :param str name: Name of the contract document.
        :param str id: Id uniquely identifying this document within the contract
               terms instance.
        :param str url: (optional) URL that can be used to retrieve the contract
               document.
        :param ContractTermsDocumentAttachment attachment: (optional) Attachment
               associated witht the document.
        :param str upload_url: (optional) URL which can be used to upload document
               file.
        """
        self.url = url
        self.type = type
        self.name = name
        self.id = id
        self.attachment = attachment
        self.upload_url = upload_url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContractTermsDocument':
        """Initialize a ContractTermsDocument object from a json dictionary."""
        args = {}
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in ContractTermsDocument JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in ContractTermsDocument JSON')
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in ContractTermsDocument JSON')
        if (attachment := _dict.get('attachment')) is not None:
            args['attachment'] = ContractTermsDocumentAttachment.from_dict(attachment)
        if (upload_url := _dict.get('upload_url')) is not None:
            args['upload_url'] = upload_url
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContractTermsDocument object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'attachment') and self.attachment is not None:
            if isinstance(self.attachment, dict):
                _dict['attachment'] = self.attachment
            else:
                _dict['attachment'] = self.attachment.to_dict()
        if hasattr(self, 'upload_url') and self.upload_url is not None:
            _dict['upload_url'] = self.upload_url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContractTermsDocument object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ContractTermsDocument') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContractTermsDocument') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Type of the contract document.
        """

        TERMS_AND_CONDITIONS = 'terms_and_conditions'
        SLA = 'sla'



class ContractTermsDocumentAttachment:
    """
    Attachment associated witht the document.

    :param str id: (optional) Id representing the corresponding attachment.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a ContractTermsDocumentAttachment object.

        :param str id: (optional) Id representing the corresponding attachment.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContractTermsDocumentAttachment':
        """Initialize a ContractTermsDocumentAttachment object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContractTermsDocumentAttachment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContractTermsDocumentAttachment object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ContractTermsDocumentAttachment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContractTermsDocumentAttachment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ContractTermsMoreInfo:
    """
    List of links to sources that provide more details on the dataset.

    :param str type: Type of Source Link.
    :param str url: Link to source that provide more details on the dataset.
    """

    def __init__(
        self,
        type: str,
        url: str,
    ) -> None:
        """
        Initialize a ContractTermsMoreInfo object.

        :param str type: Type of Source Link.
        :param str url: Link to source that provide more details on the dataset.
        """
        self.type = type
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContractTermsMoreInfo':
        """Initialize a ContractTermsMoreInfo object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in ContractTermsMoreInfo JSON')
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        else:
            raise ValueError('Required property \'url\' not present in ContractTermsMoreInfo JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContractTermsMoreInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContractTermsMoreInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ContractTermsMoreInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContractTermsMoreInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ContractTest:
    """
    Contains the contract test status and related metadata.

    :param str status: Status of the contract test (pass or fail).
    :param str last_tested_time: Timestamp of when the contract was last tested.
    :param str message: (optional) Optional message or details about the contract
          test.
    """

    def __init__(
        self,
        status: str,
        last_tested_time: str,
        *,
        message: Optional[str] = None,
    ) -> None:
        """
        Initialize a ContractTest object.

        :param str status: Status of the contract test (pass or fail).
        :param str last_tested_time: Timestamp of when the contract was last
               tested.
        :param str message: (optional) Optional message or details about the
               contract test.
        """
        self.status = status
        self.last_tested_time = last_tested_time
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContractTest':
        """Initialize a ContractTest object from a json dictionary."""
        args = {}
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in ContractTest JSON')
        if (last_tested_time := _dict.get('last_tested_time')) is not None:
            args['last_tested_time'] = last_tested_time
        else:
            raise ValueError('Required property \'last_tested_time\' not present in ContractTest JSON')
        if (message := _dict.get('message')) is not None:
            args['message'] = message
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContractTest object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'last_tested_time') and self.last_tested_time is not None:
            _dict['last_tested_time'] = self.last_tested_time
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContractTest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ContractTest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContractTest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        Status of the contract test (pass or fail).
        """

        PASS = 'pass'
        FAIL = 'fail'



class DataAssetRelationship:
    """
    Data members for visualization process.

    :param Visualization visualization: (optional) Data members for visualization.
    :param AssetReference asset: The reference schema for a asset in a container.
    :param AssetReference related_asset: The reference schema for a asset in a
          container.
    :param ErrorMessage error: (optional) Contains the code and details.
    """

    def __init__(
        self,
        asset: 'AssetReference',
        related_asset: 'AssetReference',
        *,
        visualization: Optional['Visualization'] = None,
        error: Optional['ErrorMessage'] = None,
    ) -> None:
        """
        Initialize a DataAssetRelationship object.

        :param AssetReference asset: The reference schema for a asset in a
               container.
        :param AssetReference related_asset: The reference schema for a asset in a
               container.
        :param Visualization visualization: (optional) Data members for
               visualization.
        :param ErrorMessage error: (optional) Contains the code and details.
        """
        self.visualization = visualization
        self.asset = asset
        self.related_asset = related_asset
        self.error = error

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataAssetRelationship':
        """Initialize a DataAssetRelationship object from a json dictionary."""
        args = {}
        if (visualization := _dict.get('visualization')) is not None:
            args['visualization'] = Visualization.from_dict(visualization)
        if (asset := _dict.get('asset')) is not None:
            args['asset'] = AssetReference.from_dict(asset)
        else:
            raise ValueError('Required property \'asset\' not present in DataAssetRelationship JSON')
        if (related_asset := _dict.get('related_asset')) is not None:
            args['related_asset'] = AssetReference.from_dict(related_asset)
        else:
            raise ValueError('Required property \'related_asset\' not present in DataAssetRelationship JSON')
        if (error := _dict.get('error')) is not None:
            args['error'] = ErrorMessage.from_dict(error)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataAssetRelationship object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'visualization') and self.visualization is not None:
            if isinstance(self.visualization, dict):
                _dict['visualization'] = self.visualization
            else:
                _dict['visualization'] = self.visualization.to_dict()
        if hasattr(self, 'asset') and self.asset is not None:
            if isinstance(self.asset, dict):
                _dict['asset'] = self.asset
            else:
                _dict['asset'] = self.asset.to_dict()
        if hasattr(self, 'related_asset') and self.related_asset is not None:
            if isinstance(self.related_asset, dict):
                _dict['related_asset'] = self.related_asset
            else:
                _dict['related_asset'] = self.related_asset.to_dict()
        if hasattr(self, 'error') and self.error is not None:
            if isinstance(self.error, dict):
                _dict['error'] = self.error
            else:
                _dict['error'] = self.error.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataAssetRelationship object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataAssetRelationship') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataAssetRelationship') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataAssetVisualizationRes:
    """
    Data relationships for the visualization process response.

    :param List[DataAssetRelationship] results: (optional) Data asset Ids and their
          related asset Ids.
    """

    def __init__(
        self,
        *,
        results: Optional[List['DataAssetRelationship']] = None,
    ) -> None:
        """
        Initialize a DataAssetVisualizationRes object.

        :param List[DataAssetRelationship] results: (optional) Data asset Ids and
               their related asset Ids.
        """
        self.results = results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataAssetVisualizationRes':
        """Initialize a DataAssetVisualizationRes object from a json dictionary."""
        args = {}
        if (results := _dict.get('results')) is not None:
            args['results'] = [DataAssetRelationship.from_dict(v) for v in results]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataAssetVisualizationRes object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'results') and self.results is not None:
            results_list = []
            for v in self.results:
                if isinstance(v, dict):
                    results_list.append(v)
                else:
                    results_list.append(v.to_dict())
            _dict['results'] = results_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataAssetVisualizationRes object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataAssetVisualizationRes') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataAssetVisualizationRes') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProduct:
    """
    Data Product.

    :param str id: Data product identifier.
    :param DataProductDraftVersionRelease release: (optional) A data product draft
          version object.
    :param ContainerReference container: Container reference.
    :param str name: (optional) Data product name.
    :param DataProductVersionSummary latest_release: (optional) Summary of Data
          Product Version object.
    :param List[DataProductVersionSummary] drafts: (optional) List of draft
          summaries of this data product.
    """

    def __init__(
        self,
        id: str,
        container: 'ContainerReference',
        *,
        release: Optional['DataProductDraftVersionRelease'] = None,
        name: Optional[str] = None,
        latest_release: Optional['DataProductVersionSummary'] = None,
        drafts: Optional[List['DataProductVersionSummary']] = None,
    ) -> None:
        """
        Initialize a DataProduct object.

        :param str id: Data product identifier.
        :param ContainerReference container: Container reference.
        :param DataProductDraftVersionRelease release: (optional) A data product
               draft version object.
        :param str name: (optional) Data product name.
        :param DataProductVersionSummary latest_release: (optional) Summary of Data
               Product Version object.
        :param List[DataProductVersionSummary] drafts: (optional) List of draft
               summaries of this data product.
        """
        self.id = id
        self.release = release
        self.container = container
        self.name = name
        self.latest_release = latest_release
        self.drafts = drafts

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProduct':
        """Initialize a DataProduct object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in DataProduct JSON')
        if (release := _dict.get('release')) is not None:
            args['release'] = DataProductDraftVersionRelease.from_dict(release)
        if (container := _dict.get('container')) is not None:
            args['container'] = ContainerReference.from_dict(container)
        else:
            raise ValueError('Required property \'container\' not present in DataProduct JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (latest_release := _dict.get('latest_release')) is not None:
            args['latest_release'] = DataProductVersionSummary.from_dict(latest_release)
        if (drafts := _dict.get('drafts')) is not None:
            args['drafts'] = [DataProductVersionSummary.from_dict(v) for v in drafts]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProduct object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'release') and self.release is not None:
            if isinstance(self.release, dict):
                _dict['release'] = self.release
            else:
                _dict['release'] = self.release.to_dict()
        if hasattr(self, 'container') and self.container is not None:
            if isinstance(self.container, dict):
                _dict['container'] = self.container
            else:
                _dict['container'] = self.container.to_dict()
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'latest_release') and self.latest_release is not None:
            if isinstance(self.latest_release, dict):
                _dict['latest_release'] = self.latest_release
            else:
                _dict['latest_release'] = self.latest_release.to_dict()
        if hasattr(self, 'drafts') and self.drafts is not None:
            drafts_list = []
            for v in self.drafts:
                if isinstance(v, dict):
                    drafts_list.append(v)
                else:
                    drafts_list.append(v.to_dict())
            _dict['drafts'] = drafts_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProduct object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProduct') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProduct') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductCollection:
    """
    A collection of data product summaries.

    :param int limit: Set a limit on the number of results returned.
    :param FirstPage first: First page in the collection.
    :param NextPage next: (optional) Next page in the collection.
    :param int total_results: (optional) Indicates the total number of results
          returned.
    :param List[DataProductSummary] data_products: Collection of data product
          summaries.
    """

    def __init__(
        self,
        limit: int,
        first: 'FirstPage',
        data_products: List['DataProductSummary'],
        *,
        next: Optional['NextPage'] = None,
        total_results: Optional[int] = None,
    ) -> None:
        """
        Initialize a DataProductCollection object.

        :param int limit: Set a limit on the number of results returned.
        :param FirstPage first: First page in the collection.
        :param List[DataProductSummary] data_products: Collection of data product
               summaries.
        :param NextPage next: (optional) Next page in the collection.
        :param int total_results: (optional) Indicates the total number of results
               returned.
        """
        self.limit = limit
        self.first = first
        self.next = next
        self.total_results = total_results
        self.data_products = data_products

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductCollection':
        """Initialize a DataProductCollection object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in DataProductCollection JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = FirstPage.from_dict(first)
        else:
            raise ValueError('Required property \'first\' not present in DataProductCollection JSON')
        if (next := _dict.get('next')) is not None:
            args['next'] = NextPage.from_dict(next)
        if (total_results := _dict.get('total_results')) is not None:
            args['total_results'] = total_results
        if (data_products := _dict.get('data_products')) is not None:
            args['data_products'] = [DataProductSummary.from_dict(v) for v in data_products]
        else:
            raise ValueError('Required property \'data_products\' not present in DataProductCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'total_results') and self.total_results is not None:
            _dict['total_results'] = self.total_results
        if hasattr(self, 'data_products') and self.data_products is not None:
            data_products_list = []
            for v in self.data_products:
                if isinstance(v, dict):
                    data_products_list.append(v)
                else:
                    data_products_list.append(v.to_dict())
            _dict['data_products'] = data_products_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductContractTemplate:
    """
    Defines the complete structure of a contract template.

    :param ContainerReference container: Container reference.
    :param str id: (optional) The identifier of the data product contract template.
    :param str name: (optional) The name of the contract template.
    :param ErrorMessage error: (optional) Contains the code and details.
    :param ContractTerms contract_terms: (optional) Defines the complete structure
          of a contract terms.
    """

    def __init__(
        self,
        container: 'ContainerReference',
        *,
        id: Optional[str] = None,
        name: Optional[str] = None,
        error: Optional['ErrorMessage'] = None,
        contract_terms: Optional['ContractTerms'] = None,
    ) -> None:
        """
        Initialize a DataProductContractTemplate object.

        :param ContainerReference container: Container reference.
        :param str id: (optional) The identifier of the data product contract
               template.
        :param str name: (optional) The name of the contract template.
        :param ErrorMessage error: (optional) Contains the code and details.
        :param ContractTerms contract_terms: (optional) Defines the complete
               structure of a contract terms.
        """
        self.container = container
        self.id = id
        self.name = name
        self.error = error
        self.contract_terms = contract_terms

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductContractTemplate':
        """Initialize a DataProductContractTemplate object from a json dictionary."""
        args = {}
        if (container := _dict.get('container')) is not None:
            args['container'] = ContainerReference.from_dict(container)
        else:
            raise ValueError('Required property \'container\' not present in DataProductContractTemplate JSON')
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (error := _dict.get('error')) is not None:
            args['error'] = ErrorMessage.from_dict(error)
        if (contract_terms := _dict.get('contract_terms')) is not None:
            args['contract_terms'] = ContractTerms.from_dict(contract_terms)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductContractTemplate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'container') and self.container is not None:
            if isinstance(self.container, dict):
                _dict['container'] = self.container
            else:
                _dict['container'] = self.container.to_dict()
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'error') and self.error is not None:
            if isinstance(self.error, dict):
                _dict['error'] = self.error
            else:
                _dict['error'] = self.error.to_dict()
        if hasattr(self, 'contract_terms') and self.contract_terms is not None:
            if isinstance(self.contract_terms, dict):
                _dict['contract_terms'] = self.contract_terms
            else:
                _dict['contract_terms'] = self.contract_terms.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductContractTemplate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductContractTemplate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductContractTemplate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductContractTemplateCollection:
    """
    A collection of data product contract templates.

    :param List[DataProductContractTemplate] contract_templates: Collection of data
          product contract templates.
    """

    def __init__(
        self,
        contract_templates: List['DataProductContractTemplate'],
    ) -> None:
        """
        Initialize a DataProductContractTemplateCollection object.

        :param List[DataProductContractTemplate] contract_templates: Collection of
               data product contract templates.
        """
        self.contract_templates = contract_templates

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductContractTemplateCollection':
        """Initialize a DataProductContractTemplateCollection object from a json dictionary."""
        args = {}
        if (contract_templates := _dict.get('contract_templates')) is not None:
            args['contract_templates'] = [DataProductContractTemplate.from_dict(v) for v in contract_templates]
        else:
            raise ValueError('Required property \'contract_templates\' not present in DataProductContractTemplateCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductContractTemplateCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'contract_templates') and self.contract_templates is not None:
            contract_templates_list = []
            for v in self.contract_templates:
                if isinstance(v, dict):
                    contract_templates_list.append(v)
                else:
                    contract_templates_list.append(v.to_dict())
            _dict['contract_templates'] = contract_templates_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductContractTemplateCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductContractTemplateCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductContractTemplateCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductCustomWorkflowDefinition:
    """
    A custom workflow definition to be used to create a workflow to approve a data product
    subscription.

    :param str id: (optional) ID of a workflow definition.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a DataProductCustomWorkflowDefinition object.

        :param str id: (optional) ID of a workflow definition.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductCustomWorkflowDefinition':
        """Initialize a DataProductCustomWorkflowDefinition object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductCustomWorkflowDefinition object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductCustomWorkflowDefinition object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductCustomWorkflowDefinition') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductCustomWorkflowDefinition') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductDomain:
    """
    The data product domain.

    :param ContainerReference container: Container reference.
    :param str trace: (optional) The id to trace the failed domain creations.
    :param List[ErrorModelResource] errors: (optional) Set of errors on the sub
          domain creation.
    :param str name: (optional) The name of the data product domain.
    :param str description: (optional) The description of the data product domain.
    :param str id: (optional) The identifier of the data product domain.
    :param MemberRolesSchema member_roles: (optional) Member roles of a
          corresponding asset.
    :param PropertiesSchema properties: (optional) Properties of the corresponding
          asset.
    :param List[InitializeSubDomain] sub_domains: (optional) List of sub domains to
          be added within a domain.
    """

    def __init__(
        self,
        container: 'ContainerReference',
        *,
        trace: Optional[str] = None,
        errors: Optional[List['ErrorModelResource']] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        member_roles: Optional['MemberRolesSchema'] = None,
        properties: Optional['PropertiesSchema'] = None,
        sub_domains: Optional[List['InitializeSubDomain']] = None,
    ) -> None:
        """
        Initialize a DataProductDomain object.

        :param ContainerReference container: Container reference.
        :param str trace: (optional) The id to trace the failed domain creations.
        :param List[ErrorModelResource] errors: (optional) Set of errors on the sub
               domain creation.
        :param str name: (optional) The name of the data product domain.
        :param str description: (optional) The description of the data product
               domain.
        :param str id: (optional) The identifier of the data product domain.
        :param MemberRolesSchema member_roles: (optional) Member roles of a
               corresponding asset.
        :param PropertiesSchema properties: (optional) Properties of the
               corresponding asset.
        :param List[InitializeSubDomain] sub_domains: (optional) List of sub
               domains to be added within a domain.
        """
        self.container = container
        self.trace = trace
        self.errors = errors
        self.name = name
        self.description = description
        self.id = id
        self.member_roles = member_roles
        self.properties = properties
        self.sub_domains = sub_domains

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductDomain':
        """Initialize a DataProductDomain object from a json dictionary."""
        args = {}
        if (container := _dict.get('container')) is not None:
            args['container'] = ContainerReference.from_dict(container)
        else:
            raise ValueError('Required property \'container\' not present in DataProductDomain JSON')
        if (trace := _dict.get('trace')) is not None:
            args['trace'] = trace
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = [ErrorModelResource.from_dict(v) for v in errors]
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (member_roles := _dict.get('member_roles')) is not None:
            args['member_roles'] = MemberRolesSchema.from_dict(member_roles)
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = PropertiesSchema.from_dict(properties)
        if (sub_domains := _dict.get('sub_domains')) is not None:
            args['sub_domains'] = [InitializeSubDomain.from_dict(v) for v in sub_domains]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductDomain object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'container') and self.container is not None:
            if isinstance(self.container, dict):
                _dict['container'] = self.container
            else:
                _dict['container'] = self.container.to_dict()
        if hasattr(self, 'trace') and self.trace is not None:
            _dict['trace'] = self.trace
        if hasattr(self, 'errors') and self.errors is not None:
            errors_list = []
            for v in self.errors:
                if isinstance(v, dict):
                    errors_list.append(v)
                else:
                    errors_list.append(v.to_dict())
            _dict['errors'] = errors_list
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'member_roles') and self.member_roles is not None:
            if isinstance(self.member_roles, dict):
                _dict['member_roles'] = self.member_roles
            else:
                _dict['member_roles'] = self.member_roles.to_dict()
        if hasattr(self, 'properties') and self.properties is not None:
            if isinstance(self.properties, dict):
                _dict['properties'] = self.properties
            else:
                _dict['properties'] = self.properties.to_dict()
        if hasattr(self, 'sub_domains') and self.sub_domains is not None:
            sub_domains_list = []
            for v in self.sub_domains:
                if isinstance(v, dict):
                    sub_domains_list.append(v)
                else:
                    sub_domains_list.append(v.to_dict())
            _dict['sub_domains'] = sub_domains_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductDomain object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductDomain') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductDomain') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductDomainCollection:
    """
    A collection of data product domains.

    :param List[DataProductDomain] domains: Collection of data product domains.
    """

    def __init__(
        self,
        domains: List['DataProductDomain'],
    ) -> None:
        """
        Initialize a DataProductDomainCollection object.

        :param List[DataProductDomain] domains: Collection of data product domains.
        """
        self.domains = domains

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductDomainCollection':
        """Initialize a DataProductDomainCollection object from a json dictionary."""
        args = {}
        if (domains := _dict.get('domains')) is not None:
            args['domains'] = [DataProductDomain.from_dict(v) for v in domains]
        else:
            raise ValueError('Required property \'domains\' not present in DataProductDomainCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductDomainCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'domains') and self.domains is not None:
            domains_list = []
            for v in self.domains:
                if isinstance(v, dict):
                    domains_list.append(v)
                else:
                    domains_list.append(v.to_dict())
            _dict['domains'] = domains_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductDomainCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductDomainCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductDomainCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductDraft:
    """
    Data Product version draft.

    :param str version: The data product version number.
    :param str state: The state of the data product version.
    :param DataProductDraftDataProduct data_product: Data product reference.
    :param str name: The name of the data product version. A name can contain
          letters, numbers, understores, dashes, spaces or periods. Names are mutable and
          reusable.
    :param str description: The description of the data product version.
    :param List[str] tags: Tags on the data product.
    :param List[UseCase] use_cases: (optional) A list of use cases associated with
          the data product version.
    :param List[str] types: Types of parts on the data product.
    :param List[ContractTerms] contract_terms: Contract terms binding various
          aspects of the data product.
    :param Domain domain: Domain that the data product version belongs to. If this
          is the first version of a data product, this field is required. If this is a new
          version of an existing data product, the domain will default to the domain of
          the previous version of the data product.
    :param List[DataProductPart] parts_out: The outgoing parts of this data product
          version to be delivered to consumers. If this is the first version of a data
          product, this field defaults to an empty list. If this is a new version of an
          existing data product, the data product parts will default to the parts list
          from the previous version of the data product.
    :param DataProductWorkflows workflows: (optional) The workflows associated with
          the data product version.
    :param bool dataview_enabled: (optional) Indicates whether the dataView has
          enabled for data product.
    :param str comments: (optional) Comments by a producer that are provided either
          at the time of data product version creation or retiring.
    :param AssetListAccessControl access_control: (optional) Access control object.
    :param datetime last_updated_at: (optional) Timestamp of last asset update.
    :param bool is_restricted: Indicates whether the data product is restricted or
          not. A restricted data product indicates that orders of the data product
          requires explicit approval before data is delivered.
    :param str id: The identifier of the data product version.
    :param AssetReference asset: The reference schema for a asset in a container.
    :param str published_by: (optional) The user who published this data product
          version.
    :param datetime published_at: (optional) The time when this data product version
          was published.
    :param str created_by: The creator of this data product version.
    :param datetime created_at: The time when this data product version was created.
    :param dict properties: (optional) Metadata properties on data products.
    :param List[DataAssetRelationship] visualization_errors: (optional) Errors
          encountered during the visualization creation process.
    """

    def __init__(
        self,
        version: str,
        state: str,
        data_product: 'DataProductDraftDataProduct',
        name: str,
        description: str,
        tags: List[str],
        types: List[str],
        contract_terms: List['ContractTerms'],
        domain: 'Domain',
        parts_out: List['DataProductPart'],
        is_restricted: bool,
        id: str,
        asset: 'AssetReference',
        created_by: str,
        created_at: datetime,
        *,
        use_cases: Optional[List['UseCase']] = None,
        workflows: Optional['DataProductWorkflows'] = None,
        dataview_enabled: Optional[bool] = None,
        comments: Optional[str] = None,
        access_control: Optional['AssetListAccessControl'] = None,
        last_updated_at: Optional[datetime] = None,
        published_by: Optional[str] = None,
        published_at: Optional[datetime] = None,
        properties: Optional[dict] = None,
        visualization_errors: Optional[List['DataAssetRelationship']] = None,
    ) -> None:
        """
        Initialize a DataProductDraft object.

        :param str version: The data product version number.
        :param str state: The state of the data product version.
        :param DataProductDraftDataProduct data_product: Data product reference.
        :param str name: The name of the data product version. A name can contain
               letters, numbers, understores, dashes, spaces or periods. Names are mutable
               and reusable.
        :param str description: The description of the data product version.
        :param List[str] tags: Tags on the data product.
        :param List[str] types: Types of parts on the data product.
        :param List[ContractTerms] contract_terms: Contract terms binding various
               aspects of the data product.
        :param Domain domain: Domain that the data product version belongs to. If
               this is the first version of a data product, this field is required. If
               this is a new version of an existing data product, the domain will default
               to the domain of the previous version of the data product.
        :param List[DataProductPart] parts_out: The outgoing parts of this data
               product version to be delivered to consumers. If this is the first version
               of a data product, this field defaults to an empty list. If this is a new
               version of an existing data product, the data product parts will default to
               the parts list from the previous version of the data product.
        :param bool is_restricted: Indicates whether the data product is restricted
               or not. A restricted data product indicates that orders of the data product
               requires explicit approval before data is delivered.
        :param str id: The identifier of the data product version.
        :param AssetReference asset: The reference schema for a asset in a
               container.
        :param str created_by: The creator of this data product version.
        :param datetime created_at: The time when this data product version was
               created.
        :param List[UseCase] use_cases: (optional) A list of use cases associated
               with the data product version.
        :param DataProductWorkflows workflows: (optional) The workflows associated
               with the data product version.
        :param bool dataview_enabled: (optional) Indicates whether the dataView has
               enabled for data product.
        :param str comments: (optional) Comments by a producer that are provided
               either at the time of data product version creation or retiring.
        :param AssetListAccessControl access_control: (optional) Access control
               object.
        :param datetime last_updated_at: (optional) Timestamp of last asset update.
        :param str published_by: (optional) The user who published this data
               product version.
        :param datetime published_at: (optional) The time when this data product
               version was published.
        :param dict properties: (optional) Metadata properties on data products.
        :param List[DataAssetRelationship] visualization_errors: (optional) Errors
               encountered during the visualization creation process.
        """
        self.version = version
        self.state = state
        self.data_product = data_product
        self.name = name
        self.description = description
        self.tags = tags
        self.use_cases = use_cases
        self.types = types
        self.contract_terms = contract_terms
        self.domain = domain
        self.parts_out = parts_out
        self.workflows = workflows
        self.dataview_enabled = dataview_enabled
        self.comments = comments
        self.access_control = access_control
        self.last_updated_at = last_updated_at
        self.is_restricted = is_restricted
        self.id = id
        self.asset = asset
        self.published_by = published_by
        self.published_at = published_at
        self.created_by = created_by
        self.created_at = created_at
        self.properties = properties
        self.visualization_errors = visualization_errors

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductDraft':
        """Initialize a DataProductDraft object from a json dictionary."""
        args = {}
        if (version := _dict.get('version')) is not None:
            args['version'] = version
        else:
            raise ValueError('Required property \'version\' not present in DataProductDraft JSON')
        if (state := _dict.get('state')) is not None:
            args['state'] = state
        else:
            raise ValueError('Required property \'state\' not present in DataProductDraft JSON')
        if (data_product := _dict.get('data_product')) is not None:
            args['data_product'] = DataProductDraftDataProduct.from_dict(data_product)
        else:
            raise ValueError('Required property \'data_product\' not present in DataProductDraft JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in DataProductDraft JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        else:
            raise ValueError('Required property \'description\' not present in DataProductDraft JSON')
        if (tags := _dict.get('tags')) is not None:
            args['tags'] = tags
        else:
            raise ValueError('Required property \'tags\' not present in DataProductDraft JSON')
        if (use_cases := _dict.get('use_cases')) is not None:
            args['use_cases'] = [UseCase.from_dict(v) for v in use_cases]
        if (types := _dict.get('types')) is not None:
            args['types'] = types
        else:
            raise ValueError('Required property \'types\' not present in DataProductDraft JSON')
        if (contract_terms := _dict.get('contract_terms')) is not None:
            args['contract_terms'] = [ContractTerms.from_dict(v) for v in contract_terms]
        else:
            raise ValueError('Required property \'contract_terms\' not present in DataProductDraft JSON')
        if (domain := _dict.get('domain')) is not None:
            args['domain'] = Domain.from_dict(domain)
        else:
            raise ValueError('Required property \'domain\' not present in DataProductDraft JSON')
        if (parts_out := _dict.get('parts_out')) is not None:
            args['parts_out'] = [DataProductPart.from_dict(v) for v in parts_out]
        else:
            raise ValueError('Required property \'parts_out\' not present in DataProductDraft JSON')
        if (workflows := _dict.get('workflows')) is not None:
            args['workflows'] = DataProductWorkflows.from_dict(workflows)
        if (dataview_enabled := _dict.get('dataview_enabled')) is not None:
            args['dataview_enabled'] = dataview_enabled
        if (comments := _dict.get('comments')) is not None:
            args['comments'] = comments
        if (access_control := _dict.get('access_control')) is not None:
            args['access_control'] = AssetListAccessControl.from_dict(access_control)
        if (last_updated_at := _dict.get('last_updated_at')) is not None:
            args['last_updated_at'] = string_to_datetime(last_updated_at)
        if (is_restricted := _dict.get('is_restricted')) is not None:
            args['is_restricted'] = is_restricted
        else:
            raise ValueError('Required property \'is_restricted\' not present in DataProductDraft JSON')
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in DataProductDraft JSON')
        if (asset := _dict.get('asset')) is not None:
            args['asset'] = AssetReference.from_dict(asset)
        else:
            raise ValueError('Required property \'asset\' not present in DataProductDraft JSON')
        if (published_by := _dict.get('published_by')) is not None:
            args['published_by'] = published_by
        if (published_at := _dict.get('published_at')) is not None:
            args['published_at'] = string_to_datetime(published_at)
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        else:
            raise ValueError('Required property \'created_by\' not present in DataProductDraft JSON')
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = string_to_datetime(created_at)
        else:
            raise ValueError('Required property \'created_at\' not present in DataProductDraft JSON')
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = properties
        if (visualization_errors := _dict.get('visualization_errors')) is not None:
            args['visualization_errors'] = [DataAssetRelationship.from_dict(v) for v in visualization_errors]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductDraft object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'data_product') and self.data_product is not None:
            if isinstance(self.data_product, dict):
                _dict['data_product'] = self.data_product
            else:
                _dict['data_product'] = self.data_product.to_dict()
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'use_cases') and self.use_cases is not None:
            use_cases_list = []
            for v in self.use_cases:
                if isinstance(v, dict):
                    use_cases_list.append(v)
                else:
                    use_cases_list.append(v.to_dict())
            _dict['use_cases'] = use_cases_list
        if hasattr(self, 'types') and self.types is not None:
            _dict['types'] = self.types
        if hasattr(self, 'contract_terms') and self.contract_terms is not None:
            contract_terms_list = []
            for v in self.contract_terms:
                if isinstance(v, dict):
                    contract_terms_list.append(v)
                else:
                    contract_terms_list.append(v.to_dict())
            _dict['contract_terms'] = contract_terms_list
        if hasattr(self, 'domain') and self.domain is not None:
            if isinstance(self.domain, dict):
                _dict['domain'] = self.domain
            else:
                _dict['domain'] = self.domain.to_dict()
        if hasattr(self, 'parts_out') and self.parts_out is not None:
            parts_out_list = []
            for v in self.parts_out:
                if isinstance(v, dict):
                    parts_out_list.append(v)
                else:
                    parts_out_list.append(v.to_dict())
            _dict['parts_out'] = parts_out_list
        if hasattr(self, 'workflows') and self.workflows is not None:
            if isinstance(self.workflows, dict):
                _dict['workflows'] = self.workflows
            else:
                _dict['workflows'] = self.workflows.to_dict()
        if hasattr(self, 'dataview_enabled') and self.dataview_enabled is not None:
            _dict['dataview_enabled'] = self.dataview_enabled
        if hasattr(self, 'comments') and self.comments is not None:
            _dict['comments'] = self.comments
        if hasattr(self, 'access_control') and self.access_control is not None:
            if isinstance(self.access_control, dict):
                _dict['access_control'] = self.access_control
            else:
                _dict['access_control'] = self.access_control.to_dict()
        if hasattr(self, 'last_updated_at') and self.last_updated_at is not None:
            _dict['last_updated_at'] = datetime_to_string(self.last_updated_at)
        if hasattr(self, 'is_restricted') and self.is_restricted is not None:
            _dict['is_restricted'] = self.is_restricted
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'asset') and self.asset is not None:
            if isinstance(self.asset, dict):
                _dict['asset'] = self.asset
            else:
                _dict['asset'] = self.asset.to_dict()
        if hasattr(self, 'published_by') and self.published_by is not None:
            _dict['published_by'] = self.published_by
        if hasattr(self, 'published_at') and self.published_at is not None:
            _dict['published_at'] = datetime_to_string(self.published_at)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'properties') and self.properties is not None:
            _dict['properties'] = self.properties
        if hasattr(self, 'visualization_errors') and self.visualization_errors is not None:
            visualization_errors_list = []
            for v in self.visualization_errors:
                if isinstance(v, dict):
                    visualization_errors_list.append(v)
                else:
                    visualization_errors_list.append(v.to_dict())
            _dict['visualization_errors'] = visualization_errors_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductDraft object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductDraft') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductDraft') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        The state of the data product version.
        """

        DRAFT = 'draft'
        AVAILABLE = 'available'
        RETIRED = 'retired'


    class TypesEnum(str, Enum):
        """
        types.
        """

        DATA = 'data'
        CODE = 'code'



class DataProductDraftCollection:
    """
    A collection of data product draft summaries.

    :param int limit: Set a limit on the number of results returned.
    :param FirstPage first: First page in the collection.
    :param NextPage next: (optional) Next page in the collection.
    :param int total_results: (optional) Indicates the total number of results
          returned.
    :param List[DataProductDraftSummary] drafts: Collection of data product drafts.
    """

    def __init__(
        self,
        limit: int,
        first: 'FirstPage',
        drafts: List['DataProductDraftSummary'],
        *,
        next: Optional['NextPage'] = None,
        total_results: Optional[int] = None,
    ) -> None:
        """
        Initialize a DataProductDraftCollection object.

        :param int limit: Set a limit on the number of results returned.
        :param FirstPage first: First page in the collection.
        :param List[DataProductDraftSummary] drafts: Collection of data product
               drafts.
        :param NextPage next: (optional) Next page in the collection.
        :param int total_results: (optional) Indicates the total number of results
               returned.
        """
        self.limit = limit
        self.first = first
        self.next = next
        self.total_results = total_results
        self.drafts = drafts

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductDraftCollection':
        """Initialize a DataProductDraftCollection object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in DataProductDraftCollection JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = FirstPage.from_dict(first)
        else:
            raise ValueError('Required property \'first\' not present in DataProductDraftCollection JSON')
        if (next := _dict.get('next')) is not None:
            args['next'] = NextPage.from_dict(next)
        if (total_results := _dict.get('total_results')) is not None:
            args['total_results'] = total_results
        if (drafts := _dict.get('drafts')) is not None:
            args['drafts'] = [DataProductDraftSummary.from_dict(v) for v in drafts]
        else:
            raise ValueError('Required property \'drafts\' not present in DataProductDraftCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductDraftCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'total_results') and self.total_results is not None:
            _dict['total_results'] = self.total_results
        if hasattr(self, 'drafts') and self.drafts is not None:
            drafts_list = []
            for v in self.drafts:
                if isinstance(v, dict):
                    drafts_list.append(v)
                else:
                    drafts_list.append(v.to_dict())
            _dict['drafts'] = drafts_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductDraftCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductDraftCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductDraftCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductDraftDataProduct:
    """
    Data product reference.

    :param str id: Data product identifier.
    :param DataProductDraftVersionRelease release: (optional) A data product draft
          version object.
    :param ContainerReference container: Container reference.
    """

    def __init__(
        self,
        id: str,
        container: 'ContainerReference',
        *,
        release: Optional['DataProductDraftVersionRelease'] = None,
    ) -> None:
        """
        Initialize a DataProductDraftDataProduct object.

        :param str id: Data product identifier.
        :param ContainerReference container: Container reference.
        :param DataProductDraftVersionRelease release: (optional) A data product
               draft version object.
        """
        self.id = id
        self.release = release
        self.container = container

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductDraftDataProduct':
        """Initialize a DataProductDraftDataProduct object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in DataProductDraftDataProduct JSON')
        if (release := _dict.get('release')) is not None:
            args['release'] = DataProductDraftVersionRelease.from_dict(release)
        if (container := _dict.get('container')) is not None:
            args['container'] = ContainerReference.from_dict(container)
        else:
            raise ValueError('Required property \'container\' not present in DataProductDraftDataProduct JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductDraftDataProduct object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'release') and self.release is not None:
            if isinstance(self.release, dict):
                _dict['release'] = self.release
            else:
                _dict['release'] = self.release.to_dict()
        if hasattr(self, 'container') and self.container is not None:
            if isinstance(self.container, dict):
                _dict['container'] = self.container
            else:
                _dict['container'] = self.container.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductDraftDataProduct object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductDraftDataProduct') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductDraftDataProduct') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductDraftPrototype:
    """
    New data product version input properties.

    :param str version: (optional) The data product version number.
    :param str state: (optional) The state of the data product version. If not
          specified, the data product version will be created in `draft` state.
    :param DataProductIdentity data_product: (optional) Data product identifier.
    :param str name: (optional) The name that refers to the new data product
          version. If this is a new data product, this value must be specified. If this is
          a new version of an existing data product, the name will default to the name of
          the previous data product version. A name can contain letters, numbers,
          understores, dashes, spaces or periods. A name must contain at least one
          non-space character.
    :param str description: (optional) Description of the data product version. If
          this is a new version of an existing data product, the description will default
          to the description of the previous version of the data product.
    :param List[str] tags: (optional) Tags on the data product.
    :param List[UseCase] use_cases: (optional) A list of use cases associated with
          the data product version.
    :param List[str] types: (optional) Types of parts on the data product.
    :param List[ContractTerms] contract_terms: (optional) Contract terms binding
          various aspects of the data product.
    :param Domain domain: (optional) Domain that the data product version belongs
          to. If this is the first version of a data product, this field is required. If
          this is a new version of an existing data product, the domain will default to
          the domain of the previous version of the data product.
    :param List[DataProductPart] parts_out: (optional) The outgoing parts of this
          data product version to be delivered to consumers. If this is the first version
          of a data product, this field defaults to an empty list. If this is a new
          version of an existing data product, the data product parts will default to the
          parts list from the previous version of the data product.
    :param DataProductWorkflows workflows: (optional) The workflows associated with
          the data product version.
    :param bool dataview_enabled: (optional) Indicates whether the dataView has
          enabled for data product.
    :param str comments: (optional) Comments by a producer that are provided either
          at the time of data product version creation or retiring.
    :param AssetListAccessControl access_control: (optional) Access control object.
    :param datetime last_updated_at: (optional) Timestamp of last asset update.
    :param bool is_restricted: (optional) Indicates whether the data product is
          restricted or not. A restricted data product indicates that orders of the data
          product requires explicit approval before data is delivered.
    :param AssetPrototype asset: New asset input properties.
    """

    def __init__(
        self,
        asset: 'AssetPrototype',
        *,
        version: Optional[str] = None,
        state: Optional[str] = None,
        data_product: Optional['DataProductIdentity'] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
        use_cases: Optional[List['UseCase']] = None,
        types: Optional[List[str]] = None,
        contract_terms: Optional[List['ContractTerms']] = None,
        domain: Optional['Domain'] = None,
        parts_out: Optional[List['DataProductPart']] = None,
        workflows: Optional['DataProductWorkflows'] = None,
        dataview_enabled: Optional[bool] = None,
        comments: Optional[str] = None,
        access_control: Optional['AssetListAccessControl'] = None,
        last_updated_at: Optional[datetime] = None,
        is_restricted: Optional[bool] = None,
    ) -> None:
        """
        Initialize a DataProductDraftPrototype object.

        :param AssetPrototype asset: New asset input properties.
        :param str version: (optional) The data product version number.
        :param str state: (optional) The state of the data product version. If not
               specified, the data product version will be created in `draft` state.
        :param DataProductIdentity data_product: (optional) Data product
               identifier.
        :param str name: (optional) The name that refers to the new data product
               version. If this is a new data product, this value must be specified. If
               this is a new version of an existing data product, the name will default to
               the name of the previous data product version. A name can contain letters,
               numbers, understores, dashes, spaces or periods. A name must contain at
               least one non-space character.
        :param str description: (optional) Description of the data product version.
               If this is a new version of an existing data product, the description will
               default to the description of the previous version of the data product.
        :param List[str] tags: (optional) Tags on the data product.
        :param List[UseCase] use_cases: (optional) A list of use cases associated
               with the data product version.
        :param List[str] types: (optional) Types of parts on the data product.
        :param List[ContractTerms] contract_terms: (optional) Contract terms
               binding various aspects of the data product.
        :param Domain domain: (optional) Domain that the data product version
               belongs to. If this is the first version of a data product, this field is
               required. If this is a new version of an existing data product, the domain
               will default to the domain of the previous version of the data product.
        :param List[DataProductPart] parts_out: (optional) The outgoing parts of
               this data product version to be delivered to consumers. If this is the
               first version of a data product, this field defaults to an empty list. If
               this is a new version of an existing data product, the data product parts
               will default to the parts list from the previous version of the data
               product.
        :param DataProductWorkflows workflows: (optional) The workflows associated
               with the data product version.
        :param bool dataview_enabled: (optional) Indicates whether the dataView has
               enabled for data product.
        :param str comments: (optional) Comments by a producer that are provided
               either at the time of data product version creation or retiring.
        :param AssetListAccessControl access_control: (optional) Access control
               object.
        :param datetime last_updated_at: (optional) Timestamp of last asset update.
        :param bool is_restricted: (optional) Indicates whether the data product is
               restricted or not. A restricted data product indicates that orders of the
               data product requires explicit approval before data is delivered.
        """
        self.version = version
        self.state = state
        self.data_product = data_product
        self.name = name
        self.description = description
        self.tags = tags
        self.use_cases = use_cases
        self.types = types
        self.contract_terms = contract_terms
        self.domain = domain
        self.parts_out = parts_out
        self.workflows = workflows
        self.dataview_enabled = dataview_enabled
        self.comments = comments
        self.access_control = access_control
        self.last_updated_at = last_updated_at
        self.is_restricted = is_restricted
        self.asset = asset

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductDraftPrototype':
        """Initialize a DataProductDraftPrototype object from a json dictionary."""
        args = {}
        if (version := _dict.get('version')) is not None:
            args['version'] = version
        if (state := _dict.get('state')) is not None:
            args['state'] = state
        if (data_product := _dict.get('data_product')) is not None:
            args['data_product'] = DataProductIdentity.from_dict(data_product)
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (tags := _dict.get('tags')) is not None:
            args['tags'] = tags
        if (use_cases := _dict.get('use_cases')) is not None:
            args['use_cases'] = [UseCase.from_dict(v) for v in use_cases]
        if (types := _dict.get('types')) is not None:
            args['types'] = types
        if (contract_terms := _dict.get('contract_terms')) is not None:
            args['contract_terms'] = [ContractTerms.from_dict(v) for v in contract_terms]
        if (domain := _dict.get('domain')) is not None:
            args['domain'] = Domain.from_dict(domain)
        if (parts_out := _dict.get('parts_out')) is not None:
            args['parts_out'] = [DataProductPart.from_dict(v) for v in parts_out]
        if (workflows := _dict.get('workflows')) is not None:
            args['workflows'] = DataProductWorkflows.from_dict(workflows)
        if (dataview_enabled := _dict.get('dataview_enabled')) is not None:
            args['dataview_enabled'] = dataview_enabled
        if (comments := _dict.get('comments')) is not None:
            args['comments'] = comments
        if (access_control := _dict.get('access_control')) is not None:
            args['access_control'] = AssetListAccessControl.from_dict(access_control)
        if (last_updated_at := _dict.get('last_updated_at')) is not None:
            args['last_updated_at'] = string_to_datetime(last_updated_at)
        if (is_restricted := _dict.get('is_restricted')) is not None:
            args['is_restricted'] = is_restricted
        if (asset := _dict.get('asset')) is not None:
            args['asset'] = AssetPrototype.from_dict(asset)
        else:
            raise ValueError('Required property \'asset\' not present in DataProductDraftPrototype JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductDraftPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'data_product') and self.data_product is not None:
            if isinstance(self.data_product, dict):
                _dict['data_product'] = self.data_product
            else:
                _dict['data_product'] = self.data_product.to_dict()
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'use_cases') and self.use_cases is not None:
            use_cases_list = []
            for v in self.use_cases:
                if isinstance(v, dict):
                    use_cases_list.append(v)
                else:
                    use_cases_list.append(v.to_dict())
            _dict['use_cases'] = use_cases_list
        if hasattr(self, 'types') and self.types is not None:
            _dict['types'] = self.types
        if hasattr(self, 'contract_terms') and self.contract_terms is not None:
            contract_terms_list = []
            for v in self.contract_terms:
                if isinstance(v, dict):
                    contract_terms_list.append(v)
                else:
                    contract_terms_list.append(v.to_dict())
            _dict['contract_terms'] = contract_terms_list
        if hasattr(self, 'domain') and self.domain is not None:
            if isinstance(self.domain, dict):
                _dict['domain'] = self.domain
            else:
                _dict['domain'] = self.domain.to_dict()
        if hasattr(self, 'parts_out') and self.parts_out is not None:
            parts_out_list = []
            for v in self.parts_out:
                if isinstance(v, dict):
                    parts_out_list.append(v)
                else:
                    parts_out_list.append(v.to_dict())
            _dict['parts_out'] = parts_out_list
        if hasattr(self, 'workflows') and self.workflows is not None:
            if isinstance(self.workflows, dict):
                _dict['workflows'] = self.workflows
            else:
                _dict['workflows'] = self.workflows.to_dict()
        if hasattr(self, 'dataview_enabled') and self.dataview_enabled is not None:
            _dict['dataview_enabled'] = self.dataview_enabled
        if hasattr(self, 'comments') and self.comments is not None:
            _dict['comments'] = self.comments
        if hasattr(self, 'access_control') and self.access_control is not None:
            if isinstance(self.access_control, dict):
                _dict['access_control'] = self.access_control
            else:
                _dict['access_control'] = self.access_control.to_dict()
        if hasattr(self, 'last_updated_at') and self.last_updated_at is not None:
            _dict['last_updated_at'] = datetime_to_string(self.last_updated_at)
        if hasattr(self, 'is_restricted') and self.is_restricted is not None:
            _dict['is_restricted'] = self.is_restricted
        if hasattr(self, 'asset') and self.asset is not None:
            if isinstance(self.asset, dict):
                _dict['asset'] = self.asset
            else:
                _dict['asset'] = self.asset.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductDraftPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductDraftPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductDraftPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        The state of the data product version. If not specified, the data product version
        will be created in `draft` state.
        """

        DRAFT = 'draft'
        AVAILABLE = 'available'
        RETIRED = 'retired'


    class TypesEnum(str, Enum):
        """
        types.
        """

        DATA = 'data'
        CODE = 'code'



class DataProductDraftSummary:
    """
    Summary of Data Product Version object.

    :param str version: The data product version number.
    :param str state: The state of the data product version.
    :param DataProductDraftSummaryDataProduct data_product: Data product reference.
    :param str name: The name of the data product version. A name can contain
          letters, numbers, understores, dashes, spaces or periods. Names are mutable and
          reusable.
    :param str description: The description of the data product version.
    :param List[str] tags: Tags on the data product.
    :param List[UseCase] use_cases: (optional) A list of use cases associated with
          the data product version.
    :param List[str] types: Types of parts on the data product.
    :param List[ContractTerms] contract_terms: Contract terms binding various
          aspects of the data product.
    :param Domain domain: Domain that the data product version belongs to. If this
          is the first version of a data product, this field is required. If this is a new
          version of an existing data product, the domain will default to the domain of
          the previous version of the data product.
    :param List[DataProductPart] parts_out: The outgoing parts of this data product
          version to be delivered to consumers. If this is the first version of a data
          product, this field defaults to an empty list. If this is a new version of an
          existing data product, the data product parts will default to the parts list
          from the previous version of the data product.
    :param DataProductWorkflows workflows: (optional) The workflows associated with
          the data product version.
    :param bool dataview_enabled: (optional) Indicates whether the dataView has
          enabled for data product.
    :param str comments: (optional) Comments by a producer that are provided either
          at the time of data product version creation or retiring.
    :param AssetListAccessControl access_control: (optional) Access control object.
    :param datetime last_updated_at: (optional) Timestamp of last asset update.
    :param bool is_restricted: Indicates whether the data product is restricted or
          not. A restricted data product indicates that orders of the data product
          requires explicit approval before data is delivered.
    :param str id: The identifier of the data product version.
    :param AssetReference asset: The reference schema for a asset in a container.
    """

    def __init__(
        self,
        version: str,
        state: str,
        data_product: 'DataProductDraftSummaryDataProduct',
        name: str,
        description: str,
        tags: List[str],
        types: List[str],
        contract_terms: List['ContractTerms'],
        domain: 'Domain',
        parts_out: List['DataProductPart'],
        is_restricted: bool,
        id: str,
        asset: 'AssetReference',
        *,
        use_cases: Optional[List['UseCase']] = None,
        workflows: Optional['DataProductWorkflows'] = None,
        dataview_enabled: Optional[bool] = None,
        comments: Optional[str] = None,
        access_control: Optional['AssetListAccessControl'] = None,
        last_updated_at: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a DataProductDraftSummary object.

        :param str version: The data product version number.
        :param str state: The state of the data product version.
        :param DataProductDraftSummaryDataProduct data_product: Data product
               reference.
        :param str name: The name of the data product version. A name can contain
               letters, numbers, understores, dashes, spaces or periods. Names are mutable
               and reusable.
        :param str description: The description of the data product version.
        :param List[str] tags: Tags on the data product.
        :param List[str] types: Types of parts on the data product.
        :param List[ContractTerms] contract_terms: Contract terms binding various
               aspects of the data product.
        :param Domain domain: Domain that the data product version belongs to. If
               this is the first version of a data product, this field is required. If
               this is a new version of an existing data product, the domain will default
               to the domain of the previous version of the data product.
        :param List[DataProductPart] parts_out: The outgoing parts of this data
               product version to be delivered to consumers. If this is the first version
               of a data product, this field defaults to an empty list. If this is a new
               version of an existing data product, the data product parts will default to
               the parts list from the previous version of the data product.
        :param bool is_restricted: Indicates whether the data product is restricted
               or not. A restricted data product indicates that orders of the data product
               requires explicit approval before data is delivered.
        :param str id: The identifier of the data product version.
        :param AssetReference asset: The reference schema for a asset in a
               container.
        :param List[UseCase] use_cases: (optional) A list of use cases associated
               with the data product version.
        :param DataProductWorkflows workflows: (optional) The workflows associated
               with the data product version.
        :param bool dataview_enabled: (optional) Indicates whether the dataView has
               enabled for data product.
        :param str comments: (optional) Comments by a producer that are provided
               either at the time of data product version creation or retiring.
        :param AssetListAccessControl access_control: (optional) Access control
               object.
        :param datetime last_updated_at: (optional) Timestamp of last asset update.
        """
        self.version = version
        self.state = state
        self.data_product = data_product
        self.name = name
        self.description = description
        self.tags = tags
        self.use_cases = use_cases
        self.types = types
        self.contract_terms = contract_terms
        self.domain = domain
        self.parts_out = parts_out
        self.workflows = workflows
        self.dataview_enabled = dataview_enabled
        self.comments = comments
        self.access_control = access_control
        self.last_updated_at = last_updated_at
        self.is_restricted = is_restricted
        self.id = id
        self.asset = asset

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductDraftSummary':
        """Initialize a DataProductDraftSummary object from a json dictionary."""
        args = {}
        if (version := _dict.get('version')) is not None:
            args['version'] = version
        else:
            raise ValueError('Required property \'version\' not present in DataProductDraftSummary JSON')
        if (state := _dict.get('state')) is not None:
            args['state'] = state
        else:
            raise ValueError('Required property \'state\' not present in DataProductDraftSummary JSON')
        if (data_product := _dict.get('data_product')) is not None:
            args['data_product'] = DataProductDraftSummaryDataProduct.from_dict(data_product)
        else:
            raise ValueError('Required property \'data_product\' not present in DataProductDraftSummary JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in DataProductDraftSummary JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        else:
            raise ValueError('Required property \'description\' not present in DataProductDraftSummary JSON')
        if (tags := _dict.get('tags')) is not None:
            args['tags'] = tags
        else:
            raise ValueError('Required property \'tags\' not present in DataProductDraftSummary JSON')
        if (use_cases := _dict.get('use_cases')) is not None:
            args['use_cases'] = [UseCase.from_dict(v) for v in use_cases]
        if (types := _dict.get('types')) is not None:
            args['types'] = types
        else:
            raise ValueError('Required property \'types\' not present in DataProductDraftSummary JSON')
        if (contract_terms := _dict.get('contract_terms')) is not None:
            args['contract_terms'] = [ContractTerms.from_dict(v) for v in contract_terms]
        else:
            raise ValueError('Required property \'contract_terms\' not present in DataProductDraftSummary JSON')
        if (domain := _dict.get('domain')) is not None:
            args['domain'] = Domain.from_dict(domain)
        else:
            raise ValueError('Required property \'domain\' not present in DataProductDraftSummary JSON')
        if (parts_out := _dict.get('parts_out')) is not None:
            args['parts_out'] = [DataProductPart.from_dict(v) for v in parts_out]
        else:
            raise ValueError('Required property \'parts_out\' not present in DataProductDraftSummary JSON')
        if (workflows := _dict.get('workflows')) is not None:
            args['workflows'] = DataProductWorkflows.from_dict(workflows)
        if (dataview_enabled := _dict.get('dataview_enabled')) is not None:
            args['dataview_enabled'] = dataview_enabled
        if (comments := _dict.get('comments')) is not None:
            args['comments'] = comments
        if (access_control := _dict.get('access_control')) is not None:
            args['access_control'] = AssetListAccessControl.from_dict(access_control)
        if (last_updated_at := _dict.get('last_updated_at')) is not None:
            args['last_updated_at'] = string_to_datetime(last_updated_at)
        if (is_restricted := _dict.get('is_restricted')) is not None:
            args['is_restricted'] = is_restricted
        else:
            raise ValueError('Required property \'is_restricted\' not present in DataProductDraftSummary JSON')
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in DataProductDraftSummary JSON')
        if (asset := _dict.get('asset')) is not None:
            args['asset'] = AssetReference.from_dict(asset)
        else:
            raise ValueError('Required property \'asset\' not present in DataProductDraftSummary JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductDraftSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'data_product') and self.data_product is not None:
            if isinstance(self.data_product, dict):
                _dict['data_product'] = self.data_product
            else:
                _dict['data_product'] = self.data_product.to_dict()
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'use_cases') and self.use_cases is not None:
            use_cases_list = []
            for v in self.use_cases:
                if isinstance(v, dict):
                    use_cases_list.append(v)
                else:
                    use_cases_list.append(v.to_dict())
            _dict['use_cases'] = use_cases_list
        if hasattr(self, 'types') and self.types is not None:
            _dict['types'] = self.types
        if hasattr(self, 'contract_terms') and self.contract_terms is not None:
            contract_terms_list = []
            for v in self.contract_terms:
                if isinstance(v, dict):
                    contract_terms_list.append(v)
                else:
                    contract_terms_list.append(v.to_dict())
            _dict['contract_terms'] = contract_terms_list
        if hasattr(self, 'domain') and self.domain is not None:
            if isinstance(self.domain, dict):
                _dict['domain'] = self.domain
            else:
                _dict['domain'] = self.domain.to_dict()
        if hasattr(self, 'parts_out') and self.parts_out is not None:
            parts_out_list = []
            for v in self.parts_out:
                if isinstance(v, dict):
                    parts_out_list.append(v)
                else:
                    parts_out_list.append(v.to_dict())
            _dict['parts_out'] = parts_out_list
        if hasattr(self, 'workflows') and self.workflows is not None:
            if isinstance(self.workflows, dict):
                _dict['workflows'] = self.workflows
            else:
                _dict['workflows'] = self.workflows.to_dict()
        if hasattr(self, 'dataview_enabled') and self.dataview_enabled is not None:
            _dict['dataview_enabled'] = self.dataview_enabled
        if hasattr(self, 'comments') and self.comments is not None:
            _dict['comments'] = self.comments
        if hasattr(self, 'access_control') and self.access_control is not None:
            if isinstance(self.access_control, dict):
                _dict['access_control'] = self.access_control
            else:
                _dict['access_control'] = self.access_control.to_dict()
        if hasattr(self, 'last_updated_at') and self.last_updated_at is not None:
            _dict['last_updated_at'] = datetime_to_string(self.last_updated_at)
        if hasattr(self, 'is_restricted') and self.is_restricted is not None:
            _dict['is_restricted'] = self.is_restricted
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'asset') and self.asset is not None:
            if isinstance(self.asset, dict):
                _dict['asset'] = self.asset
            else:
                _dict['asset'] = self.asset.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductDraftSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductDraftSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductDraftSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        The state of the data product version.
        """

        DRAFT = 'draft'
        AVAILABLE = 'available'
        RETIRED = 'retired'


    class TypesEnum(str, Enum):
        """
        types.
        """

        DATA = 'data'
        CODE = 'code'



class DataProductDraftSummaryDataProduct:
    """
    Data product reference.

    :param str id: Data product identifier.
    :param DataProductDraftVersionRelease release: (optional) A data product draft
          version object.
    :param ContainerReference container: Container reference.
    """

    def __init__(
        self,
        id: str,
        container: 'ContainerReference',
        *,
        release: Optional['DataProductDraftVersionRelease'] = None,
    ) -> None:
        """
        Initialize a DataProductDraftSummaryDataProduct object.

        :param str id: Data product identifier.
        :param ContainerReference container: Container reference.
        :param DataProductDraftVersionRelease release: (optional) A data product
               draft version object.
        """
        self.id = id
        self.release = release
        self.container = container

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductDraftSummaryDataProduct':
        """Initialize a DataProductDraftSummaryDataProduct object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in DataProductDraftSummaryDataProduct JSON')
        if (release := _dict.get('release')) is not None:
            args['release'] = DataProductDraftVersionRelease.from_dict(release)
        if (container := _dict.get('container')) is not None:
            args['container'] = ContainerReference.from_dict(container)
        else:
            raise ValueError('Required property \'container\' not present in DataProductDraftSummaryDataProduct JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductDraftSummaryDataProduct object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'release') and self.release is not None:
            if isinstance(self.release, dict):
                _dict['release'] = self.release
            else:
                _dict['release'] = self.release.to_dict()
        if hasattr(self, 'container') and self.container is not None:
            if isinstance(self.container, dict):
                _dict['container'] = self.container
            else:
                _dict['container'] = self.container.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductDraftSummaryDataProduct object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductDraftSummaryDataProduct') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductDraftSummaryDataProduct') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductDraftVersionRelease:
    """
    A data product draft version object.

    :param str id: (optional) ID of a draft version of data product.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a DataProductDraftVersionRelease object.

        :param str id: (optional) ID of a draft version of data product.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductDraftVersionRelease':
        """Initialize a DataProductDraftVersionRelease object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductDraftVersionRelease object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductDraftVersionRelease object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductDraftVersionRelease') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductDraftVersionRelease') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductIdentity:
    """
    Data product identifier.

    :param str id: Data product identifier.
    :param DataProductDraftVersionRelease release: (optional) A data product draft
          version object.
    """

    def __init__(
        self,
        id: str,
        *,
        release: Optional['DataProductDraftVersionRelease'] = None,
    ) -> None:
        """
        Initialize a DataProductIdentity object.

        :param str id: Data product identifier.
        :param DataProductDraftVersionRelease release: (optional) A data product
               draft version object.
        """
        self.id = id
        self.release = release

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductIdentity':
        """Initialize a DataProductIdentity object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in DataProductIdentity JSON')
        if (release := _dict.get('release')) is not None:
            args['release'] = DataProductDraftVersionRelease.from_dict(release)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductIdentity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'release') and self.release is not None:
            if isinstance(self.release, dict):
                _dict['release'] = self.release
            else:
                _dict['release'] = self.release.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductIdentity object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductIdentity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductIdentity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductOrderAccessRequest:
    """
    The approval workflows associated with the data product version.

    :param List[str] task_assignee_users: (optional) The workflow approvers
          associated with the data product version.
    :param List[str] pre_approved_users: (optional) The list of users or groups
          whose request will get pre-approved associated with the data product version.
    :param DataProductCustomWorkflowDefinition custom_workflow_definition:
          (optional) A custom workflow definition to be used to create a workflow to
          approve a data product subscription.
    """

    def __init__(
        self,
        *,
        task_assignee_users: Optional[List[str]] = None,
        pre_approved_users: Optional[List[str]] = None,
        custom_workflow_definition: Optional['DataProductCustomWorkflowDefinition'] = None,
    ) -> None:
        """
        Initialize a DataProductOrderAccessRequest object.

        :param List[str] task_assignee_users: (optional) The workflow approvers
               associated with the data product version.
        :param List[str] pre_approved_users: (optional) The list of users or groups
               whose request will get pre-approved associated with the data product
               version.
        :param DataProductCustomWorkflowDefinition custom_workflow_definition:
               (optional) A custom workflow definition to be used to create a workflow to
               approve a data product subscription.
        """
        self.task_assignee_users = task_assignee_users
        self.pre_approved_users = pre_approved_users
        self.custom_workflow_definition = custom_workflow_definition

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductOrderAccessRequest':
        """Initialize a DataProductOrderAccessRequest object from a json dictionary."""
        args = {}
        if (task_assignee_users := _dict.get('task_assignee_users')) is not None:
            args['task_assignee_users'] = task_assignee_users
        if (pre_approved_users := _dict.get('pre_approved_users')) is not None:
            args['pre_approved_users'] = pre_approved_users
        if (custom_workflow_definition := _dict.get('custom_workflow_definition')) is not None:
            args['custom_workflow_definition'] = DataProductCustomWorkflowDefinition.from_dict(custom_workflow_definition)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductOrderAccessRequest object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'task_assignee_users') and self.task_assignee_users is not None:
            _dict['task_assignee_users'] = self.task_assignee_users
        if hasattr(self, 'pre_approved_users') and self.pre_approved_users is not None:
            _dict['pre_approved_users'] = self.pre_approved_users
        if hasattr(self, 'custom_workflow_definition') and self.custom_workflow_definition is not None:
            if isinstance(self.custom_workflow_definition, dict):
                _dict['custom_workflow_definition'] = self.custom_workflow_definition
            else:
                _dict['custom_workflow_definition'] = self.custom_workflow_definition.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductOrderAccessRequest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductOrderAccessRequest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductOrderAccessRequest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductPart:
    """
    Data Product Part.

    :param AssetPartReference asset: The asset represented in this part.
    :param List[DeliveryMethod] delivery_methods: (optional) Delivery methods
          describing the delivery options available for this part.
    """

    def __init__(
        self,
        asset: 'AssetPartReference',
        *,
        delivery_methods: Optional[List['DeliveryMethod']] = None,
    ) -> None:
        """
        Initialize a DataProductPart object.

        :param AssetPartReference asset: The asset represented in this part.
        :param List[DeliveryMethod] delivery_methods: (optional) Delivery methods
               describing the delivery options available for this part.
        """
        self.asset = asset
        self.delivery_methods = delivery_methods

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductPart':
        """Initialize a DataProductPart object from a json dictionary."""
        args = {}
        if (asset := _dict.get('asset')) is not None:
            args['asset'] = AssetPartReference.from_dict(asset)
        else:
            raise ValueError('Required property \'asset\' not present in DataProductPart JSON')
        if (delivery_methods := _dict.get('delivery_methods')) is not None:
            args['delivery_methods'] = [DeliveryMethod.from_dict(v) for v in delivery_methods]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductPart object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'asset') and self.asset is not None:
            if isinstance(self.asset, dict):
                _dict['asset'] = self.asset
            else:
                _dict['asset'] = self.asset.to_dict()
        if hasattr(self, 'delivery_methods') and self.delivery_methods is not None:
            delivery_methods_list = []
            for v in self.delivery_methods:
                if isinstance(v, dict):
                    delivery_methods_list.append(v)
                else:
                    delivery_methods_list.append(v.to_dict())
            _dict['delivery_methods'] = delivery_methods_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductPart object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductPart') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductPart') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductRelease:
    """
    Data Product version release.

    :param str version: The data product version number.
    :param str state: The state of the data product version.
    :param DataProductReleaseDataProduct data_product: Data product reference.
    :param str name: The name of the data product version. A name can contain
          letters, numbers, understores, dashes, spaces or periods. Names are mutable and
          reusable.
    :param str description: The description of the data product version.
    :param List[str] tags: Tags on the data product.
    :param List[UseCase] use_cases: (optional) A list of use cases associated with
          the data product version.
    :param List[str] types: Types of parts on the data product.
    :param List[ContractTerms] contract_terms: Contract terms binding various
          aspects of the data product.
    :param Domain domain: Domain that the data product version belongs to. If this
          is the first version of a data product, this field is required. If this is a new
          version of an existing data product, the domain will default to the domain of
          the previous version of the data product.
    :param List[DataProductPart] parts_out: The outgoing parts of this data product
          version to be delivered to consumers. If this is the first version of a data
          product, this field defaults to an empty list. If this is a new version of an
          existing data product, the data product parts will default to the parts list
          from the previous version of the data product.
    :param DataProductWorkflows workflows: (optional) The workflows associated with
          the data product version.
    :param bool dataview_enabled: (optional) Indicates whether the dataView has
          enabled for data product.
    :param str comments: (optional) Comments by a producer that are provided either
          at the time of data product version creation or retiring.
    :param AssetListAccessControl access_control: (optional) Access control object.
    :param datetime last_updated_at: (optional) Timestamp of last asset update.
    :param bool is_restricted: Indicates whether the data product is restricted or
          not. A restricted data product indicates that orders of the data product
          requires explicit approval before data is delivered.
    :param str id: The identifier of the data product version.
    :param AssetReference asset: The reference schema for a asset in a container.
    :param str published_by: (optional) The user who published this data product
          version.
    :param datetime published_at: (optional) The time when this data product version
          was published.
    :param str created_by: The creator of this data product version.
    :param datetime created_at: The time when this data product version was created.
    :param dict properties: (optional) Metadata properties on data products.
    :param List[DataAssetRelationship] visualization_errors: (optional) Errors
          encountered during the visualization creation process.
    """

    def __init__(
        self,
        version: str,
        state: str,
        data_product: 'DataProductReleaseDataProduct',
        name: str,
        description: str,
        tags: List[str],
        types: List[str],
        contract_terms: List['ContractTerms'],
        domain: 'Domain',
        parts_out: List['DataProductPart'],
        is_restricted: bool,
        id: str,
        asset: 'AssetReference',
        created_by: str,
        created_at: datetime,
        *,
        use_cases: Optional[List['UseCase']] = None,
        workflows: Optional['DataProductWorkflows'] = None,
        dataview_enabled: Optional[bool] = None,
        comments: Optional[str] = None,
        access_control: Optional['AssetListAccessControl'] = None,
        last_updated_at: Optional[datetime] = None,
        published_by: Optional[str] = None,
        published_at: Optional[datetime] = None,
        properties: Optional[dict] = None,
        visualization_errors: Optional[List['DataAssetRelationship']] = None,
    ) -> None:
        """
        Initialize a DataProductRelease object.

        :param str version: The data product version number.
        :param str state: The state of the data product version.
        :param DataProductReleaseDataProduct data_product: Data product reference.
        :param str name: The name of the data product version. A name can contain
               letters, numbers, understores, dashes, spaces or periods. Names are mutable
               and reusable.
        :param str description: The description of the data product version.
        :param List[str] tags: Tags on the data product.
        :param List[str] types: Types of parts on the data product.
        :param List[ContractTerms] contract_terms: Contract terms binding various
               aspects of the data product.
        :param Domain domain: Domain that the data product version belongs to. If
               this is the first version of a data product, this field is required. If
               this is a new version of an existing data product, the domain will default
               to the domain of the previous version of the data product.
        :param List[DataProductPart] parts_out: The outgoing parts of this data
               product version to be delivered to consumers. If this is the first version
               of a data product, this field defaults to an empty list. If this is a new
               version of an existing data product, the data product parts will default to
               the parts list from the previous version of the data product.
        :param bool is_restricted: Indicates whether the data product is restricted
               or not. A restricted data product indicates that orders of the data product
               requires explicit approval before data is delivered.
        :param str id: The identifier of the data product version.
        :param AssetReference asset: The reference schema for a asset in a
               container.
        :param str created_by: The creator of this data product version.
        :param datetime created_at: The time when this data product version was
               created.
        :param List[UseCase] use_cases: (optional) A list of use cases associated
               with the data product version.
        :param DataProductWorkflows workflows: (optional) The workflows associated
               with the data product version.
        :param bool dataview_enabled: (optional) Indicates whether the dataView has
               enabled for data product.
        :param str comments: (optional) Comments by a producer that are provided
               either at the time of data product version creation or retiring.
        :param AssetListAccessControl access_control: (optional) Access control
               object.
        :param datetime last_updated_at: (optional) Timestamp of last asset update.
        :param str published_by: (optional) The user who published this data
               product version.
        :param datetime published_at: (optional) The time when this data product
               version was published.
        :param dict properties: (optional) Metadata properties on data products.
        :param List[DataAssetRelationship] visualization_errors: (optional) Errors
               encountered during the visualization creation process.
        """
        self.version = version
        self.state = state
        self.data_product = data_product
        self.name = name
        self.description = description
        self.tags = tags
        self.use_cases = use_cases
        self.types = types
        self.contract_terms = contract_terms
        self.domain = domain
        self.parts_out = parts_out
        self.workflows = workflows
        self.dataview_enabled = dataview_enabled
        self.comments = comments
        self.access_control = access_control
        self.last_updated_at = last_updated_at
        self.is_restricted = is_restricted
        self.id = id
        self.asset = asset
        self.published_by = published_by
        self.published_at = published_at
        self.created_by = created_by
        self.created_at = created_at
        self.properties = properties
        self.visualization_errors = visualization_errors

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductRelease':
        """Initialize a DataProductRelease object from a json dictionary."""
        args = {}
        if (version := _dict.get('version')) is not None:
            args['version'] = version
        else:
            raise ValueError('Required property \'version\' not present in DataProductRelease JSON')
        if (state := _dict.get('state')) is not None:
            args['state'] = state
        else:
            raise ValueError('Required property \'state\' not present in DataProductRelease JSON')
        if (data_product := _dict.get('data_product')) is not None:
            args['data_product'] = DataProductReleaseDataProduct.from_dict(data_product)
        else:
            raise ValueError('Required property \'data_product\' not present in DataProductRelease JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in DataProductRelease JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        else:
            raise ValueError('Required property \'description\' not present in DataProductRelease JSON')
        if (tags := _dict.get('tags')) is not None:
            args['tags'] = tags
        else:
            raise ValueError('Required property \'tags\' not present in DataProductRelease JSON')
        if (use_cases := _dict.get('use_cases')) is not None:
            args['use_cases'] = [UseCase.from_dict(v) for v in use_cases]
        if (types := _dict.get('types')) is not None:
            args['types'] = types
        else:
            raise ValueError('Required property \'types\' not present in DataProductRelease JSON')
        if (contract_terms := _dict.get('contract_terms')) is not None:
            args['contract_terms'] = [ContractTerms.from_dict(v) for v in contract_terms]
        else:
            raise ValueError('Required property \'contract_terms\' not present in DataProductRelease JSON')
        if (domain := _dict.get('domain')) is not None:
            args['domain'] = Domain.from_dict(domain)
        else:
            raise ValueError('Required property \'domain\' not present in DataProductRelease JSON')
        if (parts_out := _dict.get('parts_out')) is not None:
            args['parts_out'] = [DataProductPart.from_dict(v) for v in parts_out]
        else:
            raise ValueError('Required property \'parts_out\' not present in DataProductRelease JSON')
        if (workflows := _dict.get('workflows')) is not None:
            args['workflows'] = DataProductWorkflows.from_dict(workflows)
        if (dataview_enabled := _dict.get('dataview_enabled')) is not None:
            args['dataview_enabled'] = dataview_enabled
        if (comments := _dict.get('comments')) is not None:
            args['comments'] = comments
        if (access_control := _dict.get('access_control')) is not None:
            args['access_control'] = AssetListAccessControl.from_dict(access_control)
        if (last_updated_at := _dict.get('last_updated_at')) is not None:
            args['last_updated_at'] = string_to_datetime(last_updated_at)
        if (is_restricted := _dict.get('is_restricted')) is not None:
            args['is_restricted'] = is_restricted
        else:
            raise ValueError('Required property \'is_restricted\' not present in DataProductRelease JSON')
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in DataProductRelease JSON')
        if (asset := _dict.get('asset')) is not None:
            args['asset'] = AssetReference.from_dict(asset)
        else:
            raise ValueError('Required property \'asset\' not present in DataProductRelease JSON')
        if (published_by := _dict.get('published_by')) is not None:
            args['published_by'] = published_by
        if (published_at := _dict.get('published_at')) is not None:
            args['published_at'] = string_to_datetime(published_at)
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        else:
            raise ValueError('Required property \'created_by\' not present in DataProductRelease JSON')
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = string_to_datetime(created_at)
        else:
            raise ValueError('Required property \'created_at\' not present in DataProductRelease JSON')
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = properties
        if (visualization_errors := _dict.get('visualization_errors')) is not None:
            args['visualization_errors'] = [DataAssetRelationship.from_dict(v) for v in visualization_errors]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductRelease object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'data_product') and self.data_product is not None:
            if isinstance(self.data_product, dict):
                _dict['data_product'] = self.data_product
            else:
                _dict['data_product'] = self.data_product.to_dict()
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'use_cases') and self.use_cases is not None:
            use_cases_list = []
            for v in self.use_cases:
                if isinstance(v, dict):
                    use_cases_list.append(v)
                else:
                    use_cases_list.append(v.to_dict())
            _dict['use_cases'] = use_cases_list
        if hasattr(self, 'types') and self.types is not None:
            _dict['types'] = self.types
        if hasattr(self, 'contract_terms') and self.contract_terms is not None:
            contract_terms_list = []
            for v in self.contract_terms:
                if isinstance(v, dict):
                    contract_terms_list.append(v)
                else:
                    contract_terms_list.append(v.to_dict())
            _dict['contract_terms'] = contract_terms_list
        if hasattr(self, 'domain') and self.domain is not None:
            if isinstance(self.domain, dict):
                _dict['domain'] = self.domain
            else:
                _dict['domain'] = self.domain.to_dict()
        if hasattr(self, 'parts_out') and self.parts_out is not None:
            parts_out_list = []
            for v in self.parts_out:
                if isinstance(v, dict):
                    parts_out_list.append(v)
                else:
                    parts_out_list.append(v.to_dict())
            _dict['parts_out'] = parts_out_list
        if hasattr(self, 'workflows') and self.workflows is not None:
            if isinstance(self.workflows, dict):
                _dict['workflows'] = self.workflows
            else:
                _dict['workflows'] = self.workflows.to_dict()
        if hasattr(self, 'dataview_enabled') and self.dataview_enabled is not None:
            _dict['dataview_enabled'] = self.dataview_enabled
        if hasattr(self, 'comments') and self.comments is not None:
            _dict['comments'] = self.comments
        if hasattr(self, 'access_control') and self.access_control is not None:
            if isinstance(self.access_control, dict):
                _dict['access_control'] = self.access_control
            else:
                _dict['access_control'] = self.access_control.to_dict()
        if hasattr(self, 'last_updated_at') and self.last_updated_at is not None:
            _dict['last_updated_at'] = datetime_to_string(self.last_updated_at)
        if hasattr(self, 'is_restricted') and self.is_restricted is not None:
            _dict['is_restricted'] = self.is_restricted
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'asset') and self.asset is not None:
            if isinstance(self.asset, dict):
                _dict['asset'] = self.asset
            else:
                _dict['asset'] = self.asset.to_dict()
        if hasattr(self, 'published_by') and self.published_by is not None:
            _dict['published_by'] = self.published_by
        if hasattr(self, 'published_at') and self.published_at is not None:
            _dict['published_at'] = datetime_to_string(self.published_at)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'properties') and self.properties is not None:
            _dict['properties'] = self.properties
        if hasattr(self, 'visualization_errors') and self.visualization_errors is not None:
            visualization_errors_list = []
            for v in self.visualization_errors:
                if isinstance(v, dict):
                    visualization_errors_list.append(v)
                else:
                    visualization_errors_list.append(v.to_dict())
            _dict['visualization_errors'] = visualization_errors_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductRelease object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductRelease') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductRelease') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        The state of the data product version.
        """

        DRAFT = 'draft'
        AVAILABLE = 'available'
        RETIRED = 'retired'


    class TypesEnum(str, Enum):
        """
        types.
        """

        DATA = 'data'
        CODE = 'code'



class DataProductReleaseCollection:
    """
    A collection of data product release summaries.

    :param int limit: Set a limit on the number of results returned.
    :param FirstPage first: First page in the collection.
    :param NextPage next: (optional) Next page in the collection.
    :param int total_results: (optional) Indicates the total number of results
          returned.
    :param List[DataProductReleaseSummary] releases: Collection of data product
          releases.
    """

    def __init__(
        self,
        limit: int,
        first: 'FirstPage',
        releases: List['DataProductReleaseSummary'],
        *,
        next: Optional['NextPage'] = None,
        total_results: Optional[int] = None,
    ) -> None:
        """
        Initialize a DataProductReleaseCollection object.

        :param int limit: Set a limit on the number of results returned.
        :param FirstPage first: First page in the collection.
        :param List[DataProductReleaseSummary] releases: Collection of data product
               releases.
        :param NextPage next: (optional) Next page in the collection.
        :param int total_results: (optional) Indicates the total number of results
               returned.
        """
        self.limit = limit
        self.first = first
        self.next = next
        self.total_results = total_results
        self.releases = releases

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductReleaseCollection':
        """Initialize a DataProductReleaseCollection object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in DataProductReleaseCollection JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = FirstPage.from_dict(first)
        else:
            raise ValueError('Required property \'first\' not present in DataProductReleaseCollection JSON')
        if (next := _dict.get('next')) is not None:
            args['next'] = NextPage.from_dict(next)
        if (total_results := _dict.get('total_results')) is not None:
            args['total_results'] = total_results
        if (releases := _dict.get('releases')) is not None:
            args['releases'] = [DataProductReleaseSummary.from_dict(v) for v in releases]
        else:
            raise ValueError('Required property \'releases\' not present in DataProductReleaseCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductReleaseCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'total_results') and self.total_results is not None:
            _dict['total_results'] = self.total_results
        if hasattr(self, 'releases') and self.releases is not None:
            releases_list = []
            for v in self.releases:
                if isinstance(v, dict):
                    releases_list.append(v)
                else:
                    releases_list.append(v.to_dict())
            _dict['releases'] = releases_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductReleaseCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductReleaseCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductReleaseCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductReleaseDataProduct:
    """
    Data product reference.

    :param str id: Data product identifier.
    :param DataProductDraftVersionRelease release: (optional) A data product draft
          version object.
    :param ContainerReference container: Container reference.
    """

    def __init__(
        self,
        id: str,
        container: 'ContainerReference',
        *,
        release: Optional['DataProductDraftVersionRelease'] = None,
    ) -> None:
        """
        Initialize a DataProductReleaseDataProduct object.

        :param str id: Data product identifier.
        :param ContainerReference container: Container reference.
        :param DataProductDraftVersionRelease release: (optional) A data product
               draft version object.
        """
        self.id = id
        self.release = release
        self.container = container

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductReleaseDataProduct':
        """Initialize a DataProductReleaseDataProduct object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in DataProductReleaseDataProduct JSON')
        if (release := _dict.get('release')) is not None:
            args['release'] = DataProductDraftVersionRelease.from_dict(release)
        if (container := _dict.get('container')) is not None:
            args['container'] = ContainerReference.from_dict(container)
        else:
            raise ValueError('Required property \'container\' not present in DataProductReleaseDataProduct JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductReleaseDataProduct object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'release') and self.release is not None:
            if isinstance(self.release, dict):
                _dict['release'] = self.release
            else:
                _dict['release'] = self.release.to_dict()
        if hasattr(self, 'container') and self.container is not None:
            if isinstance(self.container, dict):
                _dict['container'] = self.container
            else:
                _dict['container'] = self.container.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductReleaseDataProduct object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductReleaseDataProduct') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductReleaseDataProduct') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductReleaseSummary:
    """
    Summary of Data Product Version object.

    :param str version: The data product version number.
    :param str state: The state of the data product version.
    :param DataProductReleaseSummaryDataProduct data_product: Data product
          reference.
    :param str name: The name of the data product version. A name can contain
          letters, numbers, understores, dashes, spaces or periods. Names are mutable and
          reusable.
    :param str description: The description of the data product version.
    :param List[str] tags: (optional) Tags on the data product.
    :param List[UseCase] use_cases: (optional) A list of use cases associated with
          the data product version.
    :param List[str] types: Types of parts on the data product.
    :param List[ContractTerms] contract_terms: Contract terms binding various
          aspects of the data product.
    :param Domain domain: (optional) Domain that the data product version belongs
          to. If this is the first version of a data product, this field is required. If
          this is a new version of an existing data product, the domain will default to
          the domain of the previous version of the data product.
    :param List[DataProductPart] parts_out: (optional) The outgoing parts of this
          data product version to be delivered to consumers. If this is the first version
          of a data product, this field defaults to an empty list. If this is a new
          version of an existing data product, the data product parts will default to the
          parts list from the previous version of the data product.
    :param DataProductWorkflows workflows: (optional) The workflows associated with
          the data product version.
    :param bool dataview_enabled: (optional) Indicates whether the dataView has
          enabled for data product.
    :param str comments: (optional) Comments by a producer that are provided either
          at the time of data product version creation or retiring.
    :param AssetListAccessControl access_control: (optional) Access control object.
    :param datetime last_updated_at: (optional) Timestamp of last asset update.
    :param bool is_restricted: Indicates whether the data product is restricted or
          not. A restricted data product indicates that orders of the data product
          requires explicit approval before data is delivered.
    :param str id: The identifier of the data product version.
    :param AssetReference asset: The reference schema for a asset in a container.
    """

    def __init__(
        self,
        version: str,
        state: str,
        data_product: 'DataProductReleaseSummaryDataProduct',
        name: str,
        description: str,
        types: List[str],
        contract_terms: List['ContractTerms'],
        is_restricted: bool,
        id: str,
        asset: 'AssetReference',
        *,
        tags: Optional[List[str]] = None,
        use_cases: Optional[List['UseCase']] = None,
        domain: Optional['Domain'] = None,
        parts_out: Optional[List['DataProductPart']] = None,
        workflows: Optional['DataProductWorkflows'] = None,
        dataview_enabled: Optional[bool] = None,
        comments: Optional[str] = None,
        access_control: Optional['AssetListAccessControl'] = None,
        last_updated_at: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a DataProductReleaseSummary object.

        :param str version: The data product version number.
        :param str state: The state of the data product version.
        :param DataProductReleaseSummaryDataProduct data_product: Data product
               reference.
        :param str name: The name of the data product version. A name can contain
               letters, numbers, understores, dashes, spaces or periods. Names are mutable
               and reusable.
        :param str description: The description of the data product version.
        :param List[str] types: Types of parts on the data product.
        :param List[ContractTerms] contract_terms: Contract terms binding various
               aspects of the data product.
        :param bool is_restricted: Indicates whether the data product is restricted
               or not. A restricted data product indicates that orders of the data product
               requires explicit approval before data is delivered.
        :param str id: The identifier of the data product version.
        :param AssetReference asset: The reference schema for a asset in a
               container.
        :param List[str] tags: (optional) Tags on the data product.
        :param List[UseCase] use_cases: (optional) A list of use cases associated
               with the data product version.
        :param Domain domain: (optional) Domain that the data product version
               belongs to. If this is the first version of a data product, this field is
               required. If this is a new version of an existing data product, the domain
               will default to the domain of the previous version of the data product.
        :param List[DataProductPart] parts_out: (optional) The outgoing parts of
               this data product version to be delivered to consumers. If this is the
               first version of a data product, this field defaults to an empty list. If
               this is a new version of an existing data product, the data product parts
               will default to the parts list from the previous version of the data
               product.
        :param DataProductWorkflows workflows: (optional) The workflows associated
               with the data product version.
        :param bool dataview_enabled: (optional) Indicates whether the dataView has
               enabled for data product.
        :param str comments: (optional) Comments by a producer that are provided
               either at the time of data product version creation or retiring.
        :param AssetListAccessControl access_control: (optional) Access control
               object.
        :param datetime last_updated_at: (optional) Timestamp of last asset update.
        """
        self.version = version
        self.state = state
        self.data_product = data_product
        self.name = name
        self.description = description
        self.tags = tags
        self.use_cases = use_cases
        self.types = types
        self.contract_terms = contract_terms
        self.domain = domain
        self.parts_out = parts_out
        self.workflows = workflows
        self.dataview_enabled = dataview_enabled
        self.comments = comments
        self.access_control = access_control
        self.last_updated_at = last_updated_at
        self.is_restricted = is_restricted
        self.id = id
        self.asset = asset

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductReleaseSummary':
        """Initialize a DataProductReleaseSummary object from a json dictionary."""
        args = {}
        if (version := _dict.get('version')) is not None:
            args['version'] = version
        else:
            raise ValueError('Required property \'version\' not present in DataProductReleaseSummary JSON')
        if (state := _dict.get('state')) is not None:
            args['state'] = state
        else:
            raise ValueError('Required property \'state\' not present in DataProductReleaseSummary JSON')
        if (data_product := _dict.get('data_product')) is not None:
            args['data_product'] = DataProductReleaseSummaryDataProduct.from_dict(data_product)
        else:
            raise ValueError('Required property \'data_product\' not present in DataProductReleaseSummary JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in DataProductReleaseSummary JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        else:
            raise ValueError('Required property \'description\' not present in DataProductReleaseSummary JSON')
        if (tags := _dict.get('tags')) is not None:
            args['tags'] = tags
        if (use_cases := _dict.get('use_cases')) is not None:
            args['use_cases'] = [UseCase.from_dict(v) for v in use_cases]
        if (types := _dict.get('types')) is not None:
            args['types'] = types
        else:
            raise ValueError('Required property \'types\' not present in DataProductReleaseSummary JSON')
        if (contract_terms := _dict.get('contract_terms')) is not None:
            args['contract_terms'] = [ContractTerms.from_dict(v) for v in contract_terms]
        else:
            raise ValueError('Required property \'contract_terms\' not present in DataProductReleaseSummary JSON')
        if (domain := _dict.get('domain')) is not None:
            args['domain'] = Domain.from_dict(domain)
        if (parts_out := _dict.get('parts_out')) is not None:
            args['parts_out'] = [DataProductPart.from_dict(v) for v in parts_out]
        if (workflows := _dict.get('workflows')) is not None:
            args['workflows'] = DataProductWorkflows.from_dict(workflows)
        if (dataview_enabled := _dict.get('dataview_enabled')) is not None:
            args['dataview_enabled'] = dataview_enabled
        if (comments := _dict.get('comments')) is not None:
            args['comments'] = comments
        if (access_control := _dict.get('access_control')) is not None:
            args['access_control'] = AssetListAccessControl.from_dict(access_control)
        if (last_updated_at := _dict.get('last_updated_at')) is not None:
            args['last_updated_at'] = string_to_datetime(last_updated_at)
        if (is_restricted := _dict.get('is_restricted')) is not None:
            args['is_restricted'] = is_restricted
        else:
            raise ValueError('Required property \'is_restricted\' not present in DataProductReleaseSummary JSON')
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in DataProductReleaseSummary JSON')
        if (asset := _dict.get('asset')) is not None:
            args['asset'] = AssetReference.from_dict(asset)
        else:
            raise ValueError('Required property \'asset\' not present in DataProductReleaseSummary JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductReleaseSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'data_product') and self.data_product is not None:
            if isinstance(self.data_product, dict):
                _dict['data_product'] = self.data_product
            else:
                _dict['data_product'] = self.data_product.to_dict()
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'use_cases') and self.use_cases is not None:
            use_cases_list = []
            for v in self.use_cases:
                if isinstance(v, dict):
                    use_cases_list.append(v)
                else:
                    use_cases_list.append(v.to_dict())
            _dict['use_cases'] = use_cases_list
        if hasattr(self, 'types') and self.types is not None:
            _dict['types'] = self.types
        if hasattr(self, 'contract_terms') and self.contract_terms is not None:
            contract_terms_list = []
            for v in self.contract_terms:
                if isinstance(v, dict):
                    contract_terms_list.append(v)
                else:
                    contract_terms_list.append(v.to_dict())
            _dict['contract_terms'] = contract_terms_list
        if hasattr(self, 'domain') and self.domain is not None:
            if isinstance(self.domain, dict):
                _dict['domain'] = self.domain
            else:
                _dict['domain'] = self.domain.to_dict()
        if hasattr(self, 'parts_out') and self.parts_out is not None:
            parts_out_list = []
            for v in self.parts_out:
                if isinstance(v, dict):
                    parts_out_list.append(v)
                else:
                    parts_out_list.append(v.to_dict())
            _dict['parts_out'] = parts_out_list
        if hasattr(self, 'workflows') and self.workflows is not None:
            if isinstance(self.workflows, dict):
                _dict['workflows'] = self.workflows
            else:
                _dict['workflows'] = self.workflows.to_dict()
        if hasattr(self, 'dataview_enabled') and self.dataview_enabled is not None:
            _dict['dataview_enabled'] = self.dataview_enabled
        if hasattr(self, 'comments') and self.comments is not None:
            _dict['comments'] = self.comments
        if hasattr(self, 'access_control') and self.access_control is not None:
            if isinstance(self.access_control, dict):
                _dict['access_control'] = self.access_control
            else:
                _dict['access_control'] = self.access_control.to_dict()
        if hasattr(self, 'last_updated_at') and self.last_updated_at is not None:
            _dict['last_updated_at'] = datetime_to_string(self.last_updated_at)
        if hasattr(self, 'is_restricted') and self.is_restricted is not None:
            _dict['is_restricted'] = self.is_restricted
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'asset') and self.asset is not None:
            if isinstance(self.asset, dict):
                _dict['asset'] = self.asset
            else:
                _dict['asset'] = self.asset.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductReleaseSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductReleaseSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductReleaseSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        The state of the data product version.
        """

        DRAFT = 'draft'
        AVAILABLE = 'available'
        RETIRED = 'retired'


    class TypesEnum(str, Enum):
        """
        types.
        """

        DATA = 'data'
        CODE = 'code'



class DataProductReleaseSummaryDataProduct:
    """
    Data product reference.

    :param str id: Data product identifier.
    :param DataProductDraftVersionRelease release: (optional) A data product draft
          version object.
    :param ContainerReference container: Container reference.
    """

    def __init__(
        self,
        id: str,
        container: 'ContainerReference',
        *,
        release: Optional['DataProductDraftVersionRelease'] = None,
    ) -> None:
        """
        Initialize a DataProductReleaseSummaryDataProduct object.

        :param str id: Data product identifier.
        :param ContainerReference container: Container reference.
        :param DataProductDraftVersionRelease release: (optional) A data product
               draft version object.
        """
        self.id = id
        self.release = release
        self.container = container

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductReleaseSummaryDataProduct':
        """Initialize a DataProductReleaseSummaryDataProduct object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in DataProductReleaseSummaryDataProduct JSON')
        if (release := _dict.get('release')) is not None:
            args['release'] = DataProductDraftVersionRelease.from_dict(release)
        if (container := _dict.get('container')) is not None:
            args['container'] = ContainerReference.from_dict(container)
        else:
            raise ValueError('Required property \'container\' not present in DataProductReleaseSummaryDataProduct JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductReleaseSummaryDataProduct object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'release') and self.release is not None:
            if isinstance(self.release, dict):
                _dict['release'] = self.release
            else:
                _dict['release'] = self.release.to_dict()
        if hasattr(self, 'container') and self.container is not None:
            if isinstance(self.container, dict):
                _dict['container'] = self.container
            else:
                _dict['container'] = self.container.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductReleaseSummaryDataProduct object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductReleaseSummaryDataProduct') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductReleaseSummaryDataProduct') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductSummary:
    """
    Data Product Summary.

    :param str id: Data product identifier.
    :param DataProductDraftVersionRelease release: (optional) A data product draft
          version object.
    :param ContainerReference container: Container reference.
    :param str name: (optional) Data product name.
    """

    def __init__(
        self,
        id: str,
        container: 'ContainerReference',
        *,
        release: Optional['DataProductDraftVersionRelease'] = None,
        name: Optional[str] = None,
    ) -> None:
        """
        Initialize a DataProductSummary object.

        :param str id: Data product identifier.
        :param ContainerReference container: Container reference.
        :param DataProductDraftVersionRelease release: (optional) A data product
               draft version object.
        :param str name: (optional) Data product name.
        """
        self.id = id
        self.release = release
        self.container = container
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductSummary':
        """Initialize a DataProductSummary object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in DataProductSummary JSON')
        if (release := _dict.get('release')) is not None:
            args['release'] = DataProductDraftVersionRelease.from_dict(release)
        if (container := _dict.get('container')) is not None:
            args['container'] = ContainerReference.from_dict(container)
        else:
            raise ValueError('Required property \'container\' not present in DataProductSummary JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'release') and self.release is not None:
            if isinstance(self.release, dict):
                _dict['release'] = self.release
            else:
                _dict['release'] = self.release.to_dict()
        if hasattr(self, 'container') and self.container is not None:
            if isinstance(self.container, dict):
                _dict['container'] = self.container
            else:
                _dict['container'] = self.container.to_dict()
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductVersionCollection:
    """
    A collection of data product version summaries.

    :param int limit: Set a limit on the number of results returned.
    :param FirstPage first: First page in the collection.
    :param NextPage next: (optional) Next page in the collection.
    :param int total_results: (optional) Indicates the total number of results
          returned.
    :param List[DataProductVersionSummary] data_product_versions: Collection of data
          product versions.
    """

    def __init__(
        self,
        limit: int,
        first: 'FirstPage',
        data_product_versions: List['DataProductVersionSummary'],
        *,
        next: Optional['NextPage'] = None,
        total_results: Optional[int] = None,
    ) -> None:
        """
        Initialize a DataProductVersionCollection object.

        :param int limit: Set a limit on the number of results returned.
        :param FirstPage first: First page in the collection.
        :param List[DataProductVersionSummary] data_product_versions: Collection of
               data product versions.
        :param NextPage next: (optional) Next page in the collection.
        :param int total_results: (optional) Indicates the total number of results
               returned.
        """
        self.limit = limit
        self.first = first
        self.next = next
        self.total_results = total_results
        self.data_product_versions = data_product_versions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductVersionCollection':
        """Initialize a DataProductVersionCollection object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in DataProductVersionCollection JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = FirstPage.from_dict(first)
        else:
            raise ValueError('Required property \'first\' not present in DataProductVersionCollection JSON')
        if (next := _dict.get('next')) is not None:
            args['next'] = NextPage.from_dict(next)
        if (total_results := _dict.get('total_results')) is not None:
            args['total_results'] = total_results
        if (data_product_versions := _dict.get('data_product_versions')) is not None:
            args['data_product_versions'] = [DataProductVersionSummary.from_dict(v) for v in data_product_versions]
        else:
            raise ValueError('Required property \'data_product_versions\' not present in DataProductVersionCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductVersionCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'total_results') and self.total_results is not None:
            _dict['total_results'] = self.total_results
        if hasattr(self, 'data_product_versions') and self.data_product_versions is not None:
            data_product_versions_list = []
            for v in self.data_product_versions:
                if isinstance(v, dict):
                    data_product_versions_list.append(v)
                else:
                    data_product_versions_list.append(v.to_dict())
            _dict['data_product_versions'] = data_product_versions_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductVersionCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductVersionCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductVersionCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductVersionSummary:
    """
    Summary of Data Product Version object.

    :param str version: The data product version number.
    :param str state: The state of the data product version.
    :param DataProductVersionSummaryDataProduct data_product: Data product
          reference.
    :param str name: The name of the data product version. A name can contain
          letters, numbers, understores, dashes, spaces or periods. Names are mutable and
          reusable.
    :param str description: The description of the data product version.
    :param List[str] tags: (optional) Tags on the data product.
    :param List[UseCase] use_cases: (optional) A list of use cases associated with
          the data product version.
    :param List[str] types: Types of parts on the data product.
    :param List[ContractTerms] contract_terms: Contract terms binding various
          aspects of the data product.
    :param Domain domain: (optional) Domain that the data product version belongs
          to. If this is the first version of a data product, this field is required. If
          this is a new version of an existing data product, the domain will default to
          the domain of the previous version of the data product.
    :param List[DataProductPart] parts_out: (optional) The outgoing parts of this
          data product version to be delivered to consumers. If this is the first version
          of a data product, this field defaults to an empty list. If this is a new
          version of an existing data product, the data product parts will default to the
          parts list from the previous version of the data product.
    :param DataProductWorkflows workflows: (optional) The workflows associated with
          the data product version.
    :param bool dataview_enabled: (optional) Indicates whether the dataView has
          enabled for data product.
    :param str comments: (optional) Comments by a producer that are provided either
          at the time of data product version creation or retiring.
    :param AssetListAccessControl access_control: (optional) Access control object.
    :param datetime last_updated_at: (optional) Timestamp of last asset update.
    :param bool is_restricted: Indicates whether the data product is restricted or
          not. A restricted data product indicates that orders of the data product
          requires explicit approval before data is delivered.
    :param str id: The identifier of the data product version.
    :param AssetReference asset: The reference schema for a asset in a container.
    """

    def __init__(
        self,
        version: str,
        state: str,
        data_product: 'DataProductVersionSummaryDataProduct',
        name: str,
        description: str,
        types: List[str],
        contract_terms: List['ContractTerms'],
        is_restricted: bool,
        id: str,
        asset: 'AssetReference',
        *,
        tags: Optional[List[str]] = None,
        use_cases: Optional[List['UseCase']] = None,
        domain: Optional['Domain'] = None,
        parts_out: Optional[List['DataProductPart']] = None,
        workflows: Optional['DataProductWorkflows'] = None,
        dataview_enabled: Optional[bool] = None,
        comments: Optional[str] = None,
        access_control: Optional['AssetListAccessControl'] = None,
        last_updated_at: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a DataProductVersionSummary object.

        :param str version: The data product version number.
        :param str state: The state of the data product version.
        :param DataProductVersionSummaryDataProduct data_product: Data product
               reference.
        :param str name: The name of the data product version. A name can contain
               letters, numbers, understores, dashes, spaces or periods. Names are mutable
               and reusable.
        :param str description: The description of the data product version.
        :param List[str] types: Types of parts on the data product.
        :param List[ContractTerms] contract_terms: Contract terms binding various
               aspects of the data product.
        :param bool is_restricted: Indicates whether the data product is restricted
               or not. A restricted data product indicates that orders of the data product
               requires explicit approval before data is delivered.
        :param str id: The identifier of the data product version.
        :param AssetReference asset: The reference schema for a asset in a
               container.
        :param List[str] tags: (optional) Tags on the data product.
        :param List[UseCase] use_cases: (optional) A list of use cases associated
               with the data product version.
        :param Domain domain: (optional) Domain that the data product version
               belongs to. If this is the first version of a data product, this field is
               required. If this is a new version of an existing data product, the domain
               will default to the domain of the previous version of the data product.
        :param List[DataProductPart] parts_out: (optional) The outgoing parts of
               this data product version to be delivered to consumers. If this is the
               first version of a data product, this field defaults to an empty list. If
               this is a new version of an existing data product, the data product parts
               will default to the parts list from the previous version of the data
               product.
        :param DataProductWorkflows workflows: (optional) The workflows associated
               with the data product version.
        :param bool dataview_enabled: (optional) Indicates whether the dataView has
               enabled for data product.
        :param str comments: (optional) Comments by a producer that are provided
               either at the time of data product version creation or retiring.
        :param AssetListAccessControl access_control: (optional) Access control
               object.
        :param datetime last_updated_at: (optional) Timestamp of last asset update.
        """
        self.version = version
        self.state = state
        self.data_product = data_product
        self.name = name
        self.description = description
        self.tags = tags
        self.use_cases = use_cases
        self.types = types
        self.contract_terms = contract_terms
        self.domain = domain
        self.parts_out = parts_out
        self.workflows = workflows
        self.dataview_enabled = dataview_enabled
        self.comments = comments
        self.access_control = access_control
        self.last_updated_at = last_updated_at
        self.is_restricted = is_restricted
        self.id = id
        self.asset = asset

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductVersionSummary':
        """Initialize a DataProductVersionSummary object from a json dictionary."""
        args = {}
        if (version := _dict.get('version')) is not None:
            args['version'] = version
        else:
            raise ValueError('Required property \'version\' not present in DataProductVersionSummary JSON')
        if (state := _dict.get('state')) is not None:
            args['state'] = state
        else:
            raise ValueError('Required property \'state\' not present in DataProductVersionSummary JSON')
        if (data_product := _dict.get('data_product')) is not None:
            args['data_product'] = DataProductVersionSummaryDataProduct.from_dict(data_product)
        else:
            raise ValueError('Required property \'data_product\' not present in DataProductVersionSummary JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in DataProductVersionSummary JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        else:
            raise ValueError('Required property \'description\' not present in DataProductVersionSummary JSON')
        if (tags := _dict.get('tags')) is not None:
            args['tags'] = tags
        if (use_cases := _dict.get('use_cases')) is not None:
            args['use_cases'] = [UseCase.from_dict(v) for v in use_cases]
        if (types := _dict.get('types')) is not None:
            args['types'] = types
        else:
            raise ValueError('Required property \'types\' not present in DataProductVersionSummary JSON')
        if (contract_terms := _dict.get('contract_terms')) is not None:
            args['contract_terms'] = [ContractTerms.from_dict(v) for v in contract_terms]
        else:
            raise ValueError('Required property \'contract_terms\' not present in DataProductVersionSummary JSON')
        if (domain := _dict.get('domain')) is not None:
            args['domain'] = Domain.from_dict(domain)
        if (parts_out := _dict.get('parts_out')) is not None:
            args['parts_out'] = [DataProductPart.from_dict(v) for v in parts_out]
        if (workflows := _dict.get('workflows')) is not None:
            args['workflows'] = DataProductWorkflows.from_dict(workflows)
        if (dataview_enabled := _dict.get('dataview_enabled')) is not None:
            args['dataview_enabled'] = dataview_enabled
        if (comments := _dict.get('comments')) is not None:
            args['comments'] = comments
        if (access_control := _dict.get('access_control')) is not None:
            args['access_control'] = AssetListAccessControl.from_dict(access_control)
        if (last_updated_at := _dict.get('last_updated_at')) is not None:
            args['last_updated_at'] = string_to_datetime(last_updated_at)
        if (is_restricted := _dict.get('is_restricted')) is not None:
            args['is_restricted'] = is_restricted
        else:
            raise ValueError('Required property \'is_restricted\' not present in DataProductVersionSummary JSON')
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in DataProductVersionSummary JSON')
        if (asset := _dict.get('asset')) is not None:
            args['asset'] = AssetReference.from_dict(asset)
        else:
            raise ValueError('Required property \'asset\' not present in DataProductVersionSummary JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductVersionSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'data_product') and self.data_product is not None:
            if isinstance(self.data_product, dict):
                _dict['data_product'] = self.data_product
            else:
                _dict['data_product'] = self.data_product.to_dict()
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'use_cases') and self.use_cases is not None:
            use_cases_list = []
            for v in self.use_cases:
                if isinstance(v, dict):
                    use_cases_list.append(v)
                else:
                    use_cases_list.append(v.to_dict())
            _dict['use_cases'] = use_cases_list
        if hasattr(self, 'types') and self.types is not None:
            _dict['types'] = self.types
        if hasattr(self, 'contract_terms') and self.contract_terms is not None:
            contract_terms_list = []
            for v in self.contract_terms:
                if isinstance(v, dict):
                    contract_terms_list.append(v)
                else:
                    contract_terms_list.append(v.to_dict())
            _dict['contract_terms'] = contract_terms_list
        if hasattr(self, 'domain') and self.domain is not None:
            if isinstance(self.domain, dict):
                _dict['domain'] = self.domain
            else:
                _dict['domain'] = self.domain.to_dict()
        if hasattr(self, 'parts_out') and self.parts_out is not None:
            parts_out_list = []
            for v in self.parts_out:
                if isinstance(v, dict):
                    parts_out_list.append(v)
                else:
                    parts_out_list.append(v.to_dict())
            _dict['parts_out'] = parts_out_list
        if hasattr(self, 'workflows') and self.workflows is not None:
            if isinstance(self.workflows, dict):
                _dict['workflows'] = self.workflows
            else:
                _dict['workflows'] = self.workflows.to_dict()
        if hasattr(self, 'dataview_enabled') and self.dataview_enabled is not None:
            _dict['dataview_enabled'] = self.dataview_enabled
        if hasattr(self, 'comments') and self.comments is not None:
            _dict['comments'] = self.comments
        if hasattr(self, 'access_control') and self.access_control is not None:
            if isinstance(self.access_control, dict):
                _dict['access_control'] = self.access_control
            else:
                _dict['access_control'] = self.access_control.to_dict()
        if hasattr(self, 'last_updated_at') and self.last_updated_at is not None:
            _dict['last_updated_at'] = datetime_to_string(self.last_updated_at)
        if hasattr(self, 'is_restricted') and self.is_restricted is not None:
            _dict['is_restricted'] = self.is_restricted
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'asset') and self.asset is not None:
            if isinstance(self.asset, dict):
                _dict['asset'] = self.asset
            else:
                _dict['asset'] = self.asset.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductVersionSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductVersionSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductVersionSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        The state of the data product version.
        """

        DRAFT = 'draft'
        AVAILABLE = 'available'
        RETIRED = 'retired'


    class TypesEnum(str, Enum):
        """
        types.
        """

        DATA = 'data'
        CODE = 'code'



class DataProductVersionSummaryDataProduct:
    """
    Data product reference.

    :param str id: Data product identifier.
    :param DataProductDraftVersionRelease release: (optional) A data product draft
          version object.
    :param ContainerReference container: Container reference.
    """

    def __init__(
        self,
        id: str,
        container: 'ContainerReference',
        *,
        release: Optional['DataProductDraftVersionRelease'] = None,
    ) -> None:
        """
        Initialize a DataProductVersionSummaryDataProduct object.

        :param str id: Data product identifier.
        :param ContainerReference container: Container reference.
        :param DataProductDraftVersionRelease release: (optional) A data product
               draft version object.
        """
        self.id = id
        self.release = release
        self.container = container

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductVersionSummaryDataProduct':
        """Initialize a DataProductVersionSummaryDataProduct object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in DataProductVersionSummaryDataProduct JSON')
        if (release := _dict.get('release')) is not None:
            args['release'] = DataProductDraftVersionRelease.from_dict(release)
        if (container := _dict.get('container')) is not None:
            args['container'] = ContainerReference.from_dict(container)
        else:
            raise ValueError('Required property \'container\' not present in DataProductVersionSummaryDataProduct JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductVersionSummaryDataProduct object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'release') and self.release is not None:
            if isinstance(self.release, dict):
                _dict['release'] = self.release
            else:
                _dict['release'] = self.release.to_dict()
        if hasattr(self, 'container') and self.container is not None:
            if isinstance(self.container, dict):
                _dict['container'] = self.container
            else:
                _dict['container'] = self.container.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductVersionSummaryDataProduct object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductVersionSummaryDataProduct') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductVersionSummaryDataProduct') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductWorkflows:
    """
    The workflows associated with the data product version.

    :param DataProductOrderAccessRequest order_access_request: (optional) The
          approval workflows associated with the data product version.
    """

    def __init__(
        self,
        *,
        order_access_request: Optional['DataProductOrderAccessRequest'] = None,
    ) -> None:
        """
        Initialize a DataProductWorkflows object.

        :param DataProductOrderAccessRequest order_access_request: (optional) The
               approval workflows associated with the data product version.
        """
        self.order_access_request = order_access_request

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductWorkflows':
        """Initialize a DataProductWorkflows object from a json dictionary."""
        args = {}
        if (order_access_request := _dict.get('order_access_request')) is not None:
            args['order_access_request'] = DataProductOrderAccessRequest.from_dict(order_access_request)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductWorkflows object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'order_access_request') and self.order_access_request is not None:
            if isinstance(self.order_access_request, dict):
                _dict['order_access_request'] = self.order_access_request
            else:
                _dict['order_access_request'] = self.order_access_request.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductWorkflows object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductWorkflows') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductWorkflows') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeliveryMethod:
    """
    DeliveryMethod.

    :param str id: The ID of the delivery method.
    :param ContainerReference container: Container reference.
    :param DeliveryMethodPropertiesModel getproperties: (optional) The propertiess
          of the delivery method.
    """

    def __init__(
        self,
        id: str,
        container: 'ContainerReference',
        *,
        getproperties: Optional['DeliveryMethodPropertiesModel'] = None,
    ) -> None:
        """
        Initialize a DeliveryMethod object.

        :param str id: The ID of the delivery method.
        :param ContainerReference container: Container reference.
        :param DeliveryMethodPropertiesModel getproperties: (optional) The
               propertiess of the delivery method.
        """
        self.id = id
        self.container = container
        self.getproperties = getproperties

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeliveryMethod':
        """Initialize a DeliveryMethod object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in DeliveryMethod JSON')
        if (container := _dict.get('container')) is not None:
            args['container'] = ContainerReference.from_dict(container)
        else:
            raise ValueError('Required property \'container\' not present in DeliveryMethod JSON')
        if (getproperties := _dict.get('getproperties')) is not None:
            args['getproperties'] = DeliveryMethodPropertiesModel.from_dict(getproperties)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeliveryMethod object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'container') and self.container is not None:
            if isinstance(self.container, dict):
                _dict['container'] = self.container
            else:
                _dict['container'] = self.container.to_dict()
        if hasattr(self, 'getproperties') and self.getproperties is not None:
            if isinstance(self.getproperties, dict):
                _dict['getproperties'] = self.getproperties
            else:
                _dict['getproperties'] = self.getproperties.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeliveryMethod object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeliveryMethod') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeliveryMethod') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeliveryMethodPropertiesModel:
    """
    The propertiess of the delivery method.

    :param ProducerInputModel producer_input: (optional) Parameters for delivery
          that are set by a data product producer.
    """

    def __init__(
        self,
        *,
        producer_input: Optional['ProducerInputModel'] = None,
    ) -> None:
        """
        Initialize a DeliveryMethodPropertiesModel object.

        :param ProducerInputModel producer_input: (optional) Parameters for
               delivery that are set by a data product producer.
        """
        self.producer_input = producer_input

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeliveryMethodPropertiesModel':
        """Initialize a DeliveryMethodPropertiesModel object from a json dictionary."""
        args = {}
        if (producer_input := _dict.get('producer_input')) is not None:
            args['producer_input'] = ProducerInputModel.from_dict(producer_input)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeliveryMethodPropertiesModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'producer_input') and self.producer_input is not None:
            if isinstance(self.producer_input, dict):
                _dict['producer_input'] = self.producer_input
            else:
                _dict['producer_input'] = self.producer_input.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeliveryMethodPropertiesModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeliveryMethodPropertiesModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeliveryMethodPropertiesModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Description:
    """
    Description details of a data contract.

    :param str purpose: (optional) Intended purpose for the provided data.
    :param str limitations: (optional) Technical, compliance, and legal limitations
          for data use.
    :param str usage: (optional) Recommended usage of the data.
    :param List[ContractTermsMoreInfo] more_info: (optional) List of links to
          sources that provide more details on the dataset.
    :param str custom_properties: (optional) Custom properties that are not part of
          the standard.
    """

    def __init__(
        self,
        *,
        purpose: Optional[str] = None,
        limitations: Optional[str] = None,
        usage: Optional[str] = None,
        more_info: Optional[List['ContractTermsMoreInfo']] = None,
        custom_properties: Optional[str] = None,
    ) -> None:
        """
        Initialize a Description object.

        :param str purpose: (optional) Intended purpose for the provided data.
        :param str limitations: (optional) Technical, compliance, and legal
               limitations for data use.
        :param str usage: (optional) Recommended usage of the data.
        :param List[ContractTermsMoreInfo] more_info: (optional) List of links to
               sources that provide more details on the dataset.
        :param str custom_properties: (optional) Custom properties that are not
               part of the standard.
        """
        self.purpose = purpose
        self.limitations = limitations
        self.usage = usage
        self.more_info = more_info
        self.custom_properties = custom_properties

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Description':
        """Initialize a Description object from a json dictionary."""
        args = {}
        if (purpose := _dict.get('purpose')) is not None:
            args['purpose'] = purpose
        if (limitations := _dict.get('limitations')) is not None:
            args['limitations'] = limitations
        if (usage := _dict.get('usage')) is not None:
            args['usage'] = usage
        if (more_info := _dict.get('more_info')) is not None:
            args['more_info'] = [ContractTermsMoreInfo.from_dict(v) for v in more_info]
        if (custom_properties := _dict.get('custom_properties')) is not None:
            args['custom_properties'] = custom_properties
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Description object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'purpose') and self.purpose is not None:
            _dict['purpose'] = self.purpose
        if hasattr(self, 'limitations') and self.limitations is not None:
            _dict['limitations'] = self.limitations
        if hasattr(self, 'usage') and self.usage is not None:
            _dict['usage'] = self.usage
        if hasattr(self, 'more_info') and self.more_info is not None:
            more_info_list = []
            for v in self.more_info:
                if isinstance(v, dict):
                    more_info_list.append(v)
                else:
                    more_info_list.append(v.to_dict())
            _dict['more_info'] = more_info_list
        if hasattr(self, 'custom_properties') and self.custom_properties is not None:
            _dict['custom_properties'] = self.custom_properties
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Description object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Description') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Description') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Domain:
    """
    Domain that the data product version belongs to. If this is the first version of a
    data product, this field is required. If this is a new version of an existing data
    product, the domain will default to the domain of the previous version of the data
    product.

    :param str id: The ID of the domain.
    :param str name: (optional) The display name of the domain.
    :param ContainerReference container: (optional) Container reference.
    """

    def __init__(
        self,
        id: str,
        *,
        name: Optional[str] = None,
        container: Optional['ContainerReference'] = None,
    ) -> None:
        """
        Initialize a Domain object.

        :param str id: The ID of the domain.
        :param str name: (optional) The display name of the domain.
        :param ContainerReference container: (optional) Container reference.
        """
        self.id = id
        self.name = name
        self.container = container

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Domain':
        """Initialize a Domain object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in Domain JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (container := _dict.get('container')) is not None:
            args['container'] = ContainerReference.from_dict(container)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Domain object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'container') and self.container is not None:
            if isinstance(self.container, dict):
                _dict['container'] = self.container
            else:
                _dict['container'] = self.container.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Domain object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Domain') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Domain') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EngineDetailsModel:
    """
    Engine details as defined by the data product producer.

    :param str display_name: (optional) The name of the engine defined by the data
          product producer.
    :param str engine_id: (optional) The id of the engine defined by the data
          product producer.
    :param str engine_port: (optional) The port of the engine defined by the data
          product producer.
    :param str engine_host: (optional) The host of the engine defined by the data
          product producer.
    :param List[str] associated_catalogs: (optional) The list of associated
          catalogs.
    """

    def __init__(
        self,
        *,
        display_name: Optional[str] = None,
        engine_id: Optional[str] = None,
        engine_port: Optional[str] = None,
        engine_host: Optional[str] = None,
        associated_catalogs: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a EngineDetailsModel object.

        :param str display_name: (optional) The name of the engine defined by the
               data product producer.
        :param str engine_id: (optional) The id of the engine defined by the data
               product producer.
        :param str engine_port: (optional) The port of the engine defined by the
               data product producer.
        :param str engine_host: (optional) The host of the engine defined by the
               data product producer.
        :param List[str] associated_catalogs: (optional) The list of associated
               catalogs.
        """
        self.display_name = display_name
        self.engine_id = engine_id
        self.engine_port = engine_port
        self.engine_host = engine_host
        self.associated_catalogs = associated_catalogs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EngineDetailsModel':
        """Initialize a EngineDetailsModel object from a json dictionary."""
        args = {}
        if (display_name := _dict.get('display_name')) is not None:
            args['display_name'] = display_name
        if (engine_id := _dict.get('engine_id')) is not None:
            args['engine_id'] = engine_id
        if (engine_port := _dict.get('engine_port')) is not None:
            args['engine_port'] = engine_port
        if (engine_host := _dict.get('engine_host')) is not None:
            args['engine_host'] = engine_host
        if (associated_catalogs := _dict.get('associated_catalogs')) is not None:
            args['associated_catalogs'] = associated_catalogs
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EngineDetailsModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'display_name') and self.display_name is not None:
            _dict['display_name'] = self.display_name
        if hasattr(self, 'engine_id') and self.engine_id is not None:
            _dict['engine_id'] = self.engine_id
        if hasattr(self, 'engine_port') and self.engine_port is not None:
            _dict['engine_port'] = self.engine_port
        if hasattr(self, 'engine_host') and self.engine_host is not None:
            _dict['engine_host'] = self.engine_host
        if hasattr(self, 'associated_catalogs') and self.associated_catalogs is not None:
            _dict['associated_catalogs'] = self.associated_catalogs
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EngineDetailsModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EngineDetailsModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EngineDetailsModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ErrorExtraResource:
    """
    Detailed error information.

    :param str id: (optional) Error id.
    :param datetime timestamp: (optional) Timestamp of the error.
    :param str environment_name: (optional) Environment where the error occurred.
    :param int http_status: (optional) Http status code.
    :param int source_cluster: (optional) Source cluster of the error.
    :param int source_component: (optional) Source component of the error.
    :param int transaction_id: (optional) Transaction id of the request.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        timestamp: Optional[datetime] = None,
        environment_name: Optional[str] = None,
        http_status: Optional[int] = None,
        source_cluster: Optional[int] = None,
        source_component: Optional[int] = None,
        transaction_id: Optional[int] = None,
    ) -> None:
        """
        Initialize a ErrorExtraResource object.

        :param str id: (optional) Error id.
        :param datetime timestamp: (optional) Timestamp of the error.
        :param str environment_name: (optional) Environment where the error
               occurred.
        :param int http_status: (optional) Http status code.
        :param int source_cluster: (optional) Source cluster of the error.
        :param int source_component: (optional) Source component of the error.
        :param int transaction_id: (optional) Transaction id of the request.
        """
        self.id = id
        self.timestamp = timestamp
        self.environment_name = environment_name
        self.http_status = http_status
        self.source_cluster = source_cluster
        self.source_component = source_component
        self.transaction_id = transaction_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ErrorExtraResource':
        """Initialize a ErrorExtraResource object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (timestamp := _dict.get('timestamp')) is not None:
            args['timestamp'] = string_to_datetime(timestamp)
        if (environment_name := _dict.get('environment_name')) is not None:
            args['environment_name'] = environment_name
        if (http_status := _dict.get('http_status')) is not None:
            args['http_status'] = http_status
        if (source_cluster := _dict.get('source_cluster')) is not None:
            args['source_cluster'] = source_cluster
        if (source_component := _dict.get('source_component')) is not None:
            args['source_component'] = source_component
        if (transaction_id := _dict.get('transaction_id')) is not None:
            args['transaction_id'] = transaction_id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ErrorExtraResource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'timestamp') and self.timestamp is not None:
            _dict['timestamp'] = datetime_to_string(self.timestamp)
        if hasattr(self, 'environment_name') and self.environment_name is not None:
            _dict['environment_name'] = self.environment_name
        if hasattr(self, 'http_status') and self.http_status is not None:
            _dict['http_status'] = self.http_status
        if hasattr(self, 'source_cluster') and self.source_cluster is not None:
            _dict['source_cluster'] = self.source_cluster
        if hasattr(self, 'source_component') and self.source_component is not None:
            _dict['source_component'] = self.source_component
        if hasattr(self, 'transaction_id') and self.transaction_id is not None:
            _dict['transaction_id'] = self.transaction_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ErrorExtraResource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ErrorExtraResource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ErrorExtraResource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ErrorMessage:
    """
    Contains the code and details.

    :param str code: The error code.
    :param str message: The error details.
    """

    def __init__(
        self,
        code: str,
        message: str,
    ) -> None:
        """
        Initialize a ErrorMessage object.

        :param str code: The error code.
        :param str message: The error details.
        """
        self.code = code
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ErrorMessage':
        """Initialize a ErrorMessage object from a json dictionary."""
        args = {}
        if (code := _dict.get('code')) is not None:
            args['code'] = code
        else:
            raise ValueError('Required property \'code\' not present in ErrorMessage JSON')
        if (message := _dict.get('message')) is not None:
            args['message'] = message
        else:
            raise ValueError('Required property \'message\' not present in ErrorMessage JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ErrorMessage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'code') and self.code is not None:
            _dict['code'] = self.code
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ErrorMessage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ErrorMessage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ErrorMessage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ErrorModelResource:
    """
    Detailed error information.

    :param str code: Error code.
    :param str message: (optional) Error message.
    :param ErrorExtraResource extra: (optional) Detailed error information.
    :param str more_info: (optional) More info message.
    """

    def __init__(
        self,
        code: str,
        *,
        message: Optional[str] = None,
        extra: Optional['ErrorExtraResource'] = None,
        more_info: Optional[str] = None,
    ) -> None:
        """
        Initialize a ErrorModelResource object.

        :param str code: Error code.
        :param str message: (optional) Error message.
        :param ErrorExtraResource extra: (optional) Detailed error information.
        :param str more_info: (optional) More info message.
        """
        self.code = code
        self.message = message
        self.extra = extra
        self.more_info = more_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ErrorModelResource':
        """Initialize a ErrorModelResource object from a json dictionary."""
        args = {}
        if (code := _dict.get('code')) is not None:
            args['code'] = code
        else:
            raise ValueError('Required property \'code\' not present in ErrorModelResource JSON')
        if (message := _dict.get('message')) is not None:
            args['message'] = message
        if (extra := _dict.get('extra')) is not None:
            args['extra'] = ErrorExtraResource.from_dict(extra)
        if (more_info := _dict.get('more_info')) is not None:
            args['more_info'] = more_info
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ErrorModelResource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'code') and self.code is not None:
            _dict['code'] = self.code
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        if hasattr(self, 'extra') and self.extra is not None:
            if isinstance(self.extra, dict):
                _dict['extra'] = self.extra
            else:
                _dict['extra'] = self.extra.to_dict()
        if hasattr(self, 'more_info') and self.more_info is not None:
            _dict['more_info'] = self.more_info
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ErrorModelResource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ErrorModelResource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ErrorModelResource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class CodeEnum(str, Enum):
        """
        Error code.
        """

        REQUEST_BODY_ERROR = 'request_body_error'
        MISSING_REQUIRED_VALUE = 'missing_required_value'
        INVALID_PARAMETER = 'invalid_parameter'
        DOES_NOT_EXIST = 'does_not_exist'
        ALREADY_EXISTS = 'already_exists'
        NOT_AUTHENTICATED = 'not_authenticated'
        NOT_AUTHORIZED = 'not_authorized'
        FORBIDDEN = 'forbidden'
        CONFLICT = 'conflict'
        CREATE_ERROR = 'create_error'
        FETCH_ERROR = 'fetch_error'
        UPDATE_ERROR = 'update_error'
        DELETE_ERROR = 'delete_error'
        PATCH_ERROR = 'patch_error'
        DATA_ERROR = 'data_error'
        DATABASE_ERROR = 'database_error'
        DATABASE_QUERY_ERROR = 'database_query_error'
        CONSTRAINT_VIOLATION = 'constraint_violation'
        UNABLE_TO_PERFORM = 'unable_to_perform'
        TOO_MANY_REQUESTS = 'too_many_requests'
        DEPENDENT_SERVICE_ERROR = 'dependent_service_error'
        CONFIGURATION_ERROR = 'configuration_error'
        UNEXPECTED_EXCEPTION = 'unexpected_exception'
        GOVERNANCE_POLICY_DENIAL = 'governance_policy_denial'
        DATABASE_USAGE_LIMITS = 'database_usage_limits'
        INACTIVE_USER = 'inactive_user'
        ENTITLEMENT_ENFORCEMENT = 'entitlement_enforcement'
        DELETED = 'deleted'
        NOT_IMPLEMENTED = 'not_implemented'
        FEATURE_NOT_ENABLED = 'feature_not_enabled'
        MISSING_ASSET_DETAILS = 'missing_asset_details'



class FirstPage:
    """
    First page in the collection.

    :param str href: Link to the first page in the collection.
    """

    def __init__(
        self,
        href: str,
    ) -> None:
        """
        Initialize a FirstPage object.

        :param str href: Link to the first page in the collection.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FirstPage':
        """Initialize a FirstPage object from a json dictionary."""
        args = {}
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in FirstPage JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FirstPage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FirstPage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FirstPage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FirstPage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class InitializeResource:
    """
    Resource defining initialization parameters.

    :param ContainerReference container: (optional) Container reference.
    :param str href: (optional) Link to monitor the status of the initialize
          operation.
    :param str status: Status of the initialize operation.
    :param str trace: (optional) The id to trace the failed initialization
          operation.
    :param List[ErrorModelResource] errors: (optional) Set of errors on the latest
          initialization request.
    :param datetime last_started_at: (optional) Start time of the last
          initialization.
    :param datetime last_finished_at: (optional) End time of the last
          initialization.
    :param List[InitializedOption] initialized_options: (optional) Initialized
          options.
    :param ProvidedCatalogWorkflows workflows: (optional) Resource defining provided
          workflow definitions.
    """

    def __init__(
        self,
        status: str,
        *,
        container: Optional['ContainerReference'] = None,
        href: Optional[str] = None,
        trace: Optional[str] = None,
        errors: Optional[List['ErrorModelResource']] = None,
        last_started_at: Optional[datetime] = None,
        last_finished_at: Optional[datetime] = None,
        initialized_options: Optional[List['InitializedOption']] = None,
        workflows: Optional['ProvidedCatalogWorkflows'] = None,
    ) -> None:
        """
        Initialize a InitializeResource object.

        :param str status: Status of the initialize operation.
        :param ContainerReference container: (optional) Container reference.
        :param str href: (optional) Link to monitor the status of the initialize
               operation.
        :param str trace: (optional) The id to trace the failed initialization
               operation.
        :param List[ErrorModelResource] errors: (optional) Set of errors on the
               latest initialization request.
        :param datetime last_started_at: (optional) Start time of the last
               initialization.
        :param datetime last_finished_at: (optional) End time of the last
               initialization.
        :param List[InitializedOption] initialized_options: (optional) Initialized
               options.
        :param ProvidedCatalogWorkflows workflows: (optional) Resource defining
               provided workflow definitions.
        """
        self.container = container
        self.href = href
        self.status = status
        self.trace = trace
        self.errors = errors
        self.last_started_at = last_started_at
        self.last_finished_at = last_finished_at
        self.initialized_options = initialized_options
        self.workflows = workflows

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InitializeResource':
        """Initialize a InitializeResource object from a json dictionary."""
        args = {}
        if (container := _dict.get('container')) is not None:
            args['container'] = ContainerReference.from_dict(container)
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in InitializeResource JSON')
        if (trace := _dict.get('trace')) is not None:
            args['trace'] = trace
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = [ErrorModelResource.from_dict(v) for v in errors]
        if (last_started_at := _dict.get('last_started_at')) is not None:
            args['last_started_at'] = string_to_datetime(last_started_at)
        if (last_finished_at := _dict.get('last_finished_at')) is not None:
            args['last_finished_at'] = string_to_datetime(last_finished_at)
        if (initialized_options := _dict.get('initialized_options')) is not None:
            args['initialized_options'] = [InitializedOption.from_dict(v) for v in initialized_options]
        if (workflows := _dict.get('workflows')) is not None:
            args['workflows'] = ProvidedCatalogWorkflows.from_dict(workflows)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InitializeResource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'container') and self.container is not None:
            if isinstance(self.container, dict):
                _dict['container'] = self.container
            else:
                _dict['container'] = self.container.to_dict()
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'trace') and self.trace is not None:
            _dict['trace'] = self.trace
        if hasattr(self, 'errors') and self.errors is not None:
            errors_list = []
            for v in self.errors:
                if isinstance(v, dict):
                    errors_list.append(v)
                else:
                    errors_list.append(v.to_dict())
            _dict['errors'] = errors_list
        if hasattr(self, 'last_started_at') and self.last_started_at is not None:
            _dict['last_started_at'] = datetime_to_string(self.last_started_at)
        if hasattr(self, 'last_finished_at') and self.last_finished_at is not None:
            _dict['last_finished_at'] = datetime_to_string(self.last_finished_at)
        if hasattr(self, 'initialized_options') and self.initialized_options is not None:
            initialized_options_list = []
            for v in self.initialized_options:
                if isinstance(v, dict):
                    initialized_options_list.append(v)
                else:
                    initialized_options_list.append(v.to_dict())
            _dict['initialized_options'] = initialized_options_list
        if hasattr(self, 'workflows') and self.workflows is not None:
            if isinstance(self.workflows, dict):
                _dict['workflows'] = self.workflows
            else:
                _dict['workflows'] = self.workflows.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this InitializeResource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InitializeResource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InitializeResource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        Status of the initialize operation.
        """

        NOT_STARTED = 'not_started'
        IN_PROGRESS = 'in_progress'
        SUCCEEDED = 'succeeded'
        FAILED = 'failed'



class InitializeSubDomain:
    """
    The subdomain for a data product domain.

    :param str name: (optional) The name of the data product subdomain.
    :param str id: (optional) The identifier of the data product subdomain.
    :param str description: (optional) The description of the data product
          subdomain.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        id: Optional[str] = None,
        description: Optional[str] = None,
    ) -> None:
        """
        Initialize a InitializeSubDomain object.

        :param str name: (optional) The name of the data product subdomain.
        :param str id: (optional) The identifier of the data product subdomain.
        :param str description: (optional) The description of the data product
               subdomain.
        """
        self.name = name
        self.id = id
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InitializeSubDomain':
        """Initialize a InitializeSubDomain object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InitializeSubDomain object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this InitializeSubDomain object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InitializeSubDomain') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InitializeSubDomain') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class InitializedOption:
    """
    List of options successfully initialized.

    :param str name: (optional) The name of the option.
    :param int version: (optional) The version of the option.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        version: Optional[int] = None,
    ) -> None:
        """
        Initialize a InitializedOption object.

        :param str name: (optional) The name of the option.
        :param int version: (optional) The version of the option.
        """
        self.name = name
        self.version = version

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InitializedOption':
        """Initialize a InitializedOption object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (version := _dict.get('version')) is not None:
            args['version'] = version
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InitializedOption object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this InitializedOption object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InitializedOption') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InitializedOption') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class JsonPatchOperation:
    """
    This model represents an individual patch operation to be performed on a JSON
    document, as defined by RFC 6902.

    :param str op: The operation to be performed.
    :param str path: The JSON Pointer that identifies the field that is the target
          of the operation.
    :param str from_: (optional) The JSON Pointer that identifies the field that is
          the source of the operation.
    :param object value: (optional) The value to be used within the operation.
    """

    def __init__(
        self,
        op: str,
        path: str,
        *,
        from_: Optional[str] = None,
        value: Optional[object] = None,
    ) -> None:
        """
        Initialize a JsonPatchOperation object.

        :param str op: The operation to be performed.
        :param str path: The JSON Pointer that identifies the field that is the
               target of the operation.
        :param str from_: (optional) The JSON Pointer that identifies the field
               that is the source of the operation.
        :param object value: (optional) The value to be used within the operation.
        """
        self.op = op
        self.path = path
        self.from_ = from_
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'JsonPatchOperation':
        """Initialize a JsonPatchOperation object from a json dictionary."""
        args = {}
        if (op := _dict.get('op')) is not None:
            args['op'] = op
        else:
            raise ValueError('Required property \'op\' not present in JsonPatchOperation JSON')
        if (path := _dict.get('path')) is not None:
            args['path'] = path
        else:
            raise ValueError('Required property \'path\' not present in JsonPatchOperation JSON')
        if (from_ := _dict.get('from')) is not None:
            args['from_'] = from_
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a JsonPatchOperation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'op') and self.op is not None:
            _dict['op'] = self.op
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'from_') and self.from_ is not None:
            _dict['from'] = self.from_
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this JsonPatchOperation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'JsonPatchOperation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'JsonPatchOperation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OpEnum(str, Enum):
        """
        The operation to be performed.
        """

        ADD = 'add'
        REMOVE = 'remove'
        REPLACE = 'replace'
        MOVE = 'move'
        COPY = 'copy'
        TEST = 'test'



class MemberRolesSchema:
    """
    Member roles of a corresponding asset.

    :param str user_iam_id: (optional) User id.
    :param List[str] roles: (optional) Roles of the given user.
    """

    def __init__(
        self,
        *,
        user_iam_id: Optional[str] = None,
        roles: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a MemberRolesSchema object.

        :param str user_iam_id: (optional) User id.
        :param List[str] roles: (optional) Roles of the given user.
        """
        self.user_iam_id = user_iam_id
        self.roles = roles

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MemberRolesSchema':
        """Initialize a MemberRolesSchema object from a json dictionary."""
        args = {}
        if (user_iam_id := _dict.get('user_iam_id')) is not None:
            args['user_iam_id'] = user_iam_id
        if (roles := _dict.get('roles')) is not None:
            args['roles'] = roles
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MemberRolesSchema object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'user_iam_id') and self.user_iam_id is not None:
            _dict['user_iam_id'] = self.user_iam_id
        if hasattr(self, 'roles') and self.roles is not None:
            _dict['roles'] = self.roles
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MemberRolesSchema object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MemberRolesSchema') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MemberRolesSchema') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class NextPage:
    """
    Next page in the collection.

    :param str href: Link to the next page in the collection.
    :param str start: Start token for pagination to the next page in the collection.
    """

    def __init__(
        self,
        href: str,
        start: str,
    ) -> None:
        """
        Initialize a NextPage object.

        :param str href: Link to the next page in the collection.
        :param str start: Start token for pagination to the next page in the
               collection.
        """
        self.href = href
        self.start = start

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NextPage':
        """Initialize a NextPage object from a json dictionary."""
        args = {}
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in NextPage JSON')
        if (start := _dict.get('start')) is not None:
            args['start'] = start
        else:
            raise ValueError('Required property \'start\' not present in NextPage JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NextPage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NextPage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'NextPage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NextPage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Overview:
    """
    Overview details of a data contract.

    :param str api_version: (optional) The API version of the contract.
    :param str kind: (optional) The kind of contract.
    :param str name: (optional) The name of the contract.
    :param str version: The version of the contract.
    :param Domain domain: Domain that the data product version belongs to. If this
          is the first version of a data product, this field is required. If this is a new
          version of an existing data product, the domain will default to the domain of
          the previous version of the data product.
    :param str more_info: (optional) Additional information links about the
          contract.
    """

    def __init__(
        self,
        version: str,
        domain: 'Domain',
        *,
        api_version: Optional[str] = None,
        kind: Optional[str] = None,
        name: Optional[str] = None,
        more_info: Optional[str] = None,
    ) -> None:
        """
        Initialize a Overview object.

        :param str version: The version of the contract.
        :param Domain domain: Domain that the data product version belongs to. If
               this is the first version of a data product, this field is required. If
               this is a new version of an existing data product, the domain will default
               to the domain of the previous version of the data product.
        :param str api_version: (optional) The API version of the contract.
        :param str kind: (optional) The kind of contract.
        :param str name: (optional) The name of the contract.
        :param str more_info: (optional) Additional information links about the
               contract.
        """
        self.api_version = api_version
        self.kind = kind
        self.name = name
        self.version = version
        self.domain = domain
        self.more_info = more_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Overview':
        """Initialize a Overview object from a json dictionary."""
        args = {}
        if (api_version := _dict.get('api_version')) is not None:
            args['api_version'] = api_version
        if (kind := _dict.get('kind')) is not None:
            args['kind'] = kind
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (version := _dict.get('version')) is not None:
            args['version'] = version
        else:
            raise ValueError('Required property \'version\' not present in Overview JSON')
        if (domain := _dict.get('domain')) is not None:
            args['domain'] = Domain.from_dict(domain)
        else:
            raise ValueError('Required property \'domain\' not present in Overview JSON')
        if (more_info := _dict.get('more_info')) is not None:
            args['more_info'] = more_info
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Overview object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'api_version') and self.api_version is not None:
            _dict['api_version'] = self.api_version
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'domain') and self.domain is not None:
            if isinstance(self.domain, dict):
                _dict['domain'] = self.domain
            else:
                _dict['domain'] = self.domain.to_dict()
        if hasattr(self, 'more_info') and self.more_info is not None:
            _dict['more_info'] = self.more_info
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Overview object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Overview') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Overview') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Pricing:
    """
    Represents the pricing details of the contract.

    :param str amount: (optional) The amount for the contract pricing.
    :param str currency: (optional) The currency for the pricing amount.
    :param str unit: (optional) The unit associated with the pricing.
    """

    def __init__(
        self,
        *,
        amount: Optional[str] = None,
        currency: Optional[str] = None,
        unit: Optional[str] = None,
    ) -> None:
        """
        Initialize a Pricing object.

        :param str amount: (optional) The amount for the contract pricing.
        :param str currency: (optional) The currency for the pricing amount.
        :param str unit: (optional) The unit associated with the pricing.
        """
        self.amount = amount
        self.currency = currency
        self.unit = unit

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Pricing':
        """Initialize a Pricing object from a json dictionary."""
        args = {}
        if (amount := _dict.get('amount')) is not None:
            args['amount'] = amount
        if (currency := _dict.get('currency')) is not None:
            args['currency'] = currency
        if (unit := _dict.get('unit')) is not None:
            args['unit'] = unit
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Pricing object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'amount') and self.amount is not None:
            _dict['amount'] = self.amount
        if hasattr(self, 'currency') and self.currency is not None:
            _dict['currency'] = self.currency
        if hasattr(self, 'unit') and self.unit is not None:
            _dict['unit'] = self.unit
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Pricing object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Pricing') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Pricing') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProducerInputModel:
    """
    Parameters for delivery that are set by a data product producer.

    :param EngineDetailsModel engine_details: (optional) Engine details as defined
          by the data product producer.
    """

    def __init__(
        self,
        *,
        engine_details: Optional['EngineDetailsModel'] = None,
    ) -> None:
        """
        Initialize a ProducerInputModel object.

        :param EngineDetailsModel engine_details: (optional) Engine details as
               defined by the data product producer.
        """
        self.engine_details = engine_details

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProducerInputModel':
        """Initialize a ProducerInputModel object from a json dictionary."""
        args = {}
        if (engine_details := _dict.get('engine_details')) is not None:
            args['engine_details'] = EngineDetailsModel.from_dict(engine_details)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProducerInputModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'engine_details') and self.engine_details is not None:
            if isinstance(self.engine_details, dict):
                _dict['engine_details'] = self.engine_details
            else:
                _dict['engine_details'] = self.engine_details.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProducerInputModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProducerInputModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProducerInputModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PropertiesSchema:
    """
    Properties of the corresponding asset.

    :param str value: (optional) Value of the property object.
    """

    def __init__(
        self,
        *,
        value: Optional[str] = None,
    ) -> None:
        """
        Initialize a PropertiesSchema object.

        :param str value: (optional) Value of the property object.
        """
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PropertiesSchema':
        """Initialize a PropertiesSchema object from a json dictionary."""
        args = {}
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PropertiesSchema object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PropertiesSchema object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PropertiesSchema') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PropertiesSchema') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProvidedCatalogWorkflows:
    """
    Resource defining provided workflow definitions.

    :param ProvidedWorkflowResource data_access: (optional) A reference to a
          workflow definition.
    :param ProvidedWorkflowResource request_new_product: (optional) A reference to a
          workflow definition.
    """

    def __init__(
        self,
        *,
        data_access: Optional['ProvidedWorkflowResource'] = None,
        request_new_product: Optional['ProvidedWorkflowResource'] = None,
    ) -> None:
        """
        Initialize a ProvidedCatalogWorkflows object.

        :param ProvidedWorkflowResource data_access: (optional) A reference to a
               workflow definition.
        :param ProvidedWorkflowResource request_new_product: (optional) A reference
               to a workflow definition.
        """
        self.data_access = data_access
        self.request_new_product = request_new_product

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProvidedCatalogWorkflows':
        """Initialize a ProvidedCatalogWorkflows object from a json dictionary."""
        args = {}
        if (data_access := _dict.get('data_access')) is not None:
            args['data_access'] = ProvidedWorkflowResource.from_dict(data_access)
        if (request_new_product := _dict.get('request_new_product')) is not None:
            args['request_new_product'] = ProvidedWorkflowResource.from_dict(request_new_product)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProvidedCatalogWorkflows object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'data_access') and self.data_access is not None:
            if isinstance(self.data_access, dict):
                _dict['data_access'] = self.data_access
            else:
                _dict['data_access'] = self.data_access.to_dict()
        if hasattr(self, 'request_new_product') and self.request_new_product is not None:
            if isinstance(self.request_new_product, dict):
                _dict['request_new_product'] = self.request_new_product
            else:
                _dict['request_new_product'] = self.request_new_product.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProvidedCatalogWorkflows object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProvidedCatalogWorkflows') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProvidedCatalogWorkflows') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProvidedWorkflowResource:
    """
    A reference to a workflow definition.

    :param WorkflowDefinitionReference definition: (optional) Reference to a
          workflow definition.
    """

    def __init__(
        self,
        *,
        definition: Optional['WorkflowDefinitionReference'] = None,
    ) -> None:
        """
        Initialize a ProvidedWorkflowResource object.

        :param WorkflowDefinitionReference definition: (optional) Reference to a
               workflow definition.
        """
        self.definition = definition

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProvidedWorkflowResource':
        """Initialize a ProvidedWorkflowResource object from a json dictionary."""
        args = {}
        if (definition := _dict.get('definition')) is not None:
            args['definition'] = WorkflowDefinitionReference.from_dict(definition)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProvidedWorkflowResource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'definition') and self.definition is not None:
            if isinstance(self.definition, dict):
                _dict['definition'] = self.definition
            else:
                _dict['definition'] = self.definition.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProvidedWorkflowResource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProvidedWorkflowResource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProvidedWorkflowResource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Roles:
    """
    Represents a role associated with the contract.

    :param str role: (optional) The role associated with the contract.
    """

    def __init__(
        self,
        *,
        role: Optional[str] = None,
    ) -> None:
        """
        Initialize a Roles object.

        :param str role: (optional) The role associated with the contract.
        """
        self.role = role

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Roles':
        """Initialize a Roles object from a json dictionary."""
        args = {}
        if (role := _dict.get('role')) is not None:
            args['role'] = role
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Roles object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'role') and self.role is not None:
            _dict['role'] = self.role
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Roles object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Roles') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Roles') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ServiceIdCredentials:
    """
    Service id credentials.

    :param str name: (optional) Name of the api key of the service id.
    :param datetime created_at: (optional) Created date of the api key of the
          service id.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        created_at: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a ServiceIdCredentials object.

        :param str name: (optional) Name of the api key of the service id.
        :param datetime created_at: (optional) Created date of the api key of the
               service id.
        """
        self.name = name
        self.created_at = created_at

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServiceIdCredentials':
        """Initialize a ServiceIdCredentials object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = string_to_datetime(created_at)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServiceIdCredentials object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ServiceIdCredentials object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServiceIdCredentials') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServiceIdCredentials') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UseCase:
    """
    UseCase.

    :param str id: The id of the use case associated with the data product.
    :param str name: (optional) The display name of the use case associated with the
          data product.
    :param ContainerReference container: (optional) Container reference.
    """

    def __init__(
        self,
        id: str,
        *,
        name: Optional[str] = None,
        container: Optional['ContainerReference'] = None,
    ) -> None:
        """
        Initialize a UseCase object.

        :param str id: The id of the use case associated with the data product.
        :param str name: (optional) The display name of the use case associated
               with the data product.
        :param ContainerReference container: (optional) Container reference.
        """
        self.id = id
        self.name = name
        self.container = container

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UseCase':
        """Initialize a UseCase object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in UseCase JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (container := _dict.get('container')) is not None:
            args['container'] = ContainerReference.from_dict(container)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UseCase object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'container') and self.container is not None:
            if isinstance(self.container, dict):
                _dict['container'] = self.container
            else:
                _dict['container'] = self.container.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UseCase object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UseCase') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UseCase') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Visualization:
    """
    Data members for visualization.

    :param str id: (optional) Visualization identifier.
    :param str name: (optional) Visualization name.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> None:
        """
        Initialize a Visualization object.

        :param str id: (optional) Visualization identifier.
        :param str name: (optional) Visualization name.
        """
        self.id = id
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Visualization':
        """Initialize a Visualization object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Visualization object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Visualization object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Visualization') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Visualization') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WorkflowDefinitionReference:
    """
    Reference to a workflow definition.

    :param str id: (optional) ID of a workflow definition.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a WorkflowDefinitionReference object.

        :param str id: (optional) ID of a workflow definition.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WorkflowDefinitionReference':
        """Initialize a WorkflowDefinitionReference object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WorkflowDefinitionReference object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WorkflowDefinitionReference object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WorkflowDefinitionReference') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WorkflowDefinitionReference') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

##############################################################################
# Pagers
##############################################################################


class DataProductsPager:
    """
    DataProductsPager can be used to simplify the use of the "list_data_products" method.
    """

    def __init__(
        self,
        *,
        client: DphV1,
        limit: int = None,
    ) -> None:
        """
        Initialize a DataProductsPager object.
        :param int limit: (optional) Limit the number of data products in the
               results. The maximum limit is 200.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of DataProductSummary.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_data_products(
            limit=self._limit,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('data_products')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of DataProductSummary.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class DataProductDraftsPager:
    """
    DataProductDraftsPager can be used to simplify the use of the "list_data_product_drafts" method.
    """

    def __init__(
        self,
        *,
        client: DphV1,
        data_product_id: str,
        asset_container_id: str = None,
        version: str = None,
        limit: int = None,
    ) -> None:
        """
        Initialize a DataProductDraftsPager object.
        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str asset_container_id: (optional) Filter the list of data product
               drafts by container id.
        :param str version: (optional) Filter the list of data product drafts by
               version number.
        :param int limit: (optional) Limit the number of data product drafts in the
               results. The maximum limit is 200.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._data_product_id = data_product_id
        self._asset_container_id = asset_container_id
        self._version = version
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of DataProductDraftSummary.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_data_product_drafts(
            data_product_id=self._data_product_id,
            asset_container_id=self._asset_container_id,
            version=self._version,
            limit=self._limit,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('drafts')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of DataProductDraftSummary.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class DataProductReleasesPager:
    """
    DataProductReleasesPager can be used to simplify the use of the "list_data_product_releases" method.
    """

    def __init__(
        self,
        *,
        client: DphV1,
        data_product_id: str,
        asset_container_id: str = None,
        state: List[str] = None,
        version: str = None,
        limit: int = None,
    ) -> None:
        """
        Initialize a DataProductReleasesPager object.
        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str asset_container_id: (optional) Filter the list of data product
               releases by container id.
        :param List[str] state: (optional) Filter the list of data product versions
               by state. States are: available and retired. Default is
               "available","retired".
        :param str version: (optional) Filter the list of data product releases by
               version number.
        :param int limit: (optional) Limit the number of data product releases in
               the results. The maximum is 200.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._data_product_id = data_product_id
        self._asset_container_id = asset_container_id
        self._state = state
        self._version = version
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of DataProductReleaseSummary.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_data_product_releases(
            data_product_id=self._data_product_id,
            asset_container_id=self._asset_container_id,
            state=self._state,
            version=self._version,
            limit=self._limit,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('releases')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of DataProductReleaseSummary.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results
