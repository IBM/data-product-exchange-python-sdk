# coding: utf-8

# (C) Copyright IBM Corp. 2023.
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

# IBM OpenAPI SDK Code Generator Version: 3.82.1-2082d402-20231115-195014

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
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class DataProductExchangeApiServiceV1(BaseService):
    """The Data Product Exchange API Service V1 service."""

    DEFAULT_SERVICE_URL = None
    DEFAULT_SERVICE_NAME = 'data_product_exchange_api_service'

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'DataProductExchangeApiServiceV1':
        """
        Return a new client for the Data Product Exchange API Service service using
               the specified parameters and external configuration.
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
        Construct a new client for the Data Product Exchange API Service service.

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
        Get the status of resources initialization in data product exchange.

        Use this API to get the status of the resource initialization in data product
        exchange. <br/><br/>If the data product catalog exists but has never been
        initialized, the status will be "not_started".<br/>If the data product catalog
        exists and has been or is being initialized, the response will contain the status
        of the last or current initialization.If the initialization failed, the "errors"
        and the "trace" fields will contain the error(s) encountered during the
        initialization and the id to trace the error(s).<br/>If the data product catalog
        doesn't exist, a HTTP 404 response will be returned.

        :param str container_id: (optional) Container ID of the data product
               catalog. If not supplied, the data product catalog will be looked up by
               using the uid of the default data product catalog.
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
        Initialize resources in a data product exchange.

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
        `delivery_methods` and at least one domain taxonomy is included in the initialize
        operation.<br/><br/>If the data product exchange has already been initialized, you
        may call this API again to initialize new resources, such as new delivery
        methods.In this case, specify the default data product catalog container
        information.

        :param ContainerReference container: (optional) Data product exchange
               container.
        :param List[str] include: (optional) List of configuration options to
               initialize.
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

    #########################
    # Data Products
    #########################

    def get_data_product(
        self,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a data product identified by id.

        Retrieve a data product identified by id.

        :param str id: Data product id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProduct` object
        """

        if not id:
            raise ValueError('id must be provided')
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

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_products/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

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

    #########################
    # Data Product Versions
    #########################

    def list_data_product_versions(
        self,
        *,
        asset_container_id: Optional[str] = None,
        data_product: Optional[str] = None,
        state: Optional[str] = None,
        version: Optional[str] = None,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a list of data product versions.

        Retrieve a list of data product versions.

        :param str asset_container_id: (optional) Filter the list of data product
               versions by container id.
        :param str data_product: (optional) Filter the list of data product
               versions by data product id.
        :param str state: (optional) Filter the list of data product versions by
               state. States are: draft, available and retired.
        :param str version: (optional) Filter the list of data product versions by
               version number.
        :param int limit: (optional) Limit the number of data products in the
               results. The maximum limit is 200.
        :param str start: (optional) Start token for pagination.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductVersionCollection` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_data_product_versions',
        )
        headers.update(sdk_headers)

        params = {
            'asset.container.id': asset_container_id,
            'data_product': data_product,
            'state': state,
            'version': version,
            'limit': limit,
            'start': start,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/data_product_exchange/v1/data_product_versions'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_data_product_version(
        self,
        container: 'ContainerReference',
        *,
        version: Optional[str] = None,
        state: Optional[str] = None,
        data_product: Optional['DataProductIdentity'] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
        use_cases: Optional[List['UseCase']] = None,
        domain: Optional['Domain'] = None,
        type: Optional[List[str]] = None,
        parts_out: Optional[List['DataProductPart']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a new data product version.

        Use this API to create a new data product version.<br/><br/>If the `state` is not
        specified, the data product version will be created in **draft**
        state.<br/><br/>**Create the first version of a data product**<br/><br/>Required
        fields:<br/><br/>- name<br/>- container<br/><br/>If `version` is not specified,
        the default version **1.0.0** will be used.<br/><br/>**Create a new version of an
        existing data product**<br/><br/>Required fields:<br/><br/>- container<br/>-
        data_product<br/>- version<br/><br/>The `domain` is required if state of data
        product is available. If no additional properties are specified, the values will
        be copied from the most recently available version of the data product.

        :param ContainerReference container: Data product exchange container.
        :param str version: (optional) The data product version number.
        :param str state: (optional) The state of the data product version. If not
               specified, the data product version will be created in `draft` state.
        :param DataProductIdentity data_product: (optional) Data product
               identifier.
        :param str name: (optional) The name to use to refer to the new data
               product version. If this is a new data product, this value must be
               specified. If this is a new version of an existing data product, the name
               will default to the name of the previous data product version. A name can
               contain letters, numbers, understores, dashes, spaces or periods. A name
               must contain at least one non-space character.
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
        :param Domain domain: (optional) The business domain associated with the
               data product version.
        :param List[str] type: (optional) The types of the parts included in this
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
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductVersion` object
        """

        if container is None:
            raise ValueError('container must be provided')
        container = convert_model(container)
        if data_product is not None:
            data_product = convert_model(data_product)
        if use_cases is not None:
            use_cases = [convert_model(x) for x in use_cases]
        if domain is not None:
            domain = convert_model(domain)
        if parts_out is not None:
            parts_out = [convert_model(x) for x in parts_out]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_data_product_version',
        )
        headers.update(sdk_headers)

        data = {
            'container': container,
            'version': version,
            'state': state,
            'data_product': data_product,
            'name': name,
            'description': description,
            'tags': tags,
            'use_cases': use_cases,
            'domain': domain,
            'type': type,
            'parts_out': parts_out,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/data_product_exchange/v1/data_product_versions'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_data_product_version(
        self,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a data product version identified by ID.

        Retrieve a data product version identified by a valid ID.

        :param str id: Data product version ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductVersion` object
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_data_product_version',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_product_versions/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_data_product_version(
        self,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a data product version identified by ID.

        Delete a data product version identified by a valid ID. Delete can be performed
        only on data product versions in **draft** state. To retire a data product version
        which has already been published, use `PATCH
        /data_product_exchange/v1/data_product_versions` to change the data product
        version state to **retired**.

        :param str id: Data product version ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_data_product_version',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_product_versions/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_data_product_version(
        self,
        id: str,
        json_patch_instructions: List['JsonPatchOperation'],
        **kwargs,
    ) -> DetailedResponse:
        """
        Update the data product version identified by ID.

        Use this API to update the properties of a data product version identified by a
        valid ID.<br/><br/>Specify patch operations using http://jsonpatch.com/
        syntax.<br/><br/>Supported patch operations include:<br/><br/>- Update the
        properties of a data product<br/><br/>- Add/Remove parts from a data
        product<br/><br/>- Add/Remove use cases from a data product<br/><br/>- Update the
        data product state<br/><br/>.

        :param str id: Data product version ID.
        :param List[JsonPatchOperation] json_patch_instructions: A set of patch
               operations as defined in RFC 6902. See http://jsonpatch.com/ for more
               information.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataProductVersion` object
        """

        if not id:
            raise ValueError('id must be provided')
        if json_patch_instructions is None:
            raise ValueError('json_patch_instructions must be provided')
        json_patch_instructions = [convert_model(x) for x in json_patch_instructions]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_data_product_version',
        )
        headers.update(sdk_headers)

        data = json.dumps(json_patch_instructions)
        headers['content-type'] = 'application/json-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_product_versions/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def deliver_data_product_version(
        self,
        id: str,
        *,
        order: Optional['OrderReference'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Deliver a data product identified by id.

        Deliver a data product version identified by id.

        :param str id: Data product version id.
        :param OrderReference order: (optional) The order for the data product that
               should be delivered as part of this delivery operation.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeliveryResource` object
        """

        if not id:
            raise ValueError('id must be provided')
        if order is not None:
            order = convert_model(order)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='deliver_data_product_version',
        )
        headers.update(sdk_headers)

        data = {
            'order': order,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/data_product_exchange/v1/data_product_versions/{id}/deliver'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response


class ListDataProductVersionsEnums:
    """
    Enums for list_data_product_versions parameters.
    """

    class State(str, Enum):
        """
        Filter the list of data product versions by state. States are: draft, available
        and retired.
        """

        DRAFT = 'draft'
        AVAILABLE = 'available'
        RETIRED = 'retired'


##############################################################################
# Models
##############################################################################


class AssetPartReference:
    """
    The asset represented in this part.

    :param str id: The unique identifier of the asset.
    :param ContainerReference container: Data product exchange container.
    :param str type: (optional) The type of the asset.
    """

    def __init__(
        self,
        id: str,
        container: 'ContainerReference',
        *,
        type: Optional[str] = None,
    ) -> None:
        """
        Initialize a AssetPartReference object.

        :param str id: The unique identifier of the asset.
        :param ContainerReference container: Data product exchange container.
        :param str type: (optional) The type of the asset.
        """
        self.id = id
        self.container = container
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AssetPartReference':
        """Initialize a AssetPartReference object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in AssetPartReference JSON')
        if 'container' in _dict:
            args['container'] = ContainerReference.from_dict(_dict.get('container'))
        else:
            raise ValueError('Required property \'container\' not present in AssetPartReference JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
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

    :param str id: The unique identifier of the asset.
    :param ContainerReference container: Data product exchange container.
    """

    def __init__(
        self,
        id: str,
        container: 'ContainerReference',
    ) -> None:
        """
        Initialize a AssetReference object.

        :param str id: The unique identifier of the asset.
        :param ContainerReference container: Data product exchange container.
        """
        self.id = id
        self.container = container

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AssetReference':
        """Initialize a AssetReference object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in AssetReference JSON')
        if 'container' in _dict:
            args['container'] = ContainerReference.from_dict(_dict.get('container'))
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
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ContainerReference JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
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


class DataProduct:
    """
    Data Product.

    :param str id: Data product identifier.
    :param ContainerReference container: Data product exchange container.
    :param str name: Name to refer to the data product.
    """

    def __init__(
        self,
        id: str,
        container: 'ContainerReference',
        name: str,
    ) -> None:
        """
        Initialize a DataProduct object.

        :param str id: Data product identifier.
        :param ContainerReference container: Data product exchange container.
        :param str name: Name to refer to the data product.
        """
        self.id = id
        self.container = container
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProduct':
        """Initialize a DataProduct object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in DataProduct JSON')
        if 'container' in _dict:
            args['container'] = ContainerReference.from_dict(_dict.get('container'))
        else:
            raise ValueError('Required property \'container\' not present in DataProduct JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in DataProduct JSON')
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
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
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
    A collection of data products.

    :param int limit: Set a limit on the number of results returned.
    :param FirstPage first: First page in the collection.
    :param NextPage next: (optional) Next page in the collection.
    :param List[DataProduct] data_products: Collection of data products.
    """

    def __init__(
        self,
        limit: int,
        first: 'FirstPage',
        data_products: List['DataProduct'],
        *,
        next: Optional['NextPage'] = None,
    ) -> None:
        """
        Initialize a DataProductCollection object.

        :param int limit: Set a limit on the number of results returned.
        :param FirstPage first: First page in the collection.
        :param List[DataProduct] data_products: Collection of data products.
        :param NextPage next: (optional) Next page in the collection.
        """
        self.limit = limit
        self.first = first
        self.next = next
        self.data_products = data_products

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductCollection':
        """Initialize a DataProductCollection object from a json dictionary."""
        args = {}
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in DataProductCollection JSON')
        if 'first' in _dict:
            args['first'] = FirstPage.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in DataProductCollection JSON')
        if 'next' in _dict:
            args['next'] = NextPage.from_dict(_dict.get('next'))
        if 'data_products' in _dict:
            args['data_products'] = [DataProduct.from_dict(v) for v in _dict.get('data_products')]
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
        if 'id' in _dict:
            args['id'] = _dict.get('id')
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
        if 'asset' in _dict:
            args['asset'] = AssetPartReference.from_dict(_dict.get('asset'))
        else:
            raise ValueError('Required property \'asset\' not present in DataProductPart JSON')
        if 'revision' in _dict:
            args['revision'] = _dict.get('revision')
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        if 'delivery_methods' in _dict:
            args['delivery_methods'] = [DeliveryMethod.from_dict(v) for v in _dict.get('delivery_methods')]
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
    :param List[UseCase] use_cases: A list of use cases associated with the data
          product version.
    :param Domain domain: The business domain associated with the data product
          version.
    :param List[str] type: (optional) Type of parts on the data product.
    :param List[DataProductPart] parts_out: Outgoing parts of a data product used to
          deliver the data product to consumers.
    :param str published_by: (optional) The user who published this data product
          version.
    :param datetime published_at: (optional) The time when this data product version
          was published.
    :param str created_by: The creator of this data product version.
    :param datetime created_at: The time when this data product version was created.
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
        use_cases: List['UseCase'],
        domain: 'Domain',
        parts_out: List['DataProductPart'],
        created_by: str,
        created_at: datetime,
        *,
        tags: Optional[List[str]] = None,
        type: Optional[List[str]] = None,
        published_by: Optional[str] = None,
        published_at: Optional[datetime] = None,
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
        :param List[UseCase] use_cases: A list of use cases associated with the
               data product version.
        :param Domain domain: The business domain associated with the data product
               version.
        :param List[DataProductPart] parts_out: Outgoing parts of a data product
               used to deliver the data product to consumers.
        :param str created_by: The creator of this data product version.
        :param datetime created_at: The time when this data product version was
               created.
        :param List[str] tags: (optional) Tags on the data product.
        :param List[str] type: (optional) Type of parts on the data product.
        :param str published_by: (optional) The user who published this data
               product version.
        :param datetime published_at: (optional) The time when this data product
               version was published.
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
        self.type = type
        self.parts_out = parts_out
        self.published_by = published_by
        self.published_at = published_at
        self.created_by = created_by
        self.created_at = created_at

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductVersion':
        """Initialize a DataProductVersion object from a json dictionary."""
        args = {}
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        else:
            raise ValueError('Required property \'version\' not present in DataProductVersion JSON')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in DataProductVersion JSON')
        if 'data_product' in _dict:
            args['data_product'] = DataProductIdentity.from_dict(_dict.get('data_product'))
        else:
            raise ValueError('Required property \'data_product\' not present in DataProductVersion JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in DataProductVersion JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in DataProductVersion JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in DataProductVersion JSON')
        if 'asset' in _dict:
            args['asset'] = AssetReference.from_dict(_dict.get('asset'))
        else:
            raise ValueError('Required property \'asset\' not present in DataProductVersion JSON')
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'use_cases' in _dict:
            args['use_cases'] = [UseCase.from_dict(v) for v in _dict.get('use_cases')]
        else:
            raise ValueError('Required property \'use_cases\' not present in DataProductVersion JSON')
        if 'domain' in _dict:
            args['domain'] = Domain.from_dict(_dict.get('domain'))
        else:
            raise ValueError('Required property \'domain\' not present in DataProductVersion JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'parts_out' in _dict:
            args['parts_out'] = [DataProductPart.from_dict(v) for v in _dict.get('parts_out')]
        else:
            raise ValueError('Required property \'parts_out\' not present in DataProductVersion JSON')
        if 'published_by' in _dict:
            args['published_by'] = _dict.get('published_by')
        if 'published_at' in _dict:
            args['published_at'] = string_to_datetime(_dict.get('published_at'))
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        else:
            raise ValueError('Required property \'created_by\' not present in DataProductVersion JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in DataProductVersion JSON')
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
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
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
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
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

    class TypeEnum(str, Enum):
        """
        type.
        """

        DATA = 'data'
        CODE = 'code'


class DataProductVersionCollection:
    """
    A collection of data product version summaries.

    :param int limit: Set a limit on the number of results returned.
    :param FirstPage first: First page in the collection.
    :param NextPage next: (optional) Next page in the collection.
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
    ) -> None:
        """
        Initialize a DataProductVersionCollection object.

        :param int limit: Set a limit on the number of results returned.
        :param FirstPage first: First page in the collection.
        :param List[DataProductVersionSummary] data_product_versions: Collection of
               data product versions.
        :param NextPage next: (optional) Next page in the collection.
        """
        self.limit = limit
        self.first = first
        self.next = next
        self.data_product_versions = data_product_versions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataProductVersionCollection':
        """Initialize a DataProductVersionCollection object from a json dictionary."""
        args = {}
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in DataProductVersionCollection JSON')
        if 'first' in _dict:
            args['first'] = FirstPage.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in DataProductVersionCollection JSON')
        if 'next' in _dict:
            args['next'] = NextPage.from_dict(_dict.get('next'))
        if 'data_product_versions' in _dict:
            args['data_product_versions'] = [
                DataProductVersionSummary.from_dict(v) for v in _dict.get('data_product_versions')
            ]
        else:
            raise ValueError(
                'Required property \'data_product_versions\' not present in DataProductVersionCollection JSON'
            )
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
    DataProductVersionSummary.

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
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        else:
            raise ValueError('Required property \'version\' not present in DataProductVersionSummary JSON')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in DataProductVersionSummary JSON')
        if 'data_product' in _dict:
            args['data_product'] = DataProductIdentity.from_dict(_dict.get('data_product'))
        else:
            raise ValueError('Required property \'data_product\' not present in DataProductVersionSummary JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in DataProductVersionSummary JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in DataProductVersionSummary JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in DataProductVersionSummary JSON')
        if 'asset' in _dict:
            args['asset'] = AssetReference.from_dict(_dict.get('asset'))
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
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in DeliveryMethod JSON')
        if 'container' in _dict:
            args['container'] = ContainerReference.from_dict(_dict.get('container'))
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


class DeliveryResource:
    """
    DeliveryResource.

    :param str status: Status of the deliver operation.
    :param str href: (optional) Link to monitor the status of the deliver operation.
    """

    def __init__(
        self,
        status: str,
        *,
        href: Optional[str] = None,
    ) -> None:
        """
        Initialize a DeliveryResource object.

        :param str status: Status of the deliver operation.
        :param str href: (optional) Link to monitor the status of the deliver
               operation.
        """
        self.status = status
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeliveryResource':
        """Initialize a DeliveryResource object from a json dictionary."""
        args = {}
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in DeliveryResource JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeliveryResource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeliveryResource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeliveryResource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeliveryResource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        Status of the deliver operation.
        """

        NOT_STARTED = 'not_started'
        RECEIVED = 'received'
        DELIVERED = 'delivered'
        SUCCEEDED = 'succeeded'
        FAILED = 'failed'


class Domain:
    """
    The business domain associated with the data product version.

    :param str id: The ID of the domain.
    :param str name: The display name of the domain.
    :param ContainerReference container: (optional) Data product exchange container.
    """

    def __init__(
        self,
        id: str,
        name: str,
        *,
        container: Optional['ContainerReference'] = None,
    ) -> None:
        """
        Initialize a Domain object.

        :param str id: The ID of the domain.
        :param str name: The display name of the domain.
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
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Domain JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in Domain JSON')
        if 'container' in _dict:
            args['container'] = ContainerReference.from_dict(_dict.get('container'))
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


class ErrorModel:
    """
    ErrorModel.

    :param str code: (optional)
    :param ErrorTargetModel target: (optional)
    :param str message: (optional)
    :param str more_info: (optional)
    """

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        target: Optional['ErrorTargetModel'] = None,
        message: Optional[str] = None,
        more_info: Optional[str] = None,
    ) -> None:
        """
        Initialize a ErrorModel object.

        :param str code: (optional)
        :param ErrorTargetModel target: (optional)
        :param str message: (optional)
        :param str more_info: (optional)
        """
        self.code = code
        self.target = target
        self.message = message
        self.more_info = more_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ErrorModel':
        """Initialize a ErrorModel object from a json dictionary."""
        args = {}
        if 'code' in _dict:
            args['code'] = _dict.get('code')
        if 'target' in _dict:
            args['target'] = ErrorTargetModel.from_dict(_dict.get('target'))
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        if 'more_info' in _dict:
            args['more_info'] = _dict.get('more_info')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ErrorModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'code') and self.code is not None:
            _dict['code'] = self.code
        if hasattr(self, 'target') and self.target is not None:
            if isinstance(self.target, dict):
                _dict['target'] = self.target
            else:
                _dict['target'] = self.target.to_dict()
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        if hasattr(self, 'more_info') and self.more_info is not None:
            _dict['more_info'] = self.more_info
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ErrorModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ErrorModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ErrorModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ErrorTargetModel:
    """
    ErrorTargetModel.

    :param str type: (optional)
    :param str name: (optional)
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        name: Optional[str] = None,
    ) -> None:
        """
        Initialize a ErrorTargetModel object.

        :param str type: (optional)
        :param str name: (optional)
        """
        self.type = type
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ErrorTargetModel':
        """Initialize a ErrorTargetModel object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ErrorTargetModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ErrorTargetModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ErrorTargetModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ErrorTargetModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        type.
        """

        FIELD = 'field'
        PARAMETER = 'parameter'
        HEADER = 'header'


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
        if 'href' in _dict:
            args['href'] = _dict.get('href')
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
    InitializeResource.

    :param ContainerReference container: (optional) Data product exchange container.
    :param str href: (optional) Link to monitor the status of the initialize
          operation.
    :param str status: (optional) Status of the initialize operation.
    :param str trace: (optional) The id to trace the failed initialization
          operation.
    :param List[ErrorModel] errors: (optional) The error(s) encountered in the
          initialization operation.
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
        errors: Optional[List['ErrorModel']] = None,
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
        :param List[ErrorModel] errors: (optional) The error(s) encountered in the
               initialization operation.
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
        if 'container' in _dict:
            args['container'] = ContainerReference.from_dict(_dict.get('container'))
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'trace' in _dict:
            args['trace'] = _dict.get('trace')
        if 'errors' in _dict:
            args['errors'] = [ErrorModel.from_dict(v) for v in _dict.get('errors')]
        if 'last_started_at' in _dict:
            args['last_started_at'] = string_to_datetime(_dict.get('last_started_at'))
        if 'last_finished_at' in _dict:
            args['last_finished_at'] = string_to_datetime(_dict.get('last_finished_at'))
        if 'initialized_options' in _dict:
            args['initialized_options'] = [InitializedOption.from_dict(v) for v in _dict.get('initialized_options')]
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
    Initialized options.

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
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
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


class ItemReference:
    """
    ItemReference.

    :param str id: The unique identifier of an item on an asset list representing a
          data product order.
    """

    def __init__(
        self,
        id: str,
    ) -> None:
        """
        Initialize a ItemReference object.

        :param str id: The unique identifier of an item on an asset list
               representing a data product order.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ItemReference':
        """Initialize a ItemReference object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ItemReference JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ItemReference object from a json dictionary."""
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
        """Return a `str` version of this ItemReference object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ItemReference') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ItemReference') -> bool:
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
        if 'op' in _dict:
            args['op'] = _dict.get('op')
        else:
            raise ValueError('Required property \'op\' not present in JsonPatchOperation JSON')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        else:
            raise ValueError('Required property \'path\' not present in JsonPatchOperation JSON')
        if 'from' in _dict:
            args['from_'] = _dict.get('from')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
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
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in NextPage JSON')
        if 'start' in _dict:
            args['start'] = _dict.get('start')
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


class OrderReference:
    """
    The order for the data product that should be delivered as part of this delivery
    operation.

    :param str id: The unique identifier of the asset list representing a data
          product order.
    :param List[ItemReference] items: (optional) The list of items to be delivered
          as part of this operation. This list can be a subset of items belonging to this
          order. All items specified must belong to this order.
    """

    def __init__(
        self,
        id: str,
        *,
        items: Optional[List['ItemReference']] = None,
    ) -> None:
        """
        Initialize a OrderReference object.

        :param str id: The unique identifier of the asset list representing a data
               product order.
        :param List[ItemReference] items: (optional) The list of items to be
               delivered as part of this operation. This list can be a subset of items
               belonging to this order. All items specified must belong to this order.
        """
        self.id = id
        self.items = items

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'OrderReference':
        """Initialize a OrderReference object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in OrderReference JSON')
        if 'items' in _dict:
            args['items'] = [ItemReference.from_dict(v) for v in _dict.get('items')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OrderReference object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'items') and self.items is not None:
            items_list = []
            for v in self.items:
                if isinstance(v, dict):
                    items_list.append(v)
                else:
                    items_list.append(v.to_dict())
            _dict['items'] = items_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this OrderReference object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'OrderReference') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OrderReference') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UseCase:
    """
    UseCase.

    :param str id: The id of the use case associated with the data product.
    :param str name: The display name of the use case associated with the data
          product.
    :param ContainerReference container: (optional) Data product exchange container.
    """

    def __init__(
        self,
        id: str,
        name: str,
        *,
        container: Optional['ContainerReference'] = None,
    ) -> None:
        """
        Initialize a UseCase object.

        :param str id: The id of the use case associated with the data product.
        :param str name: The display name of the use case associated with the data
               product.
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
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in UseCase JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in UseCase JSON')
        if 'container' in _dict:
            args['container'] = ContainerReference.from_dict(_dict.get('container'))
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
        client: DataProductExchangeApiServiceV1,
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
        :return: A List[dict], where each element is a dict that represents an instance of DataProduct.
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
        :return: A List[dict], where each element is a dict that represents an instance of DataProduct.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class DataProductVersionsPager:
    """
    DataProductVersionsPager can be used to simplify the use of the "list_data_product_versions" method.
    """

    def __init__(
        self,
        *,
        client: DataProductExchangeApiServiceV1,
        asset_container_id: str = None,
        data_product: str = None,
        state: str = None,
        version: str = None,
        limit: int = None,
    ) -> None:
        """
        Initialize a DataProductVersionsPager object.
        :param str asset_container_id: (optional) Filter the list of data product
               versions by container id.
        :param str data_product: (optional) Filter the list of data product
               versions by data product id.
        :param str state: (optional) Filter the list of data product versions by
               state. States are: draft, available and retired.
        :param str version: (optional) Filter the list of data product versions by
               version number.
        :param int limit: (optional) Limit the number of data products in the
               results. The maximum limit is 200.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._asset_container_id = asset_container_id
        self._data_product = data_product
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

        result = self._client.list_data_product_versions(
            asset_container_id=self._asset_container_id,
            data_product=self._data_product,
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

        return result.get('data_product_versions')

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
