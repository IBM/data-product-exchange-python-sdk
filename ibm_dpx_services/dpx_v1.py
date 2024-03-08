# coding: utf-8

# (C) Copyright IBM Corp. 2024.
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

# IBM OpenAPI SDK Code Generator Version: 3.86.0-bc6f14b3-20240221-193958

"""
Data Product Exchange API Service

API Version: 1.0.0
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

##############################################################################
# Service
##############################################################################


class DpxV1(BaseService):
    """The DPX V1 service."""

    DEFAULT_SERVICE_URL = None
    DEFAULT_SERVICE_NAME = 'dpx'

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'DpxV1':
        """
        Return a new client for the DPX service using the specified parameters and
               external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(authenticator)
        service.configure_service(service_name)
        return service

    def __init__(
        self,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the DPX service.

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
        Exchange.<br/><br/>If the data product catalog exists but has never been
        initialized, the status will be "not_started".<br/><br/>If the data product
        catalog exists and has been or is being initialized, the response will contain the
        status of the last or current initialization. If the initialization failed, the
        "errors" and "trace" fields will contain the error(s) encountered during the
        initialization, including the ID to trace the error(s).<br/><br/>If the data
        product catalog doesn't exist, an HTTP 404 response is returned.

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

    def initialize(
        self,
        *,
        container: Optional['ContainerReference'] = None,
        include: Optional[List[str]] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Initialize resources.

        Use this API to initialize default assets for data product exchange. <br/><br/>You
        can initialize: <br/><ul><li>`delivery_methods` - Methods through which data
        product parts can be delivered to consumers of the data product
        exchange</li><li>`domains_multi_industry` - Taxonomy of domains and use cases
        applicable to multiple industries</li><li>`data_product_samples` - Sample data
        products used to illustrate capabilities of the data product
        exchange</li></ul><br/><br/>If a resource depends on resources that are not
        specified in the request, these dependent resources will be automatically
        initialized. E.g., initializing `data_product_samples` will also initialize
        `domains_multi_industry` and `delivery_methods` even if they are not specified in
        the request because it depends on them.<br/><br/>If initializing the data product
        exchange for the first time, do not specify a container. The default data product
        catalog will be created.<br/>For first time initialization, it is recommended that
        at least `delivery_methods` and `domains_multi_industry` is included in the
        initialize operation.<br/><br/>If the data product exchange has already been
        initialized, you may call this API again to initialize new resources, such as new
        delivery methods.In this case, specify the default data product catalog container
        information.

        :param ContainerReference container: (optional) Data product exchange
               container.
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
        Rotate credentials for a Data Product Exchange instance.

        Use this API to rotate credentials for a Data Product Exchange instance.

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
        :rtype: DetailedResponse with `dict` result representing a `DataProductSummaryCollection` object
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
        drafts: List['DataProductVersionPrototype'],
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a new data product.

        Use this API to create a new data product.<br/><br/>Provide the initial draft of
        the data product.<br/><br/>Required fields:<br/><br/>- name<br/>-
        container<br/><br/>If `version` is not specified, the default version **1.0.0**
        will be used.<br/><br/>The `domain` is optional.

        :param List[DataProductVersionPrototype] drafts: Collection of data
               products drafts to add to data product.
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
        available to download.
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
        url = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/contract_terms/{contract_terms_id}/documents/{document_id}/complete'.format(
            **path_param_dict
        )
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

        Retrieve a list of data product drafts.

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
        asset: 'AssetReference',
        *,
        version: Optional[str] = None,
        state: Optional[str] = None,
        data_product: Optional['DataProductIdentity'] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
        use_cases: Optional[List['UseCase']] = None,
        domain: Optional['Domain'] = None,
        types: Optional[List[str]] = None,
        parts_out: Optional[List['DataProductPart']] = None,
        contract_terms: Optional[List['DataProductContractTerms']] = None,
        is_restricted: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a new draft of an existing data product.

        Create a new draft of an existing data product.

        :param str data_product_id: Data product ID.
        :param AssetReference asset: The asset referenced by the data product
               version.
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
        :param List[str] tags: (optional) Tags on the new data product version. If
               this is the first version of a data product, tags defaults to an empty
               list. If this is a new version of an existing data product, tags will
               default to the list of tags on the previous version of the data product.
        :param List[UseCase] use_cases: (optional) Use cases that the data product
               version serves. If this is the first version of a data product, use cases
               defaults to an empty list. If this is a new version of an existing data
               product, use cases will default to the list of use cases on the previous
               version of the data product.
        :param Domain domain: (optional) Domain that the data product version
               belongs to. If this is the first version of a data product, this field is
               required. If this is a new version of an existing data product, the domain
               will default to the domain of the previous version of the data product.
        :param List[str] types: (optional) The types of the parts included in this
               data product version. If this is the first version of a data product, this
               field defaults to an empty list. If this is a new version of an existing
               data product, the types will default to the types of the previous version
               of the data product.
        :param List[DataProductPart] parts_out: (optional) The outgoing parts of
               this data product version to be delivered to consumers. If this is the
               first version of a data product, this field defaults to an empty list. If
               this is a new version of an existing data product, the data product parts
               will default to the parts list from the previous version of the data
               product.
        :param List[DataProductContractTerms] contract_terms: (optional) The
               contract terms that bind interactions with this data product version.
        :param bool is_restricted: (optional) Indicates whether the data product is
               restricted or not. A restricted data product indicates that orders of the
               data product requires explicit approval before data is delivered.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductVersion` object
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
        if domain is not None:
            domain = convert_model(domain)
        if parts_out is not None:
            parts_out = [convert_model(x) for x in parts_out]
        if contract_terms is not None:
            contract_terms = [convert_model(x) for x in contract_terms]
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
            'domain': domain,
            'types': types,
            'parts_out': parts_out,
            'contract_terms': contract_terms,
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
        id: str,
        *,
        url: Optional[str] = None,
        attachment: Optional['ContractTermsDocumentAttachment'] = None,
        upload_url: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Upload a contract document to the data product draft contract terms.

        Upload a contract document to the data product draft identified by draft_id.
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
        :param str id: Id uniquely identifying this document within the contract
               terms instance.
        :param str url: (optional) URL that can be used to retrieve the contract
               document.
        :param ContractTermsDocumentAttachment attachment: (optional) Attachment
               associated witht the document.
        :param str upload_url: (optional) URL which can be used to upload document
               file.
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
        if id is None:
            raise ValueError('id must be provided')
        if attachment is not None:
            attachment = convert_model(attachment)
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
            'id': id,
            'url': url,
            'attachment': attachment,
            'upload_url': upload_url,
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
        url = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/contract_terms/{contract_terms_id}/documents'.format(
            **path_param_dict
        )
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

        Get a draft of an existing data product.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str draft_id: Data product draft id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductVersion` object
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

        Delete a data product draft identified by a valid ID.

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
        valid ID.<br/><br/>Specify patch operations using http://jsonpatch.com/
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
        :rtype: DetailedResponse with `dict` result representing a `DataProductVersion` object
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
        to prompt the user to upload the document file and complete it.

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
        url = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/contract_terms/{contract_terms_id}/documents/{document_id}'.format(
            **path_param_dict
        )
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
        state.

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
        url = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/contract_terms/{contract_terms_id}/documents/{document_id}'.format(
            **path_param_dict
        )
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
        product version is in DRAFT state.

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
        url = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/contract_terms/{contract_terms_id}/documents/{document_id}'.format(
            **path_param_dict
        )
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

        Publish a draft of an existing data product.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str draft_id: Data product draft id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductVersion` object
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
        url = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/publish'.format(
            **path_param_dict
        )
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
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a release of an existing data product.

        Get a release of an existing data product.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str release_id: Data product release id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductVersion` object
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

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['data_product_id', 'release_id']
        path_param_values = self.encode_path_vars(data_product_id, release_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}/releases/{release_id}'.format(
            **path_param_dict
        )
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
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
        valid ID.<br/><br/>Specify patch operations using http://jsonpatch.com/
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
        :rtype: DetailedResponse with `dict` result representing a `DataProductVersion` object
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
        url = '/data_product_exchange/v1/data_products/{data_product_id}/releases/{release_id}'.format(
            **path_param_dict
        )
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
        attachment.

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
        url = '/data_product_exchange/v1/data_products/{data_product_id}/releases/{release_id}/contract_terms/{contract_terms_id}/documents/{document_id}'.format(
            **path_param_dict
        )
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

        Retrieve a list of data product releases.

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
        **kwargs,
    ) -> DetailedResponse:
        """
        Retire a release of an existing data product.

        Retire a release of an existing data product.

        :param str data_product_id: Data product ID. Use '-' to skip specifying the
               data product ID explicitly.
        :param str release_id: Data product release id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductVersion` object
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

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['data_product_id', 'release_id']
        path_param_values = self.encode_path_vars(data_product_id, release_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{data_product_id}/releases/{release_id}/retire'.format(
            **path_param_dict
        )
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response


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


class AssetPartReference:
    """
    The asset represented in this part.

    :param str id: (optional) The unique identifier of the asset.
    :param ContainerReference container: Data product exchange container.
    :param str type: (optional) The type of the asset.
    """

    def __init__(
        self,
        container: 'ContainerReference',
        *,
        id: Optional[str] = None,
        type: Optional[str] = None,
    ) -> None:
        """
        Initialize a AssetPartReference object.

        :param ContainerReference container: Data product exchange container.
        :param str id: (optional) The unique identifier of the asset.
        :param str type: (optional) The type of the asset.
        """
        self.id = id
        self.container = container
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AssetPartReference':
        """Initialize a AssetPartReference object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
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


class AssetReference:
    """
    The asset referenced by the data product version.

    :param str id: (optional) The unique identifier of the asset.
    :param ContainerReference container: Data product exchange container.
    """

    def __init__(
        self,
        container: 'ContainerReference',
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a AssetReference object.

        :param ContainerReference container: Data product exchange container.
        :param str id: (optional) The unique identifier of the asset.
        """
        self.id = id
        self.container = container

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AssetReference':
        """Initialize a AssetReference object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
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


class ContainerReference:
    """
    Data product exchange container.

    :param str id: Container identifier.
    :param str type: (optional) Container type.
    """

    def __init__(
        self,
        id: str,
        *,
        type: Optional[str] = None,
    ) -> None:
        """
        Initialize a ContainerReference object.

        :param str id: Container identifier.
        :param str type: (optional) Container type.
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


class DataProduct:
    """
    Data Product.

    :param str id: Data product identifier.
    :param ContainerReference container: Data product exchange container.
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
        latest_release: Optional['DataProductVersionSummary'] = None,
        drafts: Optional[List['DataProductVersionSummary']] = None,
    ) -> None:
        """
        Initialize a DataProduct object.

        :param str id: Data product identifier.
        :param ContainerReference container: Data product exchange container.
        :param DataProductVersionSummary latest_release: (optional) Summary of Data
               Product Version object.
        :param List[DataProductVersionSummary] drafts: (optional) List of draft
               summaries of this data product.
        """
        self.id = id
        self.container = container
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
        if (container := _dict.get('container')) is not None:
            args['container'] = ContainerReference.from_dict(container)
        else:
            raise ValueError('Required property \'container\' not present in DataProduct JSON')
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
        if hasattr(self, 'container') and self.container is not None:
            if isinstance(self.container, dict):
                _dict['container'] = self.container
            else:
                _dict['container'] = self.container.to_dict()
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


class DataProductContractTerms:
    """
    DataProductContractTerms.

    :param AssetReference asset: (optional) The asset referenced by the data product
          version.
    :param str id: (optional) ID of the contract terms.
    :param List[ContractTermsDocument] documents: (optional) Collection of contract
          terms documents.
    """

    def __init__(
        self,
        *,
        asset: Optional['AssetReference'] = None,
        id: Optional[str] = None,
        documents: Optional[List['ContractTermsDocument']] = None,
    ) -> None:
        """
        Initialize a DataProductContractTerms object.

        :param AssetReference asset: (optional) The asset referenced by the data
               product version.
        :param str id: (optional) ID of the contract terms.
        :param List[ContractTermsDocument] documents: (optional) Collection of
               contract terms documents.
        """
        self.asset = asset
        self.id = id
        self.documents = documents

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductContractTerms':
        """Initialize a DataProductContractTerms object from a json dictionary."""
        args = {}
        if (asset := _dict.get('asset')) is not None:
            args['asset'] = AssetReference.from_dict(asset)
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (documents := _dict.get('documents')) is not None:
            args['documents'] = [ContractTermsDocument.from_dict(v) for v in documents]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductContractTerms object from a json dictionary."""
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
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductContractTerms object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductContractTerms') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductContractTerms') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductDraftCollection:
    """
    A collection of data product draft summaries.

    :param int limit: Set a limit on the number of results returned.
    :param FirstPage first: First page in the collection.
    :param NextPage next: (optional) Next page in the collection.
    :param List[DataProductVersionSummary] drafts: Collection of data product
          drafts.
    """

    def __init__(
        self,
        limit: int,
        first: 'FirstPage',
        drafts: List['DataProductVersionSummary'],
        *,
        next: Optional['NextPage'] = None,
    ) -> None:
        """
        Initialize a DataProductDraftCollection object.

        :param int limit: Set a limit on the number of results returned.
        :param FirstPage first: First page in the collection.
        :param List[DataProductVersionSummary] drafts: Collection of data product
               drafts.
        :param NextPage next: (optional) Next page in the collection.
        """
        self.limit = limit
        self.first = first
        self.next = next
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
        if (drafts := _dict.get('drafts')) is not None:
            args['drafts'] = [DataProductVersionSummary.from_dict(v) for v in drafts]
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


class DataProductIdentity:
    """
    Data product identifier.

    :param str id: Data product identifier.
    """

    def __init__(
        self,
        id: str,
    ) -> None:
        """
        Initialize a DataProductIdentity object.

        :param str id: Data product identifier.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductIdentity':
        """Initialize a DataProductIdentity object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in DataProductIdentity JSON')
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


class DataProductPart:
    """
    DataProductPart.

    :param AssetPartReference asset: The asset represented in this part.
    :param int revision: (optional) The revision number of the asset represented in
          this part.
    :param datetime updated_at: (optional) The time for when the part was last
          updated.
    :param List[DeliveryMethod] delivery_methods: (optional) Delivery methods
          describing the delivery options available for this part.
    """

    def __init__(
        self,
        asset: 'AssetPartReference',
        *,
        revision: Optional[int] = None,
        updated_at: Optional[datetime] = None,
        delivery_methods: Optional[List['DeliveryMethod']] = None,
    ) -> None:
        """
        Initialize a DataProductPart object.

        :param AssetPartReference asset: The asset represented in this part.
        :param int revision: (optional) The revision number of the asset
               represented in this part.
        :param datetime updated_at: (optional) The time for when the part was last
               updated.
        :param List[DeliveryMethod] delivery_methods: (optional) Delivery methods
               describing the delivery options available for this part.
        """
        self.asset = asset
        self.revision = revision
        self.updated_at = updated_at
        self.delivery_methods = delivery_methods

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductPart':
        """Initialize a DataProductPart object from a json dictionary."""
        args = {}
        if (asset := _dict.get('asset')) is not None:
            args['asset'] = AssetPartReference.from_dict(asset)
        else:
            raise ValueError('Required property \'asset\' not present in DataProductPart JSON')
        if (revision := _dict.get('revision')) is not None:
            args['revision'] = revision
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = string_to_datetime(updated_at)
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
        if hasattr(self, 'revision') and self.revision is not None:
            _dict['revision'] = self.revision
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
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


class DataProductReleaseCollection:
    """
    A collection of data product release summaries.

    :param int limit: Set a limit on the number of results returned.
    :param FirstPage first: First page in the collection.
    :param NextPage next: (optional) Next page in the collection.
    :param List[DataProductVersionSummary] releases: Collection of data product
          releases.
    """

    def __init__(
        self,
        limit: int,
        first: 'FirstPage',
        releases: List['DataProductVersionSummary'],
        *,
        next: Optional['NextPage'] = None,
    ) -> None:
        """
        Initialize a DataProductReleaseCollection object.

        :param int limit: Set a limit on the number of results returned.
        :param FirstPage first: First page in the collection.
        :param List[DataProductVersionSummary] releases: Collection of data product
               releases.
        :param NextPage next: (optional) Next page in the collection.
        """
        self.limit = limit
        self.first = first
        self.next = next
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
        if (releases := _dict.get('releases')) is not None:
            args['releases'] = [DataProductVersionSummary.from_dict(v) for v in releases]
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


class DataProductSummary:
    """
    Data Product Summary.

    :param str id: Data product identifier.
    :param ContainerReference container: Data product exchange container.
    """

    def __init__(
        self,
        id: str,
        container: 'ContainerReference',
    ) -> None:
        """
        Initialize a DataProductSummary object.

        :param str id: Data product identifier.
        :param ContainerReference container: Data product exchange container.
        """
        self.id = id
        self.container = container

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductSummary':
        """Initialize a DataProductSummary object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in DataProductSummary JSON')
        if (container := _dict.get('container')) is not None:
            args['container'] = ContainerReference.from_dict(container)
        else:
            raise ValueError('Required property \'container\' not present in DataProductSummary JSON')
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


class DataProductSummaryCollection:
    """
    A collection of data product summaries.

    :param int limit: Set a limit on the number of results returned.
    :param FirstPage first: First page in the collection.
    :param NextPage next: (optional) Next page in the collection.
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
    ) -> None:
        """
        Initialize a DataProductSummaryCollection object.

        :param int limit: Set a limit on the number of results returned.
        :param FirstPage first: First page in the collection.
        :param List[DataProductSummary] data_products: Collection of data product
               summaries.
        :param NextPage next: (optional) Next page in the collection.
        """
        self.limit = limit
        self.first = first
        self.next = next
        self.data_products = data_products

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductSummaryCollection':
        """Initialize a DataProductSummaryCollection object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in DataProductSummaryCollection JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = FirstPage.from_dict(first)
        else:
            raise ValueError('Required property \'first\' not present in DataProductSummaryCollection JSON')
        if (next := _dict.get('next')) is not None:
            args['next'] = NextPage.from_dict(next)
        if (data_products := _dict.get('data_products')) is not None:
            args['data_products'] = [DataProductSummary.from_dict(v) for v in data_products]
        else:
            raise ValueError('Required property \'data_products\' not present in DataProductSummaryCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductSummaryCollection object from a json dictionary."""
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
        """Return a `str` version of this DataProductSummaryCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductSummaryCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductSummaryCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataProductVersion:
    """
    Data Product version.

    :param str version: The data product version number.
    :param str state: The state of the data product version.
    :param DataProductIdentity data_product: Data product identifier.
    :param str name: The name of the data product version. A name can contain
          letters, numbers, understores, dashes, spaces or periods. Names are mutable and
          reusable.
    :param str description: The description of the data product version.
    :param str id: The identifier of the data product version.
    :param AssetReference asset: The asset referenced by the data product version.
    :param List[str] tags: (optional) Tags on the data product.
    :param List[UseCase] use_cases: (optional) A list of use cases associated with
          the data product version.
    :param Domain domain: Domain that the data product version belongs to. If this
          is the first version of a data product, this field is required. If this is a new
          version of an existing data product, the domain will default to the domain of
          the previous version of the data product.
    :param List[str] types: (optional) Types of parts on the data product.
    :param List[DataProductPart] parts_out: Outgoing parts of a data product used to
          deliver the data product to consumers.
    :param str published_by: (optional) The user who published this data product
          version.
    :param datetime published_at: (optional) The time when this data product version
          was published.
    :param List[DataProductContractTerms] contract_terms: (optional) Contract terms
          binding various aspects of the data product.
    :param str created_by: The creator of this data product version.
    :param datetime created_at: The time when this data product version was created.
    :param bool is_restricted: (optional) Indicates whether the data product is
          restricted or not. A restricted data product indicates that orders of the data
          product requires explicit approval before data is delivered.
    """

    def __init__(
        self,
        version: str,
        state: str,
        data_product: 'DataProductIdentity',
        name: str,
        description: str,
        id: str,
        asset: 'AssetReference',
        domain: 'Domain',
        parts_out: List['DataProductPart'],
        created_by: str,
        created_at: datetime,
        *,
        tags: Optional[List[str]] = None,
        use_cases: Optional[List['UseCase']] = None,
        types: Optional[List[str]] = None,
        published_by: Optional[str] = None,
        published_at: Optional[datetime] = None,
        contract_terms: Optional[List['DataProductContractTerms']] = None,
        is_restricted: Optional[bool] = None,
    ) -> None:
        """
        Initialize a DataProductVersion object.

        :param str version: The data product version number.
        :param str state: The state of the data product version.
        :param DataProductIdentity data_product: Data product identifier.
        :param str name: The name of the data product version. A name can contain
               letters, numbers, understores, dashes, spaces or periods. Names are mutable
               and reusable.
        :param str description: The description of the data product version.
        :param str id: The identifier of the data product version.
        :param AssetReference asset: The asset referenced by the data product
               version.
        :param Domain domain: Domain that the data product version belongs to. If
               this is the first version of a data product, this field is required. If
               this is a new version of an existing data product, the domain will default
               to the domain of the previous version of the data product.
        :param List[DataProductPart] parts_out: Outgoing parts of a data product
               used to deliver the data product to consumers.
        :param str created_by: The creator of this data product version.
        :param datetime created_at: The time when this data product version was
               created.
        :param List[str] tags: (optional) Tags on the data product.
        :param List[UseCase] use_cases: (optional) A list of use cases associated
               with the data product version.
        :param List[str] types: (optional) Types of parts on the data product.
        :param str published_by: (optional) The user who published this data
               product version.
        :param datetime published_at: (optional) The time when this data product
               version was published.
        :param List[DataProductContractTerms] contract_terms: (optional) Contract
               terms binding various aspects of the data product.
        :param bool is_restricted: (optional) Indicates whether the data product is
               restricted or not. A restricted data product indicates that orders of the
               data product requires explicit approval before data is delivered.
        """
        self.version = version
        self.state = state
        self.data_product = data_product
        self.name = name
        self.description = description
        self.id = id
        self.asset = asset
        self.tags = tags
        self.use_cases = use_cases
        self.domain = domain
        self.types = types
        self.parts_out = parts_out
        self.published_by = published_by
        self.published_at = published_at
        self.contract_terms = contract_terms
        self.created_by = created_by
        self.created_at = created_at
        self.is_restricted = is_restricted

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductVersion':
        """Initialize a DataProductVersion object from a json dictionary."""
        args = {}
        if (version := _dict.get('version')) is not None:
            args['version'] = version
        else:
            raise ValueError('Required property \'version\' not present in DataProductVersion JSON')
        if (state := _dict.get('state')) is not None:
            args['state'] = state
        else:
            raise ValueError('Required property \'state\' not present in DataProductVersion JSON')
        if (data_product := _dict.get('data_product')) is not None:
            args['data_product'] = DataProductIdentity.from_dict(data_product)
        else:
            raise ValueError('Required property \'data_product\' not present in DataProductVersion JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in DataProductVersion JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        else:
            raise ValueError('Required property \'description\' not present in DataProductVersion JSON')
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in DataProductVersion JSON')
        if (asset := _dict.get('asset')) is not None:
            args['asset'] = AssetReference.from_dict(asset)
        else:
            raise ValueError('Required property \'asset\' not present in DataProductVersion JSON')
        if (tags := _dict.get('tags')) is not None:
            args['tags'] = tags
        if (use_cases := _dict.get('use_cases')) is not None:
            args['use_cases'] = [UseCase.from_dict(v) for v in use_cases]
        if (domain := _dict.get('domain')) is not None:
            args['domain'] = Domain.from_dict(domain)
        else:
            raise ValueError('Required property \'domain\' not present in DataProductVersion JSON')
        if (types := _dict.get('types')) is not None:
            args['types'] = types
        if (parts_out := _dict.get('parts_out')) is not None:
            args['parts_out'] = [DataProductPart.from_dict(v) for v in parts_out]
        else:
            raise ValueError('Required property \'parts_out\' not present in DataProductVersion JSON')
        if (published_by := _dict.get('published_by')) is not None:
            args['published_by'] = published_by
        if (published_at := _dict.get('published_at')) is not None:
            args['published_at'] = string_to_datetime(published_at)
        if (contract_terms := _dict.get('contract_terms')) is not None:
            args['contract_terms'] = [DataProductContractTerms.from_dict(v) for v in contract_terms]
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        else:
            raise ValueError('Required property \'created_by\' not present in DataProductVersion JSON')
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = string_to_datetime(created_at)
        else:
            raise ValueError('Required property \'created_at\' not present in DataProductVersion JSON')
        if (is_restricted := _dict.get('is_restricted')) is not None:
            args['is_restricted'] = is_restricted
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductVersion object from a json dictionary."""
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
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'asset') and self.asset is not None:
            if isinstance(self.asset, dict):
                _dict['asset'] = self.asset
            else:
                _dict['asset'] = self.asset.to_dict()
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
        if hasattr(self, 'domain') and self.domain is not None:
            if isinstance(self.domain, dict):
                _dict['domain'] = self.domain
            else:
                _dict['domain'] = self.domain.to_dict()
        if hasattr(self, 'types') and self.types is not None:
            _dict['types'] = self.types
        if hasattr(self, 'parts_out') and self.parts_out is not None:
            parts_out_list = []
            for v in self.parts_out:
                if isinstance(v, dict):
                    parts_out_list.append(v)
                else:
                    parts_out_list.append(v.to_dict())
            _dict['parts_out'] = parts_out_list
        if hasattr(self, 'published_by') and self.published_by is not None:
            _dict['published_by'] = self.published_by
        if hasattr(self, 'published_at') and self.published_at is not None:
            _dict['published_at'] = datetime_to_string(self.published_at)
        if hasattr(self, 'contract_terms') and self.contract_terms is not None:
            contract_terms_list = []
            for v in self.contract_terms:
                if isinstance(v, dict):
                    contract_terms_list.append(v)
                else:
                    contract_terms_list.append(v.to_dict())
            _dict['contract_terms'] = contract_terms_list
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'is_restricted') and self.is_restricted is not None:
            _dict['is_restricted'] = self.is_restricted
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductVersion object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductVersion') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductVersion') -> bool:
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


class DataProductVersionPrototype:
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
    :param AssetReference asset: The asset referenced by the data product version.
    :param List[str] tags: (optional) Tags on the new data product version. If this
          is the first version of a data product, tags defaults to an empty list. If this
          is a new version of an existing data product, tags will default to the list of
          tags on the previous version of the data product.
    :param List[UseCase] use_cases: (optional) Use cases that the data product
          version serves. If this is the first version of a data product, use cases
          defaults to an empty list. If this is a new version of an existing data product,
          use cases will default to the list of use cases on the previous version of the
          data product.
    :param Domain domain: (optional) Domain that the data product version belongs
          to. If this is the first version of a data product, this field is required. If
          this is a new version of an existing data product, the domain will default to
          the domain of the previous version of the data product.
    :param List[str] types: (optional) The types of the parts included in this data
          product version. If this is the first version of a data product, this field
          defaults to an empty list. If this is a new version of an existing data product,
          the types will default to the types of the previous version of the data product.
    :param List[DataProductPart] parts_out: (optional) The outgoing parts of this
          data product version to be delivered to consumers. If this is the first version
          of a data product, this field defaults to an empty list. If this is a new
          version of an existing data product, the data product parts will default to the
          parts list from the previous version of the data product.
    :param List[DataProductContractTerms] contract_terms: (optional) The contract
          terms that bind interactions with this data product version.
    :param bool is_restricted: (optional) Indicates whether the data product is
          restricted or not. A restricted data product indicates that orders of the data
          product requires explicit approval before data is delivered.
    """

    def __init__(
        self,
        asset: 'AssetReference',
        *,
        version: Optional[str] = None,
        state: Optional[str] = None,
        data_product: Optional['DataProductIdentity'] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
        use_cases: Optional[List['UseCase']] = None,
        domain: Optional['Domain'] = None,
        types: Optional[List[str]] = None,
        parts_out: Optional[List['DataProductPart']] = None,
        contract_terms: Optional[List['DataProductContractTerms']] = None,
        is_restricted: Optional[bool] = None,
    ) -> None:
        """
        Initialize a DataProductVersionPrototype object.

        :param AssetReference asset: The asset referenced by the data product
               version.
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
        :param List[str] tags: (optional) Tags on the new data product version. If
               this is the first version of a data product, tags defaults to an empty
               list. If this is a new version of an existing data product, tags will
               default to the list of tags on the previous version of the data product.
        :param List[UseCase] use_cases: (optional) Use cases that the data product
               version serves. If this is the first version of a data product, use cases
               defaults to an empty list. If this is a new version of an existing data
               product, use cases will default to the list of use cases on the previous
               version of the data product.
        :param Domain domain: (optional) Domain that the data product version
               belongs to. If this is the first version of a data product, this field is
               required. If this is a new version of an existing data product, the domain
               will default to the domain of the previous version of the data product.
        :param List[str] types: (optional) The types of the parts included in this
               data product version. If this is the first version of a data product, this
               field defaults to an empty list. If this is a new version of an existing
               data product, the types will default to the types of the previous version
               of the data product.
        :param List[DataProductPart] parts_out: (optional) The outgoing parts of
               this data product version to be delivered to consumers. If this is the
               first version of a data product, this field defaults to an empty list. If
               this is a new version of an existing data product, the data product parts
               will default to the parts list from the previous version of the data
               product.
        :param List[DataProductContractTerms] contract_terms: (optional) The
               contract terms that bind interactions with this data product version.
        :param bool is_restricted: (optional) Indicates whether the data product is
               restricted or not. A restricted data product indicates that orders of the
               data product requires explicit approval before data is delivered.
        """
        self.version = version
        self.state = state
        self.data_product = data_product
        self.name = name
        self.description = description
        self.asset = asset
        self.tags = tags
        self.use_cases = use_cases
        self.domain = domain
        self.types = types
        self.parts_out = parts_out
        self.contract_terms = contract_terms
        self.is_restricted = is_restricted

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductVersionPrototype':
        """Initialize a DataProductVersionPrototype object from a json dictionary."""
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
        if (asset := _dict.get('asset')) is not None:
            args['asset'] = AssetReference.from_dict(asset)
        else:
            raise ValueError('Required property \'asset\' not present in DataProductVersionPrototype JSON')
        if (tags := _dict.get('tags')) is not None:
            args['tags'] = tags
        if (use_cases := _dict.get('use_cases')) is not None:
            args['use_cases'] = [UseCase.from_dict(v) for v in use_cases]
        if (domain := _dict.get('domain')) is not None:
            args['domain'] = Domain.from_dict(domain)
        if (types := _dict.get('types')) is not None:
            args['types'] = types
        if (parts_out := _dict.get('parts_out')) is not None:
            args['parts_out'] = [DataProductPart.from_dict(v) for v in parts_out]
        if (contract_terms := _dict.get('contract_terms')) is not None:
            args['contract_terms'] = [DataProductContractTerms.from_dict(v) for v in contract_terms]
        if (is_restricted := _dict.get('is_restricted')) is not None:
            args['is_restricted'] = is_restricted
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataProductVersionPrototype object from a json dictionary."""
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
        if hasattr(self, 'asset') and self.asset is not None:
            if isinstance(self.asset, dict):
                _dict['asset'] = self.asset
            else:
                _dict['asset'] = self.asset.to_dict()
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
        if hasattr(self, 'domain') and self.domain is not None:
            if isinstance(self.domain, dict):
                _dict['domain'] = self.domain
            else:
                _dict['domain'] = self.domain.to_dict()
        if hasattr(self, 'types') and self.types is not None:
            _dict['types'] = self.types
        if hasattr(self, 'parts_out') and self.parts_out is not None:
            parts_out_list = []
            for v in self.parts_out:
                if isinstance(v, dict):
                    parts_out_list.append(v)
                else:
                    parts_out_list.append(v.to_dict())
            _dict['parts_out'] = parts_out_list
        if hasattr(self, 'contract_terms') and self.contract_terms is not None:
            contract_terms_list = []
            for v in self.contract_terms:
                if isinstance(v, dict):
                    contract_terms_list.append(v)
                else:
                    contract_terms_list.append(v.to_dict())
            _dict['contract_terms'] = contract_terms_list
        if hasattr(self, 'is_restricted') and self.is_restricted is not None:
            _dict['is_restricted'] = self.is_restricted
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataProductVersionPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataProductVersionPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataProductVersionPrototype') -> bool:
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


class DataProductVersionSummary:
    """
    Summary of Data Product Version object.

    :param str version: The data product version number.
    :param str state: The state of the data product version.
    :param DataProductIdentity data_product: Data product identifier.
    :param str name: The name of the data product version. A name can contain
          letters, numbers, understores, dashes, spaces or periods. Names are mutable and
          reusable.
    :param str description: The description of the data product version.
    :param str id: The identifier of the data product version.
    :param AssetReference asset: The asset referenced by the data product version.
    """

    def __init__(
        self,
        version: str,
        state: str,
        data_product: 'DataProductIdentity',
        name: str,
        description: str,
        id: str,
        asset: 'AssetReference',
    ) -> None:
        """
        Initialize a DataProductVersionSummary object.

        :param str version: The data product version number.
        :param str state: The state of the data product version.
        :param DataProductIdentity data_product: Data product identifier.
        :param str name: The name of the data product version. A name can contain
               letters, numbers, understores, dashes, spaces or periods. Names are mutable
               and reusable.
        :param str description: The description of the data product version.
        :param str id: The identifier of the data product version.
        :param AssetReference asset: The asset referenced by the data product
               version.
        """
        self.version = version
        self.state = state
        self.data_product = data_product
        self.name = name
        self.description = description
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
            args['data_product'] = DataProductIdentity.from_dict(data_product)
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


class DeliveryMethod:
    """
    DeliveryMethod.

    :param str id: The ID of the delivery method.
    :param ContainerReference container: Data product exchange container.
    """

    def __init__(
        self,
        id: str,
        container: 'ContainerReference',
    ) -> None:
        """
        Initialize a DeliveryMethod object.

        :param str id: The ID of the delivery method.
        :param ContainerReference container: Data product exchange container.
        """
        self.id = id
        self.container = container

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


class Domain:
    """
    Domain that the data product version belongs to. If this is the first version of a
    data product, this field is required. If this is a new version of an existing data
    product, the domain will default to the domain of the previous version of the data
    product.

    :param str id: The ID of the domain.
    :param str name: (optional) The display name of the domain.
    :param ContainerReference container: (optional) Data product exchange container.
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
        :param ContainerReference container: (optional) Data product exchange
               container.
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


class ErrorModelResource:
    """
    Detailed error information.

    :param str code: (optional) Error code.
    :param str message: (optional) Error message.
    :param dict extra: (optional) Extra information about the error.
    :param str more_info: (optional) More info message.
    """

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        extra: Optional[dict] = None,
        more_info: Optional[str] = None,
    ) -> None:
        """
        Initialize a ErrorModelResource object.

        :param str code: (optional) Error code.
        :param str message: (optional) Error message.
        :param dict extra: (optional) Extra information about the error.
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
        if (message := _dict.get('message')) is not None:
            args['message'] = message
        if (extra := _dict.get('extra')) is not None:
            args['extra'] = extra
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
            _dict['extra'] = self.extra
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

    :param ContainerReference container: (optional) Data product exchange container.
    :param str href: (optional) Link to monitor the status of the initialize
          operation.
    :param str status: (optional) Status of the initialize operation.
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
    """

    def __init__(
        self,
        *,
        container: Optional['ContainerReference'] = None,
        href: Optional[str] = None,
        status: Optional[str] = None,
        trace: Optional[str] = None,
        errors: Optional[List['ErrorModelResource']] = None,
        last_started_at: Optional[datetime] = None,
        last_finished_at: Optional[datetime] = None,
        initialized_options: Optional[List['InitializedOption']] = None,
    ) -> None:
        """
        Initialize a InitializeResource object.

        :param ContainerReference container: (optional) Data product exchange
               container.
        :param str href: (optional) Link to monitor the status of the initialize
               operation.
        :param str status: (optional) Status of the initialize operation.
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
        """
        self.container = container
        self.href = href
        self.status = status
        self.trace = trace
        self.errors = errors
        self.last_started_at = last_started_at
        self.last_finished_at = last_finished_at
        self.initialized_options = initialized_options

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


class UseCase:
    """
    UseCase.

    :param str id: The id of the use case associated with the data product.
    :param str name: (optional) The display name of the use case associated with the
          data product.
    :param ContainerReference container: (optional) Data product exchange container.
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
        :param ContainerReference container: (optional) Data product exchange
               container.
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
        client: DpxV1,
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
        client: DpxV1,
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
        :return: A List[dict], where each element is a dict that represents an instance of DataProductVersionSummary.
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
        :return: A List[dict], where each element is a dict that represents an instance of DataProductVersionSummary.
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
        client: DpxV1,
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
        :return: A List[dict], where each element is a dict that represents an instance of DataProductVersionSummary.
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
        :return: A List[dict], where each element is a dict that represents an instance of DataProductVersionSummary.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results
