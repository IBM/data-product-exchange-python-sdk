# -*- coding: utf-8 -*-
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

"""
Unit Tests for DataProductHubApiServiceV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import os
import pytest
import re
import requests
import responses
import urllib
from dph_services.data_product_hub_api_service_v1 import *


_service = DataProductHubApiServiceV1(authenticator=NoAuthAuthenticator())

_base_url = 'https://fake'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """

    # Form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if not request_url.endswith('/'):
        return request_url
    return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: Configuration
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = DataProductHubApiServiceV1.new_instance(service_name='TEST_SERVICE')

        assert service is not None
        assert isinstance(service, DataProductHubApiServiceV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DataProductHubApiServiceV1.new_instance(service_name='TEST_SERVICE_NOT_FOUND')


class TestGetInitializeStatus:
    """
    Test Class for get_initialize_status
    """

    @responses.activate
    def test_get_initialize_status_all_params(self):
        """
        get_initialize_status()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/configuration/initialize/status')
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "href": "https://api.example.com/configuration/initialize/status?catalog_id=d29c42eb-7100-4b7a-8257-c196dbcca1cd", "status": "not_started", "trace": "trace", "errors": [{"code": "request_body_error", "message": "message", "extra": {"anyKey": "anyValue"}, "more_info": "more_info"}], "last_started_at": "2023-08-21T15:24:06.021Z", "last_finished_at": "2023-08-21T20:24:34.450Z", "initialized_options": [{"name": "name", "version": 1}], "workflows": {"data_access": {"definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}, "request_new_product": {"definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        container_id = 'testString'

        # Invoke method
        response = _service.get_initialize_status(container_id=container_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'container.id={}'.format(container_id) in query_string

    def test_get_initialize_status_all_params_with_retries(self):
        # Enable retries and run test_get_initialize_status_all_params.
        _service.enable_retries()
        self.test_get_initialize_status_all_params()

        # Disable retries and run test_get_initialize_status_all_params.
        _service.disable_retries()
        self.test_get_initialize_status_all_params()

    @responses.activate
    def test_get_initialize_status_required_params(self):
        """
        test_get_initialize_status_required_params()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/configuration/initialize/status')
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "href": "https://api.example.com/configuration/initialize/status?catalog_id=d29c42eb-7100-4b7a-8257-c196dbcca1cd", "status": "not_started", "trace": "trace", "errors": [{"code": "request_body_error", "message": "message", "extra": {"anyKey": "anyValue"}, "more_info": "more_info"}], "last_started_at": "2023-08-21T15:24:06.021Z", "last_finished_at": "2023-08-21T20:24:34.450Z", "initialized_options": [{"name": "name", "version": 1}], "workflows": {"data_access": {"definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}, "request_new_product": {"definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Invoke method
        response = _service.get_initialize_status()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_initialize_status_required_params_with_retries(self):
        # Enable retries and run test_get_initialize_status_required_params.
        _service.enable_retries()
        self.test_get_initialize_status_required_params()

        # Disable retries and run test_get_initialize_status_required_params.
        _service.disable_retries()
        self.test_get_initialize_status_required_params()


class TestGetServiceIdCredentials:
    """
    Test Class for get_service_id_credentials
    """

    @responses.activate
    def test_get_service_id_credentials_all_params(self):
        """
        get_service_id_credentials()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/configuration/credentials')
        mock_response = '{"name": "data-product-admin-service-id-API-key", "created_at": "2024-03-15T04:07+0000"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Invoke method
        response = _service.get_service_id_credentials()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_service_id_credentials_all_params_with_retries(self):
        # Enable retries and run test_get_service_id_credentials_all_params.
        _service.enable_retries()
        self.test_get_service_id_credentials_all_params()

        # Disable retries and run test_get_service_id_credentials_all_params.
        _service.disable_retries()
        self.test_get_service_id_credentials_all_params()


class TestInitialize:
    """
    Test Class for initialize
    """

    @responses.activate
    def test_initialize_all_params(self):
        """
        initialize()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/configuration/initialize')
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "href": "https://api.example.com/configuration/initialize/status?catalog_id=d29c42eb-7100-4b7a-8257-c196dbcca1cd", "status": "not_started", "trace": "trace", "errors": [{"code": "request_body_error", "message": "message", "extra": {"anyKey": "anyValue"}, "more_info": "more_info"}], "last_started_at": "2023-08-21T15:24:06.021Z", "last_finished_at": "2023-08-21T20:24:34.450Z", "initialized_options": [{"name": "name", "version": 1}], "workflows": {"data_access": {"definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}, "request_new_product": {"definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=202)

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {}
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Set up parameter values
        container = container_reference_model
        include = [
            'delivery_methods',
            'domains_multi_industry',
            'data_product_samples',
            'workflows',
            'project',
            'catalog_configurations',
        ]

        # Invoke method
        response = _service.initialize(container=container, include=include, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['container'] == container_reference_model
        assert req_body['include'] == [
            'delivery_methods',
            'domains_multi_industry',
            'data_product_samples',
            'workflows',
            'project',
            'catalog_configurations',
        ]

    def test_initialize_all_params_with_retries(self):
        # Enable retries and run test_initialize_all_params.
        _service.enable_retries()
        self.test_initialize_all_params()

        # Disable retries and run test_initialize_all_params.
        _service.disable_retries()
        self.test_initialize_all_params()


class TestManageApiKeys:
    """
    Test Class for manage_api_keys
    """

    @responses.activate
    def test_manage_api_keys_all_params(self):
        """
        manage_api_keys()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/configuration/rotate_credentials')
        responses.add(responses.POST, url, status=204)

        # Invoke method
        response = _service.manage_api_keys()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_manage_api_keys_all_params_with_retries(self):
        # Enable retries and run test_manage_api_keys_all_params.
        _service.enable_retries()
        self.test_manage_api_keys_all_params()

        # Disable retries and run test_manage_api_keys_all_params.
        _service.disable_retries()
        self.test_manage_api_keys_all_params()


# endregion
##############################################################################
# End of Service: Configuration
##############################################################################

##############################################################################
# Start of Service: DataProducts
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = DataProductHubApiServiceV1.new_instance(service_name='TEST_SERVICE')

        assert service is not None
        assert isinstance(service, DataProductHubApiServiceV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DataProductHubApiServiceV1.new_instance(service_name='TEST_SERVICE_NOT_FOUND')


class TestListDataProducts:
    """
    Test Class for list_data_products
    """

    @responses.activate
    def test_list_data_products_all_params(self):
        """
        list_data_products()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products')
        mock_response = '{"limit": 200, "first": {"href": "https://api.example.com/collection"}, "next": {"href": "https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "data_products": [{"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        limit = 200
        start = 'testString'

        # Invoke method
        response = _service.list_data_products(limit=limit, start=start, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_data_products_all_params_with_retries(self):
        # Enable retries and run test_list_data_products_all_params.
        _service.enable_retries()
        self.test_list_data_products_all_params()

        # Disable retries and run test_list_data_products_all_params.
        _service.disable_retries()
        self.test_list_data_products_all_params()

    @responses.activate
    def test_list_data_products_required_params(self):
        """
        test_list_data_products_required_params()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products')
        mock_response = '{"limit": 200, "first": {"href": "https://api.example.com/collection"}, "next": {"href": "https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "data_products": [{"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Invoke method
        response = _service.list_data_products()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_data_products_required_params_with_retries(self):
        # Enable retries and run test_list_data_products_required_params.
        _service.enable_retries()
        self.test_list_data_products_required_params()

        # Disable retries and run test_list_data_products_required_params.
        _service.disable_retries()
        self.test_list_data_products_required_params()

    @responses.activate
    def test_list_data_products_with_pager_get_next(self):
        """
        test_list_data_products_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/data_product_exchange/v1/data_products')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"data_products":[{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"data_products":[{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = DataProductsPager(client=_service, limit=10)
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_data_products_with_pager_get_all(self):
        """
        test_list_data_products_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/data_product_exchange/v1/data_products')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"data_products":[{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"data_products":[{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        pager = DataProductsPager(client=_service, limit=10)
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateDataProduct:
    """
    Test Class for create_data_product
    """

    @responses.activate
    def test_create_data_product_all_params(self):
        """
        create_data_product()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products')
        mock_response = '{"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "latest_release": {"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}, "drafts": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Construct a dict representation of a DataProductDraftVersionRelease model
        data_product_draft_version_release_model = {}
        data_product_draft_version_release_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        # Construct a dict representation of a DataProductIdentity model
        data_product_identity_model = {}
        data_product_identity_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_identity_model['release'] = data_product_draft_version_release_model

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {}
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Construct a dict representation of a UseCase model
        use_case_model = {}
        use_case_model['id'] = 'testString'
        use_case_model['name'] = 'testString'
        use_case_model['container'] = container_reference_model

        # Construct a dict representation of a AssetReference model
        asset_reference_model = {}
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['container'] = container_reference_model

        # Construct a dict representation of a ContractTermsDocumentAttachment model
        contract_terms_document_attachment_model = {}
        contract_terms_document_attachment_model['id'] = 'testString'

        # Construct a dict representation of a ContractTermsDocument model
        contract_terms_document_model = {}
        contract_terms_document_model['url'] = 'testString'
        contract_terms_document_model['type'] = 'terms_and_conditions'
        contract_terms_document_model['name'] = 'testString'
        contract_terms_document_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        contract_terms_document_model['attachment'] = contract_terms_document_attachment_model
        contract_terms_document_model['upload_url'] = 'testString'

        # Construct a dict representation of a DataProductContractTerms model
        data_product_contract_terms_model = {}
        data_product_contract_terms_model['asset'] = asset_reference_model
        data_product_contract_terms_model['id'] = 'testString'
        data_product_contract_terms_model['documents'] = [contract_terms_document_model]
        data_product_contract_terms_model['error_msg'] = 'testString'

        # Construct a dict representation of a ContainerIdentity model
        container_identity_model = {}
        container_identity_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'

        # Construct a dict representation of a AssetPrototype model
        asset_prototype_model = {}
        asset_prototype_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_prototype_model['container'] = container_identity_model

        # Construct a dict representation of a Domain model
        domain_model = {}
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        # Construct a dict representation of a AssetPartReference model
        asset_part_reference_model = {}
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        # Construct a dict representation of a DeliveryMethod model
        delivery_method_model = {}
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model

        # Construct a dict representation of a DataProductPart model
        data_product_part_model = {}
        data_product_part_model['asset'] = asset_part_reference_model
        data_product_part_model['delivery_methods'] = [delivery_method_model]

        # Construct a dict representation of a DataProductCustomWorkflowDefinition model
        data_product_custom_workflow_definition_model = {}
        data_product_custom_workflow_definition_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        # Construct a dict representation of a DataProductOrderAccessRequest model
        data_product_order_access_request_model = {}
        data_product_order_access_request_model['task_assignee_users'] = ['testString']
        data_product_order_access_request_model['pre_approved_users'] = ['testString']
        data_product_order_access_request_model['custom_workflow_definition'] = (
            data_product_custom_workflow_definition_model
        )

        # Construct a dict representation of a DataProductWorkflows model
        data_product_workflows_model = {}
        data_product_workflows_model['order_access_request'] = data_product_order_access_request_model

        # Construct a dict representation of a DataProductVersionPrototype model
        data_product_version_prototype_model = {}
        data_product_version_prototype_model['version'] = '1.0.0'
        data_product_version_prototype_model['state'] = 'draft'
        data_product_version_prototype_model['data_product'] = data_product_identity_model
        data_product_version_prototype_model['name'] = 'My New Data Product'
        data_product_version_prototype_model['description'] = 'This is a description of My Data Product.'
        data_product_version_prototype_model['tags'] = ['testString']
        data_product_version_prototype_model['use_cases'] = [use_case_model]
        data_product_version_prototype_model['types'] = ['data']
        data_product_version_prototype_model['contract_terms'] = [data_product_contract_terms_model]
        data_product_version_prototype_model['is_restricted'] = True
        data_product_version_prototype_model['asset'] = asset_prototype_model
        data_product_version_prototype_model['domain'] = domain_model
        data_product_version_prototype_model['parts_out'] = [data_product_part_model]
        data_product_version_prototype_model['workflows'] = data_product_workflows_model

        # Set up parameter values
        drafts = [data_product_version_prototype_model]

        # Invoke method
        response = _service.create_data_product(drafts, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['drafts'] == [data_product_version_prototype_model]

    def test_create_data_product_all_params_with_retries(self):
        # Enable retries and run test_create_data_product_all_params.
        _service.enable_retries()
        self.test_create_data_product_all_params()

        # Disable retries and run test_create_data_product_all_params.
        _service.disable_retries()
        self.test_create_data_product_all_params()

    @responses.activate
    def test_create_data_product_value_error(self):
        """
        test_create_data_product_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products')
        mock_response = '{"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "latest_release": {"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}, "drafts": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Construct a dict representation of a DataProductDraftVersionRelease model
        data_product_draft_version_release_model = {}
        data_product_draft_version_release_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        # Construct a dict representation of a DataProductIdentity model
        data_product_identity_model = {}
        data_product_identity_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_identity_model['release'] = data_product_draft_version_release_model

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {}
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Construct a dict representation of a UseCase model
        use_case_model = {}
        use_case_model['id'] = 'testString'
        use_case_model['name'] = 'testString'
        use_case_model['container'] = container_reference_model

        # Construct a dict representation of a AssetReference model
        asset_reference_model = {}
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['container'] = container_reference_model

        # Construct a dict representation of a ContractTermsDocumentAttachment model
        contract_terms_document_attachment_model = {}
        contract_terms_document_attachment_model['id'] = 'testString'

        # Construct a dict representation of a ContractTermsDocument model
        contract_terms_document_model = {}
        contract_terms_document_model['url'] = 'testString'
        contract_terms_document_model['type'] = 'terms_and_conditions'
        contract_terms_document_model['name'] = 'testString'
        contract_terms_document_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        contract_terms_document_model['attachment'] = contract_terms_document_attachment_model
        contract_terms_document_model['upload_url'] = 'testString'

        # Construct a dict representation of a DataProductContractTerms model
        data_product_contract_terms_model = {}
        data_product_contract_terms_model['asset'] = asset_reference_model
        data_product_contract_terms_model['id'] = 'testString'
        data_product_contract_terms_model['documents'] = [contract_terms_document_model]
        data_product_contract_terms_model['error_msg'] = 'testString'

        # Construct a dict representation of a ContainerIdentity model
        container_identity_model = {}
        container_identity_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'

        # Construct a dict representation of a AssetPrototype model
        asset_prototype_model = {}
        asset_prototype_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_prototype_model['container'] = container_identity_model

        # Construct a dict representation of a Domain model
        domain_model = {}
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        # Construct a dict representation of a AssetPartReference model
        asset_part_reference_model = {}
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        # Construct a dict representation of a DeliveryMethod model
        delivery_method_model = {}
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model

        # Construct a dict representation of a DataProductPart model
        data_product_part_model = {}
        data_product_part_model['asset'] = asset_part_reference_model
        data_product_part_model['delivery_methods'] = [delivery_method_model]

        # Construct a dict representation of a DataProductCustomWorkflowDefinition model
        data_product_custom_workflow_definition_model = {}
        data_product_custom_workflow_definition_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        # Construct a dict representation of a DataProductOrderAccessRequest model
        data_product_order_access_request_model = {}
        data_product_order_access_request_model['task_assignee_users'] = ['testString']
        data_product_order_access_request_model['pre_approved_users'] = ['testString']
        data_product_order_access_request_model['custom_workflow_definition'] = (
            data_product_custom_workflow_definition_model
        )

        # Construct a dict representation of a DataProductWorkflows model
        data_product_workflows_model = {}
        data_product_workflows_model['order_access_request'] = data_product_order_access_request_model

        # Construct a dict representation of a DataProductVersionPrototype model
        data_product_version_prototype_model = {}
        data_product_version_prototype_model['version'] = '1.0.0'
        data_product_version_prototype_model['state'] = 'draft'
        data_product_version_prototype_model['data_product'] = data_product_identity_model
        data_product_version_prototype_model['name'] = 'My New Data Product'
        data_product_version_prototype_model['description'] = 'This is a description of My Data Product.'
        data_product_version_prototype_model['tags'] = ['testString']
        data_product_version_prototype_model['use_cases'] = [use_case_model]
        data_product_version_prototype_model['types'] = ['data']
        data_product_version_prototype_model['contract_terms'] = [data_product_contract_terms_model]
        data_product_version_prototype_model['is_restricted'] = True
        data_product_version_prototype_model['asset'] = asset_prototype_model
        data_product_version_prototype_model['domain'] = domain_model
        data_product_version_prototype_model['parts_out'] = [data_product_part_model]
        data_product_version_prototype_model['workflows'] = data_product_workflows_model

        # Set up parameter values
        drafts = [data_product_version_prototype_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {"drafts": drafts}
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_data_product(**req_copy)

    def test_create_data_product_value_error_with_retries(self):
        # Enable retries and run test_create_data_product_value_error.
        _service.enable_retries()
        self.test_create_data_product_value_error()

        # Disable retries and run test_create_data_product_value_error.
        _service.disable_retries()
        self.test_create_data_product_value_error()


class TestGetDataProduct:
    """
    Test Class for get_data_product
    """

    @responses.activate
    def test_get_data_product_all_params(self):
        """
        get_data_product()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString')
        mock_response = '{"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "latest_release": {"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}, "drafts": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'

        # Invoke method
        response = _service.get_data_product(data_product_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_data_product_all_params_with_retries(self):
        # Enable retries and run test_get_data_product_all_params.
        _service.enable_retries()
        self.test_get_data_product_all_params()

        # Disable retries and run test_get_data_product_all_params.
        _service.disable_retries()
        self.test_get_data_product_all_params()

    @responses.activate
    def test_get_data_product_value_error(self):
        """
        test_get_data_product_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString')
        mock_response = '{"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "latest_release": {"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}, "drafts": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {"data_product_id": data_product_id}
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_data_product(**req_copy)

    def test_get_data_product_value_error_with_retries(self):
        # Enable retries and run test_get_data_product_value_error.
        _service.enable_retries()
        self.test_get_data_product_value_error()

        # Disable retries and run test_get_data_product_value_error.
        _service.disable_retries()
        self.test_get_data_product_value_error()


# endregion
##############################################################################
# End of Service: DataProducts
##############################################################################

##############################################################################
# Start of Service: DataProductDrafts
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = DataProductHubApiServiceV1.new_instance(service_name='TEST_SERVICE')

        assert service is not None
        assert isinstance(service, DataProductHubApiServiceV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DataProductHubApiServiceV1.new_instance(service_name='TEST_SERVICE_NOT_FOUND')


class TestCompleteDraftContractTermsDocument:
    """
    Test Class for complete_draft_contract_terms_document
    """

    @responses.activate
    def test_complete_draft_contract_terms_document_all_params(self):
        """
        complete_draft_contract_terms_document()
        """
        # Set up mock
        url = preprocess_url(
            '/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString/documents/testString/complete'
        )
        mock_response = '{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'
        contract_terms_id = 'testString'
        document_id = 'testString'

        # Invoke method
        response = _service.complete_draft_contract_terms_document(
            data_product_id, draft_id, contract_terms_id, document_id, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_complete_draft_contract_terms_document_all_params_with_retries(self):
        # Enable retries and run test_complete_draft_contract_terms_document_all_params.
        _service.enable_retries()
        self.test_complete_draft_contract_terms_document_all_params()

        # Disable retries and run test_complete_draft_contract_terms_document_all_params.
        _service.disable_retries()
        self.test_complete_draft_contract_terms_document_all_params()

    @responses.activate
    def test_complete_draft_contract_terms_document_value_error(self):
        """
        test_complete_draft_contract_terms_document_value_error()
        """
        # Set up mock
        url = preprocess_url(
            '/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString/documents/testString/complete'
        )
        mock_response = '{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'
        contract_terms_id = 'testString'
        document_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_product_id": data_product_id,
            "draft_id": draft_id,
            "contract_terms_id": contract_terms_id,
            "document_id": document_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.complete_draft_contract_terms_document(**req_copy)

    def test_complete_draft_contract_terms_document_value_error_with_retries(self):
        # Enable retries and run test_complete_draft_contract_terms_document_value_error.
        _service.enable_retries()
        self.test_complete_draft_contract_terms_document_value_error()

        # Disable retries and run test_complete_draft_contract_terms_document_value_error.
        _service.disable_retries()
        self.test_complete_draft_contract_terms_document_value_error()


class TestListDataProductDrafts:
    """
    Test Class for list_data_product_drafts
    """

    @responses.activate
    def test_list_data_product_drafts_all_params(self):
        """
        list_data_product_drafts()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts')
        mock_response = '{"limit": 200, "first": {"href": "https://api.example.com/collection"}, "next": {"href": "https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "drafts": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'
        asset_container_id = 'testString'
        version = 'testString'
        limit = 200
        start = 'testString'

        # Invoke method
        response = _service.list_data_product_drafts(
            data_product_id,
            asset_container_id=asset_container_id,
            version=version,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'asset.container.id={}'.format(asset_container_id) in query_string
        assert 'version={}'.format(version) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_data_product_drafts_all_params_with_retries(self):
        # Enable retries and run test_list_data_product_drafts_all_params.
        _service.enable_retries()
        self.test_list_data_product_drafts_all_params()

        # Disable retries and run test_list_data_product_drafts_all_params.
        _service.disable_retries()
        self.test_list_data_product_drafts_all_params()

    @responses.activate
    def test_list_data_product_drafts_required_params(self):
        """
        test_list_data_product_drafts_required_params()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts')
        mock_response = '{"limit": 200, "first": {"href": "https://api.example.com/collection"}, "next": {"href": "https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "drafts": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'

        # Invoke method
        response = _service.list_data_product_drafts(data_product_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_data_product_drafts_required_params_with_retries(self):
        # Enable retries and run test_list_data_product_drafts_required_params.
        _service.enable_retries()
        self.test_list_data_product_drafts_required_params()

        # Disable retries and run test_list_data_product_drafts_required_params.
        _service.disable_retries()
        self.test_list_data_product_drafts_required_params()

    @responses.activate
    def test_list_data_product_drafts_value_error(self):
        """
        test_list_data_product_drafts_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts')
        mock_response = '{"limit": 200, "first": {"href": "https://api.example.com/collection"}, "next": {"href": "https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "drafts": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {"data_product_id": data_product_id}
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_data_product_drafts(**req_copy)

    def test_list_data_product_drafts_value_error_with_retries(self):
        # Enable retries and run test_list_data_product_drafts_value_error.
        _service.enable_retries()
        self.test_list_data_product_drafts_value_error()

        # Disable retries and run test_list_data_product_drafts_value_error.
        _service.disable_retries()
        self.test_list_data_product_drafts_value_error()

    @responses.activate
    def test_list_data_product_drafts_with_pager_get_next(self):
        """
        test_list_data_product_drafts_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"drafts":[{"version":"1.0.0","state":"draft","data_product":{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"name":"My Data Product","description":"This is a description of My Data Product.","tags":["tags"],"use_cases":[{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}],"types":["data"],"contract_terms":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"id":"id","documents":[{"url":"url","type":"terms_and_conditions","name":"name","id":"2b0bf220-079c-11ee-be56-0242ac120002","attachment":{"id":"id"},"upload_url":"upload_url"}],"error_msg":"error_msg"}],"is_restricted":false,"id":"2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd","asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"drafts":[{"version":"1.0.0","state":"draft","data_product":{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"name":"My Data Product","description":"This is a description of My Data Product.","tags":["tags"],"use_cases":[{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}],"types":["data"],"contract_terms":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"id":"id","documents":[{"url":"url","type":"terms_and_conditions","name":"name","id":"2b0bf220-079c-11ee-be56-0242ac120002","attachment":{"id":"id"},"upload_url":"upload_url"}],"error_msg":"error_msg"}],"is_restricted":false,"id":"2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd","asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = DataProductDraftsPager(
            client=_service,
            data_product_id='testString',
            asset_container_id='testString',
            version='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_data_product_drafts_with_pager_get_all(self):
        """
        test_list_data_product_drafts_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"drafts":[{"version":"1.0.0","state":"draft","data_product":{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"name":"My Data Product","description":"This is a description of My Data Product.","tags":["tags"],"use_cases":[{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}],"types":["data"],"contract_terms":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"id":"id","documents":[{"url":"url","type":"terms_and_conditions","name":"name","id":"2b0bf220-079c-11ee-be56-0242ac120002","attachment":{"id":"id"},"upload_url":"upload_url"}],"error_msg":"error_msg"}],"is_restricted":false,"id":"2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd","asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"drafts":[{"version":"1.0.0","state":"draft","data_product":{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"name":"My Data Product","description":"This is a description of My Data Product.","tags":["tags"],"use_cases":[{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}],"types":["data"],"contract_terms":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"id":"id","documents":[{"url":"url","type":"terms_and_conditions","name":"name","id":"2b0bf220-079c-11ee-be56-0242ac120002","attachment":{"id":"id"},"upload_url":"upload_url"}],"error_msg":"error_msg"}],"is_restricted":false,"id":"2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd","asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        pager = DataProductDraftsPager(
            client=_service,
            data_product_id='testString',
            asset_container_id='testString',
            version='testString',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateDataProductDraft:
    """
    Test Class for create_data_product_draft
    """

    @responses.activate
    def test_create_data_product_draft_all_params(self):
        """
        create_data_product_draft()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}], "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "properties": {"anyKey": "anyValue"}}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Construct a dict representation of a ContainerIdentity model
        container_identity_model = {}
        container_identity_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'

        # Construct a dict representation of a AssetPrototype model
        asset_prototype_model = {}
        asset_prototype_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_prototype_model['container'] = container_identity_model

        # Construct a dict representation of a DataProductDraftVersionRelease model
        data_product_draft_version_release_model = {}
        data_product_draft_version_release_model['id'] = '8bf83660-11fe-4427-a72a-8d8359af24e3'

        # Construct a dict representation of a DataProductIdentity model
        data_product_identity_model = {}
        data_product_identity_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_identity_model['release'] = data_product_draft_version_release_model

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {}
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Construct a dict representation of a UseCase model
        use_case_model = {}
        use_case_model['id'] = 'testString'
        use_case_model['name'] = 'testString'
        use_case_model['container'] = container_reference_model

        # Construct a dict representation of a AssetReference model
        asset_reference_model = {}
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['container'] = container_reference_model

        # Construct a dict representation of a ContractTermsDocumentAttachment model
        contract_terms_document_attachment_model = {}
        contract_terms_document_attachment_model['id'] = 'testString'

        # Construct a dict representation of a ContractTermsDocument model
        contract_terms_document_model = {}
        contract_terms_document_model['url'] = 'testString'
        contract_terms_document_model['type'] = 'terms_and_conditions'
        contract_terms_document_model['name'] = 'testString'
        contract_terms_document_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        contract_terms_document_model['attachment'] = contract_terms_document_attachment_model
        contract_terms_document_model['upload_url'] = 'testString'

        # Construct a dict representation of a DataProductContractTerms model
        data_product_contract_terms_model = {}
        data_product_contract_terms_model['asset'] = asset_reference_model
        data_product_contract_terms_model['id'] = 'testString'
        data_product_contract_terms_model['documents'] = [contract_terms_document_model]
        data_product_contract_terms_model['error_msg'] = 'testString'

        # Construct a dict representation of a Domain model
        domain_model = {}
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        # Construct a dict representation of a AssetPartReference model
        asset_part_reference_model = {}
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        # Construct a dict representation of a DeliveryMethod model
        delivery_method_model = {}
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model

        # Construct a dict representation of a DataProductPart model
        data_product_part_model = {}
        data_product_part_model['asset'] = asset_part_reference_model
        data_product_part_model['delivery_methods'] = [delivery_method_model]

        # Construct a dict representation of a DataProductCustomWorkflowDefinition model
        data_product_custom_workflow_definition_model = {}
        data_product_custom_workflow_definition_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        # Construct a dict representation of a DataProductOrderAccessRequest model
        data_product_order_access_request_model = {}
        data_product_order_access_request_model['task_assignee_users'] = ['testString']
        data_product_order_access_request_model['pre_approved_users'] = ['testString']
        data_product_order_access_request_model['custom_workflow_definition'] = (
            data_product_custom_workflow_definition_model
        )

        # Construct a dict representation of a DataProductWorkflows model
        data_product_workflows_model = {}
        data_product_workflows_model['order_access_request'] = data_product_order_access_request_model

        # Set up parameter values
        data_product_id = 'testString'
        asset = asset_prototype_model
        version = '1.2.0'
        state = 'draft'
        data_product = data_product_identity_model
        name = 'testString'
        description = 'testString'
        tags = ['testString']
        use_cases = [use_case_model]
        types = ['data']
        contract_terms = [data_product_contract_terms_model]
        is_restricted = True
        domain = domain_model
        parts_out = [data_product_part_model]
        workflows = data_product_workflows_model

        # Invoke method
        response = _service.create_data_product_draft(
            data_product_id,
            asset,
            version=version,
            state=state,
            data_product=data_product,
            name=name,
            description=description,
            tags=tags,
            use_cases=use_cases,
            types=types,
            contract_terms=contract_terms,
            is_restricted=is_restricted,
            domain=domain,
            parts_out=parts_out,
            workflows=workflows,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['asset'] == asset_prototype_model
        assert req_body['version'] == '1.2.0'
        assert req_body['state'] == 'draft'
        assert req_body['data_product'] == data_product_identity_model
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['tags'] == ['testString']
        assert req_body['use_cases'] == [use_case_model]
        assert req_body['types'] == ['data']
        assert req_body['contract_terms'] == [data_product_contract_terms_model]
        assert req_body['is_restricted'] == True
        assert req_body['domain'] == domain_model
        assert req_body['parts_out'] == [data_product_part_model]
        assert req_body['workflows'] == data_product_workflows_model

    def test_create_data_product_draft_all_params_with_retries(self):
        # Enable retries and run test_create_data_product_draft_all_params.
        _service.enable_retries()
        self.test_create_data_product_draft_all_params()

        # Disable retries and run test_create_data_product_draft_all_params.
        _service.disable_retries()
        self.test_create_data_product_draft_all_params()

    @responses.activate
    def test_create_data_product_draft_value_error(self):
        """
        test_create_data_product_draft_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}], "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "properties": {"anyKey": "anyValue"}}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Construct a dict representation of a ContainerIdentity model
        container_identity_model = {}
        container_identity_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'

        # Construct a dict representation of a AssetPrototype model
        asset_prototype_model = {}
        asset_prototype_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_prototype_model['container'] = container_identity_model

        # Construct a dict representation of a DataProductDraftVersionRelease model
        data_product_draft_version_release_model = {}
        data_product_draft_version_release_model['id'] = '8bf83660-11fe-4427-a72a-8d8359af24e3'

        # Construct a dict representation of a DataProductIdentity model
        data_product_identity_model = {}
        data_product_identity_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_identity_model['release'] = data_product_draft_version_release_model

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {}
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Construct a dict representation of a UseCase model
        use_case_model = {}
        use_case_model['id'] = 'testString'
        use_case_model['name'] = 'testString'
        use_case_model['container'] = container_reference_model

        # Construct a dict representation of a AssetReference model
        asset_reference_model = {}
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['container'] = container_reference_model

        # Construct a dict representation of a ContractTermsDocumentAttachment model
        contract_terms_document_attachment_model = {}
        contract_terms_document_attachment_model['id'] = 'testString'

        # Construct a dict representation of a ContractTermsDocument model
        contract_terms_document_model = {}
        contract_terms_document_model['url'] = 'testString'
        contract_terms_document_model['type'] = 'terms_and_conditions'
        contract_terms_document_model['name'] = 'testString'
        contract_terms_document_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        contract_terms_document_model['attachment'] = contract_terms_document_attachment_model
        contract_terms_document_model['upload_url'] = 'testString'

        # Construct a dict representation of a DataProductContractTerms model
        data_product_contract_terms_model = {}
        data_product_contract_terms_model['asset'] = asset_reference_model
        data_product_contract_terms_model['id'] = 'testString'
        data_product_contract_terms_model['documents'] = [contract_terms_document_model]
        data_product_contract_terms_model['error_msg'] = 'testString'

        # Construct a dict representation of a Domain model
        domain_model = {}
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        # Construct a dict representation of a AssetPartReference model
        asset_part_reference_model = {}
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        # Construct a dict representation of a DeliveryMethod model
        delivery_method_model = {}
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model

        # Construct a dict representation of a DataProductPart model
        data_product_part_model = {}
        data_product_part_model['asset'] = asset_part_reference_model
        data_product_part_model['delivery_methods'] = [delivery_method_model]

        # Construct a dict representation of a DataProductCustomWorkflowDefinition model
        data_product_custom_workflow_definition_model = {}
        data_product_custom_workflow_definition_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        # Construct a dict representation of a DataProductOrderAccessRequest model
        data_product_order_access_request_model = {}
        data_product_order_access_request_model['task_assignee_users'] = ['testString']
        data_product_order_access_request_model['pre_approved_users'] = ['testString']
        data_product_order_access_request_model['custom_workflow_definition'] = (
            data_product_custom_workflow_definition_model
        )

        # Construct a dict representation of a DataProductWorkflows model
        data_product_workflows_model = {}
        data_product_workflows_model['order_access_request'] = data_product_order_access_request_model

        # Set up parameter values
        data_product_id = 'testString'
        asset = asset_prototype_model
        version = '1.2.0'
        state = 'draft'
        data_product = data_product_identity_model
        name = 'testString'
        description = 'testString'
        tags = ['testString']
        use_cases = [use_case_model]
        types = ['data']
        contract_terms = [data_product_contract_terms_model]
        is_restricted = True
        domain = domain_model
        parts_out = [data_product_part_model]
        workflows = data_product_workflows_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {"data_product_id": data_product_id, "asset": asset}
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_data_product_draft(**req_copy)

    def test_create_data_product_draft_value_error_with_retries(self):
        # Enable retries and run test_create_data_product_draft_value_error.
        _service.enable_retries()
        self.test_create_data_product_draft_value_error()

        # Disable retries and run test_create_data_product_draft_value_error.
        _service.disable_retries()
        self.test_create_data_product_draft_value_error()


class TestCreateDraftContractTermsDocument:
    """
    Test Class for create_draft_contract_terms_document
    """

    @responses.activate
    def test_create_draft_contract_terms_document_all_params(self):
        """
        create_draft_contract_terms_document()
        """
        # Set up mock
        url = preprocess_url(
            '/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString/documents'
        )
        mock_response = '{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'
        contract_terms_id = 'testString'
        type = 'terms_and_conditions'
        name = 'Terms and conditions document'
        url = 'testString'

        # Invoke method
        response = _service.create_draft_contract_terms_document(
            data_product_id, draft_id, contract_terms_id, type, name, url=url, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'terms_and_conditions'
        assert req_body['name'] == 'Terms and conditions document'
        assert req_body['url'] == 'testString'

    def test_create_draft_contract_terms_document_all_params_with_retries(self):
        # Enable retries and run test_create_draft_contract_terms_document_all_params.
        _service.enable_retries()
        self.test_create_draft_contract_terms_document_all_params()

        # Disable retries and run test_create_draft_contract_terms_document_all_params.
        _service.disable_retries()
        self.test_create_draft_contract_terms_document_all_params()

    @responses.activate
    def test_create_draft_contract_terms_document_value_error(self):
        """
        test_create_draft_contract_terms_document_value_error()
        """
        # Set up mock
        url = preprocess_url(
            '/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString/documents'
        )
        mock_response = '{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'
        contract_terms_id = 'testString'
        type = 'terms_and_conditions'
        name = 'Terms and conditions document'
        url = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_product_id": data_product_id,
            "draft_id": draft_id,
            "contract_terms_id": contract_terms_id,
            "type": type,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_draft_contract_terms_document(**req_copy)

    def test_create_draft_contract_terms_document_value_error_with_retries(self):
        # Enable retries and run test_create_draft_contract_terms_document_value_error.
        _service.enable_retries()
        self.test_create_draft_contract_terms_document_value_error()

        # Disable retries and run test_create_draft_contract_terms_document_value_error.
        _service.disable_retries()
        self.test_create_draft_contract_terms_document_value_error()


class TestGetDataProductDraft:
    """
    Test Class for get_data_product_draft
    """

    @responses.activate
    def test_get_data_product_draft_all_params(self):
        """
        get_data_product_draft()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}], "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "properties": {"anyKey": "anyValue"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'

        # Invoke method
        response = _service.get_data_product_draft(data_product_id, draft_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_data_product_draft_all_params_with_retries(self):
        # Enable retries and run test_get_data_product_draft_all_params.
        _service.enable_retries()
        self.test_get_data_product_draft_all_params()

        # Disable retries and run test_get_data_product_draft_all_params.
        _service.disable_retries()
        self.test_get_data_product_draft_all_params()

    @responses.activate
    def test_get_data_product_draft_value_error(self):
        """
        test_get_data_product_draft_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}], "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "properties": {"anyKey": "anyValue"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {"data_product_id": data_product_id, "draft_id": draft_id}
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_data_product_draft(**req_copy)

    def test_get_data_product_draft_value_error_with_retries(self):
        # Enable retries and run test_get_data_product_draft_value_error.
        _service.enable_retries()
        self.test_get_data_product_draft_value_error()

        # Disable retries and run test_get_data_product_draft_value_error.
        _service.disable_retries()
        self.test_get_data_product_draft_value_error()


class TestDeleteDataProductDraft:
    """
    Test Class for delete_data_product_draft
    """

    @responses.activate
    def test_delete_data_product_draft_all_params(self):
        """
        delete_data_product_draft()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString')
        responses.add(responses.DELETE, url, status=204)

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'

        # Invoke method
        response = _service.delete_data_product_draft(data_product_id, draft_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_data_product_draft_all_params_with_retries(self):
        # Enable retries and run test_delete_data_product_draft_all_params.
        _service.enable_retries()
        self.test_delete_data_product_draft_all_params()

        # Disable retries and run test_delete_data_product_draft_all_params.
        _service.disable_retries()
        self.test_delete_data_product_draft_all_params()

    @responses.activate
    def test_delete_data_product_draft_value_error(self):
        """
        test_delete_data_product_draft_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString')
        responses.add(responses.DELETE, url, status=204)

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {"data_product_id": data_product_id, "draft_id": draft_id}
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_data_product_draft(**req_copy)

    def test_delete_data_product_draft_value_error_with_retries(self):
        # Enable retries and run test_delete_data_product_draft_value_error.
        _service.enable_retries()
        self.test_delete_data_product_draft_value_error()

        # Disable retries and run test_delete_data_product_draft_value_error.
        _service.disable_retries()
        self.test_delete_data_product_draft_value_error()


class TestUpdateDataProductDraft:
    """
    Test Class for update_data_product_draft
    """

    @responses.activate
    def test_update_data_product_draft_all_params(self):
        """
        update_data_product_draft()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}], "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "properties": {"anyKey": "anyValue"}}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'
        json_patch_instructions = [json_patch_operation_model]

        # Invoke method
        response = _service.update_data_product_draft(data_product_id, draft_id, json_patch_instructions, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == json_patch_instructions

    def test_update_data_product_draft_all_params_with_retries(self):
        # Enable retries and run test_update_data_product_draft_all_params.
        _service.enable_retries()
        self.test_update_data_product_draft_all_params()

        # Disable retries and run test_update_data_product_draft_all_params.
        _service.disable_retries()
        self.test_update_data_product_draft_all_params()

    @responses.activate
    def test_update_data_product_draft_value_error(self):
        """
        test_update_data_product_draft_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}], "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "properties": {"anyKey": "anyValue"}}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'
        json_patch_instructions = [json_patch_operation_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_product_id": data_product_id,
            "draft_id": draft_id,
            "json_patch_instructions": json_patch_instructions,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_data_product_draft(**req_copy)

    def test_update_data_product_draft_value_error_with_retries(self):
        # Enable retries and run test_update_data_product_draft_value_error.
        _service.enable_retries()
        self.test_update_data_product_draft_value_error()

        # Disable retries and run test_update_data_product_draft_value_error.
        _service.disable_retries()
        self.test_update_data_product_draft_value_error()


class TestGetDraftContractTermsDocument:
    """
    Test Class for get_draft_contract_terms_document
    """

    @responses.activate
    def test_get_draft_contract_terms_document_all_params(self):
        """
        get_draft_contract_terms_document()
        """
        # Set up mock
        url = preprocess_url(
            '/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString/documents/testString'
        )
        mock_response = '{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'
        contract_terms_id = 'testString'
        document_id = 'testString'

        # Invoke method
        response = _service.get_draft_contract_terms_document(
            data_product_id, draft_id, contract_terms_id, document_id, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_draft_contract_terms_document_all_params_with_retries(self):
        # Enable retries and run test_get_draft_contract_terms_document_all_params.
        _service.enable_retries()
        self.test_get_draft_contract_terms_document_all_params()

        # Disable retries and run test_get_draft_contract_terms_document_all_params.
        _service.disable_retries()
        self.test_get_draft_contract_terms_document_all_params()

    @responses.activate
    def test_get_draft_contract_terms_document_value_error(self):
        """
        test_get_draft_contract_terms_document_value_error()
        """
        # Set up mock
        url = preprocess_url(
            '/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString/documents/testString'
        )
        mock_response = '{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'
        contract_terms_id = 'testString'
        document_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_product_id": data_product_id,
            "draft_id": draft_id,
            "contract_terms_id": contract_terms_id,
            "document_id": document_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_draft_contract_terms_document(**req_copy)

    def test_get_draft_contract_terms_document_value_error_with_retries(self):
        # Enable retries and run test_get_draft_contract_terms_document_value_error.
        _service.enable_retries()
        self.test_get_draft_contract_terms_document_value_error()

        # Disable retries and run test_get_draft_contract_terms_document_value_error.
        _service.disable_retries()
        self.test_get_draft_contract_terms_document_value_error()


class TestDeleteDraftContractTermsDocument:
    """
    Test Class for delete_draft_contract_terms_document
    """

    @responses.activate
    def test_delete_draft_contract_terms_document_all_params(self):
        """
        delete_draft_contract_terms_document()
        """
        # Set up mock
        url = preprocess_url(
            '/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString/documents/testString'
        )
        responses.add(responses.DELETE, url, status=204)

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'
        contract_terms_id = 'testString'
        document_id = 'testString'

        # Invoke method
        response = _service.delete_draft_contract_terms_document(
            data_product_id, draft_id, contract_terms_id, document_id, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_draft_contract_terms_document_all_params_with_retries(self):
        # Enable retries and run test_delete_draft_contract_terms_document_all_params.
        _service.enable_retries()
        self.test_delete_draft_contract_terms_document_all_params()

        # Disable retries and run test_delete_draft_contract_terms_document_all_params.
        _service.disable_retries()
        self.test_delete_draft_contract_terms_document_all_params()

    @responses.activate
    def test_delete_draft_contract_terms_document_value_error(self):
        """
        test_delete_draft_contract_terms_document_value_error()
        """
        # Set up mock
        url = preprocess_url(
            '/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString/documents/testString'
        )
        responses.add(responses.DELETE, url, status=204)

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'
        contract_terms_id = 'testString'
        document_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_product_id": data_product_id,
            "draft_id": draft_id,
            "contract_terms_id": contract_terms_id,
            "document_id": document_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_draft_contract_terms_document(**req_copy)

    def test_delete_draft_contract_terms_document_value_error_with_retries(self):
        # Enable retries and run test_delete_draft_contract_terms_document_value_error.
        _service.enable_retries()
        self.test_delete_draft_contract_terms_document_value_error()

        # Disable retries and run test_delete_draft_contract_terms_document_value_error.
        _service.disable_retries()
        self.test_delete_draft_contract_terms_document_value_error()


class TestUpdateDraftContractTermsDocument:
    """
    Test Class for update_draft_contract_terms_document
    """

    @responses.activate
    def test_update_draft_contract_terms_document_all_params(self):
        """
        update_draft_contract_terms_document()
        """
        # Set up mock
        url = preprocess_url(
            '/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString/documents/testString'
        )
        mock_response = '{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'
        contract_terms_id = 'testString'
        document_id = 'testString'
        json_patch_instructions = [json_patch_operation_model]

        # Invoke method
        response = _service.update_draft_contract_terms_document(
            data_product_id, draft_id, contract_terms_id, document_id, json_patch_instructions, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == json_patch_instructions

    def test_update_draft_contract_terms_document_all_params_with_retries(self):
        # Enable retries and run test_update_draft_contract_terms_document_all_params.
        _service.enable_retries()
        self.test_update_draft_contract_terms_document_all_params()

        # Disable retries and run test_update_draft_contract_terms_document_all_params.
        _service.disable_retries()
        self.test_update_draft_contract_terms_document_all_params()

    @responses.activate
    def test_update_draft_contract_terms_document_value_error(self):
        """
        test_update_draft_contract_terms_document_value_error()
        """
        # Set up mock
        url = preprocess_url(
            '/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString/documents/testString'
        )
        mock_response = '{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'
        contract_terms_id = 'testString'
        document_id = 'testString'
        json_patch_instructions = [json_patch_operation_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_product_id": data_product_id,
            "draft_id": draft_id,
            "contract_terms_id": contract_terms_id,
            "document_id": document_id,
            "json_patch_instructions": json_patch_instructions,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_draft_contract_terms_document(**req_copy)

    def test_update_draft_contract_terms_document_value_error_with_retries(self):
        # Enable retries and run test_update_draft_contract_terms_document_value_error.
        _service.enable_retries()
        self.test_update_draft_contract_terms_document_value_error()

        # Disable retries and run test_update_draft_contract_terms_document_value_error.
        _service.disable_retries()
        self.test_update_draft_contract_terms_document_value_error()


class TestPublishDataProductDraft:
    """
    Test Class for publish_data_product_draft
    """

    @responses.activate
    def test_publish_data_product_draft_all_params(self):
        """
        publish_data_product_draft()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString/publish')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}], "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "properties": {"anyKey": "anyValue"}}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'

        # Invoke method
        response = _service.publish_data_product_draft(data_product_id, draft_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_publish_data_product_draft_all_params_with_retries(self):
        # Enable retries and run test_publish_data_product_draft_all_params.
        _service.enable_retries()
        self.test_publish_data_product_draft_all_params()

        # Disable retries and run test_publish_data_product_draft_all_params.
        _service.disable_retries()
        self.test_publish_data_product_draft_all_params()

    @responses.activate
    def test_publish_data_product_draft_value_error(self):
        """
        test_publish_data_product_draft_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString/publish')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}], "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "properties": {"anyKey": "anyValue"}}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {"data_product_id": data_product_id, "draft_id": draft_id}
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.publish_data_product_draft(**req_copy)

    def test_publish_data_product_draft_value_error_with_retries(self):
        # Enable retries and run test_publish_data_product_draft_value_error.
        _service.enable_retries()
        self.test_publish_data_product_draft_value_error()

        # Disable retries and run test_publish_data_product_draft_value_error.
        _service.disable_retries()
        self.test_publish_data_product_draft_value_error()


# endregion
##############################################################################
# End of Service: DataProductDrafts
##############################################################################

##############################################################################
# Start of Service: DataProductReleases
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = DataProductHubApiServiceV1.new_instance(service_name='TEST_SERVICE')

        assert service is not None
        assert isinstance(service, DataProductHubApiServiceV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DataProductHubApiServiceV1.new_instance(service_name='TEST_SERVICE_NOT_FOUND')


class TestGetDataProductRelease:
    """
    Test Class for get_data_product_release
    """

    @responses.activate
    def test_get_data_product_release_all_params(self):
        """
        get_data_product_release()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/releases/testString')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}], "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "properties": {"anyKey": "anyValue"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'
        release_id = 'testString'
        check_caller_approval = False

        # Invoke method
        response = _service.get_data_product_release(
            data_product_id, release_id, check_caller_approval=check_caller_approval, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'check_caller_approval={}'.format('true' if check_caller_approval else 'false') in query_string

    def test_get_data_product_release_all_params_with_retries(self):
        # Enable retries and run test_get_data_product_release_all_params.
        _service.enable_retries()
        self.test_get_data_product_release_all_params()

        # Disable retries and run test_get_data_product_release_all_params.
        _service.disable_retries()
        self.test_get_data_product_release_all_params()

    @responses.activate
    def test_get_data_product_release_required_params(self):
        """
        test_get_data_product_release_required_params()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/releases/testString')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}], "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "properties": {"anyKey": "anyValue"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'
        release_id = 'testString'

        # Invoke method
        response = _service.get_data_product_release(data_product_id, release_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_data_product_release_required_params_with_retries(self):
        # Enable retries and run test_get_data_product_release_required_params.
        _service.enable_retries()
        self.test_get_data_product_release_required_params()

        # Disable retries and run test_get_data_product_release_required_params.
        _service.disable_retries()
        self.test_get_data_product_release_required_params()

    @responses.activate
    def test_get_data_product_release_value_error(self):
        """
        test_get_data_product_release_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/releases/testString')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}], "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "properties": {"anyKey": "anyValue"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'
        release_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {"data_product_id": data_product_id, "release_id": release_id}
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_data_product_release(**req_copy)

    def test_get_data_product_release_value_error_with_retries(self):
        # Enable retries and run test_get_data_product_release_value_error.
        _service.enable_retries()
        self.test_get_data_product_release_value_error()

        # Disable retries and run test_get_data_product_release_value_error.
        _service.disable_retries()
        self.test_get_data_product_release_value_error()


class TestUpdateDataProductRelease:
    """
    Test Class for update_data_product_release
    """

    @responses.activate
    def test_update_data_product_release_all_params(self):
        """
        update_data_product_release()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/releases/testString')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}], "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "properties": {"anyKey": "anyValue"}}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        data_product_id = 'testString'
        release_id = 'testString'
        json_patch_instructions = [json_patch_operation_model]

        # Invoke method
        response = _service.update_data_product_release(
            data_product_id, release_id, json_patch_instructions, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == json_patch_instructions

    def test_update_data_product_release_all_params_with_retries(self):
        # Enable retries and run test_update_data_product_release_all_params.
        _service.enable_retries()
        self.test_update_data_product_release_all_params()

        # Disable retries and run test_update_data_product_release_all_params.
        _service.disable_retries()
        self.test_update_data_product_release_all_params()

    @responses.activate
    def test_update_data_product_release_value_error(self):
        """
        test_update_data_product_release_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/releases/testString')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}], "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "properties": {"anyKey": "anyValue"}}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        data_product_id = 'testString'
        release_id = 'testString'
        json_patch_instructions = [json_patch_operation_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_product_id": data_product_id,
            "release_id": release_id,
            "json_patch_instructions": json_patch_instructions,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_data_product_release(**req_copy)

    def test_update_data_product_release_value_error_with_retries(self):
        # Enable retries and run test_update_data_product_release_value_error.
        _service.enable_retries()
        self.test_update_data_product_release_value_error()

        # Disable retries and run test_update_data_product_release_value_error.
        _service.disable_retries()
        self.test_update_data_product_release_value_error()


class TestGetReleaseContractTermsDocument:
    """
    Test Class for get_release_contract_terms_document
    """

    @responses.activate
    def test_get_release_contract_terms_document_all_params(self):
        """
        get_release_contract_terms_document()
        """
        # Set up mock
        url = preprocess_url(
            '/data_product_exchange/v1/data_products/testString/releases/testString/contract_terms/testString/documents/testString'
        )
        mock_response = '{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'
        release_id = 'testString'
        contract_terms_id = 'testString'
        document_id = 'testString'

        # Invoke method
        response = _service.get_release_contract_terms_document(
            data_product_id, release_id, contract_terms_id, document_id, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_release_contract_terms_document_all_params_with_retries(self):
        # Enable retries and run test_get_release_contract_terms_document_all_params.
        _service.enable_retries()
        self.test_get_release_contract_terms_document_all_params()

        # Disable retries and run test_get_release_contract_terms_document_all_params.
        _service.disable_retries()
        self.test_get_release_contract_terms_document_all_params()

    @responses.activate
    def test_get_release_contract_terms_document_value_error(self):
        """
        test_get_release_contract_terms_document_value_error()
        """
        # Set up mock
        url = preprocess_url(
            '/data_product_exchange/v1/data_products/testString/releases/testString/contract_terms/testString/documents/testString'
        )
        mock_response = '{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'
        release_id = 'testString'
        contract_terms_id = 'testString'
        document_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_product_id": data_product_id,
            "release_id": release_id,
            "contract_terms_id": contract_terms_id,
            "document_id": document_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_release_contract_terms_document(**req_copy)

    def test_get_release_contract_terms_document_value_error_with_retries(self):
        # Enable retries and run test_get_release_contract_terms_document_value_error.
        _service.enable_retries()
        self.test_get_release_contract_terms_document_value_error()

        # Disable retries and run test_get_release_contract_terms_document_value_error.
        _service.disable_retries()
        self.test_get_release_contract_terms_document_value_error()


class TestListDataProductReleases:
    """
    Test Class for list_data_product_releases
    """

    @responses.activate
    def test_list_data_product_releases_all_params(self):
        """
        list_data_product_releases()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/releases')
        mock_response = '{"limit": 200, "first": {"href": "https://api.example.com/collection"}, "next": {"href": "https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "releases": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'
        asset_container_id = 'testString'
        state = ['available']
        version = 'testString'
        limit = 200
        start = 'testString'

        # Invoke method
        response = _service.list_data_product_releases(
            data_product_id,
            asset_container_id=asset_container_id,
            state=state,
            version=version,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'asset.container.id={}'.format(asset_container_id) in query_string
        assert 'state={}'.format(','.join(state)) in query_string
        assert 'version={}'.format(version) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_data_product_releases_all_params_with_retries(self):
        # Enable retries and run test_list_data_product_releases_all_params.
        _service.enable_retries()
        self.test_list_data_product_releases_all_params()

        # Disable retries and run test_list_data_product_releases_all_params.
        _service.disable_retries()
        self.test_list_data_product_releases_all_params()

    @responses.activate
    def test_list_data_product_releases_required_params(self):
        """
        test_list_data_product_releases_required_params()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/releases')
        mock_response = '{"limit": 200, "first": {"href": "https://api.example.com/collection"}, "next": {"href": "https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "releases": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'

        # Invoke method
        response = _service.list_data_product_releases(data_product_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_data_product_releases_required_params_with_retries(self):
        # Enable retries and run test_list_data_product_releases_required_params.
        _service.enable_retries()
        self.test_list_data_product_releases_required_params()

        # Disable retries and run test_list_data_product_releases_required_params.
        _service.disable_retries()
        self.test_list_data_product_releases_required_params()

    @responses.activate
    def test_list_data_product_releases_value_error(self):
        """
        test_list_data_product_releases_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/releases')
        mock_response = '{"limit": 200, "first": {"href": "https://api.example.com/collection"}, "next": {"href": "https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "releases": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {"data_product_id": data_product_id}
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_data_product_releases(**req_copy)

    def test_list_data_product_releases_value_error_with_retries(self):
        # Enable retries and run test_list_data_product_releases_value_error.
        _service.enable_retries()
        self.test_list_data_product_releases_value_error()

        # Disable retries and run test_list_data_product_releases_value_error.
        _service.disable_retries()
        self.test_list_data_product_releases_value_error()

    @responses.activate
    def test_list_data_product_releases_with_pager_get_next(self):
        """
        test_list_data_product_releases_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/releases')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"releases":[{"version":"1.0.0","state":"draft","data_product":{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"name":"My Data Product","description":"This is a description of My Data Product.","tags":["tags"],"use_cases":[{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}],"types":["data"],"contract_terms":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"id":"id","documents":[{"url":"url","type":"terms_and_conditions","name":"name","id":"2b0bf220-079c-11ee-be56-0242ac120002","attachment":{"id":"id"},"upload_url":"upload_url"}],"error_msg":"error_msg"}],"is_restricted":false,"id":"2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd","asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"releases":[{"version":"1.0.0","state":"draft","data_product":{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"name":"My Data Product","description":"This is a description of My Data Product.","tags":["tags"],"use_cases":[{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}],"types":["data"],"contract_terms":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"id":"id","documents":[{"url":"url","type":"terms_and_conditions","name":"name","id":"2b0bf220-079c-11ee-be56-0242ac120002","attachment":{"id":"id"},"upload_url":"upload_url"}],"error_msg":"error_msg"}],"is_restricted":false,"id":"2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd","asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = DataProductReleasesPager(
            client=_service,
            data_product_id='testString',
            asset_container_id='testString',
            state=['available'],
            version='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_data_product_releases_with_pager_get_all(self):
        """
        test_list_data_product_releases_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/releases')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"releases":[{"version":"1.0.0","state":"draft","data_product":{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"name":"My Data Product","description":"This is a description of My Data Product.","tags":["tags"],"use_cases":[{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}],"types":["data"],"contract_terms":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"id":"id","documents":[{"url":"url","type":"terms_and_conditions","name":"name","id":"2b0bf220-079c-11ee-be56-0242ac120002","attachment":{"id":"id"},"upload_url":"upload_url"}],"error_msg":"error_msg"}],"is_restricted":false,"id":"2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd","asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"releases":[{"version":"1.0.0","state":"draft","data_product":{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"name":"My Data Product","description":"This is a description of My Data Product.","tags":["tags"],"use_cases":[{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}],"types":["data"],"contract_terms":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"id":"id","documents":[{"url":"url","type":"terms_and_conditions","name":"name","id":"2b0bf220-079c-11ee-be56-0242ac120002","attachment":{"id":"id"},"upload_url":"upload_url"}],"error_msg":"error_msg"}],"is_restricted":false,"id":"2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd","asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        pager = DataProductReleasesPager(
            client=_service,
            data_product_id='testString',
            asset_container_id='testString',
            state=['available'],
            version='testString',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestRetireDataProductRelease:
    """
    Test Class for retire_data_product_release
    """

    @responses.activate
    def test_retire_data_product_release_all_params(self):
        """
        retire_data_product_release()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/releases/testString/retire')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}], "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "properties": {"anyKey": "anyValue"}}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'
        release_id = 'testString'

        # Invoke method
        response = _service.retire_data_product_release(data_product_id, release_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_retire_data_product_release_all_params_with_retries(self):
        # Enable retries and run test_retire_data_product_release_all_params.
        _service.enable_retries()
        self.test_retire_data_product_release_all_params()

        # Disable retries and run test_retire_data_product_release_all_params.
        _service.disable_retries()
        self.test_retire_data_product_release_all_params()

    @responses.activate
    def test_retire_data_product_release_value_error(self):
        """
        test_retire_data_product_release_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/releases/testString/retire')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg"}], "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}], "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "properties": {"anyKey": "anyValue"}}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        data_product_id = 'testString'
        release_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {"data_product_id": data_product_id, "release_id": release_id}
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.retire_data_product_release(**req_copy)

    def test_retire_data_product_release_value_error_with_retries(self):
        # Enable retries and run test_retire_data_product_release_value_error.
        _service.enable_retries()
        self.test_retire_data_product_release_value_error()

        # Disable retries and run test_retire_data_product_release_value_error.
        _service.disable_retries()
        self.test_retire_data_product_release_value_error()


# endregion
##############################################################################
# End of Service: DataProductReleases
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_AssetPartReference:
    """
    Test Class for AssetPartReference
    """

    def test_asset_part_reference_serialization(self):
        """
        Test serialization/deserialization for AssetPartReference
        """

        # Construct dict forms of any model objects needed in order to build this model.

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Construct a json representation of a AssetPartReference model
        asset_part_reference_model_json = {}
        asset_part_reference_model_json['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model_json['container'] = container_reference_model
        asset_part_reference_model_json['type'] = 'data_asset'

        # Construct a model instance of AssetPartReference by calling from_dict on the json representation
        asset_part_reference_model = AssetPartReference.from_dict(asset_part_reference_model_json)
        assert asset_part_reference_model != False

        # Construct a model instance of AssetPartReference by calling from_dict on the json representation
        asset_part_reference_model_dict = AssetPartReference.from_dict(asset_part_reference_model_json).__dict__
        asset_part_reference_model2 = AssetPartReference(**asset_part_reference_model_dict)

        # Verify the model instances are equivalent
        assert asset_part_reference_model == asset_part_reference_model2

        # Convert model instance back to dict and verify no loss of data
        asset_part_reference_model_json2 = asset_part_reference_model.to_dict()
        assert asset_part_reference_model_json2 == asset_part_reference_model_json


class TestModel_AssetPrototype:
    """
    Test Class for AssetPrototype
    """

    def test_asset_prototype_serialization(self):
        """
        Test serialization/deserialization for AssetPrototype
        """

        # Construct dict forms of any model objects needed in order to build this model.

        container_identity_model = {}  # ContainerIdentity
        container_identity_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'

        # Construct a json representation of a AssetPrototype model
        asset_prototype_model_json = {}
        asset_prototype_model_json['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_prototype_model_json['container'] = container_identity_model

        # Construct a model instance of AssetPrototype by calling from_dict on the json representation
        asset_prototype_model = AssetPrototype.from_dict(asset_prototype_model_json)
        assert asset_prototype_model != False

        # Construct a model instance of AssetPrototype by calling from_dict on the json representation
        asset_prototype_model_dict = AssetPrototype.from_dict(asset_prototype_model_json).__dict__
        asset_prototype_model2 = AssetPrototype(**asset_prototype_model_dict)

        # Verify the model instances are equivalent
        assert asset_prototype_model == asset_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        asset_prototype_model_json2 = asset_prototype_model.to_dict()
        assert asset_prototype_model_json2 == asset_prototype_model_json


class TestModel_AssetReference:
    """
    Test Class for AssetReference
    """

    def test_asset_reference_serialization(self):
        """
        Test serialization/deserialization for AssetReference
        """

        # Construct dict forms of any model objects needed in order to build this model.

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Construct a json representation of a AssetReference model
        asset_reference_model_json = {}
        asset_reference_model_json['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model_json['container'] = container_reference_model

        # Construct a model instance of AssetReference by calling from_dict on the json representation
        asset_reference_model = AssetReference.from_dict(asset_reference_model_json)
        assert asset_reference_model != False

        # Construct a model instance of AssetReference by calling from_dict on the json representation
        asset_reference_model_dict = AssetReference.from_dict(asset_reference_model_json).__dict__
        asset_reference_model2 = AssetReference(**asset_reference_model_dict)

        # Verify the model instances are equivalent
        assert asset_reference_model == asset_reference_model2

        # Convert model instance back to dict and verify no loss of data
        asset_reference_model_json2 = asset_reference_model.to_dict()
        assert asset_reference_model_json2 == asset_reference_model_json


class TestModel_ContainerIdentity:
    """
    Test Class for ContainerIdentity
    """

    def test_container_identity_serialization(self):
        """
        Test serialization/deserialization for ContainerIdentity
        """

        # Construct a json representation of a ContainerIdentity model
        container_identity_model_json = {}
        container_identity_model_json['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'

        # Construct a model instance of ContainerIdentity by calling from_dict on the json representation
        container_identity_model = ContainerIdentity.from_dict(container_identity_model_json)
        assert container_identity_model != False

        # Construct a model instance of ContainerIdentity by calling from_dict on the json representation
        container_identity_model_dict = ContainerIdentity.from_dict(container_identity_model_json).__dict__
        container_identity_model2 = ContainerIdentity(**container_identity_model_dict)

        # Verify the model instances are equivalent
        assert container_identity_model == container_identity_model2

        # Convert model instance back to dict and verify no loss of data
        container_identity_model_json2 = container_identity_model.to_dict()
        assert container_identity_model_json2 == container_identity_model_json


class TestModel_ContainerReference:
    """
    Test Class for ContainerReference
    """

    def test_container_reference_serialization(self):
        """
        Test serialization/deserialization for ContainerReference
        """

        # Construct a json representation of a ContainerReference model
        container_reference_model_json = {}
        container_reference_model_json['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model_json['type'] = 'catalog'

        # Construct a model instance of ContainerReference by calling from_dict on the json representation
        container_reference_model = ContainerReference.from_dict(container_reference_model_json)
        assert container_reference_model != False

        # Construct a model instance of ContainerReference by calling from_dict on the json representation
        container_reference_model_dict = ContainerReference.from_dict(container_reference_model_json).__dict__
        container_reference_model2 = ContainerReference(**container_reference_model_dict)

        # Verify the model instances are equivalent
        assert container_reference_model == container_reference_model2

        # Convert model instance back to dict and verify no loss of data
        container_reference_model_json2 = container_reference_model.to_dict()
        assert container_reference_model_json2 == container_reference_model_json


class TestModel_ContractTermsDocument:
    """
    Test Class for ContractTermsDocument
    """

    def test_contract_terms_document_serialization(self):
        """
        Test serialization/deserialization for ContractTermsDocument
        """

        # Construct dict forms of any model objects needed in order to build this model.

        contract_terms_document_attachment_model = {}  # ContractTermsDocumentAttachment
        contract_terms_document_attachment_model['id'] = 'testString'

        # Construct a json representation of a ContractTermsDocument model
        contract_terms_document_model_json = {}
        contract_terms_document_model_json['url'] = 'testString'
        contract_terms_document_model_json['type'] = 'terms_and_conditions'
        contract_terms_document_model_json['name'] = 'testString'
        contract_terms_document_model_json['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        contract_terms_document_model_json['attachment'] = contract_terms_document_attachment_model
        contract_terms_document_model_json['upload_url'] = 'testString'

        # Construct a model instance of ContractTermsDocument by calling from_dict on the json representation
        contract_terms_document_model = ContractTermsDocument.from_dict(contract_terms_document_model_json)
        assert contract_terms_document_model != False

        # Construct a model instance of ContractTermsDocument by calling from_dict on the json representation
        contract_terms_document_model_dict = ContractTermsDocument.from_dict(
            contract_terms_document_model_json
        ).__dict__
        contract_terms_document_model2 = ContractTermsDocument(**contract_terms_document_model_dict)

        # Verify the model instances are equivalent
        assert contract_terms_document_model == contract_terms_document_model2

        # Convert model instance back to dict and verify no loss of data
        contract_terms_document_model_json2 = contract_terms_document_model.to_dict()
        assert contract_terms_document_model_json2 == contract_terms_document_model_json


class TestModel_ContractTermsDocumentAttachment:
    """
    Test Class for ContractTermsDocumentAttachment
    """

    def test_contract_terms_document_attachment_serialization(self):
        """
        Test serialization/deserialization for ContractTermsDocumentAttachment
        """

        # Construct a json representation of a ContractTermsDocumentAttachment model
        contract_terms_document_attachment_model_json = {}
        contract_terms_document_attachment_model_json['id'] = 'testString'

        # Construct a model instance of ContractTermsDocumentAttachment by calling from_dict on the json representation
        contract_terms_document_attachment_model = ContractTermsDocumentAttachment.from_dict(
            contract_terms_document_attachment_model_json
        )
        assert contract_terms_document_attachment_model != False

        # Construct a model instance of ContractTermsDocumentAttachment by calling from_dict on the json representation
        contract_terms_document_attachment_model_dict = ContractTermsDocumentAttachment.from_dict(
            contract_terms_document_attachment_model_json
        ).__dict__
        contract_terms_document_attachment_model2 = ContractTermsDocumentAttachment(
            **contract_terms_document_attachment_model_dict
        )

        # Verify the model instances are equivalent
        assert contract_terms_document_attachment_model == contract_terms_document_attachment_model2

        # Convert model instance back to dict and verify no loss of data
        contract_terms_document_attachment_model_json2 = contract_terms_document_attachment_model.to_dict()
        assert contract_terms_document_attachment_model_json2 == contract_terms_document_attachment_model_json


class TestModel_DataProduct:
    """
    Test Class for DataProduct
    """

    def test_data_product_serialization(self):
        """
        Test serialization/deserialization for DataProduct
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_product_draft_version_release_model = {}  # DataProductDraftVersionRelease
        data_product_draft_version_release_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        data_product_version_summary_data_product_model = {}  # DataProductVersionSummaryDataProduct
        data_product_version_summary_data_product_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_version_summary_data_product_model['release'] = data_product_draft_version_release_model
        data_product_version_summary_data_product_model['container'] = container_reference_model

        use_case_model = {}  # UseCase
        use_case_model['id'] = 'testString'
        use_case_model['name'] = 'testString'
        use_case_model['container'] = container_reference_model

        asset_reference_model = {}  # AssetReference
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['container'] = container_reference_model

        contract_terms_document_attachment_model = {}  # ContractTermsDocumentAttachment
        contract_terms_document_attachment_model['id'] = 'testString'

        contract_terms_document_model = {}  # ContractTermsDocument
        contract_terms_document_model['url'] = 'testString'
        contract_terms_document_model['type'] = 'terms_and_conditions'
        contract_terms_document_model['name'] = 'testString'
        contract_terms_document_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        contract_terms_document_model['attachment'] = contract_terms_document_attachment_model
        contract_terms_document_model['upload_url'] = 'testString'

        data_product_contract_terms_model = {}  # DataProductContractTerms
        data_product_contract_terms_model['asset'] = asset_reference_model
        data_product_contract_terms_model['id'] = 'testString'
        data_product_contract_terms_model['documents'] = [contract_terms_document_model]
        data_product_contract_terms_model['error_msg'] = 'testString'

        data_product_version_summary_model = {}  # DataProductVersionSummary
        data_product_version_summary_model['version'] = '1.0.0'
        data_product_version_summary_model['state'] = 'draft'
        data_product_version_summary_model['data_product'] = data_product_version_summary_data_product_model
        data_product_version_summary_model['name'] = 'My Data Product'
        data_product_version_summary_model['description'] = 'This is a description of My Data Product.'
        data_product_version_summary_model['tags'] = ['testString']
        data_product_version_summary_model['use_cases'] = [use_case_model]
        data_product_version_summary_model['types'] = ['data']
        data_product_version_summary_model['contract_terms'] = [data_product_contract_terms_model]
        data_product_version_summary_model['is_restricted'] = True
        data_product_version_summary_model['id'] = (
            '2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd'
        )
        data_product_version_summary_model['asset'] = asset_reference_model

        # Construct a json representation of a DataProduct model
        data_product_model_json = {}
        data_product_model_json['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_model_json['release'] = data_product_draft_version_release_model
        data_product_model_json['container'] = container_reference_model
        data_product_model_json['latest_release'] = data_product_version_summary_model
        data_product_model_json['drafts'] = [data_product_version_summary_model]

        # Construct a model instance of DataProduct by calling from_dict on the json representation
        data_product_model = DataProduct.from_dict(data_product_model_json)
        assert data_product_model != False

        # Construct a model instance of DataProduct by calling from_dict on the json representation
        data_product_model_dict = DataProduct.from_dict(data_product_model_json).__dict__
        data_product_model2 = DataProduct(**data_product_model_dict)

        # Verify the model instances are equivalent
        assert data_product_model == data_product_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_model_json2 = data_product_model.to_dict()
        assert data_product_model_json2 == data_product_model_json


class TestModel_DataProductContractTerms:
    """
    Test Class for DataProductContractTerms
    """

    def test_data_product_contract_terms_serialization(self):
        """
        Test serialization/deserialization for DataProductContractTerms
        """

        # Construct dict forms of any model objects needed in order to build this model.

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        asset_reference_model = {}  # AssetReference
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['container'] = container_reference_model

        contract_terms_document_attachment_model = {}  # ContractTermsDocumentAttachment
        contract_terms_document_attachment_model['id'] = 'testString'

        contract_terms_document_model = {}  # ContractTermsDocument
        contract_terms_document_model['url'] = 'testString'
        contract_terms_document_model['type'] = 'terms_and_conditions'
        contract_terms_document_model['name'] = 'testString'
        contract_terms_document_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        contract_terms_document_model['attachment'] = contract_terms_document_attachment_model
        contract_terms_document_model['upload_url'] = 'testString'

        # Construct a json representation of a DataProductContractTerms model
        data_product_contract_terms_model_json = {}
        data_product_contract_terms_model_json['asset'] = asset_reference_model
        data_product_contract_terms_model_json['id'] = 'testString'
        data_product_contract_terms_model_json['documents'] = [contract_terms_document_model]
        data_product_contract_terms_model_json['error_msg'] = 'testString'

        # Construct a model instance of DataProductContractTerms by calling from_dict on the json representation
        data_product_contract_terms_model = DataProductContractTerms.from_dict(data_product_contract_terms_model_json)
        assert data_product_contract_terms_model != False

        # Construct a model instance of DataProductContractTerms by calling from_dict on the json representation
        data_product_contract_terms_model_dict = DataProductContractTerms.from_dict(
            data_product_contract_terms_model_json
        ).__dict__
        data_product_contract_terms_model2 = DataProductContractTerms(**data_product_contract_terms_model_dict)

        # Verify the model instances are equivalent
        assert data_product_contract_terms_model == data_product_contract_terms_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_contract_terms_model_json2 = data_product_contract_terms_model.to_dict()
        assert data_product_contract_terms_model_json2 == data_product_contract_terms_model_json


class TestModel_DataProductCustomWorkflowDefinition:
    """
    Test Class for DataProductCustomWorkflowDefinition
    """

    def test_data_product_custom_workflow_definition_serialization(self):
        """
        Test serialization/deserialization for DataProductCustomWorkflowDefinition
        """

        # Construct a json representation of a DataProductCustomWorkflowDefinition model
        data_product_custom_workflow_definition_model_json = {}
        data_product_custom_workflow_definition_model_json['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        # Construct a model instance of DataProductCustomWorkflowDefinition by calling from_dict on the json representation
        data_product_custom_workflow_definition_model = DataProductCustomWorkflowDefinition.from_dict(
            data_product_custom_workflow_definition_model_json
        )
        assert data_product_custom_workflow_definition_model != False

        # Construct a model instance of DataProductCustomWorkflowDefinition by calling from_dict on the json representation
        data_product_custom_workflow_definition_model_dict = DataProductCustomWorkflowDefinition.from_dict(
            data_product_custom_workflow_definition_model_json
        ).__dict__
        data_product_custom_workflow_definition_model2 = DataProductCustomWorkflowDefinition(
            **data_product_custom_workflow_definition_model_dict
        )

        # Verify the model instances are equivalent
        assert data_product_custom_workflow_definition_model == data_product_custom_workflow_definition_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_custom_workflow_definition_model_json2 = data_product_custom_workflow_definition_model.to_dict()
        assert data_product_custom_workflow_definition_model_json2 == data_product_custom_workflow_definition_model_json


class TestModel_DataProductDraftCollection:
    """
    Test Class for DataProductDraftCollection
    """

    def test_data_product_draft_collection_serialization(self):
        """
        Test serialization/deserialization for DataProductDraftCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        first_page_model = {}  # FirstPage
        first_page_model['href'] = 'https://api.example.com/collection'

        next_page_model = {}  # NextPage
        next_page_model['href'] = 'https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9'
        next_page_model['start'] = 'eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9'

        data_product_draft_version_release_model = {}  # DataProductDraftVersionRelease
        data_product_draft_version_release_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        data_product_version_summary_data_product_model = {}  # DataProductVersionSummaryDataProduct
        data_product_version_summary_data_product_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_version_summary_data_product_model['release'] = data_product_draft_version_release_model
        data_product_version_summary_data_product_model['container'] = container_reference_model

        use_case_model = {}  # UseCase
        use_case_model['id'] = 'testString'
        use_case_model['name'] = 'testString'
        use_case_model['container'] = container_reference_model

        asset_reference_model = {}  # AssetReference
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['container'] = container_reference_model

        contract_terms_document_attachment_model = {}  # ContractTermsDocumentAttachment
        contract_terms_document_attachment_model['id'] = 'testString'

        contract_terms_document_model = {}  # ContractTermsDocument
        contract_terms_document_model['url'] = 'testString'
        contract_terms_document_model['type'] = 'terms_and_conditions'
        contract_terms_document_model['name'] = 'testString'
        contract_terms_document_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        contract_terms_document_model['attachment'] = contract_terms_document_attachment_model
        contract_terms_document_model['upload_url'] = 'testString'

        data_product_contract_terms_model = {}  # DataProductContractTerms
        data_product_contract_terms_model['asset'] = asset_reference_model
        data_product_contract_terms_model['id'] = 'testString'
        data_product_contract_terms_model['documents'] = [contract_terms_document_model]
        data_product_contract_terms_model['error_msg'] = 'testString'

        data_product_version_summary_model = {}  # DataProductVersionSummary
        data_product_version_summary_model['version'] = '1.0.0'
        data_product_version_summary_model['state'] = 'draft'
        data_product_version_summary_model['data_product'] = data_product_version_summary_data_product_model
        data_product_version_summary_model['name'] = 'My Data Product'
        data_product_version_summary_model['description'] = 'This is a description of My Data Product.'
        data_product_version_summary_model['tags'] = ['testString']
        data_product_version_summary_model['use_cases'] = [use_case_model]
        data_product_version_summary_model['types'] = ['data']
        data_product_version_summary_model['contract_terms'] = [data_product_contract_terms_model]
        data_product_version_summary_model['is_restricted'] = True
        data_product_version_summary_model['id'] = (
            '2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd'
        )
        data_product_version_summary_model['asset'] = asset_reference_model

        # Construct a json representation of a DataProductDraftCollection model
        data_product_draft_collection_model_json = {}
        data_product_draft_collection_model_json['limit'] = 200
        data_product_draft_collection_model_json['first'] = first_page_model
        data_product_draft_collection_model_json['next'] = next_page_model
        data_product_draft_collection_model_json['drafts'] = [data_product_version_summary_model]

        # Construct a model instance of DataProductDraftCollection by calling from_dict on the json representation
        data_product_draft_collection_model = DataProductDraftCollection.from_dict(
            data_product_draft_collection_model_json
        )
        assert data_product_draft_collection_model != False

        # Construct a model instance of DataProductDraftCollection by calling from_dict on the json representation
        data_product_draft_collection_model_dict = DataProductDraftCollection.from_dict(
            data_product_draft_collection_model_json
        ).__dict__
        data_product_draft_collection_model2 = DataProductDraftCollection(**data_product_draft_collection_model_dict)

        # Verify the model instances are equivalent
        assert data_product_draft_collection_model == data_product_draft_collection_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_draft_collection_model_json2 = data_product_draft_collection_model.to_dict()
        assert data_product_draft_collection_model_json2 == data_product_draft_collection_model_json


class TestModel_DataProductDraftVersionRelease:
    """
    Test Class for DataProductDraftVersionRelease
    """

    def test_data_product_draft_version_release_serialization(self):
        """
        Test serialization/deserialization for DataProductDraftVersionRelease
        """

        # Construct a json representation of a DataProductDraftVersionRelease model
        data_product_draft_version_release_model_json = {}
        data_product_draft_version_release_model_json['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        # Construct a model instance of DataProductDraftVersionRelease by calling from_dict on the json representation
        data_product_draft_version_release_model = DataProductDraftVersionRelease.from_dict(
            data_product_draft_version_release_model_json
        )
        assert data_product_draft_version_release_model != False

        # Construct a model instance of DataProductDraftVersionRelease by calling from_dict on the json representation
        data_product_draft_version_release_model_dict = DataProductDraftVersionRelease.from_dict(
            data_product_draft_version_release_model_json
        ).__dict__
        data_product_draft_version_release_model2 = DataProductDraftVersionRelease(
            **data_product_draft_version_release_model_dict
        )

        # Verify the model instances are equivalent
        assert data_product_draft_version_release_model == data_product_draft_version_release_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_draft_version_release_model_json2 = data_product_draft_version_release_model.to_dict()
        assert data_product_draft_version_release_model_json2 == data_product_draft_version_release_model_json


class TestModel_DataProductIdentity:
    """
    Test Class for DataProductIdentity
    """

    def test_data_product_identity_serialization(self):
        """
        Test serialization/deserialization for DataProductIdentity
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_product_draft_version_release_model = {}  # DataProductDraftVersionRelease
        data_product_draft_version_release_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        # Construct a json representation of a DataProductIdentity model
        data_product_identity_model_json = {}
        data_product_identity_model_json['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_identity_model_json['release'] = data_product_draft_version_release_model

        # Construct a model instance of DataProductIdentity by calling from_dict on the json representation
        data_product_identity_model = DataProductIdentity.from_dict(data_product_identity_model_json)
        assert data_product_identity_model != False

        # Construct a model instance of DataProductIdentity by calling from_dict on the json representation
        data_product_identity_model_dict = DataProductIdentity.from_dict(data_product_identity_model_json).__dict__
        data_product_identity_model2 = DataProductIdentity(**data_product_identity_model_dict)

        # Verify the model instances are equivalent
        assert data_product_identity_model == data_product_identity_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_identity_model_json2 = data_product_identity_model.to_dict()
        assert data_product_identity_model_json2 == data_product_identity_model_json


class TestModel_DataProductOrderAccessRequest:
    """
    Test Class for DataProductOrderAccessRequest
    """

    def test_data_product_order_access_request_serialization(self):
        """
        Test serialization/deserialization for DataProductOrderAccessRequest
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_product_custom_workflow_definition_model = {}  # DataProductCustomWorkflowDefinition
        data_product_custom_workflow_definition_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        # Construct a json representation of a DataProductOrderAccessRequest model
        data_product_order_access_request_model_json = {}
        data_product_order_access_request_model_json['task_assignee_users'] = ['testString']
        data_product_order_access_request_model_json['pre_approved_users'] = ['testString']
        data_product_order_access_request_model_json['custom_workflow_definition'] = (
            data_product_custom_workflow_definition_model
        )

        # Construct a model instance of DataProductOrderAccessRequest by calling from_dict on the json representation
        data_product_order_access_request_model = DataProductOrderAccessRequest.from_dict(
            data_product_order_access_request_model_json
        )
        assert data_product_order_access_request_model != False

        # Construct a model instance of DataProductOrderAccessRequest by calling from_dict on the json representation
        data_product_order_access_request_model_dict = DataProductOrderAccessRequest.from_dict(
            data_product_order_access_request_model_json
        ).__dict__
        data_product_order_access_request_model2 = DataProductOrderAccessRequest(
            **data_product_order_access_request_model_dict
        )

        # Verify the model instances are equivalent
        assert data_product_order_access_request_model == data_product_order_access_request_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_order_access_request_model_json2 = data_product_order_access_request_model.to_dict()
        assert data_product_order_access_request_model_json2 == data_product_order_access_request_model_json


class TestModel_DataProductPart:
    """
    Test Class for DataProductPart
    """

    def test_data_product_part_serialization(self):
        """
        Test serialization/deserialization for DataProductPart
        """

        # Construct dict forms of any model objects needed in order to build this model.

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        asset_part_reference_model = {}  # AssetPartReference
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        delivery_method_model = {}  # DeliveryMethod
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model

        # Construct a json representation of a DataProductPart model
        data_product_part_model_json = {}
        data_product_part_model_json['asset'] = asset_part_reference_model
        data_product_part_model_json['delivery_methods'] = [delivery_method_model]

        # Construct a model instance of DataProductPart by calling from_dict on the json representation
        data_product_part_model = DataProductPart.from_dict(data_product_part_model_json)
        assert data_product_part_model != False

        # Construct a model instance of DataProductPart by calling from_dict on the json representation
        data_product_part_model_dict = DataProductPart.from_dict(data_product_part_model_json).__dict__
        data_product_part_model2 = DataProductPart(**data_product_part_model_dict)

        # Verify the model instances are equivalent
        assert data_product_part_model == data_product_part_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_part_model_json2 = data_product_part_model.to_dict()
        assert data_product_part_model_json2 == data_product_part_model_json


class TestModel_DataProductReleaseCollection:
    """
    Test Class for DataProductReleaseCollection
    """

    def test_data_product_release_collection_serialization(self):
        """
        Test serialization/deserialization for DataProductReleaseCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        first_page_model = {}  # FirstPage
        first_page_model['href'] = 'https://api.example.com/collection'

        next_page_model = {}  # NextPage
        next_page_model['href'] = 'https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9'
        next_page_model['start'] = 'eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9'

        data_product_draft_version_release_model = {}  # DataProductDraftVersionRelease
        data_product_draft_version_release_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        data_product_version_summary_data_product_model = {}  # DataProductVersionSummaryDataProduct
        data_product_version_summary_data_product_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_version_summary_data_product_model['release'] = data_product_draft_version_release_model
        data_product_version_summary_data_product_model['container'] = container_reference_model

        use_case_model = {}  # UseCase
        use_case_model['id'] = 'testString'
        use_case_model['name'] = 'testString'
        use_case_model['container'] = container_reference_model

        asset_reference_model = {}  # AssetReference
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['container'] = container_reference_model

        contract_terms_document_attachment_model = {}  # ContractTermsDocumentAttachment
        contract_terms_document_attachment_model['id'] = 'testString'

        contract_terms_document_model = {}  # ContractTermsDocument
        contract_terms_document_model['url'] = 'testString'
        contract_terms_document_model['type'] = 'terms_and_conditions'
        contract_terms_document_model['name'] = 'testString'
        contract_terms_document_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        contract_terms_document_model['attachment'] = contract_terms_document_attachment_model
        contract_terms_document_model['upload_url'] = 'testString'

        data_product_contract_terms_model = {}  # DataProductContractTerms
        data_product_contract_terms_model['asset'] = asset_reference_model
        data_product_contract_terms_model['id'] = 'testString'
        data_product_contract_terms_model['documents'] = [contract_terms_document_model]
        data_product_contract_terms_model['error_msg'] = 'testString'

        data_product_version_summary_model = {}  # DataProductVersionSummary
        data_product_version_summary_model['version'] = '1.0.0'
        data_product_version_summary_model['state'] = 'draft'
        data_product_version_summary_model['data_product'] = data_product_version_summary_data_product_model
        data_product_version_summary_model['name'] = 'My Data Product'
        data_product_version_summary_model['description'] = 'This is a description of My Data Product.'
        data_product_version_summary_model['tags'] = ['testString']
        data_product_version_summary_model['use_cases'] = [use_case_model]
        data_product_version_summary_model['types'] = ['data']
        data_product_version_summary_model['contract_terms'] = [data_product_contract_terms_model]
        data_product_version_summary_model['is_restricted'] = True
        data_product_version_summary_model['id'] = (
            '2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd'
        )
        data_product_version_summary_model['asset'] = asset_reference_model

        # Construct a json representation of a DataProductReleaseCollection model
        data_product_release_collection_model_json = {}
        data_product_release_collection_model_json['limit'] = 200
        data_product_release_collection_model_json['first'] = first_page_model
        data_product_release_collection_model_json['next'] = next_page_model
        data_product_release_collection_model_json['releases'] = [data_product_version_summary_model]

        # Construct a model instance of DataProductReleaseCollection by calling from_dict on the json representation
        data_product_release_collection_model = DataProductReleaseCollection.from_dict(
            data_product_release_collection_model_json
        )
        assert data_product_release_collection_model != False

        # Construct a model instance of DataProductReleaseCollection by calling from_dict on the json representation
        data_product_release_collection_model_dict = DataProductReleaseCollection.from_dict(
            data_product_release_collection_model_json
        ).__dict__
        data_product_release_collection_model2 = DataProductReleaseCollection(
            **data_product_release_collection_model_dict
        )

        # Verify the model instances are equivalent
        assert data_product_release_collection_model == data_product_release_collection_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_release_collection_model_json2 = data_product_release_collection_model.to_dict()
        assert data_product_release_collection_model_json2 == data_product_release_collection_model_json


class TestModel_DataProductSummary:
    """
    Test Class for DataProductSummary
    """

    def test_data_product_summary_serialization(self):
        """
        Test serialization/deserialization for DataProductSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_product_draft_version_release_model = {}  # DataProductDraftVersionRelease
        data_product_draft_version_release_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Construct a json representation of a DataProductSummary model
        data_product_summary_model_json = {}
        data_product_summary_model_json['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_summary_model_json['release'] = data_product_draft_version_release_model
        data_product_summary_model_json['container'] = container_reference_model

        # Construct a model instance of DataProductSummary by calling from_dict on the json representation
        data_product_summary_model = DataProductSummary.from_dict(data_product_summary_model_json)
        assert data_product_summary_model != False

        # Construct a model instance of DataProductSummary by calling from_dict on the json representation
        data_product_summary_model_dict = DataProductSummary.from_dict(data_product_summary_model_json).__dict__
        data_product_summary_model2 = DataProductSummary(**data_product_summary_model_dict)

        # Verify the model instances are equivalent
        assert data_product_summary_model == data_product_summary_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_summary_model_json2 = data_product_summary_model.to_dict()
        assert data_product_summary_model_json2 == data_product_summary_model_json


class TestModel_DataProductSummaryCollection:
    """
    Test Class for DataProductSummaryCollection
    """

    def test_data_product_summary_collection_serialization(self):
        """
        Test serialization/deserialization for DataProductSummaryCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        first_page_model = {}  # FirstPage
        first_page_model['href'] = 'https://api.example.com/collection'

        next_page_model = {}  # NextPage
        next_page_model['href'] = 'https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9'
        next_page_model['start'] = 'eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9'

        data_product_draft_version_release_model = {}  # DataProductDraftVersionRelease
        data_product_draft_version_release_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        data_product_summary_model = {}  # DataProductSummary
        data_product_summary_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_summary_model['release'] = data_product_draft_version_release_model
        data_product_summary_model['container'] = container_reference_model

        # Construct a json representation of a DataProductSummaryCollection model
        data_product_summary_collection_model_json = {}
        data_product_summary_collection_model_json['limit'] = 200
        data_product_summary_collection_model_json['first'] = first_page_model
        data_product_summary_collection_model_json['next'] = next_page_model
        data_product_summary_collection_model_json['data_products'] = [data_product_summary_model]

        # Construct a model instance of DataProductSummaryCollection by calling from_dict on the json representation
        data_product_summary_collection_model = DataProductSummaryCollection.from_dict(
            data_product_summary_collection_model_json
        )
        assert data_product_summary_collection_model != False

        # Construct a model instance of DataProductSummaryCollection by calling from_dict on the json representation
        data_product_summary_collection_model_dict = DataProductSummaryCollection.from_dict(
            data_product_summary_collection_model_json
        ).__dict__
        data_product_summary_collection_model2 = DataProductSummaryCollection(
            **data_product_summary_collection_model_dict
        )

        # Verify the model instances are equivalent
        assert data_product_summary_collection_model == data_product_summary_collection_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_summary_collection_model_json2 = data_product_summary_collection_model.to_dict()
        assert data_product_summary_collection_model_json2 == data_product_summary_collection_model_json


class TestModel_DataProductVersion:
    """
    Test Class for DataProductVersion
    """

    def test_data_product_version_serialization(self):
        """
        Test serialization/deserialization for DataProductVersion
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_product_draft_version_release_model = {}  # DataProductDraftVersionRelease
        data_product_draft_version_release_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        data_product_version_data_product_model = {}  # DataProductVersionDataProduct
        data_product_version_data_product_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_version_data_product_model['release'] = data_product_draft_version_release_model
        data_product_version_data_product_model['container'] = container_reference_model

        use_case_model = {}  # UseCase
        use_case_model['id'] = 'testString'
        use_case_model['name'] = 'testString'
        use_case_model['container'] = container_reference_model

        asset_reference_model = {}  # AssetReference
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['container'] = container_reference_model

        contract_terms_document_attachment_model = {}  # ContractTermsDocumentAttachment
        contract_terms_document_attachment_model['id'] = 'testString'

        contract_terms_document_model = {}  # ContractTermsDocument
        contract_terms_document_model['url'] = 'testString'
        contract_terms_document_model['type'] = 'terms_and_conditions'
        contract_terms_document_model['name'] = 'testString'
        contract_terms_document_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        contract_terms_document_model['attachment'] = contract_terms_document_attachment_model
        contract_terms_document_model['upload_url'] = 'testString'

        data_product_contract_terms_model = {}  # DataProductContractTerms
        data_product_contract_terms_model['asset'] = asset_reference_model
        data_product_contract_terms_model['id'] = 'testString'
        data_product_contract_terms_model['documents'] = [contract_terms_document_model]
        data_product_contract_terms_model['error_msg'] = 'testString'

        domain_model = {}  # Domain
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        asset_part_reference_model = {}  # AssetPartReference
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        delivery_method_model = {}  # DeliveryMethod
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model

        data_product_part_model = {}  # DataProductPart
        data_product_part_model['asset'] = asset_part_reference_model
        data_product_part_model['delivery_methods'] = [delivery_method_model]

        data_product_custom_workflow_definition_model = {}  # DataProductCustomWorkflowDefinition
        data_product_custom_workflow_definition_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        data_product_order_access_request_model = {}  # DataProductOrderAccessRequest
        data_product_order_access_request_model['task_assignee_users'] = ['testString']
        data_product_order_access_request_model['pre_approved_users'] = ['testString']
        data_product_order_access_request_model['custom_workflow_definition'] = (
            data_product_custom_workflow_definition_model
        )

        data_product_workflows_model = {}  # DataProductWorkflows
        data_product_workflows_model['order_access_request'] = data_product_order_access_request_model

        # Construct a json representation of a DataProductVersion model
        data_product_version_model_json = {}
        data_product_version_model_json['version'] = '1.0.0'
        data_product_version_model_json['state'] = 'draft'
        data_product_version_model_json['data_product'] = data_product_version_data_product_model
        data_product_version_model_json['name'] = 'My Data Product'
        data_product_version_model_json['description'] = 'This is a description of My Data Product.'
        data_product_version_model_json['tags'] = ['testString']
        data_product_version_model_json['use_cases'] = [use_case_model]
        data_product_version_model_json['types'] = ['data']
        data_product_version_model_json['contract_terms'] = [data_product_contract_terms_model]
        data_product_version_model_json['is_restricted'] = True
        data_product_version_model_json['id'] = (
            '2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd'
        )
        data_product_version_model_json['asset'] = asset_reference_model
        data_product_version_model_json['domain'] = domain_model
        data_product_version_model_json['parts_out'] = [data_product_part_model]
        data_product_version_model_json['published_by'] = 'testString'
        data_product_version_model_json['published_at'] = '2019-01-01T12:00:00Z'
        data_product_version_model_json['created_by'] = 'testString'
        data_product_version_model_json['created_at'] = '2019-01-01T12:00:00Z'
        data_product_version_model_json['workflows'] = data_product_workflows_model
        data_product_version_model_json['properties'] = {'anyKey': 'anyValue'}

        # Construct a model instance of DataProductVersion by calling from_dict on the json representation
        data_product_version_model = DataProductVersion.from_dict(data_product_version_model_json)
        assert data_product_version_model != False

        # Construct a model instance of DataProductVersion by calling from_dict on the json representation
        data_product_version_model_dict = DataProductVersion.from_dict(data_product_version_model_json).__dict__
        data_product_version_model2 = DataProductVersion(**data_product_version_model_dict)

        # Verify the model instances are equivalent
        assert data_product_version_model == data_product_version_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_version_model_json2 = data_product_version_model.to_dict()
        assert data_product_version_model_json2 == data_product_version_model_json


class TestModel_DataProductVersionDataProduct:
    """
    Test Class for DataProductVersionDataProduct
    """

    def test_data_product_version_data_product_serialization(self):
        """
        Test serialization/deserialization for DataProductVersionDataProduct
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_product_draft_version_release_model = {}  # DataProductDraftVersionRelease
        data_product_draft_version_release_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Construct a json representation of a DataProductVersionDataProduct model
        data_product_version_data_product_model_json = {}
        data_product_version_data_product_model_json['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_version_data_product_model_json['release'] = data_product_draft_version_release_model
        data_product_version_data_product_model_json['container'] = container_reference_model

        # Construct a model instance of DataProductVersionDataProduct by calling from_dict on the json representation
        data_product_version_data_product_model = DataProductVersionDataProduct.from_dict(
            data_product_version_data_product_model_json
        )
        assert data_product_version_data_product_model != False

        # Construct a model instance of DataProductVersionDataProduct by calling from_dict on the json representation
        data_product_version_data_product_model_dict = DataProductVersionDataProduct.from_dict(
            data_product_version_data_product_model_json
        ).__dict__
        data_product_version_data_product_model2 = DataProductVersionDataProduct(
            **data_product_version_data_product_model_dict
        )

        # Verify the model instances are equivalent
        assert data_product_version_data_product_model == data_product_version_data_product_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_version_data_product_model_json2 = data_product_version_data_product_model.to_dict()
        assert data_product_version_data_product_model_json2 == data_product_version_data_product_model_json


class TestModel_DataProductVersionPrototype:
    """
    Test Class for DataProductVersionPrototype
    """

    def test_data_product_version_prototype_serialization(self):
        """
        Test serialization/deserialization for DataProductVersionPrototype
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_product_draft_version_release_model = {}  # DataProductDraftVersionRelease
        data_product_draft_version_release_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        data_product_identity_model = {}  # DataProductIdentity
        data_product_identity_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_identity_model['release'] = data_product_draft_version_release_model

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        use_case_model = {}  # UseCase
        use_case_model['id'] = 'testString'
        use_case_model['name'] = 'testString'
        use_case_model['container'] = container_reference_model

        asset_reference_model = {}  # AssetReference
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['container'] = container_reference_model

        contract_terms_document_attachment_model = {}  # ContractTermsDocumentAttachment
        contract_terms_document_attachment_model['id'] = 'testString'

        contract_terms_document_model = {}  # ContractTermsDocument
        contract_terms_document_model['url'] = 'testString'
        contract_terms_document_model['type'] = 'terms_and_conditions'
        contract_terms_document_model['name'] = 'testString'
        contract_terms_document_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        contract_terms_document_model['attachment'] = contract_terms_document_attachment_model
        contract_terms_document_model['upload_url'] = 'testString'

        data_product_contract_terms_model = {}  # DataProductContractTerms
        data_product_contract_terms_model['asset'] = asset_reference_model
        data_product_contract_terms_model['id'] = 'testString'
        data_product_contract_terms_model['documents'] = [contract_terms_document_model]
        data_product_contract_terms_model['error_msg'] = 'testString'

        container_identity_model = {}  # ContainerIdentity
        container_identity_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'

        asset_prototype_model = {}  # AssetPrototype
        asset_prototype_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_prototype_model['container'] = container_identity_model

        domain_model = {}  # Domain
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        asset_part_reference_model = {}  # AssetPartReference
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        delivery_method_model = {}  # DeliveryMethod
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model

        data_product_part_model = {}  # DataProductPart
        data_product_part_model['asset'] = asset_part_reference_model
        data_product_part_model['delivery_methods'] = [delivery_method_model]

        data_product_custom_workflow_definition_model = {}  # DataProductCustomWorkflowDefinition
        data_product_custom_workflow_definition_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        data_product_order_access_request_model = {}  # DataProductOrderAccessRequest
        data_product_order_access_request_model['task_assignee_users'] = ['testString']
        data_product_order_access_request_model['pre_approved_users'] = ['testString']
        data_product_order_access_request_model['custom_workflow_definition'] = (
            data_product_custom_workflow_definition_model
        )

        data_product_workflows_model = {}  # DataProductWorkflows
        data_product_workflows_model['order_access_request'] = data_product_order_access_request_model

        # Construct a json representation of a DataProductVersionPrototype model
        data_product_version_prototype_model_json = {}
        data_product_version_prototype_model_json['version'] = '1.0.0'
        data_product_version_prototype_model_json['state'] = 'draft'
        data_product_version_prototype_model_json['data_product'] = data_product_identity_model
        data_product_version_prototype_model_json['name'] = 'My Data Product'
        data_product_version_prototype_model_json['description'] = 'This is a description of My Data Product.'
        data_product_version_prototype_model_json['tags'] = ['testString']
        data_product_version_prototype_model_json['use_cases'] = [use_case_model]
        data_product_version_prototype_model_json['types'] = ['data']
        data_product_version_prototype_model_json['contract_terms'] = [data_product_contract_terms_model]
        data_product_version_prototype_model_json['is_restricted'] = True
        data_product_version_prototype_model_json['asset'] = asset_prototype_model
        data_product_version_prototype_model_json['domain'] = domain_model
        data_product_version_prototype_model_json['parts_out'] = [data_product_part_model]
        data_product_version_prototype_model_json['workflows'] = data_product_workflows_model

        # Construct a model instance of DataProductVersionPrototype by calling from_dict on the json representation
        data_product_version_prototype_model = DataProductVersionPrototype.from_dict(
            data_product_version_prototype_model_json
        )
        assert data_product_version_prototype_model != False

        # Construct a model instance of DataProductVersionPrototype by calling from_dict on the json representation
        data_product_version_prototype_model_dict = DataProductVersionPrototype.from_dict(
            data_product_version_prototype_model_json
        ).__dict__
        data_product_version_prototype_model2 = DataProductVersionPrototype(**data_product_version_prototype_model_dict)

        # Verify the model instances are equivalent
        assert data_product_version_prototype_model == data_product_version_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_version_prototype_model_json2 = data_product_version_prototype_model.to_dict()
        assert data_product_version_prototype_model_json2 == data_product_version_prototype_model_json


class TestModel_DataProductVersionSummary:
    """
    Test Class for DataProductVersionSummary
    """

    def test_data_product_version_summary_serialization(self):
        """
        Test serialization/deserialization for DataProductVersionSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_product_draft_version_release_model = {}  # DataProductDraftVersionRelease
        data_product_draft_version_release_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        data_product_version_summary_data_product_model = {}  # DataProductVersionSummaryDataProduct
        data_product_version_summary_data_product_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_version_summary_data_product_model['release'] = data_product_draft_version_release_model
        data_product_version_summary_data_product_model['container'] = container_reference_model

        use_case_model = {}  # UseCase
        use_case_model['id'] = 'testString'
        use_case_model['name'] = 'testString'
        use_case_model['container'] = container_reference_model

        asset_reference_model = {}  # AssetReference
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['container'] = container_reference_model

        contract_terms_document_attachment_model = {}  # ContractTermsDocumentAttachment
        contract_terms_document_attachment_model['id'] = 'testString'

        contract_terms_document_model = {}  # ContractTermsDocument
        contract_terms_document_model['url'] = 'testString'
        contract_terms_document_model['type'] = 'terms_and_conditions'
        contract_terms_document_model['name'] = 'testString'
        contract_terms_document_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        contract_terms_document_model['attachment'] = contract_terms_document_attachment_model
        contract_terms_document_model['upload_url'] = 'testString'

        data_product_contract_terms_model = {}  # DataProductContractTerms
        data_product_contract_terms_model['asset'] = asset_reference_model
        data_product_contract_terms_model['id'] = 'testString'
        data_product_contract_terms_model['documents'] = [contract_terms_document_model]
        data_product_contract_terms_model['error_msg'] = 'testString'

        # Construct a json representation of a DataProductVersionSummary model
        data_product_version_summary_model_json = {}
        data_product_version_summary_model_json['version'] = '1.0.0'
        data_product_version_summary_model_json['state'] = 'draft'
        data_product_version_summary_model_json['data_product'] = data_product_version_summary_data_product_model
        data_product_version_summary_model_json['name'] = 'My Data Product'
        data_product_version_summary_model_json['description'] = 'This is a description of My Data Product.'
        data_product_version_summary_model_json['tags'] = ['testString']
        data_product_version_summary_model_json['use_cases'] = [use_case_model]
        data_product_version_summary_model_json['types'] = ['data']
        data_product_version_summary_model_json['contract_terms'] = [data_product_contract_terms_model]
        data_product_version_summary_model_json['is_restricted'] = True
        data_product_version_summary_model_json['id'] = (
            '2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd'
        )
        data_product_version_summary_model_json['asset'] = asset_reference_model

        # Construct a model instance of DataProductVersionSummary by calling from_dict on the json representation
        data_product_version_summary_model = DataProductVersionSummary.from_dict(
            data_product_version_summary_model_json
        )
        assert data_product_version_summary_model != False

        # Construct a model instance of DataProductVersionSummary by calling from_dict on the json representation
        data_product_version_summary_model_dict = DataProductVersionSummary.from_dict(
            data_product_version_summary_model_json
        ).__dict__
        data_product_version_summary_model2 = DataProductVersionSummary(**data_product_version_summary_model_dict)

        # Verify the model instances are equivalent
        assert data_product_version_summary_model == data_product_version_summary_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_version_summary_model_json2 = data_product_version_summary_model.to_dict()
        assert data_product_version_summary_model_json2 == data_product_version_summary_model_json


class TestModel_DataProductVersionSummaryDataProduct:
    """
    Test Class for DataProductVersionSummaryDataProduct
    """

    def test_data_product_version_summary_data_product_serialization(self):
        """
        Test serialization/deserialization for DataProductVersionSummaryDataProduct
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_product_draft_version_release_model = {}  # DataProductDraftVersionRelease
        data_product_draft_version_release_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Construct a json representation of a DataProductVersionSummaryDataProduct model
        data_product_version_summary_data_product_model_json = {}
        data_product_version_summary_data_product_model_json['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_version_summary_data_product_model_json['release'] = data_product_draft_version_release_model
        data_product_version_summary_data_product_model_json['container'] = container_reference_model

        # Construct a model instance of DataProductVersionSummaryDataProduct by calling from_dict on the json representation
        data_product_version_summary_data_product_model = DataProductVersionSummaryDataProduct.from_dict(
            data_product_version_summary_data_product_model_json
        )
        assert data_product_version_summary_data_product_model != False

        # Construct a model instance of DataProductVersionSummaryDataProduct by calling from_dict on the json representation
        data_product_version_summary_data_product_model_dict = DataProductVersionSummaryDataProduct.from_dict(
            data_product_version_summary_data_product_model_json
        ).__dict__
        data_product_version_summary_data_product_model2 = DataProductVersionSummaryDataProduct(
            **data_product_version_summary_data_product_model_dict
        )

        # Verify the model instances are equivalent
        assert data_product_version_summary_data_product_model == data_product_version_summary_data_product_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_version_summary_data_product_model_json2 = (
            data_product_version_summary_data_product_model.to_dict()
        )
        assert (
            data_product_version_summary_data_product_model_json2
            == data_product_version_summary_data_product_model_json
        )


class TestModel_DataProductWorkflows:
    """
    Test Class for DataProductWorkflows
    """

    def test_data_product_workflows_serialization(self):
        """
        Test serialization/deserialization for DataProductWorkflows
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_product_custom_workflow_definition_model = {}  # DataProductCustomWorkflowDefinition
        data_product_custom_workflow_definition_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        data_product_order_access_request_model = {}  # DataProductOrderAccessRequest
        data_product_order_access_request_model['task_assignee_users'] = ['testString']
        data_product_order_access_request_model['pre_approved_users'] = ['testString']
        data_product_order_access_request_model['custom_workflow_definition'] = (
            data_product_custom_workflow_definition_model
        )

        # Construct a json representation of a DataProductWorkflows model
        data_product_workflows_model_json = {}
        data_product_workflows_model_json['order_access_request'] = data_product_order_access_request_model

        # Construct a model instance of DataProductWorkflows by calling from_dict on the json representation
        data_product_workflows_model = DataProductWorkflows.from_dict(data_product_workflows_model_json)
        assert data_product_workflows_model != False

        # Construct a model instance of DataProductWorkflows by calling from_dict on the json representation
        data_product_workflows_model_dict = DataProductWorkflows.from_dict(data_product_workflows_model_json).__dict__
        data_product_workflows_model2 = DataProductWorkflows(**data_product_workflows_model_dict)

        # Verify the model instances are equivalent
        assert data_product_workflows_model == data_product_workflows_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_workflows_model_json2 = data_product_workflows_model.to_dict()
        assert data_product_workflows_model_json2 == data_product_workflows_model_json


class TestModel_DeliveryMethod:
    """
    Test Class for DeliveryMethod
    """

    def test_delivery_method_serialization(self):
        """
        Test serialization/deserialization for DeliveryMethod
        """

        # Construct dict forms of any model objects needed in order to build this model.

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Construct a json representation of a DeliveryMethod model
        delivery_method_model_json = {}
        delivery_method_model_json['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model_json['container'] = container_reference_model

        # Construct a model instance of DeliveryMethod by calling from_dict on the json representation
        delivery_method_model = DeliveryMethod.from_dict(delivery_method_model_json)
        assert delivery_method_model != False

        # Construct a model instance of DeliveryMethod by calling from_dict on the json representation
        delivery_method_model_dict = DeliveryMethod.from_dict(delivery_method_model_json).__dict__
        delivery_method_model2 = DeliveryMethod(**delivery_method_model_dict)

        # Verify the model instances are equivalent
        assert delivery_method_model == delivery_method_model2

        # Convert model instance back to dict and verify no loss of data
        delivery_method_model_json2 = delivery_method_model.to_dict()
        assert delivery_method_model_json2 == delivery_method_model_json


class TestModel_Domain:
    """
    Test Class for Domain
    """

    def test_domain_serialization(self):
        """
        Test serialization/deserialization for Domain
        """

        # Construct dict forms of any model objects needed in order to build this model.

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Construct a json representation of a Domain model
        domain_model_json = {}
        domain_model_json['id'] = 'testString'
        domain_model_json['name'] = 'testString'
        domain_model_json['container'] = container_reference_model

        # Construct a model instance of Domain by calling from_dict on the json representation
        domain_model = Domain.from_dict(domain_model_json)
        assert domain_model != False

        # Construct a model instance of Domain by calling from_dict on the json representation
        domain_model_dict = Domain.from_dict(domain_model_json).__dict__
        domain_model2 = Domain(**domain_model_dict)

        # Verify the model instances are equivalent
        assert domain_model == domain_model2

        # Convert model instance back to dict and verify no loss of data
        domain_model_json2 = domain_model.to_dict()
        assert domain_model_json2 == domain_model_json


class TestModel_ErrorModelResource:
    """
    Test Class for ErrorModelResource
    """

    def test_error_model_resource_serialization(self):
        """
        Test serialization/deserialization for ErrorModelResource
        """

        # Construct a json representation of a ErrorModelResource model
        error_model_resource_model_json = {}
        error_model_resource_model_json['code'] = 'request_body_error'
        error_model_resource_model_json['message'] = 'testString'
        error_model_resource_model_json['extra'] = {'anyKey': 'anyValue'}
        error_model_resource_model_json['more_info'] = 'testString'

        # Construct a model instance of ErrorModelResource by calling from_dict on the json representation
        error_model_resource_model = ErrorModelResource.from_dict(error_model_resource_model_json)
        assert error_model_resource_model != False

        # Construct a model instance of ErrorModelResource by calling from_dict on the json representation
        error_model_resource_model_dict = ErrorModelResource.from_dict(error_model_resource_model_json).__dict__
        error_model_resource_model2 = ErrorModelResource(**error_model_resource_model_dict)

        # Verify the model instances are equivalent
        assert error_model_resource_model == error_model_resource_model2

        # Convert model instance back to dict and verify no loss of data
        error_model_resource_model_json2 = error_model_resource_model.to_dict()
        assert error_model_resource_model_json2 == error_model_resource_model_json


class TestModel_FirstPage:
    """
    Test Class for FirstPage
    """

    def test_first_page_serialization(self):
        """
        Test serialization/deserialization for FirstPage
        """

        # Construct a json representation of a FirstPage model
        first_page_model_json = {}
        first_page_model_json['href'] = 'https://api.example.com/collection'

        # Construct a model instance of FirstPage by calling from_dict on the json representation
        first_page_model = FirstPage.from_dict(first_page_model_json)
        assert first_page_model != False

        # Construct a model instance of FirstPage by calling from_dict on the json representation
        first_page_model_dict = FirstPage.from_dict(first_page_model_json).__dict__
        first_page_model2 = FirstPage(**first_page_model_dict)

        # Verify the model instances are equivalent
        assert first_page_model == first_page_model2

        # Convert model instance back to dict and verify no loss of data
        first_page_model_json2 = first_page_model.to_dict()
        assert first_page_model_json2 == first_page_model_json


class TestModel_InitializeResource:
    """
    Test Class for InitializeResource
    """

    def test_initialize_resource_serialization(self):
        """
        Test serialization/deserialization for InitializeResource
        """

        # Construct dict forms of any model objects needed in order to build this model.

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        error_model_resource_model = {}  # ErrorModelResource
        error_model_resource_model['code'] = 'request_body_error'
        error_model_resource_model['message'] = 'testString'
        error_model_resource_model['extra'] = {'anyKey': 'anyValue'}
        error_model_resource_model['more_info'] = 'testString'

        initialized_option_model = {}  # InitializedOption
        initialized_option_model['name'] = 'testString'
        initialized_option_model['version'] = 1

        workflow_definition_reference_model = {}  # WorkflowDefinitionReference
        workflow_definition_reference_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        provided_workflow_resource_model = {}  # ProvidedWorkflowResource
        provided_workflow_resource_model['definition'] = workflow_definition_reference_model

        provided_catalog_workflows_model = {}  # ProvidedCatalogWorkflows
        provided_catalog_workflows_model['data_access'] = provided_workflow_resource_model
        provided_catalog_workflows_model['request_new_product'] = provided_workflow_resource_model

        # Construct a json representation of a InitializeResource model
        initialize_resource_model_json = {}
        initialize_resource_model_json['container'] = container_reference_model
        initialize_resource_model_json['href'] = (
            'https://api.example.com/configuration/initialize/status?catalog_id=d29c42eb-7100-4b7a-8257-c196dbcca1cd'
        )
        initialize_resource_model_json['status'] = 'not_started'
        initialize_resource_model_json['trace'] = 'testString'
        initialize_resource_model_json['errors'] = [error_model_resource_model]
        initialize_resource_model_json['last_started_at'] = '2023-08-21T15:24:06.021000Z'
        initialize_resource_model_json['last_finished_at'] = '2023-08-21T20:24:34.450000Z'
        initialize_resource_model_json['initialized_options'] = [initialized_option_model]
        initialize_resource_model_json['workflows'] = provided_catalog_workflows_model

        # Construct a model instance of InitializeResource by calling from_dict on the json representation
        initialize_resource_model = InitializeResource.from_dict(initialize_resource_model_json)
        assert initialize_resource_model != False

        # Construct a model instance of InitializeResource by calling from_dict on the json representation
        initialize_resource_model_dict = InitializeResource.from_dict(initialize_resource_model_json).__dict__
        initialize_resource_model2 = InitializeResource(**initialize_resource_model_dict)

        # Verify the model instances are equivalent
        assert initialize_resource_model == initialize_resource_model2

        # Convert model instance back to dict and verify no loss of data
        initialize_resource_model_json2 = initialize_resource_model.to_dict()
        assert initialize_resource_model_json2 == initialize_resource_model_json


class TestModel_InitializedOption:
    """
    Test Class for InitializedOption
    """

    def test_initialized_option_serialization(self):
        """
        Test serialization/deserialization for InitializedOption
        """

        # Construct a json representation of a InitializedOption model
        initialized_option_model_json = {}
        initialized_option_model_json['name'] = 'testString'
        initialized_option_model_json['version'] = 1

        # Construct a model instance of InitializedOption by calling from_dict on the json representation
        initialized_option_model = InitializedOption.from_dict(initialized_option_model_json)
        assert initialized_option_model != False

        # Construct a model instance of InitializedOption by calling from_dict on the json representation
        initialized_option_model_dict = InitializedOption.from_dict(initialized_option_model_json).__dict__
        initialized_option_model2 = InitializedOption(**initialized_option_model_dict)

        # Verify the model instances are equivalent
        assert initialized_option_model == initialized_option_model2

        # Convert model instance back to dict and verify no loss of data
        initialized_option_model_json2 = initialized_option_model.to_dict()
        assert initialized_option_model_json2 == initialized_option_model_json


class TestModel_JsonPatchOperation:
    """
    Test Class for JsonPatchOperation
    """

    def test_json_patch_operation_serialization(self):
        """
        Test serialization/deserialization for JsonPatchOperation
        """

        # Construct a json representation of a JsonPatchOperation model
        json_patch_operation_model_json = {}
        json_patch_operation_model_json['op'] = 'add'
        json_patch_operation_model_json['path'] = 'testString'
        json_patch_operation_model_json['from'] = 'testString'
        json_patch_operation_model_json['value'] = 'testString'

        # Construct a model instance of JsonPatchOperation by calling from_dict on the json representation
        json_patch_operation_model = JsonPatchOperation.from_dict(json_patch_operation_model_json)
        assert json_patch_operation_model != False

        # Construct a model instance of JsonPatchOperation by calling from_dict on the json representation
        json_patch_operation_model_dict = JsonPatchOperation.from_dict(json_patch_operation_model_json).__dict__
        json_patch_operation_model2 = JsonPatchOperation(**json_patch_operation_model_dict)

        # Verify the model instances are equivalent
        assert json_patch_operation_model == json_patch_operation_model2

        # Convert model instance back to dict and verify no loss of data
        json_patch_operation_model_json2 = json_patch_operation_model.to_dict()
        assert json_patch_operation_model_json2 == json_patch_operation_model_json


class TestModel_NextPage:
    """
    Test Class for NextPage
    """

    def test_next_page_serialization(self):
        """
        Test serialization/deserialization for NextPage
        """

        # Construct a json representation of a NextPage model
        next_page_model_json = {}
        next_page_model_json['href'] = 'https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9'
        next_page_model_json['start'] = 'eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9'

        # Construct a model instance of NextPage by calling from_dict on the json representation
        next_page_model = NextPage.from_dict(next_page_model_json)
        assert next_page_model != False

        # Construct a model instance of NextPage by calling from_dict on the json representation
        next_page_model_dict = NextPage.from_dict(next_page_model_json).__dict__
        next_page_model2 = NextPage(**next_page_model_dict)

        # Verify the model instances are equivalent
        assert next_page_model == next_page_model2

        # Convert model instance back to dict and verify no loss of data
        next_page_model_json2 = next_page_model.to_dict()
        assert next_page_model_json2 == next_page_model_json


class TestModel_ProvidedCatalogWorkflows:
    """
    Test Class for ProvidedCatalogWorkflows
    """

    def test_provided_catalog_workflows_serialization(self):
        """
        Test serialization/deserialization for ProvidedCatalogWorkflows
        """

        # Construct dict forms of any model objects needed in order to build this model.

        workflow_definition_reference_model = {}  # WorkflowDefinitionReference
        workflow_definition_reference_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        provided_workflow_resource_model = {}  # ProvidedWorkflowResource
        provided_workflow_resource_model['definition'] = workflow_definition_reference_model

        # Construct a json representation of a ProvidedCatalogWorkflows model
        provided_catalog_workflows_model_json = {}
        provided_catalog_workflows_model_json['data_access'] = provided_workflow_resource_model
        provided_catalog_workflows_model_json['request_new_product'] = provided_workflow_resource_model

        # Construct a model instance of ProvidedCatalogWorkflows by calling from_dict on the json representation
        provided_catalog_workflows_model = ProvidedCatalogWorkflows.from_dict(provided_catalog_workflows_model_json)
        assert provided_catalog_workflows_model != False

        # Construct a model instance of ProvidedCatalogWorkflows by calling from_dict on the json representation
        provided_catalog_workflows_model_dict = ProvidedCatalogWorkflows.from_dict(
            provided_catalog_workflows_model_json
        ).__dict__
        provided_catalog_workflows_model2 = ProvidedCatalogWorkflows(**provided_catalog_workflows_model_dict)

        # Verify the model instances are equivalent
        assert provided_catalog_workflows_model == provided_catalog_workflows_model2

        # Convert model instance back to dict and verify no loss of data
        provided_catalog_workflows_model_json2 = provided_catalog_workflows_model.to_dict()
        assert provided_catalog_workflows_model_json2 == provided_catalog_workflows_model_json


class TestModel_ProvidedWorkflowResource:
    """
    Test Class for ProvidedWorkflowResource
    """

    def test_provided_workflow_resource_serialization(self):
        """
        Test serialization/deserialization for ProvidedWorkflowResource
        """

        # Construct dict forms of any model objects needed in order to build this model.

        workflow_definition_reference_model = {}  # WorkflowDefinitionReference
        workflow_definition_reference_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        # Construct a json representation of a ProvidedWorkflowResource model
        provided_workflow_resource_model_json = {}
        provided_workflow_resource_model_json['definition'] = workflow_definition_reference_model

        # Construct a model instance of ProvidedWorkflowResource by calling from_dict on the json representation
        provided_workflow_resource_model = ProvidedWorkflowResource.from_dict(provided_workflow_resource_model_json)
        assert provided_workflow_resource_model != False

        # Construct a model instance of ProvidedWorkflowResource by calling from_dict on the json representation
        provided_workflow_resource_model_dict = ProvidedWorkflowResource.from_dict(
            provided_workflow_resource_model_json
        ).__dict__
        provided_workflow_resource_model2 = ProvidedWorkflowResource(**provided_workflow_resource_model_dict)

        # Verify the model instances are equivalent
        assert provided_workflow_resource_model == provided_workflow_resource_model2

        # Convert model instance back to dict and verify no loss of data
        provided_workflow_resource_model_json2 = provided_workflow_resource_model.to_dict()
        assert provided_workflow_resource_model_json2 == provided_workflow_resource_model_json


class TestModel_ServiceIdCredentials:
    """
    Test Class for ServiceIdCredentials
    """

    def test_service_id_credentials_serialization(self):
        """
        Test serialization/deserialization for ServiceIdCredentials
        """

        # Construct a json representation of a ServiceIdCredentials model
        service_id_credentials_model_json = {}
        service_id_credentials_model_json['name'] = 'data-product-admin-service-id-API-key'
        service_id_credentials_model_json['created_at'] = '2024-03-15T04:07+0000'

        # Construct a model instance of ServiceIdCredentials by calling from_dict on the json representation
        service_id_credentials_model = ServiceIdCredentials.from_dict(service_id_credentials_model_json)
        assert service_id_credentials_model != False

        # Construct a model instance of ServiceIdCredentials by calling from_dict on the json representation
        service_id_credentials_model_dict = ServiceIdCredentials.from_dict(service_id_credentials_model_json).__dict__
        service_id_credentials_model2 = ServiceIdCredentials(**service_id_credentials_model_dict)

        # Verify the model instances are equivalent
        assert service_id_credentials_model == service_id_credentials_model2

        # Convert model instance back to dict and verify no loss of data
        service_id_credentials_model_json2 = service_id_credentials_model.to_dict()
        assert service_id_credentials_model_json2 == service_id_credentials_model_json


class TestModel_UseCase:
    """
    Test Class for UseCase
    """

    def test_use_case_serialization(self):
        """
        Test serialization/deserialization for UseCase
        """

        # Construct dict forms of any model objects needed in order to build this model.

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Construct a json representation of a UseCase model
        use_case_model_json = {}
        use_case_model_json['id'] = 'testString'
        use_case_model_json['name'] = 'testString'
        use_case_model_json['container'] = container_reference_model

        # Construct a model instance of UseCase by calling from_dict on the json representation
        use_case_model = UseCase.from_dict(use_case_model_json)
        assert use_case_model != False

        # Construct a model instance of UseCase by calling from_dict on the json representation
        use_case_model_dict = UseCase.from_dict(use_case_model_json).__dict__
        use_case_model2 = UseCase(**use_case_model_dict)

        # Verify the model instances are equivalent
        assert use_case_model == use_case_model2

        # Convert model instance back to dict and verify no loss of data
        use_case_model_json2 = use_case_model.to_dict()
        assert use_case_model_json2 == use_case_model_json


class TestModel_WorkflowDefinitionReference:
    """
    Test Class for WorkflowDefinitionReference
    """

    def test_workflow_definition_reference_serialization(self):
        """
        Test serialization/deserialization for WorkflowDefinitionReference
        """

        # Construct a json representation of a WorkflowDefinitionReference model
        workflow_definition_reference_model_json = {}
        workflow_definition_reference_model_json['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        # Construct a model instance of WorkflowDefinitionReference by calling from_dict on the json representation
        workflow_definition_reference_model = WorkflowDefinitionReference.from_dict(
            workflow_definition_reference_model_json
        )
        assert workflow_definition_reference_model != False

        # Construct a model instance of WorkflowDefinitionReference by calling from_dict on the json representation
        workflow_definition_reference_model_dict = WorkflowDefinitionReference.from_dict(
            workflow_definition_reference_model_json
        ).__dict__
        workflow_definition_reference_model2 = WorkflowDefinitionReference(**workflow_definition_reference_model_dict)

        # Verify the model instances are equivalent
        assert workflow_definition_reference_model == workflow_definition_reference_model2

        # Convert model instance back to dict and verify no loss of data
        workflow_definition_reference_model_json2 = workflow_definition_reference_model.to_dict()
        assert workflow_definition_reference_model_json2 == workflow_definition_reference_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
