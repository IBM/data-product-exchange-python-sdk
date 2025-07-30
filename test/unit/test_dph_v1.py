# -*- coding: utf-8 -*-
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

"""
Unit Tests for DphV1
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
from dph_services.dph_v1 import *


_service = DphV1(
    authenticator=NoAuthAuthenticator()
)

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

        service = DphV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DphV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DphV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


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
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "href": "https://api.example.com/configuration/initialize/status?catalog_id=d29c42eb-7100-4b7a-8257-c196dbcca1cd", "status": "not_started", "trace": "trace", "errors": [{"code": "request_body_error", "message": "message", "extra": {"id": "id", "timestamp": "2019-01-01T12:00:00.000Z", "environment_name": "environment_name", "http_status": 0, "source_cluster": 0, "source_component": 0, "transaction_id": 0}, "more_info": "more_info"}], "last_started_at": "2023-08-21T15:24:06.021Z", "last_finished_at": "2023-08-21T20:24:34.450Z", "initialized_options": [{"name": "name", "version": 1}], "workflows": {"data_access": {"definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}, "request_new_product": {"definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        container_id = 'testString'

        # Invoke method
        response = _service.get_initialize_status(
            container_id=container_id,
            headers={},
        )

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
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "href": "https://api.example.com/configuration/initialize/status?catalog_id=d29c42eb-7100-4b7a-8257-c196dbcca1cd", "status": "not_started", "trace": "trace", "errors": [{"code": "request_body_error", "message": "message", "extra": {"id": "id", "timestamp": "2019-01-01T12:00:00.000Z", "environment_name": "environment_name", "http_status": 0, "source_cluster": 0, "source_component": 0, "transaction_id": 0}, "more_info": "more_info"}], "last_started_at": "2023-08-21T15:24:06.021Z", "last_finished_at": "2023-08-21T20:24:34.450Z", "initialized_options": [{"name": "name", "version": 1}], "workflows": {"data_access": {"definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}, "request_new_product": {"definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
        mock_response = '{"name": "data-product-admin-service-id-API-key", "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "href": "https://api.example.com/configuration/initialize/status?catalog_id=d29c42eb-7100-4b7a-8257-c196dbcca1cd", "status": "not_started", "trace": "trace", "errors": [{"code": "request_body_error", "message": "message", "extra": {"id": "id", "timestamp": "2019-01-01T12:00:00.000Z", "environment_name": "environment_name", "http_status": 0, "source_cluster": 0, "source_component": 0, "transaction_id": 0}, "more_info": "more_info"}], "last_started_at": "2023-08-21T15:24:06.021Z", "last_finished_at": "2023-08-21T20:24:34.450Z", "initialized_options": [{"name": "name", "version": 1}], "workflows": {"data_access": {"definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}, "request_new_product": {"definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {}
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Set up parameter values
        container = container_reference_model
        include = ['delivery_methods', 'domains_multi_industry', 'data_product_samples', 'workflows', 'project', 'catalog_configurations']

        # Invoke method
        response = _service.initialize(
            container=container,
            include=include,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['container'] == container_reference_model
        assert req_body['include'] == ['delivery_methods', 'domains_multi_industry', 'data_product_samples', 'workflows', 'project', 'catalog_configurations']

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
        responses.add(
            responses.POST,
            url,
            status=204,
        )

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
# Start of Service: DataAssetVisualization
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

        service = DphV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DphV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DphV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateDataAssetVisualization:
    """
    Test Class for create_data_asset_visualization
    """

    @responses.activate
    def test_create_data_asset_visualization_all_params(self):
        """
        create_data_asset_visualization()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_asset/visualization')
        mock_response = '{"results": [{"visualization": {"id": "id", "name": "name"}, "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "related_asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "error": {"code": "code", "message": "message"}}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a Visualization model
        visualization_model = {}
        visualization_model['id'] = 'testString'
        visualization_model['name'] = 'testString'

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {}
        container_reference_model['id'] = '2be8f727-c5d2-4cb0-9216-f9888f428048'
        container_reference_model['type'] = 'catalog'

        # Construct a dict representation of a AssetReference model
        asset_reference_model = {}
        asset_reference_model['id'] = 'caeee3f3-756e-47d5-846d-da4600809e22'
        asset_reference_model['name'] = 'testString'
        asset_reference_model['container'] = container_reference_model

        # Construct a dict representation of a ErrorMessage model
        error_message_model = {}
        error_message_model['code'] = 'testString'
        error_message_model['message'] = 'testString'

        # Construct a dict representation of a DataAssetRelationship model
        data_asset_relationship_model = {}
        data_asset_relationship_model['visualization'] = visualization_model
        data_asset_relationship_model['asset'] = asset_reference_model
        data_asset_relationship_model['related_asset'] = asset_reference_model
        data_asset_relationship_model['error'] = error_message_model

        # Set up parameter values
        assets = [data_asset_relationship_model]

        # Invoke method
        response = _service.create_data_asset_visualization(
            assets=assets,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['assets'] == [data_asset_relationship_model]

    def test_create_data_asset_visualization_all_params_with_retries(self):
        # Enable retries and run test_create_data_asset_visualization_all_params.
        _service.enable_retries()
        self.test_create_data_asset_visualization_all_params()

        # Disable retries and run test_create_data_asset_visualization_all_params.
        _service.disable_retries()
        self.test_create_data_asset_visualization_all_params()


class TestReinitiateDataAssetVisualization:
    """
    Test Class for reinitiate_data_asset_visualization
    """

    @responses.activate
    def test_reinitiate_data_asset_visualization_all_params(self):
        """
        reinitiate_data_asset_visualization()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_asset/visualization/reinitiate')
        mock_response = '{"results": [{"visualization": {"id": "id", "name": "name"}, "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "related_asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "error": {"code": "code", "message": "message"}}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a Visualization model
        visualization_model = {}
        visualization_model['id'] = 'testString'
        visualization_model['name'] = 'testString'

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {}
        container_reference_model['id'] = '2be8f727-c5d2-4cb0-9216-f9888f428048'
        container_reference_model['type'] = 'catalog'

        # Construct a dict representation of a AssetReference model
        asset_reference_model = {}
        asset_reference_model['id'] = 'caeee3f3-756e-47d5-846d-da4600809e22'
        asset_reference_model['name'] = 'testString'
        asset_reference_model['container'] = container_reference_model

        # Construct a dict representation of a ErrorMessage model
        error_message_model = {}
        error_message_model['code'] = 'testString'
        error_message_model['message'] = 'testString'

        # Construct a dict representation of a DataAssetRelationship model
        data_asset_relationship_model = {}
        data_asset_relationship_model['visualization'] = visualization_model
        data_asset_relationship_model['asset'] = asset_reference_model
        data_asset_relationship_model['related_asset'] = asset_reference_model
        data_asset_relationship_model['error'] = error_message_model

        # Set up parameter values
        assets = [data_asset_relationship_model]

        # Invoke method
        response = _service.reinitiate_data_asset_visualization(
            assets=assets,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['assets'] == [data_asset_relationship_model]

    def test_reinitiate_data_asset_visualization_all_params_with_retries(self):
        # Enable retries and run test_reinitiate_data_asset_visualization_all_params.
        _service.enable_retries()
        self.test_reinitiate_data_asset_visualization_all_params()

        # Disable retries and run test_reinitiate_data_asset_visualization_all_params.
        _service.disable_retries()
        self.test_reinitiate_data_asset_visualization_all_params()


# endregion
##############################################################################
# End of Service: DataAssetVisualization
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

        service = DphV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DphV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DphV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


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
        mock_response = '{"limit": 200, "first": {"href": "https://api.example.com/collection"}, "next": {"href": "https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "total_results": 200, "data_products": [{"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "name": "name"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        limit = 200
        start = 'testString'

        # Invoke method
        response = _service.list_data_products(
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
        mock_response = '{"limit": 200, "first": {"href": "https://api.example.com/collection"}, "next": {"href": "https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "total_results": 200, "data_products": [{"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "name": "name"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"data_products":[{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"name":"name"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"data_products":[{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"name":"name"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = DataProductsPager(
            client=_service,
            limit=10,
        )
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
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"data_products":[{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"name":"name"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"data_products":[{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"name":"name"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = DataProductsPager(
            client=_service,
            limit=10,
        )
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
        mock_response = '{"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "name": "name", "latest_release": {"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}, "drafts": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
        asset_reference_model['name'] = 'testString'
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

        # Construct a dict representation of a Domain model
        domain_model = {}
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = '0.0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        # Construct a dict representation of a ContractTermsMoreInfo model
        contract_terms_more_info_model = {}
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://moreinfo.example.com'

        # Construct a dict representation of a Description model
        description_model = {}
        description_model['purpose'] = 'Used for customer behavior analysis.'
        description_model['limitations'] = 'Data cannot be used for marketing.'
        description_model['usage'] = 'Data should be used only for analytics.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = '{"property1":"value1"}'

        # Construct a dict representation of a ContractTemplateOrganization model
        contract_template_organization_model = {}
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role'] = 'owner'

        # Construct a dict representation of a Pricing model
        pricing_model = {}
        pricing_model['amount'] = '100.0'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        # Construct a dict representation of a ContractTemplateSLAProperty model
        contract_template_sla_property_model = {}
        contract_template_sla_property_model['property'] = 'Uptime Guarantee'
        contract_template_sla_property_model['value'] = '99.9'

        # Construct a dict representation of a ContractTemplateSLA model
        contract_template_sla_model = {}
        contract_template_sla_model['default_element'] = 'Standard SLA Policy'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        # Construct a dict representation of a ContractTemplateSupportAndCommunication model
        contract_template_support_and_communication_model = {}
        contract_template_support_and_communication_model['channel'] = 'Email Support'
        contract_template_support_and_communication_model['url'] = 'https://support.example.com'

        # Construct a dict representation of a ContractTemplateCustomProperty model
        contract_template_custom_property_model = {}
        contract_template_custom_property_model['key'] = 'customPropertyKey'
        contract_template_custom_property_model['value'] = 'customPropertyValue'

        # Construct a dict representation of a ContractTest model
        contract_test_model = {}
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        # Construct a dict representation of a ContractSchemaPropertyType model
        contract_schema_property_type_model = {}
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        # Construct a dict representation of a ContractSchemaProperty model
        contract_schema_property_model = {}
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        # Construct a dict representation of a ContractSchema model
        contract_schema_model = {}
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        # Construct a dict representation of a ContractTerms model
        contract_terms_model = {}
        contract_terms_model['asset'] = asset_reference_model
        contract_terms_model['id'] = 'testString'
        contract_terms_model['documents'] = [contract_terms_document_model]
        contract_terms_model['error_msg'] = 'testString'
        contract_terms_model['overview'] = overview_model
        contract_terms_model['description'] = description_model
        contract_terms_model['organization'] = [contract_template_organization_model]
        contract_terms_model['roles'] = [roles_model]
        contract_terms_model['price'] = pricing_model
        contract_terms_model['sla'] = [contract_template_sla_model]
        contract_terms_model['support_and_communication'] = [contract_template_support_and_communication_model]
        contract_terms_model['custom_properties'] = [contract_template_custom_property_model]
        contract_terms_model['contract_test'] = contract_test_model
        contract_terms_model['schema'] = [contract_schema_model]

        # Construct a dict representation of a AssetPartReference model
        asset_part_reference_model = {}
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['name'] = 'testString'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        # Construct a dict representation of a EngineDetailsModel model
        engine_details_model_model = {}
        engine_details_model_model['display_name'] = 'Iceberg Engine'
        engine_details_model_model['engine_id'] = 'presto767'
        engine_details_model_model['engine_port'] = '34567'
        engine_details_model_model['engine_host'] = 'a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud'
        engine_details_model_model['associated_catalogs'] = ['testString']

        # Construct a dict representation of a ProducerInputModel model
        producer_input_model_model = {}
        producer_input_model_model['engine_details'] = engine_details_model_model

        # Construct a dict representation of a DeliveryMethodPropertiesModel model
        delivery_method_properties_model_model = {}
        delivery_method_properties_model_model['producer_input'] = producer_input_model_model

        # Construct a dict representation of a DeliveryMethod model
        delivery_method_model = {}
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model
        delivery_method_model['getproperties'] = delivery_method_properties_model_model

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
        data_product_order_access_request_model['custom_workflow_definition'] = data_product_custom_workflow_definition_model

        # Construct a dict representation of a DataProductWorkflows model
        data_product_workflows_model = {}
        data_product_workflows_model['order_access_request'] = data_product_order_access_request_model

        # Construct a dict representation of a AssetListAccessControl model
        asset_list_access_control_model = {}
        asset_list_access_control_model['owner'] = 'IBMid-696000KYV9'

        # Construct a dict representation of a ContainerIdentity model
        container_identity_model = {}
        container_identity_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'

        # Construct a dict representation of a AssetPrototype model
        asset_prototype_model = {}
        asset_prototype_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_prototype_model['container'] = container_identity_model

        # Construct a dict representation of a DataProductDraftPrototype model
        data_product_draft_prototype_model = {}
        data_product_draft_prototype_model['version'] = '1.0.0'
        data_product_draft_prototype_model['state'] = 'draft'
        data_product_draft_prototype_model['data_product'] = data_product_identity_model
        data_product_draft_prototype_model['name'] = 'My New Data Product'
        data_product_draft_prototype_model['description'] = 'This is a description of My Data Product.'
        data_product_draft_prototype_model['tags'] = ['testString']
        data_product_draft_prototype_model['use_cases'] = [use_case_model]
        data_product_draft_prototype_model['types'] = ['data']
        data_product_draft_prototype_model['contract_terms'] = [contract_terms_model]
        data_product_draft_prototype_model['domain'] = domain_model
        data_product_draft_prototype_model['parts_out'] = [data_product_part_model]
        data_product_draft_prototype_model['workflows'] = data_product_workflows_model
        data_product_draft_prototype_model['dataview_enabled'] = True
        data_product_draft_prototype_model['comments'] = 'Comments by a producer that are provided either at the time of data product version creation or retiring'
        data_product_draft_prototype_model['access_control'] = asset_list_access_control_model
        data_product_draft_prototype_model['last_updated_at'] = '2019-01-01T12:00:00Z'
        data_product_draft_prototype_model['is_restricted'] = True
        data_product_draft_prototype_model['asset'] = asset_prototype_model

        # Set up parameter values
        drafts = [data_product_draft_prototype_model]
        limit = 200
        start = 'testString'

        # Invoke method
        response = _service.create_data_product(
            drafts,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['drafts'] == [data_product_draft_prototype_model]

    def test_create_data_product_all_params_with_retries(self):
        # Enable retries and run test_create_data_product_all_params.
        _service.enable_retries()
        self.test_create_data_product_all_params()

        # Disable retries and run test_create_data_product_all_params.
        _service.disable_retries()
        self.test_create_data_product_all_params()

    @responses.activate
    def test_create_data_product_required_params(self):
        """
        test_create_data_product_required_params()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products')
        mock_response = '{"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "name": "name", "latest_release": {"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}, "drafts": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
        asset_reference_model['name'] = 'testString'
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

        # Construct a dict representation of a Domain model
        domain_model = {}
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = '0.0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        # Construct a dict representation of a ContractTermsMoreInfo model
        contract_terms_more_info_model = {}
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://moreinfo.example.com'

        # Construct a dict representation of a Description model
        description_model = {}
        description_model['purpose'] = 'Used for customer behavior analysis.'
        description_model['limitations'] = 'Data cannot be used for marketing.'
        description_model['usage'] = 'Data should be used only for analytics.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = '{"property1":"value1"}'

        # Construct a dict representation of a ContractTemplateOrganization model
        contract_template_organization_model = {}
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role'] = 'owner'

        # Construct a dict representation of a Pricing model
        pricing_model = {}
        pricing_model['amount'] = '100.0'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        # Construct a dict representation of a ContractTemplateSLAProperty model
        contract_template_sla_property_model = {}
        contract_template_sla_property_model['property'] = 'Uptime Guarantee'
        contract_template_sla_property_model['value'] = '99.9'

        # Construct a dict representation of a ContractTemplateSLA model
        contract_template_sla_model = {}
        contract_template_sla_model['default_element'] = 'Standard SLA Policy'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        # Construct a dict representation of a ContractTemplateSupportAndCommunication model
        contract_template_support_and_communication_model = {}
        contract_template_support_and_communication_model['channel'] = 'Email Support'
        contract_template_support_and_communication_model['url'] = 'https://support.example.com'

        # Construct a dict representation of a ContractTemplateCustomProperty model
        contract_template_custom_property_model = {}
        contract_template_custom_property_model['key'] = 'customPropertyKey'
        contract_template_custom_property_model['value'] = 'customPropertyValue'

        # Construct a dict representation of a ContractTest model
        contract_test_model = {}
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        # Construct a dict representation of a ContractSchemaPropertyType model
        contract_schema_property_type_model = {}
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        # Construct a dict representation of a ContractSchemaProperty model
        contract_schema_property_model = {}
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        # Construct a dict representation of a ContractSchema model
        contract_schema_model = {}
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        # Construct a dict representation of a ContractTerms model
        contract_terms_model = {}
        contract_terms_model['asset'] = asset_reference_model
        contract_terms_model['id'] = 'testString'
        contract_terms_model['documents'] = [contract_terms_document_model]
        contract_terms_model['error_msg'] = 'testString'
        contract_terms_model['overview'] = overview_model
        contract_terms_model['description'] = description_model
        contract_terms_model['organization'] = [contract_template_organization_model]
        contract_terms_model['roles'] = [roles_model]
        contract_terms_model['price'] = pricing_model
        contract_terms_model['sla'] = [contract_template_sla_model]
        contract_terms_model['support_and_communication'] = [contract_template_support_and_communication_model]
        contract_terms_model['custom_properties'] = [contract_template_custom_property_model]
        contract_terms_model['contract_test'] = contract_test_model
        contract_terms_model['schema'] = [contract_schema_model]

        # Construct a dict representation of a AssetPartReference model
        asset_part_reference_model = {}
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['name'] = 'testString'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        # Construct a dict representation of a EngineDetailsModel model
        engine_details_model_model = {}
        engine_details_model_model['display_name'] = 'Iceberg Engine'
        engine_details_model_model['engine_id'] = 'presto767'
        engine_details_model_model['engine_port'] = '34567'
        engine_details_model_model['engine_host'] = 'a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud'
        engine_details_model_model['associated_catalogs'] = ['testString']

        # Construct a dict representation of a ProducerInputModel model
        producer_input_model_model = {}
        producer_input_model_model['engine_details'] = engine_details_model_model

        # Construct a dict representation of a DeliveryMethodPropertiesModel model
        delivery_method_properties_model_model = {}
        delivery_method_properties_model_model['producer_input'] = producer_input_model_model

        # Construct a dict representation of a DeliveryMethod model
        delivery_method_model = {}
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model
        delivery_method_model['getproperties'] = delivery_method_properties_model_model

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
        data_product_order_access_request_model['custom_workflow_definition'] = data_product_custom_workflow_definition_model

        # Construct a dict representation of a DataProductWorkflows model
        data_product_workflows_model = {}
        data_product_workflows_model['order_access_request'] = data_product_order_access_request_model

        # Construct a dict representation of a AssetListAccessControl model
        asset_list_access_control_model = {}
        asset_list_access_control_model['owner'] = 'IBMid-696000KYV9'

        # Construct a dict representation of a ContainerIdentity model
        container_identity_model = {}
        container_identity_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'

        # Construct a dict representation of a AssetPrototype model
        asset_prototype_model = {}
        asset_prototype_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_prototype_model['container'] = container_identity_model

        # Construct a dict representation of a DataProductDraftPrototype model
        data_product_draft_prototype_model = {}
        data_product_draft_prototype_model['version'] = '1.0.0'
        data_product_draft_prototype_model['state'] = 'draft'
        data_product_draft_prototype_model['data_product'] = data_product_identity_model
        data_product_draft_prototype_model['name'] = 'My New Data Product'
        data_product_draft_prototype_model['description'] = 'This is a description of My Data Product.'
        data_product_draft_prototype_model['tags'] = ['testString']
        data_product_draft_prototype_model['use_cases'] = [use_case_model]
        data_product_draft_prototype_model['types'] = ['data']
        data_product_draft_prototype_model['contract_terms'] = [contract_terms_model]
        data_product_draft_prototype_model['domain'] = domain_model
        data_product_draft_prototype_model['parts_out'] = [data_product_part_model]
        data_product_draft_prototype_model['workflows'] = data_product_workflows_model
        data_product_draft_prototype_model['dataview_enabled'] = True
        data_product_draft_prototype_model['comments'] = 'Comments by a producer that are provided either at the time of data product version creation or retiring'
        data_product_draft_prototype_model['access_control'] = asset_list_access_control_model
        data_product_draft_prototype_model['last_updated_at'] = '2019-01-01T12:00:00Z'
        data_product_draft_prototype_model['is_restricted'] = True
        data_product_draft_prototype_model['asset'] = asset_prototype_model

        # Set up parameter values
        drafts = [data_product_draft_prototype_model]

        # Invoke method
        response = _service.create_data_product(
            drafts,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['drafts'] == [data_product_draft_prototype_model]

    def test_create_data_product_required_params_with_retries(self):
        # Enable retries and run test_create_data_product_required_params.
        _service.enable_retries()
        self.test_create_data_product_required_params()

        # Disable retries and run test_create_data_product_required_params.
        _service.disable_retries()
        self.test_create_data_product_required_params()

    @responses.activate
    def test_create_data_product_value_error(self):
        """
        test_create_data_product_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products')
        mock_response = '{"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "name": "name", "latest_release": {"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}, "drafts": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
        asset_reference_model['name'] = 'testString'
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

        # Construct a dict representation of a Domain model
        domain_model = {}
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = '0.0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        # Construct a dict representation of a ContractTermsMoreInfo model
        contract_terms_more_info_model = {}
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://moreinfo.example.com'

        # Construct a dict representation of a Description model
        description_model = {}
        description_model['purpose'] = 'Used for customer behavior analysis.'
        description_model['limitations'] = 'Data cannot be used for marketing.'
        description_model['usage'] = 'Data should be used only for analytics.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = '{"property1":"value1"}'

        # Construct a dict representation of a ContractTemplateOrganization model
        contract_template_organization_model = {}
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role'] = 'owner'

        # Construct a dict representation of a Pricing model
        pricing_model = {}
        pricing_model['amount'] = '100.0'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        # Construct a dict representation of a ContractTemplateSLAProperty model
        contract_template_sla_property_model = {}
        contract_template_sla_property_model['property'] = 'Uptime Guarantee'
        contract_template_sla_property_model['value'] = '99.9'

        # Construct a dict representation of a ContractTemplateSLA model
        contract_template_sla_model = {}
        contract_template_sla_model['default_element'] = 'Standard SLA Policy'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        # Construct a dict representation of a ContractTemplateSupportAndCommunication model
        contract_template_support_and_communication_model = {}
        contract_template_support_and_communication_model['channel'] = 'Email Support'
        contract_template_support_and_communication_model['url'] = 'https://support.example.com'

        # Construct a dict representation of a ContractTemplateCustomProperty model
        contract_template_custom_property_model = {}
        contract_template_custom_property_model['key'] = 'customPropertyKey'
        contract_template_custom_property_model['value'] = 'customPropertyValue'

        # Construct a dict representation of a ContractTest model
        contract_test_model = {}
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        # Construct a dict representation of a ContractSchemaPropertyType model
        contract_schema_property_type_model = {}
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        # Construct a dict representation of a ContractSchemaProperty model
        contract_schema_property_model = {}
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        # Construct a dict representation of a ContractSchema model
        contract_schema_model = {}
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        # Construct a dict representation of a ContractTerms model
        contract_terms_model = {}
        contract_terms_model['asset'] = asset_reference_model
        contract_terms_model['id'] = 'testString'
        contract_terms_model['documents'] = [contract_terms_document_model]
        contract_terms_model['error_msg'] = 'testString'
        contract_terms_model['overview'] = overview_model
        contract_terms_model['description'] = description_model
        contract_terms_model['organization'] = [contract_template_organization_model]
        contract_terms_model['roles'] = [roles_model]
        contract_terms_model['price'] = pricing_model
        contract_terms_model['sla'] = [contract_template_sla_model]
        contract_terms_model['support_and_communication'] = [contract_template_support_and_communication_model]
        contract_terms_model['custom_properties'] = [contract_template_custom_property_model]
        contract_terms_model['contract_test'] = contract_test_model
        contract_terms_model['schema'] = [contract_schema_model]

        # Construct a dict representation of a AssetPartReference model
        asset_part_reference_model = {}
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['name'] = 'testString'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        # Construct a dict representation of a EngineDetailsModel model
        engine_details_model_model = {}
        engine_details_model_model['display_name'] = 'Iceberg Engine'
        engine_details_model_model['engine_id'] = 'presto767'
        engine_details_model_model['engine_port'] = '34567'
        engine_details_model_model['engine_host'] = 'a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud'
        engine_details_model_model['associated_catalogs'] = ['testString']

        # Construct a dict representation of a ProducerInputModel model
        producer_input_model_model = {}
        producer_input_model_model['engine_details'] = engine_details_model_model

        # Construct a dict representation of a DeliveryMethodPropertiesModel model
        delivery_method_properties_model_model = {}
        delivery_method_properties_model_model['producer_input'] = producer_input_model_model

        # Construct a dict representation of a DeliveryMethod model
        delivery_method_model = {}
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model
        delivery_method_model['getproperties'] = delivery_method_properties_model_model

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
        data_product_order_access_request_model['custom_workflow_definition'] = data_product_custom_workflow_definition_model

        # Construct a dict representation of a DataProductWorkflows model
        data_product_workflows_model = {}
        data_product_workflows_model['order_access_request'] = data_product_order_access_request_model

        # Construct a dict representation of a AssetListAccessControl model
        asset_list_access_control_model = {}
        asset_list_access_control_model['owner'] = 'IBMid-696000KYV9'

        # Construct a dict representation of a ContainerIdentity model
        container_identity_model = {}
        container_identity_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'

        # Construct a dict representation of a AssetPrototype model
        asset_prototype_model = {}
        asset_prototype_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_prototype_model['container'] = container_identity_model

        # Construct a dict representation of a DataProductDraftPrototype model
        data_product_draft_prototype_model = {}
        data_product_draft_prototype_model['version'] = '1.0.0'
        data_product_draft_prototype_model['state'] = 'draft'
        data_product_draft_prototype_model['data_product'] = data_product_identity_model
        data_product_draft_prototype_model['name'] = 'My New Data Product'
        data_product_draft_prototype_model['description'] = 'This is a description of My Data Product.'
        data_product_draft_prototype_model['tags'] = ['testString']
        data_product_draft_prototype_model['use_cases'] = [use_case_model]
        data_product_draft_prototype_model['types'] = ['data']
        data_product_draft_prototype_model['contract_terms'] = [contract_terms_model]
        data_product_draft_prototype_model['domain'] = domain_model
        data_product_draft_prototype_model['parts_out'] = [data_product_part_model]
        data_product_draft_prototype_model['workflows'] = data_product_workflows_model
        data_product_draft_prototype_model['dataview_enabled'] = True
        data_product_draft_prototype_model['comments'] = 'Comments by a producer that are provided either at the time of data product version creation or retiring'
        data_product_draft_prototype_model['access_control'] = asset_list_access_control_model
        data_product_draft_prototype_model['last_updated_at'] = '2019-01-01T12:00:00Z'
        data_product_draft_prototype_model['is_restricted'] = True
        data_product_draft_prototype_model['asset'] = asset_prototype_model

        # Set up parameter values
        drafts = [data_product_draft_prototype_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "drafts": drafts,
        }
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
        mock_response = '{"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "name": "name", "latest_release": {"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}, "drafts": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'

        # Invoke method
        response = _service.get_data_product(
            data_product_id,
            headers={},
        )

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
        mock_response = '{"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "name": "name", "latest_release": {"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}, "drafts": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_product_id": data_product_id,
        }
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

        service = DphV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DphV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DphV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


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
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString/documents/testString/complete')
        mock_response = '{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'
        contract_terms_id = 'testString'
        document_id = 'testString'

        # Invoke method
        response = _service.complete_draft_contract_terms_document(
            data_product_id,
            draft_id,
            contract_terms_id,
            document_id,
            headers={},
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
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString/documents/testString/complete')
        mock_response = '{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
        mock_response = '{"limit": 200, "first": {"href": "https://api.example.com/collection"}, "next": {"href": "https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "total_results": 200, "drafts": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
        mock_response = '{"limit": 200, "first": {"href": "https://api.example.com/collection"}, "next": {"href": "https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "total_results": 200, "drafts": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'

        # Invoke method
        response = _service.list_data_product_drafts(
            data_product_id,
            headers={},
        )

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
        mock_response = '{"limit": 200, "first": {"href": "https://api.example.com/collection"}, "next": {"href": "https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "total_results": 200, "drafts": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_product_id": data_product_id,
        }
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
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"drafts":[{"version":"1.0.0","state":"draft","data_product":{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"name":"My Data Product","description":"This is a description of My Data Product.","tags":["tags"],"use_cases":[{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}],"types":["data"],"contract_terms":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"id":"id","documents":[{"url":"url","type":"terms_and_conditions","name":"name","id":"2b0bf220-079c-11ee-be56-0242ac120002","attachment":{"id":"id"},"upload_url":"upload_url"}],"error_msg":"error_msg","overview":{"api_version":"v3.0.1","kind":"DataContract","name":"Sample Data Contract","version":"0.0.0","domain":{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"more_info":"List of links to sources that provide more details on the data contract."},"description":{"purpose":"Used for customer behavior analysis.","limitations":"Data cannot be used for marketing.","usage":"Data should be used only for analytics.","more_info":[{"type":"privacy-statement","url":"https://moreinfo.example.com"}],"custom_properties":"{\\"property1\\":\\"value1\\"}"},"organization":[{"user_id":"IBMid-691000IN4G","role":"owner"}],"roles":[{"role":"owner"}],"price":{"amount":"100.0","currency":"USD","unit":"megabyte"},"sla":[{"default_element":"Standard SLA Policy","properties":[{"property":"Uptime Guarantee","value":"99.9"}]}],"support_and_communication":[{"channel":"Email Support","url":"https://support.example.com"}],"custom_properties":[{"key":"customPropertyKey","value":"customPropertyValue"}],"contract_test":{"status":"pass","last_tested_time":"last_tested_time","message":"message"},"schema":[{"name":"name","description":"description","physical_type":"physical_type","properties":[{"name":"name","type":{"type":"type","length":"length","scale":"scale","nullable":"nullable","signed":"signed","native_type":"native_type"}}]}]}],"domain":{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"parts_out":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"type":"data_asset"},"delivery_methods":[{"id":"09cf5fcc-cb9d-4995-a8e4-16517b25229f","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"getproperties":{"producer_input":{"engine_details":{"display_name":"Iceberg Engine","engine_id":"presto767","engine_port":"34567","engine_host":"a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud","associated_catalogs":["associated_catalogs"]}}}}]}],"workflows":{"order_access_request":{"task_assignee_users":["task_assignee_users"],"pre_approved_users":["pre_approved_users"],"custom_workflow_definition":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"}}},"dataview_enabled":true,"comments":"Comments by a producer that are provided either at the time of data product version creation or retiring","access_control":{"owner":"IBMid-696000KYV9"},"last_updated_at":"2019-01-01T12:00:00.000Z","is_restricted":false,"id":"2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd","asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"drafts":[{"version":"1.0.0","state":"draft","data_product":{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"name":"My Data Product","description":"This is a description of My Data Product.","tags":["tags"],"use_cases":[{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}],"types":["data"],"contract_terms":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"id":"id","documents":[{"url":"url","type":"terms_and_conditions","name":"name","id":"2b0bf220-079c-11ee-be56-0242ac120002","attachment":{"id":"id"},"upload_url":"upload_url"}],"error_msg":"error_msg","overview":{"api_version":"v3.0.1","kind":"DataContract","name":"Sample Data Contract","version":"0.0.0","domain":{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"more_info":"List of links to sources that provide more details on the data contract."},"description":{"purpose":"Used for customer behavior analysis.","limitations":"Data cannot be used for marketing.","usage":"Data should be used only for analytics.","more_info":[{"type":"privacy-statement","url":"https://moreinfo.example.com"}],"custom_properties":"{\\"property1\\":\\"value1\\"}"},"organization":[{"user_id":"IBMid-691000IN4G","role":"owner"}],"roles":[{"role":"owner"}],"price":{"amount":"100.0","currency":"USD","unit":"megabyte"},"sla":[{"default_element":"Standard SLA Policy","properties":[{"property":"Uptime Guarantee","value":"99.9"}]}],"support_and_communication":[{"channel":"Email Support","url":"https://support.example.com"}],"custom_properties":[{"key":"customPropertyKey","value":"customPropertyValue"}],"contract_test":{"status":"pass","last_tested_time":"last_tested_time","message":"message"},"schema":[{"name":"name","description":"description","physical_type":"physical_type","properties":[{"name":"name","type":{"type":"type","length":"length","scale":"scale","nullable":"nullable","signed":"signed","native_type":"native_type"}}]}]}],"domain":{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"parts_out":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"type":"data_asset"},"delivery_methods":[{"id":"09cf5fcc-cb9d-4995-a8e4-16517b25229f","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"getproperties":{"producer_input":{"engine_details":{"display_name":"Iceberg Engine","engine_id":"presto767","engine_port":"34567","engine_host":"a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud","associated_catalogs":["associated_catalogs"]}}}}]}],"workflows":{"order_access_request":{"task_assignee_users":["task_assignee_users"],"pre_approved_users":["pre_approved_users"],"custom_workflow_definition":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"}}},"dataview_enabled":true,"comments":"Comments by a producer that are provided either at the time of data product version creation or retiring","access_control":{"owner":"IBMid-696000KYV9"},"last_updated_at":"2019-01-01T12:00:00.000Z","is_restricted":false,"id":"2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd","asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

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
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"drafts":[{"version":"1.0.0","state":"draft","data_product":{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"name":"My Data Product","description":"This is a description of My Data Product.","tags":["tags"],"use_cases":[{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}],"types":["data"],"contract_terms":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"id":"id","documents":[{"url":"url","type":"terms_and_conditions","name":"name","id":"2b0bf220-079c-11ee-be56-0242ac120002","attachment":{"id":"id"},"upload_url":"upload_url"}],"error_msg":"error_msg","overview":{"api_version":"v3.0.1","kind":"DataContract","name":"Sample Data Contract","version":"0.0.0","domain":{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"more_info":"List of links to sources that provide more details on the data contract."},"description":{"purpose":"Used for customer behavior analysis.","limitations":"Data cannot be used for marketing.","usage":"Data should be used only for analytics.","more_info":[{"type":"privacy-statement","url":"https://moreinfo.example.com"}],"custom_properties":"{\\"property1\\":\\"value1\\"}"},"organization":[{"user_id":"IBMid-691000IN4G","role":"owner"}],"roles":[{"role":"owner"}],"price":{"amount":"100.0","currency":"USD","unit":"megabyte"},"sla":[{"default_element":"Standard SLA Policy","properties":[{"property":"Uptime Guarantee","value":"99.9"}]}],"support_and_communication":[{"channel":"Email Support","url":"https://support.example.com"}],"custom_properties":[{"key":"customPropertyKey","value":"customPropertyValue"}],"contract_test":{"status":"pass","last_tested_time":"last_tested_time","message":"message"},"schema":[{"name":"name","description":"description","physical_type":"physical_type","properties":[{"name":"name","type":{"type":"type","length":"length","scale":"scale","nullable":"nullable","signed":"signed","native_type":"native_type"}}]}]}],"domain":{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"parts_out":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"type":"data_asset"},"delivery_methods":[{"id":"09cf5fcc-cb9d-4995-a8e4-16517b25229f","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"getproperties":{"producer_input":{"engine_details":{"display_name":"Iceberg Engine","engine_id":"presto767","engine_port":"34567","engine_host":"a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud","associated_catalogs":["associated_catalogs"]}}}}]}],"workflows":{"order_access_request":{"task_assignee_users":["task_assignee_users"],"pre_approved_users":["pre_approved_users"],"custom_workflow_definition":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"}}},"dataview_enabled":true,"comments":"Comments by a producer that are provided either at the time of data product version creation or retiring","access_control":{"owner":"IBMid-696000KYV9"},"last_updated_at":"2019-01-01T12:00:00.000Z","is_restricted":false,"id":"2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd","asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"drafts":[{"version":"1.0.0","state":"draft","data_product":{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"name":"My Data Product","description":"This is a description of My Data Product.","tags":["tags"],"use_cases":[{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}],"types":["data"],"contract_terms":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"id":"id","documents":[{"url":"url","type":"terms_and_conditions","name":"name","id":"2b0bf220-079c-11ee-be56-0242ac120002","attachment":{"id":"id"},"upload_url":"upload_url"}],"error_msg":"error_msg","overview":{"api_version":"v3.0.1","kind":"DataContract","name":"Sample Data Contract","version":"0.0.0","domain":{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"more_info":"List of links to sources that provide more details on the data contract."},"description":{"purpose":"Used for customer behavior analysis.","limitations":"Data cannot be used for marketing.","usage":"Data should be used only for analytics.","more_info":[{"type":"privacy-statement","url":"https://moreinfo.example.com"}],"custom_properties":"{\\"property1\\":\\"value1\\"}"},"organization":[{"user_id":"IBMid-691000IN4G","role":"owner"}],"roles":[{"role":"owner"}],"price":{"amount":"100.0","currency":"USD","unit":"megabyte"},"sla":[{"default_element":"Standard SLA Policy","properties":[{"property":"Uptime Guarantee","value":"99.9"}]}],"support_and_communication":[{"channel":"Email Support","url":"https://support.example.com"}],"custom_properties":[{"key":"customPropertyKey","value":"customPropertyValue"}],"contract_test":{"status":"pass","last_tested_time":"last_tested_time","message":"message"},"schema":[{"name":"name","description":"description","physical_type":"physical_type","properties":[{"name":"name","type":{"type":"type","length":"length","scale":"scale","nullable":"nullable","signed":"signed","native_type":"native_type"}}]}]}],"domain":{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"parts_out":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"type":"data_asset"},"delivery_methods":[{"id":"09cf5fcc-cb9d-4995-a8e4-16517b25229f","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"getproperties":{"producer_input":{"engine_details":{"display_name":"Iceberg Engine","engine_id":"presto767","engine_port":"34567","engine_host":"a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud","associated_catalogs":["associated_catalogs"]}}}}]}],"workflows":{"order_access_request":{"task_assignee_users":["task_assignee_users"],"pre_approved_users":["pre_approved_users"],"custom_workflow_definition":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"}}},"dataview_enabled":true,"comments":"Comments by a producer that are provided either at the time of data product version creation or retiring","access_control":{"owner":"IBMid-696000KYV9"},"last_updated_at":"2019-01-01T12:00:00.000Z","is_restricted":false,"id":"2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd","asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

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
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "properties": {"anyKey": "anyValue"}, "visualization_errors": [{"visualization": {"id": "id", "name": "name"}, "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "related_asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "error": {"code": "code", "message": "message"}}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
        asset_reference_model['name'] = 'testString'
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

        # Construct a dict representation of a Domain model
        domain_model = {}
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = '0.0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        # Construct a dict representation of a ContractTermsMoreInfo model
        contract_terms_more_info_model = {}
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://moreinfo.example.com'

        # Construct a dict representation of a Description model
        description_model = {}
        description_model['purpose'] = 'Used for customer behavior analysis.'
        description_model['limitations'] = 'Data cannot be used for marketing.'
        description_model['usage'] = 'Data should be used only for analytics.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = '{"property1":"value1"}'

        # Construct a dict representation of a ContractTemplateOrganization model
        contract_template_organization_model = {}
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role'] = 'owner'

        # Construct a dict representation of a Pricing model
        pricing_model = {}
        pricing_model['amount'] = '100.0'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        # Construct a dict representation of a ContractTemplateSLAProperty model
        contract_template_sla_property_model = {}
        contract_template_sla_property_model['property'] = 'Uptime Guarantee'
        contract_template_sla_property_model['value'] = '99.9'

        # Construct a dict representation of a ContractTemplateSLA model
        contract_template_sla_model = {}
        contract_template_sla_model['default_element'] = 'Standard SLA Policy'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        # Construct a dict representation of a ContractTemplateSupportAndCommunication model
        contract_template_support_and_communication_model = {}
        contract_template_support_and_communication_model['channel'] = 'Email Support'
        contract_template_support_and_communication_model['url'] = 'https://support.example.com'

        # Construct a dict representation of a ContractTemplateCustomProperty model
        contract_template_custom_property_model = {}
        contract_template_custom_property_model['key'] = 'customPropertyKey'
        contract_template_custom_property_model['value'] = 'customPropertyValue'

        # Construct a dict representation of a ContractTest model
        contract_test_model = {}
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        # Construct a dict representation of a ContractSchemaPropertyType model
        contract_schema_property_type_model = {}
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        # Construct a dict representation of a ContractSchemaProperty model
        contract_schema_property_model = {}
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        # Construct a dict representation of a ContractSchema model
        contract_schema_model = {}
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        # Construct a dict representation of a ContractTerms model
        contract_terms_model = {}
        contract_terms_model['asset'] = asset_reference_model
        contract_terms_model['id'] = 'testString'
        contract_terms_model['documents'] = [contract_terms_document_model]
        contract_terms_model['error_msg'] = 'testString'
        contract_terms_model['overview'] = overview_model
        contract_terms_model['description'] = description_model
        contract_terms_model['organization'] = [contract_template_organization_model]
        contract_terms_model['roles'] = [roles_model]
        contract_terms_model['price'] = pricing_model
        contract_terms_model['sla'] = [contract_template_sla_model]
        contract_terms_model['support_and_communication'] = [contract_template_support_and_communication_model]
        contract_terms_model['custom_properties'] = [contract_template_custom_property_model]
        contract_terms_model['contract_test'] = contract_test_model
        contract_terms_model['schema'] = [contract_schema_model]

        # Construct a dict representation of a AssetPartReference model
        asset_part_reference_model = {}
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['name'] = 'testString'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        # Construct a dict representation of a EngineDetailsModel model
        engine_details_model_model = {}
        engine_details_model_model['display_name'] = 'Iceberg Engine'
        engine_details_model_model['engine_id'] = 'presto767'
        engine_details_model_model['engine_port'] = '34567'
        engine_details_model_model['engine_host'] = 'a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud'
        engine_details_model_model['associated_catalogs'] = ['testString']

        # Construct a dict representation of a ProducerInputModel model
        producer_input_model_model = {}
        producer_input_model_model['engine_details'] = engine_details_model_model

        # Construct a dict representation of a DeliveryMethodPropertiesModel model
        delivery_method_properties_model_model = {}
        delivery_method_properties_model_model['producer_input'] = producer_input_model_model

        # Construct a dict representation of a DeliveryMethod model
        delivery_method_model = {}
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model
        delivery_method_model['getproperties'] = delivery_method_properties_model_model

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
        data_product_order_access_request_model['custom_workflow_definition'] = data_product_custom_workflow_definition_model

        # Construct a dict representation of a DataProductWorkflows model
        data_product_workflows_model = {}
        data_product_workflows_model['order_access_request'] = data_product_order_access_request_model

        # Construct a dict representation of a AssetListAccessControl model
        asset_list_access_control_model = {}
        asset_list_access_control_model['owner'] = 'IBMid-696000KYV9'

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
        contract_terms = [contract_terms_model]
        domain = domain_model
        parts_out = [data_product_part_model]
        workflows = data_product_workflows_model
        dataview_enabled = True
        comments = 'testString'
        access_control = asset_list_access_control_model
        last_updated_at = string_to_datetime('2019-01-01T12:00:00.000Z')
        is_restricted = True

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
            domain=domain,
            parts_out=parts_out,
            workflows=workflows,
            dataview_enabled=dataview_enabled,
            comments=comments,
            access_control=access_control,
            last_updated_at=last_updated_at,
            is_restricted=is_restricted,
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
        assert req_body['contract_terms'] == [contract_terms_model]
        assert req_body['domain'] == domain_model
        assert req_body['parts_out'] == [data_product_part_model]
        assert req_body['workflows'] == data_product_workflows_model
        assert req_body['dataview_enabled'] == True
        assert req_body['comments'] == 'testString'
        assert req_body['access_control'] == asset_list_access_control_model
        assert req_body['last_updated_at'] == '2019-01-01T12:00:00Z'
        assert req_body['is_restricted'] == True

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
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "properties": {"anyKey": "anyValue"}, "visualization_errors": [{"visualization": {"id": "id", "name": "name"}, "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "related_asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "error": {"code": "code", "message": "message"}}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
        asset_reference_model['name'] = 'testString'
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

        # Construct a dict representation of a Domain model
        domain_model = {}
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = '0.0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        # Construct a dict representation of a ContractTermsMoreInfo model
        contract_terms_more_info_model = {}
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://moreinfo.example.com'

        # Construct a dict representation of a Description model
        description_model = {}
        description_model['purpose'] = 'Used for customer behavior analysis.'
        description_model['limitations'] = 'Data cannot be used for marketing.'
        description_model['usage'] = 'Data should be used only for analytics.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = '{"property1":"value1"}'

        # Construct a dict representation of a ContractTemplateOrganization model
        contract_template_organization_model = {}
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role'] = 'owner'

        # Construct a dict representation of a Pricing model
        pricing_model = {}
        pricing_model['amount'] = '100.0'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        # Construct a dict representation of a ContractTemplateSLAProperty model
        contract_template_sla_property_model = {}
        contract_template_sla_property_model['property'] = 'Uptime Guarantee'
        contract_template_sla_property_model['value'] = '99.9'

        # Construct a dict representation of a ContractTemplateSLA model
        contract_template_sla_model = {}
        contract_template_sla_model['default_element'] = 'Standard SLA Policy'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        # Construct a dict representation of a ContractTemplateSupportAndCommunication model
        contract_template_support_and_communication_model = {}
        contract_template_support_and_communication_model['channel'] = 'Email Support'
        contract_template_support_and_communication_model['url'] = 'https://support.example.com'

        # Construct a dict representation of a ContractTemplateCustomProperty model
        contract_template_custom_property_model = {}
        contract_template_custom_property_model['key'] = 'customPropertyKey'
        contract_template_custom_property_model['value'] = 'customPropertyValue'

        # Construct a dict representation of a ContractTest model
        contract_test_model = {}
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        # Construct a dict representation of a ContractSchemaPropertyType model
        contract_schema_property_type_model = {}
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        # Construct a dict representation of a ContractSchemaProperty model
        contract_schema_property_model = {}
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        # Construct a dict representation of a ContractSchema model
        contract_schema_model = {}
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        # Construct a dict representation of a ContractTerms model
        contract_terms_model = {}
        contract_terms_model['asset'] = asset_reference_model
        contract_terms_model['id'] = 'testString'
        contract_terms_model['documents'] = [contract_terms_document_model]
        contract_terms_model['error_msg'] = 'testString'
        contract_terms_model['overview'] = overview_model
        contract_terms_model['description'] = description_model
        contract_terms_model['organization'] = [contract_template_organization_model]
        contract_terms_model['roles'] = [roles_model]
        contract_terms_model['price'] = pricing_model
        contract_terms_model['sla'] = [contract_template_sla_model]
        contract_terms_model['support_and_communication'] = [contract_template_support_and_communication_model]
        contract_terms_model['custom_properties'] = [contract_template_custom_property_model]
        contract_terms_model['contract_test'] = contract_test_model
        contract_terms_model['schema'] = [contract_schema_model]

        # Construct a dict representation of a AssetPartReference model
        asset_part_reference_model = {}
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['name'] = 'testString'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        # Construct a dict representation of a EngineDetailsModel model
        engine_details_model_model = {}
        engine_details_model_model['display_name'] = 'Iceberg Engine'
        engine_details_model_model['engine_id'] = 'presto767'
        engine_details_model_model['engine_port'] = '34567'
        engine_details_model_model['engine_host'] = 'a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud'
        engine_details_model_model['associated_catalogs'] = ['testString']

        # Construct a dict representation of a ProducerInputModel model
        producer_input_model_model = {}
        producer_input_model_model['engine_details'] = engine_details_model_model

        # Construct a dict representation of a DeliveryMethodPropertiesModel model
        delivery_method_properties_model_model = {}
        delivery_method_properties_model_model['producer_input'] = producer_input_model_model

        # Construct a dict representation of a DeliveryMethod model
        delivery_method_model = {}
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model
        delivery_method_model['getproperties'] = delivery_method_properties_model_model

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
        data_product_order_access_request_model['custom_workflow_definition'] = data_product_custom_workflow_definition_model

        # Construct a dict representation of a DataProductWorkflows model
        data_product_workflows_model = {}
        data_product_workflows_model['order_access_request'] = data_product_order_access_request_model

        # Construct a dict representation of a AssetListAccessControl model
        asset_list_access_control_model = {}
        asset_list_access_control_model['owner'] = 'IBMid-696000KYV9'

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
        contract_terms = [contract_terms_model]
        domain = domain_model
        parts_out = [data_product_part_model]
        workflows = data_product_workflows_model
        dataview_enabled = True
        comments = 'testString'
        access_control = asset_list_access_control_model
        last_updated_at = string_to_datetime('2019-01-01T12:00:00.000Z')
        is_restricted = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_product_id": data_product_id,
            "asset": asset,
        }
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
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString/documents')
        mock_response = '{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'
        contract_terms_id = 'testString'
        type = 'terms_and_conditions'
        name = 'Terms and conditions document'
        url = 'testString'

        # Invoke method
        response = _service.create_draft_contract_terms_document(
            data_product_id,
            draft_id,
            contract_terms_id,
            type,
            name,
            url=url,
            headers={},
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
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString/documents')
        mock_response = '{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "properties": {"anyKey": "anyValue"}, "visualization_errors": [{"visualization": {"id": "id", "name": "name"}, "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "related_asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "error": {"code": "code", "message": "message"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'

        # Invoke method
        response = _service.get_data_product_draft(
            data_product_id,
            draft_id,
            headers={},
        )

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
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "properties": {"anyKey": "anyValue"}, "visualization_errors": [{"visualization": {"id": "id", "name": "name"}, "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "related_asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "error": {"code": "code", "message": "message"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_product_id": data_product_id,
            "draft_id": draft_id,
        }
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
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'

        # Invoke method
        response = _service.delete_data_product_draft(
            data_product_id,
            draft_id,
            headers={},
        )

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
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_product_id": data_product_id,
            "draft_id": draft_id,
        }
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
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "properties": {"anyKey": "anyValue"}, "visualization_errors": [{"visualization": {"id": "id", "name": "name"}, "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "related_asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "error": {"code": "code", "message": "message"}}]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
        response = _service.update_data_product_draft(
            data_product_id,
            draft_id,
            json_patch_instructions,
            headers={},
        )

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
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "properties": {"anyKey": "anyValue"}, "visualization_errors": [{"visualization": {"id": "id", "name": "name"}, "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "related_asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "error": {"code": "code", "message": "message"}}]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString/documents/testString')
        mock_response = '{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'
        contract_terms_id = 'testString'
        document_id = 'testString'

        # Invoke method
        response = _service.get_draft_contract_terms_document(
            data_product_id,
            draft_id,
            contract_terms_id,
            document_id,
            headers={},
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
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString/documents/testString')
        mock_response = '{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString/documents/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'
        contract_terms_id = 'testString'
        document_id = 'testString'

        # Invoke method
        response = _service.delete_draft_contract_terms_document(
            data_product_id,
            draft_id,
            contract_terms_id,
            document_id,
            headers={},
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
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString/documents/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

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
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString/documents/testString')
        mock_response = '{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
            data_product_id,
            draft_id,
            contract_terms_id,
            document_id,
            json_patch_instructions,
            headers={},
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
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString/documents/testString')
        mock_response = '{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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


class TestGetDataProductDraftContractTerms:
    """
    Test Class for get_data_product_draft_contract_terms
    """

    @responses.activate
    def test_get_data_product_draft_contract_terms_all_params(self):
        """
        get_data_product_draft_contract_terms()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/odcs+yaml',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'
        contract_terms_id = 'testString'
        accept = 'application/odcs+yaml'
        include_contract_documents = True

        # Invoke method
        response = _service.get_data_product_draft_contract_terms(
            data_product_id,
            draft_id,
            contract_terms_id,
            accept=accept,
            include_contract_documents=include_contract_documents,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_contract_documents={}'.format('true' if include_contract_documents else 'false') in query_string

    def test_get_data_product_draft_contract_terms_all_params_with_retries(self):
        # Enable retries and run test_get_data_product_draft_contract_terms_all_params.
        _service.enable_retries()
        self.test_get_data_product_draft_contract_terms_all_params()

        # Disable retries and run test_get_data_product_draft_contract_terms_all_params.
        _service.disable_retries()
        self.test_get_data_product_draft_contract_terms_all_params()

    @responses.activate
    def test_get_data_product_draft_contract_terms_required_params(self):
        """
        test_get_data_product_draft_contract_terms_required_params()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/odcs+yaml',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'
        contract_terms_id = 'testString'

        # Invoke method
        response = _service.get_data_product_draft_contract_terms(
            data_product_id,
            draft_id,
            contract_terms_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_data_product_draft_contract_terms_required_params_with_retries(self):
        # Enable retries and run test_get_data_product_draft_contract_terms_required_params.
        _service.enable_retries()
        self.test_get_data_product_draft_contract_terms_required_params()

        # Disable retries and run test_get_data_product_draft_contract_terms_required_params.
        _service.disable_retries()
        self.test_get_data_product_draft_contract_terms_required_params()

    @responses.activate
    def test_get_data_product_draft_contract_terms_value_error(self):
        """
        test_get_data_product_draft_contract_terms_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/odcs+yaml',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'
        contract_terms_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_product_id": data_product_id,
            "draft_id": draft_id,
            "contract_terms_id": contract_terms_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_data_product_draft_contract_terms(**req_copy)

    def test_get_data_product_draft_contract_terms_value_error_with_retries(self):
        # Enable retries and run test_get_data_product_draft_contract_terms_value_error.
        _service.enable_retries()
        self.test_get_data_product_draft_contract_terms_value_error()

        # Disable retries and run test_get_data_product_draft_contract_terms_value_error.
        _service.disable_retries()
        self.test_get_data_product_draft_contract_terms_value_error()


class TestReplaceDataProductDraftContractTerms:
    """
    Test Class for replace_data_product_draft_contract_terms
    """

    @responses.activate
    def test_replace_data_product_draft_contract_terms_all_params(self):
        """
        replace_data_product_draft_contract_terms()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString')
        mock_response = '{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {}
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Construct a dict representation of a AssetReference model
        asset_reference_model = {}
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['name'] = 'testString'
        asset_reference_model['container'] = container_reference_model

        # Construct a dict representation of a ContractTermsDocumentAttachment model
        contract_terms_document_attachment_model = {}
        contract_terms_document_attachment_model['id'] = 'testString'

        # Construct a dict representation of a ContractTermsDocument model
        contract_terms_document_model = {}
        contract_terms_document_model['url'] = 'https://ibm.com/document'
        contract_terms_document_model['type'] = 'terms_and_conditions'
        contract_terms_document_model['name'] = 'Terms and Conditions'
        contract_terms_document_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        contract_terms_document_model['attachment'] = contract_terms_document_attachment_model
        contract_terms_document_model['upload_url'] = 'testString'

        # Construct a dict representation of a Domain model
        domain_model = {}
        domain_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        domain_model['name'] = 'domain_name'
        domain_model['container'] = container_reference_model

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = 'v0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        # Construct a dict representation of a ContractTermsMoreInfo model
        contract_terms_more_info_model = {}
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://www.moreinfo.example.coms'

        # Construct a dict representation of a Description model
        description_model = {}
        description_model['purpose'] = 'Intended purpose for the provided data.'
        description_model['limitations'] = 'Technical, compliance, and legal limitations for data use.'
        description_model['usage'] = 'Recommended usage of the data.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = 'Custom properties that are not part of the standard.'

        # Construct a dict representation of a ContractTemplateOrganization model
        contract_template_organization_model = {}
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role'] = 'IAM Role'

        # Construct a dict representation of a Pricing model
        pricing_model = {}
        pricing_model['amount'] = '100.0'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        # Construct a dict representation of a ContractTemplateSLAProperty model
        contract_template_sla_property_model = {}
        contract_template_sla_property_model['property'] = 'slaproperty'
        contract_template_sla_property_model['value'] = 'slavalue'

        # Construct a dict representation of a ContractTemplateSLA model
        contract_template_sla_model = {}
        contract_template_sla_model['default_element'] = 'sladefaultelement'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        # Construct a dict representation of a ContractTemplateSupportAndCommunication model
        contract_template_support_and_communication_model = {}
        contract_template_support_and_communication_model['channel'] = 'channel'
        contract_template_support_and_communication_model['url'] = 'https://www.example.coms'

        # Construct a dict representation of a ContractTemplateCustomProperty model
        contract_template_custom_property_model = {}
        contract_template_custom_property_model['key'] = 'The name of the key.'
        contract_template_custom_property_model['value'] = 'The value of the key.'

        # Construct a dict representation of a ContractTest model
        contract_test_model = {}
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        # Construct a dict representation of a ContractSchemaPropertyType model
        contract_schema_property_type_model = {}
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        # Construct a dict representation of a ContractSchemaProperty model
        contract_schema_property_model = {}
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        # Construct a dict representation of a ContractSchema model
        contract_schema_model = {}
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'
        contract_terms_id = 'testString'
        asset = asset_reference_model
        id = 'testString'
        documents = [contract_terms_document_model]
        error_msg = 'testString'
        overview = overview_model
        description = description_model
        organization = [contract_template_organization_model]
        roles = [roles_model]
        price = pricing_model
        sla = [contract_template_sla_model]
        support_and_communication = [contract_template_support_and_communication_model]
        custom_properties = [contract_template_custom_property_model]
        contract_test = contract_test_model
        schema = [contract_schema_model]

        # Invoke method
        response = _service.replace_data_product_draft_contract_terms(
            data_product_id,
            draft_id,
            contract_terms_id,
            asset=asset,
            id=id,
            documents=documents,
            error_msg=error_msg,
            overview=overview,
            description=description,
            organization=organization,
            roles=roles,
            price=price,
            sla=sla,
            support_and_communication=support_and_communication,
            custom_properties=custom_properties,
            contract_test=contract_test,
            schema=schema,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['asset'] == asset_reference_model
        assert req_body['id'] == 'testString'
        assert req_body['documents'] == [contract_terms_document_model]
        assert req_body['error_msg'] == 'testString'
        assert req_body['overview'] == overview_model
        assert req_body['description'] == description_model
        assert req_body['organization'] == [contract_template_organization_model]
        assert req_body['roles'] == [roles_model]
        assert req_body['price'] == pricing_model
        assert req_body['sla'] == [contract_template_sla_model]
        assert req_body['support_and_communication'] == [contract_template_support_and_communication_model]
        assert req_body['custom_properties'] == [contract_template_custom_property_model]
        assert req_body['contract_test'] == contract_test_model
        assert req_body['schema'] == [contract_schema_model]

    def test_replace_data_product_draft_contract_terms_all_params_with_retries(self):
        # Enable retries and run test_replace_data_product_draft_contract_terms_all_params.
        _service.enable_retries()
        self.test_replace_data_product_draft_contract_terms_all_params()

        # Disable retries and run test_replace_data_product_draft_contract_terms_all_params.
        _service.disable_retries()
        self.test_replace_data_product_draft_contract_terms_all_params()

    @responses.activate
    def test_replace_data_product_draft_contract_terms_value_error(self):
        """
        test_replace_data_product_draft_contract_terms_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString')
        mock_response = '{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {}
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Construct a dict representation of a AssetReference model
        asset_reference_model = {}
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['name'] = 'testString'
        asset_reference_model['container'] = container_reference_model

        # Construct a dict representation of a ContractTermsDocumentAttachment model
        contract_terms_document_attachment_model = {}
        contract_terms_document_attachment_model['id'] = 'testString'

        # Construct a dict representation of a ContractTermsDocument model
        contract_terms_document_model = {}
        contract_terms_document_model['url'] = 'https://ibm.com/document'
        contract_terms_document_model['type'] = 'terms_and_conditions'
        contract_terms_document_model['name'] = 'Terms and Conditions'
        contract_terms_document_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        contract_terms_document_model['attachment'] = contract_terms_document_attachment_model
        contract_terms_document_model['upload_url'] = 'testString'

        # Construct a dict representation of a Domain model
        domain_model = {}
        domain_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        domain_model['name'] = 'domain_name'
        domain_model['container'] = container_reference_model

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = 'v0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        # Construct a dict representation of a ContractTermsMoreInfo model
        contract_terms_more_info_model = {}
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://www.moreinfo.example.coms'

        # Construct a dict representation of a Description model
        description_model = {}
        description_model['purpose'] = 'Intended purpose for the provided data.'
        description_model['limitations'] = 'Technical, compliance, and legal limitations for data use.'
        description_model['usage'] = 'Recommended usage of the data.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = 'Custom properties that are not part of the standard.'

        # Construct a dict representation of a ContractTemplateOrganization model
        contract_template_organization_model = {}
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role'] = 'IAM Role'

        # Construct a dict representation of a Pricing model
        pricing_model = {}
        pricing_model['amount'] = '100.0'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        # Construct a dict representation of a ContractTemplateSLAProperty model
        contract_template_sla_property_model = {}
        contract_template_sla_property_model['property'] = 'slaproperty'
        contract_template_sla_property_model['value'] = 'slavalue'

        # Construct a dict representation of a ContractTemplateSLA model
        contract_template_sla_model = {}
        contract_template_sla_model['default_element'] = 'sladefaultelement'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        # Construct a dict representation of a ContractTemplateSupportAndCommunication model
        contract_template_support_and_communication_model = {}
        contract_template_support_and_communication_model['channel'] = 'channel'
        contract_template_support_and_communication_model['url'] = 'https://www.example.coms'

        # Construct a dict representation of a ContractTemplateCustomProperty model
        contract_template_custom_property_model = {}
        contract_template_custom_property_model['key'] = 'The name of the key.'
        contract_template_custom_property_model['value'] = 'The value of the key.'

        # Construct a dict representation of a ContractTest model
        contract_test_model = {}
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        # Construct a dict representation of a ContractSchemaPropertyType model
        contract_schema_property_type_model = {}
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        # Construct a dict representation of a ContractSchemaProperty model
        contract_schema_property_model = {}
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        # Construct a dict representation of a ContractSchema model
        contract_schema_model = {}
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'
        contract_terms_id = 'testString'
        asset = asset_reference_model
        id = 'testString'
        documents = [contract_terms_document_model]
        error_msg = 'testString'
        overview = overview_model
        description = description_model
        organization = [contract_template_organization_model]
        roles = [roles_model]
        price = pricing_model
        sla = [contract_template_sla_model]
        support_and_communication = [contract_template_support_and_communication_model]
        custom_properties = [contract_template_custom_property_model]
        contract_test = contract_test_model
        schema = [contract_schema_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_product_id": data_product_id,
            "draft_id": draft_id,
            "contract_terms_id": contract_terms_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_data_product_draft_contract_terms(**req_copy)

    def test_replace_data_product_draft_contract_terms_value_error_with_retries(self):
        # Enable retries and run test_replace_data_product_draft_contract_terms_value_error.
        _service.enable_retries()
        self.test_replace_data_product_draft_contract_terms_value_error()

        # Disable retries and run test_replace_data_product_draft_contract_terms_value_error.
        _service.disable_retries()
        self.test_replace_data_product_draft_contract_terms_value_error()


class TestUpdateDataProductDraftContractTerms:
    """
    Test Class for update_data_product_draft_contract_terms
    """

    @responses.activate
    def test_update_data_product_draft_contract_terms_all_params(self):
        """
        update_data_product_draft_contract_terms()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString')
        mock_response = '{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
        json_patch_instructions = [json_patch_operation_model]

        # Invoke method
        response = _service.update_data_product_draft_contract_terms(
            data_product_id,
            draft_id,
            contract_terms_id,
            json_patch_instructions,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == json_patch_instructions

    def test_update_data_product_draft_contract_terms_all_params_with_retries(self):
        # Enable retries and run test_update_data_product_draft_contract_terms_all_params.
        _service.enable_retries()
        self.test_update_data_product_draft_contract_terms_all_params()

        # Disable retries and run test_update_data_product_draft_contract_terms_all_params.
        _service.disable_retries()
        self.test_update_data_product_draft_contract_terms_all_params()

    @responses.activate
    def test_update_data_product_draft_contract_terms_value_error(self):
        """
        test_update_data_product_draft_contract_terms_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/drafts/testString/contract_terms/testString')
        mock_response = '{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
        json_patch_instructions = [json_patch_operation_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_product_id": data_product_id,
            "draft_id": draft_id,
            "contract_terms_id": contract_terms_id,
            "json_patch_instructions": json_patch_instructions,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_data_product_draft_contract_terms(**req_copy)

    def test_update_data_product_draft_contract_terms_value_error_with_retries(self):
        # Enable retries and run test_update_data_product_draft_contract_terms_value_error.
        _service.enable_retries()
        self.test_update_data_product_draft_contract_terms_value_error()

        # Disable retries and run test_update_data_product_draft_contract_terms_value_error.
        _service.disable_retries()
        self.test_update_data_product_draft_contract_terms_value_error()


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
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "properties": {"anyKey": "anyValue"}, "visualization_errors": [{"visualization": {"id": "id", "name": "name"}, "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "related_asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "error": {"code": "code", "message": "message"}}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'

        # Invoke method
        response = _service.publish_data_product_draft(
            data_product_id,
            draft_id,
            headers={},
        )

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
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "properties": {"anyKey": "anyValue"}, "visualization_errors": [{"visualization": {"id": "id", "name": "name"}, "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "related_asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "error": {"code": "code", "message": "message"}}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'
        draft_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_product_id": data_product_id,
            "draft_id": draft_id,
        }
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

        service = DphV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DphV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DphV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


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
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "properties": {"anyKey": "anyValue"}, "visualization_errors": [{"visualization": {"id": "id", "name": "name"}, "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "related_asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "error": {"code": "code", "message": "message"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'
        release_id = 'testString'
        check_caller_approval = False

        # Invoke method
        response = _service.get_data_product_release(
            data_product_id,
            release_id,
            check_caller_approval=check_caller_approval,
            headers={},
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
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "properties": {"anyKey": "anyValue"}, "visualization_errors": [{"visualization": {"id": "id", "name": "name"}, "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "related_asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "error": {"code": "code", "message": "message"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'
        release_id = 'testString'

        # Invoke method
        response = _service.get_data_product_release(
            data_product_id,
            release_id,
            headers={},
        )

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
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "properties": {"anyKey": "anyValue"}, "visualization_errors": [{"visualization": {"id": "id", "name": "name"}, "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "related_asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "error": {"code": "code", "message": "message"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'
        release_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_product_id": data_product_id,
            "release_id": release_id,
        }
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
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "properties": {"anyKey": "anyValue"}, "visualization_errors": [{"visualization": {"id": "id", "name": "name"}, "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "related_asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "error": {"code": "code", "message": "message"}}]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
            data_product_id,
            release_id,
            json_patch_instructions,
            headers={},
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
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "properties": {"anyKey": "anyValue"}, "visualization_errors": [{"visualization": {"id": "id", "name": "name"}, "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "related_asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "error": {"code": "code", "message": "message"}}]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/releases/testString/contract_terms/testString/documents/testString')
        mock_response = '{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'
        release_id = 'testString'
        contract_terms_id = 'testString'
        document_id = 'testString'

        # Invoke method
        response = _service.get_release_contract_terms_document(
            data_product_id,
            release_id,
            contract_terms_id,
            document_id,
            headers={},
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
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/releases/testString/contract_terms/testString/documents/testString')
        mock_response = '{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
        mock_response = '{"limit": 200, "first": {"href": "https://api.example.com/collection"}, "next": {"href": "https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "total_results": 200, "releases": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
        mock_response = '{"limit": 200, "first": {"href": "https://api.example.com/collection"}, "next": {"href": "https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "total_results": 200, "releases": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'

        # Invoke method
        response = _service.list_data_product_releases(
            data_product_id,
            headers={},
        )

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
        mock_response = '{"limit": 200, "first": {"href": "https://api.example.com/collection"}, "next": {"href": "https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "total_results": 200, "releases": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_product_id": data_product_id,
        }
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
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"releases":[{"version":"1.0.0","state":"draft","data_product":{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"name":"My Data Product","description":"This is a description of My Data Product.","tags":["tags"],"use_cases":[{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}],"types":["data"],"contract_terms":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"id":"id","documents":[{"url":"url","type":"terms_and_conditions","name":"name","id":"2b0bf220-079c-11ee-be56-0242ac120002","attachment":{"id":"id"},"upload_url":"upload_url"}],"error_msg":"error_msg","overview":{"api_version":"v3.0.1","kind":"DataContract","name":"Sample Data Contract","version":"0.0.0","domain":{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"more_info":"List of links to sources that provide more details on the data contract."},"description":{"purpose":"Used for customer behavior analysis.","limitations":"Data cannot be used for marketing.","usage":"Data should be used only for analytics.","more_info":[{"type":"privacy-statement","url":"https://moreinfo.example.com"}],"custom_properties":"{\\"property1\\":\\"value1\\"}"},"organization":[{"user_id":"IBMid-691000IN4G","role":"owner"}],"roles":[{"role":"owner"}],"price":{"amount":"100.0","currency":"USD","unit":"megabyte"},"sla":[{"default_element":"Standard SLA Policy","properties":[{"property":"Uptime Guarantee","value":"99.9"}]}],"support_and_communication":[{"channel":"Email Support","url":"https://support.example.com"}],"custom_properties":[{"key":"customPropertyKey","value":"customPropertyValue"}],"contract_test":{"status":"pass","last_tested_time":"last_tested_time","message":"message"},"schema":[{"name":"name","description":"description","physical_type":"physical_type","properties":[{"name":"name","type":{"type":"type","length":"length","scale":"scale","nullable":"nullable","signed":"signed","native_type":"native_type"}}]}]}],"domain":{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"parts_out":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"type":"data_asset"},"delivery_methods":[{"id":"09cf5fcc-cb9d-4995-a8e4-16517b25229f","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"getproperties":{"producer_input":{"engine_details":{"display_name":"Iceberg Engine","engine_id":"presto767","engine_port":"34567","engine_host":"a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud","associated_catalogs":["associated_catalogs"]}}}}]}],"workflows":{"order_access_request":{"task_assignee_users":["task_assignee_users"],"pre_approved_users":["pre_approved_users"],"custom_workflow_definition":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"}}},"dataview_enabled":true,"comments":"Comments by a producer that are provided either at the time of data product version creation or retiring","access_control":{"owner":"IBMid-696000KYV9"},"last_updated_at":"2019-01-01T12:00:00.000Z","is_restricted":false,"id":"2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd","asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"releases":[{"version":"1.0.0","state":"draft","data_product":{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"name":"My Data Product","description":"This is a description of My Data Product.","tags":["tags"],"use_cases":[{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}],"types":["data"],"contract_terms":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"id":"id","documents":[{"url":"url","type":"terms_and_conditions","name":"name","id":"2b0bf220-079c-11ee-be56-0242ac120002","attachment":{"id":"id"},"upload_url":"upload_url"}],"error_msg":"error_msg","overview":{"api_version":"v3.0.1","kind":"DataContract","name":"Sample Data Contract","version":"0.0.0","domain":{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"more_info":"List of links to sources that provide more details on the data contract."},"description":{"purpose":"Used for customer behavior analysis.","limitations":"Data cannot be used for marketing.","usage":"Data should be used only for analytics.","more_info":[{"type":"privacy-statement","url":"https://moreinfo.example.com"}],"custom_properties":"{\\"property1\\":\\"value1\\"}"},"organization":[{"user_id":"IBMid-691000IN4G","role":"owner"}],"roles":[{"role":"owner"}],"price":{"amount":"100.0","currency":"USD","unit":"megabyte"},"sla":[{"default_element":"Standard SLA Policy","properties":[{"property":"Uptime Guarantee","value":"99.9"}]}],"support_and_communication":[{"channel":"Email Support","url":"https://support.example.com"}],"custom_properties":[{"key":"customPropertyKey","value":"customPropertyValue"}],"contract_test":{"status":"pass","last_tested_time":"last_tested_time","message":"message"},"schema":[{"name":"name","description":"description","physical_type":"physical_type","properties":[{"name":"name","type":{"type":"type","length":"length","scale":"scale","nullable":"nullable","signed":"signed","native_type":"native_type"}}]}]}],"domain":{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"parts_out":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"type":"data_asset"},"delivery_methods":[{"id":"09cf5fcc-cb9d-4995-a8e4-16517b25229f","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"getproperties":{"producer_input":{"engine_details":{"display_name":"Iceberg Engine","engine_id":"presto767","engine_port":"34567","engine_host":"a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud","associated_catalogs":["associated_catalogs"]}}}}]}],"workflows":{"order_access_request":{"task_assignee_users":["task_assignee_users"],"pre_approved_users":["pre_approved_users"],"custom_workflow_definition":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"}}},"dataview_enabled":true,"comments":"Comments by a producer that are provided either at the time of data product version creation or retiring","access_control":{"owner":"IBMid-696000KYV9"},"last_updated_at":"2019-01-01T12:00:00.000Z","is_restricted":false,"id":"2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd","asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

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
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"releases":[{"version":"1.0.0","state":"draft","data_product":{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"name":"My Data Product","description":"This is a description of My Data Product.","tags":["tags"],"use_cases":[{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}],"types":["data"],"contract_terms":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"id":"id","documents":[{"url":"url","type":"terms_and_conditions","name":"name","id":"2b0bf220-079c-11ee-be56-0242ac120002","attachment":{"id":"id"},"upload_url":"upload_url"}],"error_msg":"error_msg","overview":{"api_version":"v3.0.1","kind":"DataContract","name":"Sample Data Contract","version":"0.0.0","domain":{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"more_info":"List of links to sources that provide more details on the data contract."},"description":{"purpose":"Used for customer behavior analysis.","limitations":"Data cannot be used for marketing.","usage":"Data should be used only for analytics.","more_info":[{"type":"privacy-statement","url":"https://moreinfo.example.com"}],"custom_properties":"{\\"property1\\":\\"value1\\"}"},"organization":[{"user_id":"IBMid-691000IN4G","role":"owner"}],"roles":[{"role":"owner"}],"price":{"amount":"100.0","currency":"USD","unit":"megabyte"},"sla":[{"default_element":"Standard SLA Policy","properties":[{"property":"Uptime Guarantee","value":"99.9"}]}],"support_and_communication":[{"channel":"Email Support","url":"https://support.example.com"}],"custom_properties":[{"key":"customPropertyKey","value":"customPropertyValue"}],"contract_test":{"status":"pass","last_tested_time":"last_tested_time","message":"message"},"schema":[{"name":"name","description":"description","physical_type":"physical_type","properties":[{"name":"name","type":{"type":"type","length":"length","scale":"scale","nullable":"nullable","signed":"signed","native_type":"native_type"}}]}]}],"domain":{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"parts_out":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"type":"data_asset"},"delivery_methods":[{"id":"09cf5fcc-cb9d-4995-a8e4-16517b25229f","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"getproperties":{"producer_input":{"engine_details":{"display_name":"Iceberg Engine","engine_id":"presto767","engine_port":"34567","engine_host":"a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud","associated_catalogs":["associated_catalogs"]}}}}]}],"workflows":{"order_access_request":{"task_assignee_users":["task_assignee_users"],"pre_approved_users":["pre_approved_users"],"custom_workflow_definition":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"}}},"dataview_enabled":true,"comments":"Comments by a producer that are provided either at the time of data product version creation or retiring","access_control":{"owner":"IBMid-696000KYV9"},"last_updated_at":"2019-01-01T12:00:00.000Z","is_restricted":false,"id":"2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd","asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"releases":[{"version":"1.0.0","state":"draft","data_product":{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","release":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"},"container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"name":"My Data Product","description":"This is a description of My Data Product.","tags":["tags"],"use_cases":[{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}],"types":["data"],"contract_terms":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"id":"id","documents":[{"url":"url","type":"terms_and_conditions","name":"name","id":"2b0bf220-079c-11ee-be56-0242ac120002","attachment":{"id":"id"},"upload_url":"upload_url"}],"error_msg":"error_msg","overview":{"api_version":"v3.0.1","kind":"DataContract","name":"Sample Data Contract","version":"0.0.0","domain":{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"more_info":"List of links to sources that provide more details on the data contract."},"description":{"purpose":"Used for customer behavior analysis.","limitations":"Data cannot be used for marketing.","usage":"Data should be used only for analytics.","more_info":[{"type":"privacy-statement","url":"https://moreinfo.example.com"}],"custom_properties":"{\\"property1\\":\\"value1\\"}"},"organization":[{"user_id":"IBMid-691000IN4G","role":"owner"}],"roles":[{"role":"owner"}],"price":{"amount":"100.0","currency":"USD","unit":"megabyte"},"sla":[{"default_element":"Standard SLA Policy","properties":[{"property":"Uptime Guarantee","value":"99.9"}]}],"support_and_communication":[{"channel":"Email Support","url":"https://support.example.com"}],"custom_properties":[{"key":"customPropertyKey","value":"customPropertyValue"}],"contract_test":{"status":"pass","last_tested_time":"last_tested_time","message":"message"},"schema":[{"name":"name","description":"description","physical_type":"physical_type","properties":[{"name":"name","type":{"type":"type","length":"length","scale":"scale","nullable":"nullable","signed":"signed","native_type":"native_type"}}]}]}],"domain":{"id":"id","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}},"parts_out":[{"asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"type":"data_asset"},"delivery_methods":[{"id":"09cf5fcc-cb9d-4995-a8e4-16517b25229f","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"getproperties":{"producer_input":{"engine_details":{"display_name":"Iceberg Engine","engine_id":"presto767","engine_port":"34567","engine_host":"a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud","associated_catalogs":["associated_catalogs"]}}}}]}],"workflows":{"order_access_request":{"task_assignee_users":["task_assignee_users"],"pre_approved_users":["pre_approved_users"],"custom_workflow_definition":{"id":"18bdbde1-918e-4ecf-aa23-6727bf319e14"}}},"dataview_enabled":true,"comments":"Comments by a producer that are provided either at the time of data product version creation or retiring","access_control":{"owner":"IBMid-696000KYV9"},"last_updated_at":"2019-01-01T12:00:00.000Z","is_restricted":false,"id":"2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd","asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","name":"name","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

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
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "properties": {"anyKey": "anyValue"}, "visualization_errors": [{"visualization": {"id": "id", "name": "name"}, "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "related_asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "error": {"code": "code", "message": "message"}}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'
        release_id = 'testString'
        revoke_access = False

        # Invoke method
        response = _service.retire_data_product_release(
            data_product_id,
            release_id,
            revoke_access=revoke_access,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'revoke_access={}'.format('true' if revoke_access else 'false') in query_string

    def test_retire_data_product_release_all_params_with_retries(self):
        # Enable retries and run test_retire_data_product_release_all_params.
        _service.enable_retries()
        self.test_retire_data_product_release_all_params()

        # Disable retries and run test_retire_data_product_release_all_params.
        _service.disable_retries()
        self.test_retire_data_product_release_all_params()

    @responses.activate
    def test_retire_data_product_release_required_params(self):
        """
        test_retire_data_product_release_required_params()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/releases/testString/retire')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "properties": {"anyKey": "anyValue"}, "visualization_errors": [{"visualization": {"id": "id", "name": "name"}, "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "related_asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "error": {"code": "code", "message": "message"}}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'
        release_id = 'testString'

        # Invoke method
        response = _service.retire_data_product_release(
            data_product_id,
            release_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_retire_data_product_release_required_params_with_retries(self):
        # Enable retries and run test_retire_data_product_release_required_params.
        _service.enable_retries()
        self.test_retire_data_product_release_required_params()

        # Disable retries and run test_retire_data_product_release_required_params.
        _service.disable_retries()
        self.test_retire_data_product_release_required_params()

    @responses.activate
    def test_retire_data_product_release_value_error(self):
        """
        test_retire_data_product_release_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_products/testString/releases/testString/retire')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z", "properties": {"anyKey": "anyValue"}, "visualization_errors": [{"visualization": {"id": "id", "name": "name"}, "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "related_asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "error": {"code": "code", "message": "message"}}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        data_product_id = 'testString'
        release_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_product_id": data_product_id,
            "release_id": release_id,
        }
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
# Start of Service: DataProductContractTemplates
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

        service = DphV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DphV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DphV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListDataProductContractTemplate:
    """
    Test Class for list_data_product_contract_template
    """

    @responses.activate
    def test_list_data_product_contract_template_all_params(self):
        """
        list_data_product_contract_template()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/contract_templates')
        mock_response = '{"contract_templates": [{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "id": "20aa7c97-cfcc-4d16-ae76-2ca1847ce733", "name": "Sample Data Contract Template", "error": {"code": "code", "message": "message"}, "contract_terms": {"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        container_id = 'testString'
        contract_template_name = 'testString'

        # Invoke method
        response = _service.list_data_product_contract_template(
            container_id=container_id,
            contract_template_name=contract_template_name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'container.id={}'.format(container_id) in query_string
        assert 'contract_template.name={}'.format(contract_template_name) in query_string

    def test_list_data_product_contract_template_all_params_with_retries(self):
        # Enable retries and run test_list_data_product_contract_template_all_params.
        _service.enable_retries()
        self.test_list_data_product_contract_template_all_params()

        # Disable retries and run test_list_data_product_contract_template_all_params.
        _service.disable_retries()
        self.test_list_data_product_contract_template_all_params()

    @responses.activate
    def test_list_data_product_contract_template_required_params(self):
        """
        test_list_data_product_contract_template_required_params()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/contract_templates')
        mock_response = '{"contract_templates": [{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "id": "20aa7c97-cfcc-4d16-ae76-2ca1847ce733", "name": "Sample Data Contract Template", "error": {"code": "code", "message": "message"}, "contract_terms": {"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_data_product_contract_template()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_data_product_contract_template_required_params_with_retries(self):
        # Enable retries and run test_list_data_product_contract_template_required_params.
        _service.enable_retries()
        self.test_list_data_product_contract_template_required_params()

        # Disable retries and run test_list_data_product_contract_template_required_params.
        _service.disable_retries()
        self.test_list_data_product_contract_template_required_params()


class TestCreateContractTemplate:
    """
    Test Class for create_contract_template
    """

    @responses.activate
    def test_create_contract_template_all_params(self):
        """
        create_contract_template()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/contract_templates')
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "id": "20aa7c97-cfcc-4d16-ae76-2ca1847ce733", "name": "Sample Data Contract Template", "error": {"code": "code", "message": "message"}, "contract_terms": {"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {}
        container_reference_model['id'] = 'f531f74a-01c8-4e91-8e29-b018db683c86'
        container_reference_model['type'] = 'catalog'

        # Construct a dict representation of a ErrorMessage model
        error_message_model = {}
        error_message_model['code'] = 'testString'
        error_message_model['message'] = 'testString'

        # Construct a dict representation of a AssetReference model
        asset_reference_model = {}
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['name'] = 'testString'
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

        # Construct a dict representation of a Domain model
        domain_model = {}
        domain_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        domain_model['name'] = 'domain_name'
        domain_model['container'] = container_reference_model

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = '0.0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        # Construct a dict representation of a ContractTermsMoreInfo model
        contract_terms_more_info_model = {}
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://www.moreinfo.example.coms'

        # Construct a dict representation of a Description model
        description_model = {}
        description_model['purpose'] = 'Intended purpose for the provided data.'
        description_model['limitations'] = 'Technical, compliance, and legal limitations for data use.'
        description_model['usage'] = 'Recommended usage of the data.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = 'Custom properties that are not part of the standard.'

        # Construct a dict representation of a ContractTemplateOrganization model
        contract_template_organization_model = {}
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role'] = 'IAM Role'

        # Construct a dict representation of a Pricing model
        pricing_model = {}
        pricing_model['amount'] = '100.00'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        # Construct a dict representation of a ContractTemplateSLAProperty model
        contract_template_sla_property_model = {}
        contract_template_sla_property_model['property'] = 'slaproperty'
        contract_template_sla_property_model['value'] = 'slavalue'

        # Construct a dict representation of a ContractTemplateSLA model
        contract_template_sla_model = {}
        contract_template_sla_model['default_element'] = 'sladefaultelement'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        # Construct a dict representation of a ContractTemplateSupportAndCommunication model
        contract_template_support_and_communication_model = {}
        contract_template_support_and_communication_model['channel'] = 'channel'
        contract_template_support_and_communication_model['url'] = 'https://www.example.coms'

        # Construct a dict representation of a ContractTemplateCustomProperty model
        contract_template_custom_property_model = {}
        contract_template_custom_property_model['key'] = 'propertykey'
        contract_template_custom_property_model['value'] = 'propertyvalue'

        # Construct a dict representation of a ContractTest model
        contract_test_model = {}
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        # Construct a dict representation of a ContractSchemaPropertyType model
        contract_schema_property_type_model = {}
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        # Construct a dict representation of a ContractSchemaProperty model
        contract_schema_property_model = {}
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        # Construct a dict representation of a ContractSchema model
        contract_schema_model = {}
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        # Construct a dict representation of a ContractTerms model
        contract_terms_model = {}
        contract_terms_model['asset'] = asset_reference_model
        contract_terms_model['id'] = 'testString'
        contract_terms_model['documents'] = [contract_terms_document_model]
        contract_terms_model['error_msg'] = 'testString'
        contract_terms_model['overview'] = overview_model
        contract_terms_model['description'] = description_model
        contract_terms_model['organization'] = [contract_template_organization_model]
        contract_terms_model['roles'] = [roles_model]
        contract_terms_model['price'] = pricing_model
        contract_terms_model['sla'] = [contract_template_sla_model]
        contract_terms_model['support_and_communication'] = [contract_template_support_and_communication_model]
        contract_terms_model['custom_properties'] = [contract_template_custom_property_model]
        contract_terms_model['contract_test'] = contract_test_model
        contract_terms_model['schema'] = [contract_schema_model]

        # Set up parameter values
        container = container_reference_model
        id = 'testString'
        name = 'Sample Data Contract Template'
        error = error_message_model
        contract_terms = contract_terms_model
        container_id = 'testString'
        contract_template_name = 'testString'

        # Invoke method
        response = _service.create_contract_template(
            container,
            id=id,
            name=name,
            error=error,
            contract_terms=contract_terms,
            container_id=container_id,
            contract_template_name=contract_template_name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'container.id={}'.format(container_id) in query_string
        assert 'contract_template.name={}'.format(contract_template_name) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['container'] == container_reference_model
        assert req_body['id'] == 'testString'
        assert req_body['name'] == 'Sample Data Contract Template'
        assert req_body['error'] == error_message_model
        assert req_body['contract_terms'] == contract_terms_model

    def test_create_contract_template_all_params_with_retries(self):
        # Enable retries and run test_create_contract_template_all_params.
        _service.enable_retries()
        self.test_create_contract_template_all_params()

        # Disable retries and run test_create_contract_template_all_params.
        _service.disable_retries()
        self.test_create_contract_template_all_params()

    @responses.activate
    def test_create_contract_template_required_params(self):
        """
        test_create_contract_template_required_params()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/contract_templates')
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "id": "20aa7c97-cfcc-4d16-ae76-2ca1847ce733", "name": "Sample Data Contract Template", "error": {"code": "code", "message": "message"}, "contract_terms": {"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {}
        container_reference_model['id'] = 'f531f74a-01c8-4e91-8e29-b018db683c86'
        container_reference_model['type'] = 'catalog'

        # Construct a dict representation of a ErrorMessage model
        error_message_model = {}
        error_message_model['code'] = 'testString'
        error_message_model['message'] = 'testString'

        # Construct a dict representation of a AssetReference model
        asset_reference_model = {}
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['name'] = 'testString'
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

        # Construct a dict representation of a Domain model
        domain_model = {}
        domain_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        domain_model['name'] = 'domain_name'
        domain_model['container'] = container_reference_model

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = '0.0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        # Construct a dict representation of a ContractTermsMoreInfo model
        contract_terms_more_info_model = {}
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://www.moreinfo.example.coms'

        # Construct a dict representation of a Description model
        description_model = {}
        description_model['purpose'] = 'Intended purpose for the provided data.'
        description_model['limitations'] = 'Technical, compliance, and legal limitations for data use.'
        description_model['usage'] = 'Recommended usage of the data.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = 'Custom properties that are not part of the standard.'

        # Construct a dict representation of a ContractTemplateOrganization model
        contract_template_organization_model = {}
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role'] = 'IAM Role'

        # Construct a dict representation of a Pricing model
        pricing_model = {}
        pricing_model['amount'] = '100.00'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        # Construct a dict representation of a ContractTemplateSLAProperty model
        contract_template_sla_property_model = {}
        contract_template_sla_property_model['property'] = 'slaproperty'
        contract_template_sla_property_model['value'] = 'slavalue'

        # Construct a dict representation of a ContractTemplateSLA model
        contract_template_sla_model = {}
        contract_template_sla_model['default_element'] = 'sladefaultelement'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        # Construct a dict representation of a ContractTemplateSupportAndCommunication model
        contract_template_support_and_communication_model = {}
        contract_template_support_and_communication_model['channel'] = 'channel'
        contract_template_support_and_communication_model['url'] = 'https://www.example.coms'

        # Construct a dict representation of a ContractTemplateCustomProperty model
        contract_template_custom_property_model = {}
        contract_template_custom_property_model['key'] = 'propertykey'
        contract_template_custom_property_model['value'] = 'propertyvalue'

        # Construct a dict representation of a ContractTest model
        contract_test_model = {}
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        # Construct a dict representation of a ContractSchemaPropertyType model
        contract_schema_property_type_model = {}
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        # Construct a dict representation of a ContractSchemaProperty model
        contract_schema_property_model = {}
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        # Construct a dict representation of a ContractSchema model
        contract_schema_model = {}
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        # Construct a dict representation of a ContractTerms model
        contract_terms_model = {}
        contract_terms_model['asset'] = asset_reference_model
        contract_terms_model['id'] = 'testString'
        contract_terms_model['documents'] = [contract_terms_document_model]
        contract_terms_model['error_msg'] = 'testString'
        contract_terms_model['overview'] = overview_model
        contract_terms_model['description'] = description_model
        contract_terms_model['organization'] = [contract_template_organization_model]
        contract_terms_model['roles'] = [roles_model]
        contract_terms_model['price'] = pricing_model
        contract_terms_model['sla'] = [contract_template_sla_model]
        contract_terms_model['support_and_communication'] = [contract_template_support_and_communication_model]
        contract_terms_model['custom_properties'] = [contract_template_custom_property_model]
        contract_terms_model['contract_test'] = contract_test_model
        contract_terms_model['schema'] = [contract_schema_model]

        # Set up parameter values
        container = container_reference_model
        id = 'testString'
        name = 'Sample Data Contract Template'
        error = error_message_model
        contract_terms = contract_terms_model

        # Invoke method
        response = _service.create_contract_template(
            container,
            id=id,
            name=name,
            error=error,
            contract_terms=contract_terms,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['container'] == container_reference_model
        assert req_body['id'] == 'testString'
        assert req_body['name'] == 'Sample Data Contract Template'
        assert req_body['error'] == error_message_model
        assert req_body['contract_terms'] == contract_terms_model

    def test_create_contract_template_required_params_with_retries(self):
        # Enable retries and run test_create_contract_template_required_params.
        _service.enable_retries()
        self.test_create_contract_template_required_params()

        # Disable retries and run test_create_contract_template_required_params.
        _service.disable_retries()
        self.test_create_contract_template_required_params()

    @responses.activate
    def test_create_contract_template_value_error(self):
        """
        test_create_contract_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/contract_templates')
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "id": "20aa7c97-cfcc-4d16-ae76-2ca1847ce733", "name": "Sample Data Contract Template", "error": {"code": "code", "message": "message"}, "contract_terms": {"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {}
        container_reference_model['id'] = 'f531f74a-01c8-4e91-8e29-b018db683c86'
        container_reference_model['type'] = 'catalog'

        # Construct a dict representation of a ErrorMessage model
        error_message_model = {}
        error_message_model['code'] = 'testString'
        error_message_model['message'] = 'testString'

        # Construct a dict representation of a AssetReference model
        asset_reference_model = {}
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['name'] = 'testString'
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

        # Construct a dict representation of a Domain model
        domain_model = {}
        domain_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        domain_model['name'] = 'domain_name'
        domain_model['container'] = container_reference_model

        # Construct a dict representation of a Overview model
        overview_model = {}
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = '0.0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        # Construct a dict representation of a ContractTermsMoreInfo model
        contract_terms_more_info_model = {}
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://www.moreinfo.example.coms'

        # Construct a dict representation of a Description model
        description_model = {}
        description_model['purpose'] = 'Intended purpose for the provided data.'
        description_model['limitations'] = 'Technical, compliance, and legal limitations for data use.'
        description_model['usage'] = 'Recommended usage of the data.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = 'Custom properties that are not part of the standard.'

        # Construct a dict representation of a ContractTemplateOrganization model
        contract_template_organization_model = {}
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        # Construct a dict representation of a Roles model
        roles_model = {}
        roles_model['role'] = 'IAM Role'

        # Construct a dict representation of a Pricing model
        pricing_model = {}
        pricing_model['amount'] = '100.00'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        # Construct a dict representation of a ContractTemplateSLAProperty model
        contract_template_sla_property_model = {}
        contract_template_sla_property_model['property'] = 'slaproperty'
        contract_template_sla_property_model['value'] = 'slavalue'

        # Construct a dict representation of a ContractTemplateSLA model
        contract_template_sla_model = {}
        contract_template_sla_model['default_element'] = 'sladefaultelement'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        # Construct a dict representation of a ContractTemplateSupportAndCommunication model
        contract_template_support_and_communication_model = {}
        contract_template_support_and_communication_model['channel'] = 'channel'
        contract_template_support_and_communication_model['url'] = 'https://www.example.coms'

        # Construct a dict representation of a ContractTemplateCustomProperty model
        contract_template_custom_property_model = {}
        contract_template_custom_property_model['key'] = 'propertykey'
        contract_template_custom_property_model['value'] = 'propertyvalue'

        # Construct a dict representation of a ContractTest model
        contract_test_model = {}
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        # Construct a dict representation of a ContractSchemaPropertyType model
        contract_schema_property_type_model = {}
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        # Construct a dict representation of a ContractSchemaProperty model
        contract_schema_property_model = {}
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        # Construct a dict representation of a ContractSchema model
        contract_schema_model = {}
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        # Construct a dict representation of a ContractTerms model
        contract_terms_model = {}
        contract_terms_model['asset'] = asset_reference_model
        contract_terms_model['id'] = 'testString'
        contract_terms_model['documents'] = [contract_terms_document_model]
        contract_terms_model['error_msg'] = 'testString'
        contract_terms_model['overview'] = overview_model
        contract_terms_model['description'] = description_model
        contract_terms_model['organization'] = [contract_template_organization_model]
        contract_terms_model['roles'] = [roles_model]
        contract_terms_model['price'] = pricing_model
        contract_terms_model['sla'] = [contract_template_sla_model]
        contract_terms_model['support_and_communication'] = [contract_template_support_and_communication_model]
        contract_terms_model['custom_properties'] = [contract_template_custom_property_model]
        contract_terms_model['contract_test'] = contract_test_model
        contract_terms_model['schema'] = [contract_schema_model]

        # Set up parameter values
        container = container_reference_model
        id = 'testString'
        name = 'Sample Data Contract Template'
        error = error_message_model
        contract_terms = contract_terms_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "container": container,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_contract_template(**req_copy)

    def test_create_contract_template_value_error_with_retries(self):
        # Enable retries and run test_create_contract_template_value_error.
        _service.enable_retries()
        self.test_create_contract_template_value_error()

        # Disable retries and run test_create_contract_template_value_error.
        _service.disable_retries()
        self.test_create_contract_template_value_error()


class TestGetContractTemplate:
    """
    Test Class for get_contract_template
    """

    @responses.activate
    def test_get_contract_template_all_params(self):
        """
        get_contract_template()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/contract_templates/testString')
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "id": "20aa7c97-cfcc-4d16-ae76-2ca1847ce733", "name": "Sample Data Contract Template", "error": {"code": "code", "message": "message"}, "contract_terms": {"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        contract_template_id = 'testString'
        container_id = 'testString'

        # Invoke method
        response = _service.get_contract_template(
            contract_template_id,
            container_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'container.id={}'.format(container_id) in query_string

    def test_get_contract_template_all_params_with_retries(self):
        # Enable retries and run test_get_contract_template_all_params.
        _service.enable_retries()
        self.test_get_contract_template_all_params()

        # Disable retries and run test_get_contract_template_all_params.
        _service.disable_retries()
        self.test_get_contract_template_all_params()

    @responses.activate
    def test_get_contract_template_value_error(self):
        """
        test_get_contract_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/contract_templates/testString')
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "id": "20aa7c97-cfcc-4d16-ae76-2ca1847ce733", "name": "Sample Data Contract Template", "error": {"code": "code", "message": "message"}, "contract_terms": {"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        contract_template_id = 'testString'
        container_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "contract_template_id": contract_template_id,
            "container_id": container_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_contract_template(**req_copy)

    def test_get_contract_template_value_error_with_retries(self):
        # Enable retries and run test_get_contract_template_value_error.
        _service.enable_retries()
        self.test_get_contract_template_value_error()

        # Disable retries and run test_get_contract_template_value_error.
        _service.disable_retries()
        self.test_get_contract_template_value_error()


class TestDeleteDataProductContractTemplate:
    """
    Test Class for delete_data_product_contract_template
    """

    @responses.activate
    def test_delete_data_product_contract_template_all_params(self):
        """
        delete_data_product_contract_template()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/contract_templates/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        contract_template_id = 'testString'
        container_id = 'testString'

        # Invoke method
        response = _service.delete_data_product_contract_template(
            contract_template_id,
            container_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'container.id={}'.format(container_id) in query_string

    def test_delete_data_product_contract_template_all_params_with_retries(self):
        # Enable retries and run test_delete_data_product_contract_template_all_params.
        _service.enable_retries()
        self.test_delete_data_product_contract_template_all_params()

        # Disable retries and run test_delete_data_product_contract_template_all_params.
        _service.disable_retries()
        self.test_delete_data_product_contract_template_all_params()

    @responses.activate
    def test_delete_data_product_contract_template_value_error(self):
        """
        test_delete_data_product_contract_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/contract_templates/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        contract_template_id = 'testString'
        container_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "contract_template_id": contract_template_id,
            "container_id": container_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_data_product_contract_template(**req_copy)

    def test_delete_data_product_contract_template_value_error_with_retries(self):
        # Enable retries and run test_delete_data_product_contract_template_value_error.
        _service.enable_retries()
        self.test_delete_data_product_contract_template_value_error()

        # Disable retries and run test_delete_data_product_contract_template_value_error.
        _service.disable_retries()
        self.test_delete_data_product_contract_template_value_error()


class TestUpdateDataProductContractTemplate:
    """
    Test Class for update_data_product_contract_template
    """

    @responses.activate
    def test_update_data_product_contract_template_all_params(self):
        """
        update_data_product_contract_template()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/contract_templates/testString')
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "id": "20aa7c97-cfcc-4d16-ae76-2ca1847ce733", "name": "Sample Data Contract Template", "error": {"code": "code", "message": "message"}, "contract_terms": {"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        contract_template_id = 'testString'
        container_id = 'testString'
        json_patch_instructions = [json_patch_operation_model]

        # Invoke method
        response = _service.update_data_product_contract_template(
            contract_template_id,
            container_id,
            json_patch_instructions,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'container.id={}'.format(container_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == json_patch_instructions

    def test_update_data_product_contract_template_all_params_with_retries(self):
        # Enable retries and run test_update_data_product_contract_template_all_params.
        _service.enable_retries()
        self.test_update_data_product_contract_template_all_params()

        # Disable retries and run test_update_data_product_contract_template_all_params.
        _service.disable_retries()
        self.test_update_data_product_contract_template_all_params()

    @responses.activate
    def test_update_data_product_contract_template_value_error(self):
        """
        test_update_data_product_contract_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/contract_templates/testString')
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "id": "20aa7c97-cfcc-4d16-ae76-2ca1847ce733", "name": "Sample Data Contract Template", "error": {"code": "code", "message": "message"}, "contract_terms": {"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        contract_template_id = 'testString'
        container_id = 'testString'
        json_patch_instructions = [json_patch_operation_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "contract_template_id": contract_template_id,
            "container_id": container_id,
            "json_patch_instructions": json_patch_instructions,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_data_product_contract_template(**req_copy)

    def test_update_data_product_contract_template_value_error_with_retries(self):
        # Enable retries and run test_update_data_product_contract_template_value_error.
        _service.enable_retries()
        self.test_update_data_product_contract_template_value_error()

        # Disable retries and run test_update_data_product_contract_template_value_error.
        _service.disable_retries()
        self.test_update_data_product_contract_template_value_error()


# endregion
##############################################################################
# End of Service: DataProductContractTemplates
##############################################################################

##############################################################################
# Start of Service: DataProductDomains
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

        service = DphV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DphV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DphV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListDataProductDomains:
    """
    Test Class for list_data_product_domains
    """

    @responses.activate
    def test_list_data_product_domains_all_params(self):
        """
        list_data_product_domains()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/domains')
        mock_response = '{"domains": [{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "trace": "trace", "errors": [{"code": "request_body_error", "message": "message", "extra": {"id": "id", "timestamp": "2019-01-01T12:00:00.000Z", "environment_name": "environment_name", "http_status": 0, "source_cluster": 0, "source_component": 0, "transaction_id": 0}, "more_info": "more_info"}], "name": "Operations", "description": "This is a description of the data product domain.", "id": "id", "member_roles": {"user_iam_id": "user_iam_id", "roles": ["roles"]}, "properties": {"value": "value"}, "sub_domains": [{"name": "Operations", "id": "id", "description": "description"}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        container_id = 'testString'

        # Invoke method
        response = _service.list_data_product_domains(
            container_id=container_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'container.id={}'.format(container_id) in query_string

    def test_list_data_product_domains_all_params_with_retries(self):
        # Enable retries and run test_list_data_product_domains_all_params.
        _service.enable_retries()
        self.test_list_data_product_domains_all_params()

        # Disable retries and run test_list_data_product_domains_all_params.
        _service.disable_retries()
        self.test_list_data_product_domains_all_params()

    @responses.activate
    def test_list_data_product_domains_required_params(self):
        """
        test_list_data_product_domains_required_params()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/domains')
        mock_response = '{"domains": [{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "trace": "trace", "errors": [{"code": "request_body_error", "message": "message", "extra": {"id": "id", "timestamp": "2019-01-01T12:00:00.000Z", "environment_name": "environment_name", "http_status": 0, "source_cluster": 0, "source_component": 0, "transaction_id": 0}, "more_info": "more_info"}], "name": "Operations", "description": "This is a description of the data product domain.", "id": "id", "member_roles": {"user_iam_id": "user_iam_id", "roles": ["roles"]}, "properties": {"value": "value"}, "sub_domains": [{"name": "Operations", "id": "id", "description": "description"}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_data_product_domains()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_data_product_domains_required_params_with_retries(self):
        # Enable retries and run test_list_data_product_domains_required_params.
        _service.enable_retries()
        self.test_list_data_product_domains_required_params()

        # Disable retries and run test_list_data_product_domains_required_params.
        _service.disable_retries()
        self.test_list_data_product_domains_required_params()


class TestCreateDataProductDomain:
    """
    Test Class for create_data_product_domain
    """

    @responses.activate
    def test_create_data_product_domain_all_params(self):
        """
        create_data_product_domain()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/domains')
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "trace": "trace", "errors": [{"code": "request_body_error", "message": "message", "extra": {"id": "id", "timestamp": "2019-01-01T12:00:00.000Z", "environment_name": "environment_name", "http_status": 0, "source_cluster": 0, "source_component": 0, "transaction_id": 0}, "more_info": "more_info"}], "name": "Operations", "description": "This is a description of the data product domain.", "id": "id", "member_roles": {"user_iam_id": "user_iam_id", "roles": ["roles"]}, "properties": {"value": "value"}, "sub_domains": [{"name": "Operations", "id": "id", "description": "description"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {}
        container_reference_model['id'] = 'ed580171-a6e4-4b93-973f-ae2f2f62991b'
        container_reference_model['type'] = 'catalog'

        # Construct a dict representation of a ErrorExtraResource model
        error_extra_resource_model = {}
        error_extra_resource_model['id'] = 'testString'
        error_extra_resource_model['timestamp'] = '2019-01-01T12:00:00Z'
        error_extra_resource_model['environment_name'] = 'testString'
        error_extra_resource_model['http_status'] = 0
        error_extra_resource_model['source_cluster'] = 0
        error_extra_resource_model['source_component'] = 0
        error_extra_resource_model['transaction_id'] = 0

        # Construct a dict representation of a ErrorModelResource model
        error_model_resource_model = {}
        error_model_resource_model['code'] = 'request_body_error'
        error_model_resource_model['message'] = 'testString'
        error_model_resource_model['extra'] = error_extra_resource_model
        error_model_resource_model['more_info'] = 'testString'

        # Construct a dict representation of a MemberRolesSchema model
        member_roles_schema_model = {}
        member_roles_schema_model['user_iam_id'] = 'testString'
        member_roles_schema_model['roles'] = ['testString']

        # Construct a dict representation of a PropertiesSchema model
        properties_schema_model = {}
        properties_schema_model['value'] = 'testString'

        # Construct a dict representation of a InitializeSubDomain model
        initialize_sub_domain_model = {}
        initialize_sub_domain_model['name'] = 'Sub domain 1'
        initialize_sub_domain_model['id'] = 'testString'
        initialize_sub_domain_model['description'] = 'New sub domain 1'

        # Set up parameter values
        container = container_reference_model
        trace = 'testString'
        errors = [error_model_resource_model]
        name = 'Test domain'
        description = 'The sample description for new domain'
        id = 'testString'
        member_roles = member_roles_schema_model
        properties = properties_schema_model
        sub_domains = [initialize_sub_domain_model]
        container_id = 'testString'

        # Invoke method
        response = _service.create_data_product_domain(
            container,
            trace=trace,
            errors=errors,
            name=name,
            description=description,
            id=id,
            member_roles=member_roles,
            properties=properties,
            sub_domains=sub_domains,
            container_id=container_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'container.id={}'.format(container_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['container'] == container_reference_model
        assert req_body['trace'] == 'testString'
        assert req_body['errors'] == [error_model_resource_model]
        assert req_body['name'] == 'Test domain'
        assert req_body['description'] == 'The sample description for new domain'
        assert req_body['id'] == 'testString'
        assert req_body['member_roles'] == member_roles_schema_model
        assert req_body['properties'] == properties_schema_model
        assert req_body['sub_domains'] == [initialize_sub_domain_model]

    def test_create_data_product_domain_all_params_with_retries(self):
        # Enable retries and run test_create_data_product_domain_all_params.
        _service.enable_retries()
        self.test_create_data_product_domain_all_params()

        # Disable retries and run test_create_data_product_domain_all_params.
        _service.disable_retries()
        self.test_create_data_product_domain_all_params()

    @responses.activate
    def test_create_data_product_domain_required_params(self):
        """
        test_create_data_product_domain_required_params()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/domains')
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "trace": "trace", "errors": [{"code": "request_body_error", "message": "message", "extra": {"id": "id", "timestamp": "2019-01-01T12:00:00.000Z", "environment_name": "environment_name", "http_status": 0, "source_cluster": 0, "source_component": 0, "transaction_id": 0}, "more_info": "more_info"}], "name": "Operations", "description": "This is a description of the data product domain.", "id": "id", "member_roles": {"user_iam_id": "user_iam_id", "roles": ["roles"]}, "properties": {"value": "value"}, "sub_domains": [{"name": "Operations", "id": "id", "description": "description"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {}
        container_reference_model['id'] = 'ed580171-a6e4-4b93-973f-ae2f2f62991b'
        container_reference_model['type'] = 'catalog'

        # Construct a dict representation of a ErrorExtraResource model
        error_extra_resource_model = {}
        error_extra_resource_model['id'] = 'testString'
        error_extra_resource_model['timestamp'] = '2019-01-01T12:00:00Z'
        error_extra_resource_model['environment_name'] = 'testString'
        error_extra_resource_model['http_status'] = 0
        error_extra_resource_model['source_cluster'] = 0
        error_extra_resource_model['source_component'] = 0
        error_extra_resource_model['transaction_id'] = 0

        # Construct a dict representation of a ErrorModelResource model
        error_model_resource_model = {}
        error_model_resource_model['code'] = 'request_body_error'
        error_model_resource_model['message'] = 'testString'
        error_model_resource_model['extra'] = error_extra_resource_model
        error_model_resource_model['more_info'] = 'testString'

        # Construct a dict representation of a MemberRolesSchema model
        member_roles_schema_model = {}
        member_roles_schema_model['user_iam_id'] = 'testString'
        member_roles_schema_model['roles'] = ['testString']

        # Construct a dict representation of a PropertiesSchema model
        properties_schema_model = {}
        properties_schema_model['value'] = 'testString'

        # Construct a dict representation of a InitializeSubDomain model
        initialize_sub_domain_model = {}
        initialize_sub_domain_model['name'] = 'Sub domain 1'
        initialize_sub_domain_model['id'] = 'testString'
        initialize_sub_domain_model['description'] = 'New sub domain 1'

        # Set up parameter values
        container = container_reference_model
        trace = 'testString'
        errors = [error_model_resource_model]
        name = 'Test domain'
        description = 'The sample description for new domain'
        id = 'testString'
        member_roles = member_roles_schema_model
        properties = properties_schema_model
        sub_domains = [initialize_sub_domain_model]

        # Invoke method
        response = _service.create_data_product_domain(
            container,
            trace=trace,
            errors=errors,
            name=name,
            description=description,
            id=id,
            member_roles=member_roles,
            properties=properties,
            sub_domains=sub_domains,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['container'] == container_reference_model
        assert req_body['trace'] == 'testString'
        assert req_body['errors'] == [error_model_resource_model]
        assert req_body['name'] == 'Test domain'
        assert req_body['description'] == 'The sample description for new domain'
        assert req_body['id'] == 'testString'
        assert req_body['member_roles'] == member_roles_schema_model
        assert req_body['properties'] == properties_schema_model
        assert req_body['sub_domains'] == [initialize_sub_domain_model]

    def test_create_data_product_domain_required_params_with_retries(self):
        # Enable retries and run test_create_data_product_domain_required_params.
        _service.enable_retries()
        self.test_create_data_product_domain_required_params()

        # Disable retries and run test_create_data_product_domain_required_params.
        _service.disable_retries()
        self.test_create_data_product_domain_required_params()

    @responses.activate
    def test_create_data_product_domain_value_error(self):
        """
        test_create_data_product_domain_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/domains')
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "trace": "trace", "errors": [{"code": "request_body_error", "message": "message", "extra": {"id": "id", "timestamp": "2019-01-01T12:00:00.000Z", "environment_name": "environment_name", "http_status": 0, "source_cluster": 0, "source_component": 0, "transaction_id": 0}, "more_info": "more_info"}], "name": "Operations", "description": "This is a description of the data product domain.", "id": "id", "member_roles": {"user_iam_id": "user_iam_id", "roles": ["roles"]}, "properties": {"value": "value"}, "sub_domains": [{"name": "Operations", "id": "id", "description": "description"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {}
        container_reference_model['id'] = 'ed580171-a6e4-4b93-973f-ae2f2f62991b'
        container_reference_model['type'] = 'catalog'

        # Construct a dict representation of a ErrorExtraResource model
        error_extra_resource_model = {}
        error_extra_resource_model['id'] = 'testString'
        error_extra_resource_model['timestamp'] = '2019-01-01T12:00:00Z'
        error_extra_resource_model['environment_name'] = 'testString'
        error_extra_resource_model['http_status'] = 0
        error_extra_resource_model['source_cluster'] = 0
        error_extra_resource_model['source_component'] = 0
        error_extra_resource_model['transaction_id'] = 0

        # Construct a dict representation of a ErrorModelResource model
        error_model_resource_model = {}
        error_model_resource_model['code'] = 'request_body_error'
        error_model_resource_model['message'] = 'testString'
        error_model_resource_model['extra'] = error_extra_resource_model
        error_model_resource_model['more_info'] = 'testString'

        # Construct a dict representation of a MemberRolesSchema model
        member_roles_schema_model = {}
        member_roles_schema_model['user_iam_id'] = 'testString'
        member_roles_schema_model['roles'] = ['testString']

        # Construct a dict representation of a PropertiesSchema model
        properties_schema_model = {}
        properties_schema_model['value'] = 'testString'

        # Construct a dict representation of a InitializeSubDomain model
        initialize_sub_domain_model = {}
        initialize_sub_domain_model['name'] = 'Sub domain 1'
        initialize_sub_domain_model['id'] = 'testString'
        initialize_sub_domain_model['description'] = 'New sub domain 1'

        # Set up parameter values
        container = container_reference_model
        trace = 'testString'
        errors = [error_model_resource_model]
        name = 'Test domain'
        description = 'The sample description for new domain'
        id = 'testString'
        member_roles = member_roles_schema_model
        properties = properties_schema_model
        sub_domains = [initialize_sub_domain_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "container": container,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_data_product_domain(**req_copy)

    def test_create_data_product_domain_value_error_with_retries(self):
        # Enable retries and run test_create_data_product_domain_value_error.
        _service.enable_retries()
        self.test_create_data_product_domain_value_error()

        # Disable retries and run test_create_data_product_domain_value_error.
        _service.disable_retries()
        self.test_create_data_product_domain_value_error()


class TestCreateDataProductSubdomain:
    """
    Test Class for create_data_product_subdomain
    """

    @responses.activate
    def test_create_data_product_subdomain_all_params(self):
        """
        create_data_product_subdomain()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/domains/testString/subdomains')
        mock_response = '{"name": "Operations", "id": "id", "description": "description"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        domain_id = 'testString'
        container_id = 'testString'
        name = 'Sub domain 1'
        id = 'testString'
        description = 'New sub domain 1'

        # Invoke method
        response = _service.create_data_product_subdomain(
            domain_id,
            container_id,
            name=name,
            id=id,
            description=description,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'container.id={}'.format(container_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'Sub domain 1'
        assert req_body['id'] == 'testString'
        assert req_body['description'] == 'New sub domain 1'

    def test_create_data_product_subdomain_all_params_with_retries(self):
        # Enable retries and run test_create_data_product_subdomain_all_params.
        _service.enable_retries()
        self.test_create_data_product_subdomain_all_params()

        # Disable retries and run test_create_data_product_subdomain_all_params.
        _service.disable_retries()
        self.test_create_data_product_subdomain_all_params()

    @responses.activate
    def test_create_data_product_subdomain_value_error(self):
        """
        test_create_data_product_subdomain_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/domains/testString/subdomains')
        mock_response = '{"name": "Operations", "id": "id", "description": "description"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        domain_id = 'testString'
        container_id = 'testString'
        name = 'Sub domain 1'
        id = 'testString'
        description = 'New sub domain 1'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "domain_id": domain_id,
            "container_id": container_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_data_product_subdomain(**req_copy)

    def test_create_data_product_subdomain_value_error_with_retries(self):
        # Enable retries and run test_create_data_product_subdomain_value_error.
        _service.enable_retries()
        self.test_create_data_product_subdomain_value_error()

        # Disable retries and run test_create_data_product_subdomain_value_error.
        _service.disable_retries()
        self.test_create_data_product_subdomain_value_error()


class TestGetDomain:
    """
    Test Class for get_domain
    """

    @responses.activate
    def test_get_domain_all_params(self):
        """
        get_domain()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/domains/testString')
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "trace": "trace", "errors": [{"code": "request_body_error", "message": "message", "extra": {"id": "id", "timestamp": "2019-01-01T12:00:00.000Z", "environment_name": "environment_name", "http_status": 0, "source_cluster": 0, "source_component": 0, "transaction_id": 0}, "more_info": "more_info"}], "name": "Operations", "description": "This is a description of the data product domain.", "id": "id", "member_roles": {"user_iam_id": "user_iam_id", "roles": ["roles"]}, "properties": {"value": "value"}, "sub_domains": [{"name": "Operations", "id": "id", "description": "description"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        domain_id = 'testString'

        # Invoke method
        response = _service.get_domain(
            domain_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_domain_all_params_with_retries(self):
        # Enable retries and run test_get_domain_all_params.
        _service.enable_retries()
        self.test_get_domain_all_params()

        # Disable retries and run test_get_domain_all_params.
        _service.disable_retries()
        self.test_get_domain_all_params()

    @responses.activate
    def test_get_domain_value_error(self):
        """
        test_get_domain_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/domains/testString')
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "trace": "trace", "errors": [{"code": "request_body_error", "message": "message", "extra": {"id": "id", "timestamp": "2019-01-01T12:00:00.000Z", "environment_name": "environment_name", "http_status": 0, "source_cluster": 0, "source_component": 0, "transaction_id": 0}, "more_info": "more_info"}], "name": "Operations", "description": "This is a description of the data product domain.", "id": "id", "member_roles": {"user_iam_id": "user_iam_id", "roles": ["roles"]}, "properties": {"value": "value"}, "sub_domains": [{"name": "Operations", "id": "id", "description": "description"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        domain_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "domain_id": domain_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_domain(**req_copy)

    def test_get_domain_value_error_with_retries(self):
        # Enable retries and run test_get_domain_value_error.
        _service.enable_retries()
        self.test_get_domain_value_error()

        # Disable retries and run test_get_domain_value_error.
        _service.disable_retries()
        self.test_get_domain_value_error()


class TestDeleteDomain:
    """
    Test Class for delete_domain
    """

    @responses.activate
    def test_delete_domain_all_params(self):
        """
        delete_domain()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/domains/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        domain_id = 'testString'

        # Invoke method
        response = _service.delete_domain(
            domain_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_domain_all_params_with_retries(self):
        # Enable retries and run test_delete_domain_all_params.
        _service.enable_retries()
        self.test_delete_domain_all_params()

        # Disable retries and run test_delete_domain_all_params.
        _service.disable_retries()
        self.test_delete_domain_all_params()

    @responses.activate
    def test_delete_domain_value_error(self):
        """
        test_delete_domain_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/domains/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        domain_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "domain_id": domain_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_domain(**req_copy)

    def test_delete_domain_value_error_with_retries(self):
        # Enable retries and run test_delete_domain_value_error.
        _service.enable_retries()
        self.test_delete_domain_value_error()

        # Disable retries and run test_delete_domain_value_error.
        _service.disable_retries()
        self.test_delete_domain_value_error()


class TestUpdateDataProductDomain:
    """
    Test Class for update_data_product_domain
    """

    @responses.activate
    def test_update_data_product_domain_all_params(self):
        """
        update_data_product_domain()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/domains/testString')
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "trace": "trace", "errors": [{"code": "request_body_error", "message": "message", "extra": {"id": "id", "timestamp": "2019-01-01T12:00:00.000Z", "environment_name": "environment_name", "http_status": 0, "source_cluster": 0, "source_component": 0, "transaction_id": 0}, "more_info": "more_info"}], "name": "Operations", "description": "This is a description of the data product domain.", "id": "id", "member_roles": {"user_iam_id": "user_iam_id", "roles": ["roles"]}, "properties": {"value": "value"}, "sub_domains": [{"name": "Operations", "id": "id", "description": "description"}]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        domain_id = 'testString'
        container_id = 'testString'
        json_patch_instructions = [json_patch_operation_model]

        # Invoke method
        response = _service.update_data_product_domain(
            domain_id,
            container_id,
            json_patch_instructions,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'container.id={}'.format(container_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == json_patch_instructions

    def test_update_data_product_domain_all_params_with_retries(self):
        # Enable retries and run test_update_data_product_domain_all_params.
        _service.enable_retries()
        self.test_update_data_product_domain_all_params()

        # Disable retries and run test_update_data_product_domain_all_params.
        _service.disable_retries()
        self.test_update_data_product_domain_all_params()

    @responses.activate
    def test_update_data_product_domain_value_error(self):
        """
        test_update_data_product_domain_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/domains/testString')
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "trace": "trace", "errors": [{"code": "request_body_error", "message": "message", "extra": {"id": "id", "timestamp": "2019-01-01T12:00:00.000Z", "environment_name": "environment_name", "http_status": 0, "source_cluster": 0, "source_component": 0, "transaction_id": 0}, "more_info": "more_info"}], "name": "Operations", "description": "This is a description of the data product domain.", "id": "id", "member_roles": {"user_iam_id": "user_iam_id", "roles": ["roles"]}, "properties": {"value": "value"}, "sub_domains": [{"name": "Operations", "id": "id", "description": "description"}]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        domain_id = 'testString'
        container_id = 'testString'
        json_patch_instructions = [json_patch_operation_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "domain_id": domain_id,
            "container_id": container_id,
            "json_patch_instructions": json_patch_instructions,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_data_product_domain(**req_copy)

    def test_update_data_product_domain_value_error_with_retries(self):
        # Enable retries and run test_update_data_product_domain_value_error.
        _service.enable_retries()
        self.test_update_data_product_domain_value_error()

        # Disable retries and run test_update_data_product_domain_value_error.
        _service.disable_retries()
        self.test_update_data_product_domain_value_error()


class TestGetDataProductByDomain:
    """
    Test Class for get_data_product_by_domain
    """

    @responses.activate
    def test_get_data_product_by_domain_all_params(self):
        """
        get_data_product_by_domain()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/domains/testString/data_products')
        mock_response = '{"limit": 200, "first": {"href": "https://api.example.com/collection"}, "next": {"href": "https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "total_results": 200, "data_product_versions": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        domain_id = 'testString'
        container_id = 'testString'

        # Invoke method
        response = _service.get_data_product_by_domain(
            domain_id,
            container_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'container.id={}'.format(container_id) in query_string

    def test_get_data_product_by_domain_all_params_with_retries(self):
        # Enable retries and run test_get_data_product_by_domain_all_params.
        _service.enable_retries()
        self.test_get_data_product_by_domain_all_params()

        # Disable retries and run test_get_data_product_by_domain_all_params.
        _service.disable_retries()
        self.test_get_data_product_by_domain_all_params()

    @responses.activate
    def test_get_data_product_by_domain_value_error(self):
        """
        test_get_data_product_by_domain_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/domains/testString/data_products')
        mock_response = '{"limit": 200, "first": {"href": "https://api.example.com/collection"}, "next": {"href": "https://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "total_results": 200, "data_product_versions": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "release": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}, "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "name": "My Data Product", "description": "This is a description of My Data Product.", "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "types": ["data"], "contract_terms": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "id": "id", "documents": [{"url": "url", "type": "terms_and_conditions", "name": "name", "id": "2b0bf220-079c-11ee-be56-0242ac120002", "attachment": {"id": "id"}, "upload_url": "upload_url"}], "error_msg": "error_msg", "overview": {"api_version": "v3.0.1", "kind": "DataContract", "name": "Sample Data Contract", "version": "0.0.0", "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "more_info": "List of links to sources that provide more details on the data contract."}, "description": {"purpose": "Used for customer behavior analysis.", "limitations": "Data cannot be used for marketing.", "usage": "Data should be used only for analytics.", "more_info": [{"type": "privacy-statement", "url": "https://moreinfo.example.com"}], "custom_properties": "{\\"property1\\":\\"value1\\"}"}, "organization": [{"user_id": "IBMid-691000IN4G", "role": "owner"}], "roles": [{"role": "owner"}], "price": {"amount": "100.0", "currency": "USD", "unit": "megabyte"}, "sla": [{"default_element": "Standard SLA Policy", "properties": [{"property": "Uptime Guarantee", "value": "99.9"}]}], "support_and_communication": [{"channel": "Email Support", "url": "https://support.example.com"}], "custom_properties": [{"key": "customPropertyKey", "value": "customPropertyValue"}], "contract_test": {"status": "pass", "last_tested_time": "last_tested_time", "message": "message"}, "schema": [{"name": "name", "description": "description", "physical_type": "physical_type", "properties": [{"name": "name", "type": {"type": "type", "length": "length", "scale": "scale", "nullable": "nullable", "signed": "signed", "native_type": "native_type"}}]}]}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "getproperties": {"producer_input": {"engine_details": {"display_name": "Iceberg Engine", "engine_id": "presto767", "engine_port": "34567", "engine_host": "a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud", "associated_catalogs": ["associated_catalogs"]}}}}]}], "workflows": {"order_access_request": {"task_assignee_users": ["task_assignee_users"], "pre_approved_users": ["pre_approved_users"], "custom_workflow_definition": {"id": "18bdbde1-918e-4ecf-aa23-6727bf319e14"}}}, "dataview_enabled": true, "comments": "Comments by a producer that are provided either at the time of data product version creation or retiring", "access_control": {"owner": "IBMid-696000KYV9"}, "last_updated_at": "2019-01-01T12:00:00.000Z", "is_restricted": false, "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        domain_id = 'testString'
        container_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "domain_id": domain_id,
            "container_id": container_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_data_product_by_domain(**req_copy)

    def test_get_data_product_by_domain_value_error_with_retries(self):
        # Enable retries and run test_get_data_product_by_domain_value_error.
        _service.enable_retries()
        self.test_get_data_product_by_domain_value_error()

        # Disable retries and run test_get_data_product_by_domain_value_error.
        _service.disable_retries()
        self.test_get_data_product_by_domain_value_error()


# endregion
##############################################################################
# End of Service: DataProductDomains
##############################################################################

##############################################################################
# Start of Service: BucketServices
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

        service = DphV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DphV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DphV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateS3Bucket:
    """
    Test Class for create_s3_bucket
    """

    @responses.activate
    def test_create_s3_bucket_all_params(self):
        """
        create_s3_bucket()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/bucket')
        mock_response = '{"bucket_name": "bucket_name", "bucket_location": "bucket_location", "role_arn": "role_arn", "bucket_type": "bucket_type", "shared": true}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        is_shared = True

        # Invoke method
        response = _service.create_s3_bucket(
            is_shared,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'is_shared={}'.format('true' if is_shared else 'false') in query_string

    def test_create_s3_bucket_all_params_with_retries(self):
        # Enable retries and run test_create_s3_bucket_all_params.
        _service.enable_retries()
        self.test_create_s3_bucket_all_params()

        # Disable retries and run test_create_s3_bucket_all_params.
        _service.disable_retries()
        self.test_create_s3_bucket_all_params()

    @responses.activate
    def test_create_s3_bucket_value_error(self):
        """
        test_create_s3_bucket_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/bucket')
        mock_response = '{"bucket_name": "bucket_name", "bucket_location": "bucket_location", "role_arn": "role_arn", "bucket_type": "bucket_type", "shared": true}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        is_shared = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "is_shared": is_shared,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_s3_bucket(**req_copy)

    def test_create_s3_bucket_value_error_with_retries(self):
        # Enable retries and run test_create_s3_bucket_value_error.
        _service.enable_retries()
        self.test_create_s3_bucket_value_error()

        # Disable retries and run test_create_s3_bucket_value_error.
        _service.disable_retries()
        self.test_create_s3_bucket_value_error()


class TestGetS3BucketValidation:
    """
    Test Class for get_s3_bucket_validation
    """

    @responses.activate
    def test_get_s3_bucket_validation_all_params(self):
        """
        get_s3_bucket_validation()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/bucket/validate/testString')
        mock_response = '{"bucket_exists": false}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        bucket_name = 'testString'

        # Invoke method
        response = _service.get_s3_bucket_validation(
            bucket_name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_s3_bucket_validation_all_params_with_retries(self):
        # Enable retries and run test_get_s3_bucket_validation_all_params.
        _service.enable_retries()
        self.test_get_s3_bucket_validation_all_params()

        # Disable retries and run test_get_s3_bucket_validation_all_params.
        _service.disable_retries()
        self.test_get_s3_bucket_validation_all_params()

    @responses.activate
    def test_get_s3_bucket_validation_value_error(self):
        """
        test_get_s3_bucket_validation_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/bucket/validate/testString')
        mock_response = '{"bucket_exists": false}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        bucket_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "bucket_name": bucket_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_s3_bucket_validation(**req_copy)

    def test_get_s3_bucket_validation_value_error_with_retries(self):
        # Enable retries and run test_get_s3_bucket_validation_value_error.
        _service.enable_retries()
        self.test_get_s3_bucket_validation_value_error()

        # Disable retries and run test_get_s3_bucket_validation_value_error.
        _service.disable_retries()
        self.test_get_s3_bucket_validation_value_error()


# endregion
##############################################################################
# End of Service: BucketServices
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_AssetListAccessControl:
    """
    Test Class for AssetListAccessControl
    """

    def test_asset_list_access_control_serialization(self):
        """
        Test serialization/deserialization for AssetListAccessControl
        """

        # Construct a json representation of a AssetListAccessControl model
        asset_list_access_control_model_json = {}
        asset_list_access_control_model_json['owner'] = 'IBMid-696000KYV9'

        # Construct a model instance of AssetListAccessControl by calling from_dict on the json representation
        asset_list_access_control_model = AssetListAccessControl.from_dict(asset_list_access_control_model_json)
        assert asset_list_access_control_model != False

        # Construct a model instance of AssetListAccessControl by calling from_dict on the json representation
        asset_list_access_control_model_dict = AssetListAccessControl.from_dict(asset_list_access_control_model_json).__dict__
        asset_list_access_control_model2 = AssetListAccessControl(**asset_list_access_control_model_dict)

        # Verify the model instances are equivalent
        assert asset_list_access_control_model == asset_list_access_control_model2

        # Convert model instance back to dict and verify no loss of data
        asset_list_access_control_model_json2 = asset_list_access_control_model.to_dict()
        assert asset_list_access_control_model_json2 == asset_list_access_control_model_json


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
        asset_part_reference_model_json['name'] = 'testString'
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
        asset_reference_model_json['name'] = 'testString'
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


class TestModel_BucketResponse:
    """
    Test Class for BucketResponse
    """

    def test_bucket_response_serialization(self):
        """
        Test serialization/deserialization for BucketResponse
        """

        # Construct a json representation of a BucketResponse model
        bucket_response_model_json = {}
        bucket_response_model_json['bucket_name'] = 'testString'
        bucket_response_model_json['bucket_location'] = 'testString'
        bucket_response_model_json['role_arn'] = 'testString'
        bucket_response_model_json['bucket_type'] = 'testString'
        bucket_response_model_json['shared'] = True

        # Construct a model instance of BucketResponse by calling from_dict on the json representation
        bucket_response_model = BucketResponse.from_dict(bucket_response_model_json)
        assert bucket_response_model != False

        # Construct a model instance of BucketResponse by calling from_dict on the json representation
        bucket_response_model_dict = BucketResponse.from_dict(bucket_response_model_json).__dict__
        bucket_response_model2 = BucketResponse(**bucket_response_model_dict)

        # Verify the model instances are equivalent
        assert bucket_response_model == bucket_response_model2

        # Convert model instance back to dict and verify no loss of data
        bucket_response_model_json2 = bucket_response_model.to_dict()
        assert bucket_response_model_json2 == bucket_response_model_json


class TestModel_BucketValidationResponse:
    """
    Test Class for BucketValidationResponse
    """

    def test_bucket_validation_response_serialization(self):
        """
        Test serialization/deserialization for BucketValidationResponse
        """

        # Construct a json representation of a BucketValidationResponse model
        bucket_validation_response_model_json = {}
        bucket_validation_response_model_json['bucket_exists'] = True

        # Construct a model instance of BucketValidationResponse by calling from_dict on the json representation
        bucket_validation_response_model = BucketValidationResponse.from_dict(bucket_validation_response_model_json)
        assert bucket_validation_response_model != False

        # Construct a model instance of BucketValidationResponse by calling from_dict on the json representation
        bucket_validation_response_model_dict = BucketValidationResponse.from_dict(bucket_validation_response_model_json).__dict__
        bucket_validation_response_model2 = BucketValidationResponse(**bucket_validation_response_model_dict)

        # Verify the model instances are equivalent
        assert bucket_validation_response_model == bucket_validation_response_model2

        # Convert model instance back to dict and verify no loss of data
        bucket_validation_response_model_json2 = bucket_validation_response_model.to_dict()
        assert bucket_validation_response_model_json2 == bucket_validation_response_model_json


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


class TestModel_ContractSchema:
    """
    Test Class for ContractSchema
    """

    def test_contract_schema_serialization(self):
        """
        Test serialization/deserialization for ContractSchema
        """

        # Construct dict forms of any model objects needed in order to build this model.

        contract_schema_property_type_model = {}  # ContractSchemaPropertyType
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        contract_schema_property_model = {}  # ContractSchemaProperty
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        # Construct a json representation of a ContractSchema model
        contract_schema_model_json = {}
        contract_schema_model_json['name'] = 'testString'
        contract_schema_model_json['description'] = 'testString'
        contract_schema_model_json['physical_type'] = 'testString'
        contract_schema_model_json['properties'] = [contract_schema_property_model]

        # Construct a model instance of ContractSchema by calling from_dict on the json representation
        contract_schema_model = ContractSchema.from_dict(contract_schema_model_json)
        assert contract_schema_model != False

        # Construct a model instance of ContractSchema by calling from_dict on the json representation
        contract_schema_model_dict = ContractSchema.from_dict(contract_schema_model_json).__dict__
        contract_schema_model2 = ContractSchema(**contract_schema_model_dict)

        # Verify the model instances are equivalent
        assert contract_schema_model == contract_schema_model2

        # Convert model instance back to dict and verify no loss of data
        contract_schema_model_json2 = contract_schema_model.to_dict()
        assert contract_schema_model_json2 == contract_schema_model_json


class TestModel_ContractSchemaProperty:
    """
    Test Class for ContractSchemaProperty
    """

    def test_contract_schema_property_serialization(self):
        """
        Test serialization/deserialization for ContractSchemaProperty
        """

        # Construct dict forms of any model objects needed in order to build this model.

        contract_schema_property_type_model = {}  # ContractSchemaPropertyType
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        # Construct a json representation of a ContractSchemaProperty model
        contract_schema_property_model_json = {}
        contract_schema_property_model_json['name'] = 'testString'
        contract_schema_property_model_json['type'] = contract_schema_property_type_model

        # Construct a model instance of ContractSchemaProperty by calling from_dict on the json representation
        contract_schema_property_model = ContractSchemaProperty.from_dict(contract_schema_property_model_json)
        assert contract_schema_property_model != False

        # Construct a model instance of ContractSchemaProperty by calling from_dict on the json representation
        contract_schema_property_model_dict = ContractSchemaProperty.from_dict(contract_schema_property_model_json).__dict__
        contract_schema_property_model2 = ContractSchemaProperty(**contract_schema_property_model_dict)

        # Verify the model instances are equivalent
        assert contract_schema_property_model == contract_schema_property_model2

        # Convert model instance back to dict and verify no loss of data
        contract_schema_property_model_json2 = contract_schema_property_model.to_dict()
        assert contract_schema_property_model_json2 == contract_schema_property_model_json


class TestModel_ContractSchemaPropertyType:
    """
    Test Class for ContractSchemaPropertyType
    """

    def test_contract_schema_property_type_serialization(self):
        """
        Test serialization/deserialization for ContractSchemaPropertyType
        """

        # Construct a json representation of a ContractSchemaPropertyType model
        contract_schema_property_type_model_json = {}
        contract_schema_property_type_model_json['type'] = 'testString'
        contract_schema_property_type_model_json['length'] = 'testString'
        contract_schema_property_type_model_json['scale'] = 'testString'
        contract_schema_property_type_model_json['nullable'] = 'testString'
        contract_schema_property_type_model_json['signed'] = 'testString'
        contract_schema_property_type_model_json['native_type'] = 'testString'

        # Construct a model instance of ContractSchemaPropertyType by calling from_dict on the json representation
        contract_schema_property_type_model = ContractSchemaPropertyType.from_dict(contract_schema_property_type_model_json)
        assert contract_schema_property_type_model != False

        # Construct a model instance of ContractSchemaPropertyType by calling from_dict on the json representation
        contract_schema_property_type_model_dict = ContractSchemaPropertyType.from_dict(contract_schema_property_type_model_json).__dict__
        contract_schema_property_type_model2 = ContractSchemaPropertyType(**contract_schema_property_type_model_dict)

        # Verify the model instances are equivalent
        assert contract_schema_property_type_model == contract_schema_property_type_model2

        # Convert model instance back to dict and verify no loss of data
        contract_schema_property_type_model_json2 = contract_schema_property_type_model.to_dict()
        assert contract_schema_property_type_model_json2 == contract_schema_property_type_model_json


class TestModel_ContractTemplateCustomProperty:
    """
    Test Class for ContractTemplateCustomProperty
    """

    def test_contract_template_custom_property_serialization(self):
        """
        Test serialization/deserialization for ContractTemplateCustomProperty
        """

        # Construct a json representation of a ContractTemplateCustomProperty model
        contract_template_custom_property_model_json = {}
        contract_template_custom_property_model_json['key'] = 'customPropertyKey'
        contract_template_custom_property_model_json['value'] = 'customPropertyValue'

        # Construct a model instance of ContractTemplateCustomProperty by calling from_dict on the json representation
        contract_template_custom_property_model = ContractTemplateCustomProperty.from_dict(contract_template_custom_property_model_json)
        assert contract_template_custom_property_model != False

        # Construct a model instance of ContractTemplateCustomProperty by calling from_dict on the json representation
        contract_template_custom_property_model_dict = ContractTemplateCustomProperty.from_dict(contract_template_custom_property_model_json).__dict__
        contract_template_custom_property_model2 = ContractTemplateCustomProperty(**contract_template_custom_property_model_dict)

        # Verify the model instances are equivalent
        assert contract_template_custom_property_model == contract_template_custom_property_model2

        # Convert model instance back to dict and verify no loss of data
        contract_template_custom_property_model_json2 = contract_template_custom_property_model.to_dict()
        assert contract_template_custom_property_model_json2 == contract_template_custom_property_model_json


class TestModel_ContractTemplateOrganization:
    """
    Test Class for ContractTemplateOrganization
    """

    def test_contract_template_organization_serialization(self):
        """
        Test serialization/deserialization for ContractTemplateOrganization
        """

        # Construct a json representation of a ContractTemplateOrganization model
        contract_template_organization_model_json = {}
        contract_template_organization_model_json['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model_json['role'] = 'owner'

        # Construct a model instance of ContractTemplateOrganization by calling from_dict on the json representation
        contract_template_organization_model = ContractTemplateOrganization.from_dict(contract_template_organization_model_json)
        assert contract_template_organization_model != False

        # Construct a model instance of ContractTemplateOrganization by calling from_dict on the json representation
        contract_template_organization_model_dict = ContractTemplateOrganization.from_dict(contract_template_organization_model_json).__dict__
        contract_template_organization_model2 = ContractTemplateOrganization(**contract_template_organization_model_dict)

        # Verify the model instances are equivalent
        assert contract_template_organization_model == contract_template_organization_model2

        # Convert model instance back to dict and verify no loss of data
        contract_template_organization_model_json2 = contract_template_organization_model.to_dict()
        assert contract_template_organization_model_json2 == contract_template_organization_model_json


class TestModel_ContractTemplateSLA:
    """
    Test Class for ContractTemplateSLA
    """

    def test_contract_template_sla_serialization(self):
        """
        Test serialization/deserialization for ContractTemplateSLA
        """

        # Construct dict forms of any model objects needed in order to build this model.

        contract_template_sla_property_model = {}  # ContractTemplateSLAProperty
        contract_template_sla_property_model['property'] = 'Uptime Guarantee'
        contract_template_sla_property_model['value'] = '99.9'

        # Construct a json representation of a ContractTemplateSLA model
        contract_template_sla_model_json = {}
        contract_template_sla_model_json['default_element'] = 'Standard SLA Policy'
        contract_template_sla_model_json['properties'] = [contract_template_sla_property_model]

        # Construct a model instance of ContractTemplateSLA by calling from_dict on the json representation
        contract_template_sla_model = ContractTemplateSLA.from_dict(contract_template_sla_model_json)
        assert contract_template_sla_model != False

        # Construct a model instance of ContractTemplateSLA by calling from_dict on the json representation
        contract_template_sla_model_dict = ContractTemplateSLA.from_dict(contract_template_sla_model_json).__dict__
        contract_template_sla_model2 = ContractTemplateSLA(**contract_template_sla_model_dict)

        # Verify the model instances are equivalent
        assert contract_template_sla_model == contract_template_sla_model2

        # Convert model instance back to dict and verify no loss of data
        contract_template_sla_model_json2 = contract_template_sla_model.to_dict()
        assert contract_template_sla_model_json2 == contract_template_sla_model_json


class TestModel_ContractTemplateSLAProperty:
    """
    Test Class for ContractTemplateSLAProperty
    """

    def test_contract_template_sla_property_serialization(self):
        """
        Test serialization/deserialization for ContractTemplateSLAProperty
        """

        # Construct a json representation of a ContractTemplateSLAProperty model
        contract_template_sla_property_model_json = {}
        contract_template_sla_property_model_json['property'] = 'Uptime Guarantee'
        contract_template_sla_property_model_json['value'] = '99.9'

        # Construct a model instance of ContractTemplateSLAProperty by calling from_dict on the json representation
        contract_template_sla_property_model = ContractTemplateSLAProperty.from_dict(contract_template_sla_property_model_json)
        assert contract_template_sla_property_model != False

        # Construct a model instance of ContractTemplateSLAProperty by calling from_dict on the json representation
        contract_template_sla_property_model_dict = ContractTemplateSLAProperty.from_dict(contract_template_sla_property_model_json).__dict__
        contract_template_sla_property_model2 = ContractTemplateSLAProperty(**contract_template_sla_property_model_dict)

        # Verify the model instances are equivalent
        assert contract_template_sla_property_model == contract_template_sla_property_model2

        # Convert model instance back to dict and verify no loss of data
        contract_template_sla_property_model_json2 = contract_template_sla_property_model.to_dict()
        assert contract_template_sla_property_model_json2 == contract_template_sla_property_model_json


class TestModel_ContractTemplateSupportAndCommunication:
    """
    Test Class for ContractTemplateSupportAndCommunication
    """

    def test_contract_template_support_and_communication_serialization(self):
        """
        Test serialization/deserialization for ContractTemplateSupportAndCommunication
        """

        # Construct a json representation of a ContractTemplateSupportAndCommunication model
        contract_template_support_and_communication_model_json = {}
        contract_template_support_and_communication_model_json['channel'] = 'Email Support'
        contract_template_support_and_communication_model_json['url'] = 'https://support.example.com'

        # Construct a model instance of ContractTemplateSupportAndCommunication by calling from_dict on the json representation
        contract_template_support_and_communication_model = ContractTemplateSupportAndCommunication.from_dict(contract_template_support_and_communication_model_json)
        assert contract_template_support_and_communication_model != False

        # Construct a model instance of ContractTemplateSupportAndCommunication by calling from_dict on the json representation
        contract_template_support_and_communication_model_dict = ContractTemplateSupportAndCommunication.from_dict(contract_template_support_and_communication_model_json).__dict__
        contract_template_support_and_communication_model2 = ContractTemplateSupportAndCommunication(**contract_template_support_and_communication_model_dict)

        # Verify the model instances are equivalent
        assert contract_template_support_and_communication_model == contract_template_support_and_communication_model2

        # Convert model instance back to dict and verify no loss of data
        contract_template_support_and_communication_model_json2 = contract_template_support_and_communication_model.to_dict()
        assert contract_template_support_and_communication_model_json2 == contract_template_support_and_communication_model_json


class TestModel_ContractTerms:
    """
    Test Class for ContractTerms
    """

    def test_contract_terms_serialization(self):
        """
        Test serialization/deserialization for ContractTerms
        """

        # Construct dict forms of any model objects needed in order to build this model.

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        asset_reference_model = {}  # AssetReference
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['name'] = 'testString'
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

        domain_model = {}  # Domain
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        overview_model = {}  # Overview
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = '0.0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        contract_terms_more_info_model = {}  # ContractTermsMoreInfo
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://moreinfo.example.com'

        description_model = {}  # Description
        description_model['purpose'] = 'Used for customer behavior analysis.'
        description_model['limitations'] = 'Data cannot be used for marketing.'
        description_model['usage'] = 'Data should be used only for analytics.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = '{"property1":"value1"}'

        contract_template_organization_model = {}  # ContractTemplateOrganization
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        roles_model = {}  # Roles
        roles_model['role'] = 'owner'

        pricing_model = {}  # Pricing
        pricing_model['amount'] = '100.0'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        contract_template_sla_property_model = {}  # ContractTemplateSLAProperty
        contract_template_sla_property_model['property'] = 'Uptime Guarantee'
        contract_template_sla_property_model['value'] = '99.9'

        contract_template_sla_model = {}  # ContractTemplateSLA
        contract_template_sla_model['default_element'] = 'Standard SLA Policy'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        contract_template_support_and_communication_model = {}  # ContractTemplateSupportAndCommunication
        contract_template_support_and_communication_model['channel'] = 'Email Support'
        contract_template_support_and_communication_model['url'] = 'https://support.example.com'

        contract_template_custom_property_model = {}  # ContractTemplateCustomProperty
        contract_template_custom_property_model['key'] = 'customPropertyKey'
        contract_template_custom_property_model['value'] = 'customPropertyValue'

        contract_test_model = {}  # ContractTest
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        contract_schema_property_type_model = {}  # ContractSchemaPropertyType
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        contract_schema_property_model = {}  # ContractSchemaProperty
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        contract_schema_model = {}  # ContractSchema
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        # Construct a json representation of a ContractTerms model
        contract_terms_model_json = {}
        contract_terms_model_json['asset'] = asset_reference_model
        contract_terms_model_json['id'] = 'testString'
        contract_terms_model_json['documents'] = [contract_terms_document_model]
        contract_terms_model_json['error_msg'] = 'testString'
        contract_terms_model_json['overview'] = overview_model
        contract_terms_model_json['description'] = description_model
        contract_terms_model_json['organization'] = [contract_template_organization_model]
        contract_terms_model_json['roles'] = [roles_model]
        contract_terms_model_json['price'] = pricing_model
        contract_terms_model_json['sla'] = [contract_template_sla_model]
        contract_terms_model_json['support_and_communication'] = [contract_template_support_and_communication_model]
        contract_terms_model_json['custom_properties'] = [contract_template_custom_property_model]
        contract_terms_model_json['contract_test'] = contract_test_model
        contract_terms_model_json['schema'] = [contract_schema_model]

        # Construct a model instance of ContractTerms by calling from_dict on the json representation
        contract_terms_model = ContractTerms.from_dict(contract_terms_model_json)
        assert contract_terms_model != False

        # Construct a model instance of ContractTerms by calling from_dict on the json representation
        contract_terms_model_dict = ContractTerms.from_dict(contract_terms_model_json).__dict__
        contract_terms_model2 = ContractTerms(**contract_terms_model_dict)

        # Verify the model instances are equivalent
        assert contract_terms_model == contract_terms_model2

        # Convert model instance back to dict and verify no loss of data
        contract_terms_model_json2 = contract_terms_model.to_dict()
        assert contract_terms_model_json2 == contract_terms_model_json


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
        contract_terms_document_model_dict = ContractTermsDocument.from_dict(contract_terms_document_model_json).__dict__
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
        contract_terms_document_attachment_model = ContractTermsDocumentAttachment.from_dict(contract_terms_document_attachment_model_json)
        assert contract_terms_document_attachment_model != False

        # Construct a model instance of ContractTermsDocumentAttachment by calling from_dict on the json representation
        contract_terms_document_attachment_model_dict = ContractTermsDocumentAttachment.from_dict(contract_terms_document_attachment_model_json).__dict__
        contract_terms_document_attachment_model2 = ContractTermsDocumentAttachment(**contract_terms_document_attachment_model_dict)

        # Verify the model instances are equivalent
        assert contract_terms_document_attachment_model == contract_terms_document_attachment_model2

        # Convert model instance back to dict and verify no loss of data
        contract_terms_document_attachment_model_json2 = contract_terms_document_attachment_model.to_dict()
        assert contract_terms_document_attachment_model_json2 == contract_terms_document_attachment_model_json


class TestModel_ContractTermsMoreInfo:
    """
    Test Class for ContractTermsMoreInfo
    """

    def test_contract_terms_more_info_serialization(self):
        """
        Test serialization/deserialization for ContractTermsMoreInfo
        """

        # Construct a json representation of a ContractTermsMoreInfo model
        contract_terms_more_info_model_json = {}
        contract_terms_more_info_model_json['type'] = 'privacy-statement'
        contract_terms_more_info_model_json['url'] = 'https://moreinfo.example.com'

        # Construct a model instance of ContractTermsMoreInfo by calling from_dict on the json representation
        contract_terms_more_info_model = ContractTermsMoreInfo.from_dict(contract_terms_more_info_model_json)
        assert contract_terms_more_info_model != False

        # Construct a model instance of ContractTermsMoreInfo by calling from_dict on the json representation
        contract_terms_more_info_model_dict = ContractTermsMoreInfo.from_dict(contract_terms_more_info_model_json).__dict__
        contract_terms_more_info_model2 = ContractTermsMoreInfo(**contract_terms_more_info_model_dict)

        # Verify the model instances are equivalent
        assert contract_terms_more_info_model == contract_terms_more_info_model2

        # Convert model instance back to dict and verify no loss of data
        contract_terms_more_info_model_json2 = contract_terms_more_info_model.to_dict()
        assert contract_terms_more_info_model_json2 == contract_terms_more_info_model_json


class TestModel_ContractTest:
    """
    Test Class for ContractTest
    """

    def test_contract_test_serialization(self):
        """
        Test serialization/deserialization for ContractTest
        """

        # Construct a json representation of a ContractTest model
        contract_test_model_json = {}
        contract_test_model_json['status'] = 'pass'
        contract_test_model_json['last_tested_time'] = 'testString'
        contract_test_model_json['message'] = 'testString'

        # Construct a model instance of ContractTest by calling from_dict on the json representation
        contract_test_model = ContractTest.from_dict(contract_test_model_json)
        assert contract_test_model != False

        # Construct a model instance of ContractTest by calling from_dict on the json representation
        contract_test_model_dict = ContractTest.from_dict(contract_test_model_json).__dict__
        contract_test_model2 = ContractTest(**contract_test_model_dict)

        # Verify the model instances are equivalent
        assert contract_test_model == contract_test_model2

        # Convert model instance back to dict and verify no loss of data
        contract_test_model_json2 = contract_test_model.to_dict()
        assert contract_test_model_json2 == contract_test_model_json


class TestModel_DataAssetRelationship:
    """
    Test Class for DataAssetRelationship
    """

    def test_data_asset_relationship_serialization(self):
        """
        Test serialization/deserialization for DataAssetRelationship
        """

        # Construct dict forms of any model objects needed in order to build this model.

        visualization_model = {}  # Visualization
        visualization_model['id'] = 'testString'
        visualization_model['name'] = 'testString'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        asset_reference_model = {}  # AssetReference
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['name'] = 'testString'
        asset_reference_model['container'] = container_reference_model

        error_message_model = {}  # ErrorMessage
        error_message_model['code'] = 'testString'
        error_message_model['message'] = 'testString'

        # Construct a json representation of a DataAssetRelationship model
        data_asset_relationship_model_json = {}
        data_asset_relationship_model_json['visualization'] = visualization_model
        data_asset_relationship_model_json['asset'] = asset_reference_model
        data_asset_relationship_model_json['related_asset'] = asset_reference_model
        data_asset_relationship_model_json['error'] = error_message_model

        # Construct a model instance of DataAssetRelationship by calling from_dict on the json representation
        data_asset_relationship_model = DataAssetRelationship.from_dict(data_asset_relationship_model_json)
        assert data_asset_relationship_model != False

        # Construct a model instance of DataAssetRelationship by calling from_dict on the json representation
        data_asset_relationship_model_dict = DataAssetRelationship.from_dict(data_asset_relationship_model_json).__dict__
        data_asset_relationship_model2 = DataAssetRelationship(**data_asset_relationship_model_dict)

        # Verify the model instances are equivalent
        assert data_asset_relationship_model == data_asset_relationship_model2

        # Convert model instance back to dict and verify no loss of data
        data_asset_relationship_model_json2 = data_asset_relationship_model.to_dict()
        assert data_asset_relationship_model_json2 == data_asset_relationship_model_json


class TestModel_DataAssetVisualizationRes:
    """
    Test Class for DataAssetVisualizationRes
    """

    def test_data_asset_visualization_res_serialization(self):
        """
        Test serialization/deserialization for DataAssetVisualizationRes
        """

        # Construct dict forms of any model objects needed in order to build this model.

        visualization_model = {}  # Visualization
        visualization_model['id'] = 'testString'
        visualization_model['name'] = 'testString'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        asset_reference_model = {}  # AssetReference
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['name'] = 'testString'
        asset_reference_model['container'] = container_reference_model

        error_message_model = {}  # ErrorMessage
        error_message_model['code'] = 'testString'
        error_message_model['message'] = 'testString'

        data_asset_relationship_model = {}  # DataAssetRelationship
        data_asset_relationship_model['visualization'] = visualization_model
        data_asset_relationship_model['asset'] = asset_reference_model
        data_asset_relationship_model['related_asset'] = asset_reference_model
        data_asset_relationship_model['error'] = error_message_model

        # Construct a json representation of a DataAssetVisualizationRes model
        data_asset_visualization_res_model_json = {}
        data_asset_visualization_res_model_json['results'] = [data_asset_relationship_model]

        # Construct a model instance of DataAssetVisualizationRes by calling from_dict on the json representation
        data_asset_visualization_res_model = DataAssetVisualizationRes.from_dict(data_asset_visualization_res_model_json)
        assert data_asset_visualization_res_model != False

        # Construct a model instance of DataAssetVisualizationRes by calling from_dict on the json representation
        data_asset_visualization_res_model_dict = DataAssetVisualizationRes.from_dict(data_asset_visualization_res_model_json).__dict__
        data_asset_visualization_res_model2 = DataAssetVisualizationRes(**data_asset_visualization_res_model_dict)

        # Verify the model instances are equivalent
        assert data_asset_visualization_res_model == data_asset_visualization_res_model2

        # Convert model instance back to dict and verify no loss of data
        data_asset_visualization_res_model_json2 = data_asset_visualization_res_model.to_dict()
        assert data_asset_visualization_res_model_json2 == data_asset_visualization_res_model_json


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
        asset_reference_model['name'] = 'testString'
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

        domain_model = {}  # Domain
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        overview_model = {}  # Overview
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = '0.0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        contract_terms_more_info_model = {}  # ContractTermsMoreInfo
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://moreinfo.example.com'

        description_model = {}  # Description
        description_model['purpose'] = 'Used for customer behavior analysis.'
        description_model['limitations'] = 'Data cannot be used for marketing.'
        description_model['usage'] = 'Data should be used only for analytics.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = '{"property1":"value1"}'

        contract_template_organization_model = {}  # ContractTemplateOrganization
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        roles_model = {}  # Roles
        roles_model['role'] = 'owner'

        pricing_model = {}  # Pricing
        pricing_model['amount'] = '100.0'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        contract_template_sla_property_model = {}  # ContractTemplateSLAProperty
        contract_template_sla_property_model['property'] = 'Uptime Guarantee'
        contract_template_sla_property_model['value'] = '99.9'

        contract_template_sla_model = {}  # ContractTemplateSLA
        contract_template_sla_model['default_element'] = 'Standard SLA Policy'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        contract_template_support_and_communication_model = {}  # ContractTemplateSupportAndCommunication
        contract_template_support_and_communication_model['channel'] = 'Email Support'
        contract_template_support_and_communication_model['url'] = 'https://support.example.com'

        contract_template_custom_property_model = {}  # ContractTemplateCustomProperty
        contract_template_custom_property_model['key'] = 'customPropertyKey'
        contract_template_custom_property_model['value'] = 'customPropertyValue'

        contract_test_model = {}  # ContractTest
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        contract_schema_property_type_model = {}  # ContractSchemaPropertyType
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        contract_schema_property_model = {}  # ContractSchemaProperty
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        contract_schema_model = {}  # ContractSchema
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        contract_terms_model = {}  # ContractTerms
        contract_terms_model['asset'] = asset_reference_model
        contract_terms_model['id'] = 'testString'
        contract_terms_model['documents'] = [contract_terms_document_model]
        contract_terms_model['error_msg'] = 'testString'
        contract_terms_model['overview'] = overview_model
        contract_terms_model['description'] = description_model
        contract_terms_model['organization'] = [contract_template_organization_model]
        contract_terms_model['roles'] = [roles_model]
        contract_terms_model['price'] = pricing_model
        contract_terms_model['sla'] = [contract_template_sla_model]
        contract_terms_model['support_and_communication'] = [contract_template_support_and_communication_model]
        contract_terms_model['custom_properties'] = [contract_template_custom_property_model]
        contract_terms_model['contract_test'] = contract_test_model
        contract_terms_model['schema'] = [contract_schema_model]

        asset_part_reference_model = {}  # AssetPartReference
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['name'] = 'testString'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        engine_details_model_model = {}  # EngineDetailsModel
        engine_details_model_model['display_name'] = 'Iceberg Engine'
        engine_details_model_model['engine_id'] = 'presto767'
        engine_details_model_model['engine_port'] = '34567'
        engine_details_model_model['engine_host'] = 'a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud'
        engine_details_model_model['associated_catalogs'] = ['testString']

        producer_input_model_model = {}  # ProducerInputModel
        producer_input_model_model['engine_details'] = engine_details_model_model

        delivery_method_properties_model_model = {}  # DeliveryMethodPropertiesModel
        delivery_method_properties_model_model['producer_input'] = producer_input_model_model

        delivery_method_model = {}  # DeliveryMethod
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model
        delivery_method_model['getproperties'] = delivery_method_properties_model_model

        data_product_part_model = {}  # DataProductPart
        data_product_part_model['asset'] = asset_part_reference_model
        data_product_part_model['delivery_methods'] = [delivery_method_model]

        data_product_custom_workflow_definition_model = {}  # DataProductCustomWorkflowDefinition
        data_product_custom_workflow_definition_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        data_product_order_access_request_model = {}  # DataProductOrderAccessRequest
        data_product_order_access_request_model['task_assignee_users'] = ['testString']
        data_product_order_access_request_model['pre_approved_users'] = ['testString']
        data_product_order_access_request_model['custom_workflow_definition'] = data_product_custom_workflow_definition_model

        data_product_workflows_model = {}  # DataProductWorkflows
        data_product_workflows_model['order_access_request'] = data_product_order_access_request_model

        asset_list_access_control_model = {}  # AssetListAccessControl
        asset_list_access_control_model['owner'] = 'IBMid-696000KYV9'

        data_product_version_summary_model = {}  # DataProductVersionSummary
        data_product_version_summary_model['version'] = '1.0.0'
        data_product_version_summary_model['state'] = 'draft'
        data_product_version_summary_model['data_product'] = data_product_version_summary_data_product_model
        data_product_version_summary_model['name'] = 'My Data Product'
        data_product_version_summary_model['description'] = 'This is a description of My Data Product.'
        data_product_version_summary_model['tags'] = ['testString']
        data_product_version_summary_model['use_cases'] = [use_case_model]
        data_product_version_summary_model['types'] = ['data']
        data_product_version_summary_model['contract_terms'] = [contract_terms_model]
        data_product_version_summary_model['domain'] = domain_model
        data_product_version_summary_model['parts_out'] = [data_product_part_model]
        data_product_version_summary_model['workflows'] = data_product_workflows_model
        data_product_version_summary_model['dataview_enabled'] = True
        data_product_version_summary_model['comments'] = 'Comments by a producer that are provided either at the time of data product version creation or retiring'
        data_product_version_summary_model['access_control'] = asset_list_access_control_model
        data_product_version_summary_model['last_updated_at'] = '2019-01-01T12:00:00Z'
        data_product_version_summary_model['is_restricted'] = True
        data_product_version_summary_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd'
        data_product_version_summary_model['asset'] = asset_reference_model

        # Construct a json representation of a DataProduct model
        data_product_model_json = {}
        data_product_model_json['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_model_json['release'] = data_product_draft_version_release_model
        data_product_model_json['container'] = container_reference_model
        data_product_model_json['name'] = 'testString'
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


class TestModel_DataProductCollection:
    """
    Test Class for DataProductCollection
    """

    def test_data_product_collection_serialization(self):
        """
        Test serialization/deserialization for DataProductCollection
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
        data_product_summary_model['name'] = 'testString'

        # Construct a json representation of a DataProductCollection model
        data_product_collection_model_json = {}
        data_product_collection_model_json['limit'] = 200
        data_product_collection_model_json['first'] = first_page_model
        data_product_collection_model_json['next'] = next_page_model
        data_product_collection_model_json['total_results'] = 200
        data_product_collection_model_json['data_products'] = [data_product_summary_model]

        # Construct a model instance of DataProductCollection by calling from_dict on the json representation
        data_product_collection_model = DataProductCollection.from_dict(data_product_collection_model_json)
        assert data_product_collection_model != False

        # Construct a model instance of DataProductCollection by calling from_dict on the json representation
        data_product_collection_model_dict = DataProductCollection.from_dict(data_product_collection_model_json).__dict__
        data_product_collection_model2 = DataProductCollection(**data_product_collection_model_dict)

        # Verify the model instances are equivalent
        assert data_product_collection_model == data_product_collection_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_collection_model_json2 = data_product_collection_model.to_dict()
        assert data_product_collection_model_json2 == data_product_collection_model_json


class TestModel_DataProductContractTemplate:
    """
    Test Class for DataProductContractTemplate
    """

    def test_data_product_contract_template_serialization(self):
        """
        Test serialization/deserialization for DataProductContractTemplate
        """

        # Construct dict forms of any model objects needed in order to build this model.

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        error_message_model = {}  # ErrorMessage
        error_message_model['code'] = 'testString'
        error_message_model['message'] = 'testString'

        asset_reference_model = {}  # AssetReference
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['name'] = 'testString'
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

        domain_model = {}  # Domain
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        overview_model = {}  # Overview
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = '0.0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        contract_terms_more_info_model = {}  # ContractTermsMoreInfo
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://moreinfo.example.com'

        description_model = {}  # Description
        description_model['purpose'] = 'Used for customer behavior analysis.'
        description_model['limitations'] = 'Data cannot be used for marketing.'
        description_model['usage'] = 'Data should be used only for analytics.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = '{"property1":"value1"}'

        contract_template_organization_model = {}  # ContractTemplateOrganization
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        roles_model = {}  # Roles
        roles_model['role'] = 'owner'

        pricing_model = {}  # Pricing
        pricing_model['amount'] = '100.0'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        contract_template_sla_property_model = {}  # ContractTemplateSLAProperty
        contract_template_sla_property_model['property'] = 'Uptime Guarantee'
        contract_template_sla_property_model['value'] = '99.9'

        contract_template_sla_model = {}  # ContractTemplateSLA
        contract_template_sla_model['default_element'] = 'Standard SLA Policy'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        contract_template_support_and_communication_model = {}  # ContractTemplateSupportAndCommunication
        contract_template_support_and_communication_model['channel'] = 'Email Support'
        contract_template_support_and_communication_model['url'] = 'https://support.example.com'

        contract_template_custom_property_model = {}  # ContractTemplateCustomProperty
        contract_template_custom_property_model['key'] = 'customPropertyKey'
        contract_template_custom_property_model['value'] = 'customPropertyValue'

        contract_test_model = {}  # ContractTest
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        contract_schema_property_type_model = {}  # ContractSchemaPropertyType
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        contract_schema_property_model = {}  # ContractSchemaProperty
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        contract_schema_model = {}  # ContractSchema
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        contract_terms_model = {}  # ContractTerms
        contract_terms_model['asset'] = asset_reference_model
        contract_terms_model['id'] = 'testString'
        contract_terms_model['documents'] = [contract_terms_document_model]
        contract_terms_model['error_msg'] = 'testString'
        contract_terms_model['overview'] = overview_model
        contract_terms_model['description'] = description_model
        contract_terms_model['organization'] = [contract_template_organization_model]
        contract_terms_model['roles'] = [roles_model]
        contract_terms_model['price'] = pricing_model
        contract_terms_model['sla'] = [contract_template_sla_model]
        contract_terms_model['support_and_communication'] = [contract_template_support_and_communication_model]
        contract_terms_model['custom_properties'] = [contract_template_custom_property_model]
        contract_terms_model['contract_test'] = contract_test_model
        contract_terms_model['schema'] = [contract_schema_model]

        # Construct a json representation of a DataProductContractTemplate model
        data_product_contract_template_model_json = {}
        data_product_contract_template_model_json['container'] = container_reference_model
        data_product_contract_template_model_json['id'] = '20aa7c97-cfcc-4d16-ae76-2ca1847ce733'
        data_product_contract_template_model_json['name'] = 'Sample Data Contract Template'
        data_product_contract_template_model_json['error'] = error_message_model
        data_product_contract_template_model_json['contract_terms'] = contract_terms_model

        # Construct a model instance of DataProductContractTemplate by calling from_dict on the json representation
        data_product_contract_template_model = DataProductContractTemplate.from_dict(data_product_contract_template_model_json)
        assert data_product_contract_template_model != False

        # Construct a model instance of DataProductContractTemplate by calling from_dict on the json representation
        data_product_contract_template_model_dict = DataProductContractTemplate.from_dict(data_product_contract_template_model_json).__dict__
        data_product_contract_template_model2 = DataProductContractTemplate(**data_product_contract_template_model_dict)

        # Verify the model instances are equivalent
        assert data_product_contract_template_model == data_product_contract_template_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_contract_template_model_json2 = data_product_contract_template_model.to_dict()
        assert data_product_contract_template_model_json2 == data_product_contract_template_model_json


class TestModel_DataProductContractTemplateCollection:
    """
    Test Class for DataProductContractTemplateCollection
    """

    def test_data_product_contract_template_collection_serialization(self):
        """
        Test serialization/deserialization for DataProductContractTemplateCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        error_message_model = {}  # ErrorMessage
        error_message_model['code'] = 'testString'
        error_message_model['message'] = 'testString'

        asset_reference_model = {}  # AssetReference
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['name'] = 'testString'
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

        domain_model = {}  # Domain
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        overview_model = {}  # Overview
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = '0.0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        contract_terms_more_info_model = {}  # ContractTermsMoreInfo
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://moreinfo.example.com'

        description_model = {}  # Description
        description_model['purpose'] = 'Used for customer behavior analysis.'
        description_model['limitations'] = 'Data cannot be used for marketing.'
        description_model['usage'] = 'Data should be used only for analytics.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = '{"property1":"value1"}'

        contract_template_organization_model = {}  # ContractTemplateOrganization
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        roles_model = {}  # Roles
        roles_model['role'] = 'owner'

        pricing_model = {}  # Pricing
        pricing_model['amount'] = '100.0'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        contract_template_sla_property_model = {}  # ContractTemplateSLAProperty
        contract_template_sla_property_model['property'] = 'Uptime Guarantee'
        contract_template_sla_property_model['value'] = '99.9'

        contract_template_sla_model = {}  # ContractTemplateSLA
        contract_template_sla_model['default_element'] = 'Standard SLA Policy'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        contract_template_support_and_communication_model = {}  # ContractTemplateSupportAndCommunication
        contract_template_support_and_communication_model['channel'] = 'Email Support'
        contract_template_support_and_communication_model['url'] = 'https://support.example.com'

        contract_template_custom_property_model = {}  # ContractTemplateCustomProperty
        contract_template_custom_property_model['key'] = 'customPropertyKey'
        contract_template_custom_property_model['value'] = 'customPropertyValue'

        contract_test_model = {}  # ContractTest
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        contract_schema_property_type_model = {}  # ContractSchemaPropertyType
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        contract_schema_property_model = {}  # ContractSchemaProperty
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        contract_schema_model = {}  # ContractSchema
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        contract_terms_model = {}  # ContractTerms
        contract_terms_model['asset'] = asset_reference_model
        contract_terms_model['id'] = 'testString'
        contract_terms_model['documents'] = [contract_terms_document_model]
        contract_terms_model['error_msg'] = 'testString'
        contract_terms_model['overview'] = overview_model
        contract_terms_model['description'] = description_model
        contract_terms_model['organization'] = [contract_template_organization_model]
        contract_terms_model['roles'] = [roles_model]
        contract_terms_model['price'] = pricing_model
        contract_terms_model['sla'] = [contract_template_sla_model]
        contract_terms_model['support_and_communication'] = [contract_template_support_and_communication_model]
        contract_terms_model['custom_properties'] = [contract_template_custom_property_model]
        contract_terms_model['contract_test'] = contract_test_model
        contract_terms_model['schema'] = [contract_schema_model]

        data_product_contract_template_model = {}  # DataProductContractTemplate
        data_product_contract_template_model['container'] = container_reference_model
        data_product_contract_template_model['id'] = '20aa7c97-cfcc-4d16-ae76-2ca1847ce733'
        data_product_contract_template_model['name'] = 'Sample Data Contract Template'
        data_product_contract_template_model['error'] = error_message_model
        data_product_contract_template_model['contract_terms'] = contract_terms_model

        # Construct a json representation of a DataProductContractTemplateCollection model
        data_product_contract_template_collection_model_json = {}
        data_product_contract_template_collection_model_json['contract_templates'] = [data_product_contract_template_model]

        # Construct a model instance of DataProductContractTemplateCollection by calling from_dict on the json representation
        data_product_contract_template_collection_model = DataProductContractTemplateCollection.from_dict(data_product_contract_template_collection_model_json)
        assert data_product_contract_template_collection_model != False

        # Construct a model instance of DataProductContractTemplateCollection by calling from_dict on the json representation
        data_product_contract_template_collection_model_dict = DataProductContractTemplateCollection.from_dict(data_product_contract_template_collection_model_json).__dict__
        data_product_contract_template_collection_model2 = DataProductContractTemplateCollection(**data_product_contract_template_collection_model_dict)

        # Verify the model instances are equivalent
        assert data_product_contract_template_collection_model == data_product_contract_template_collection_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_contract_template_collection_model_json2 = data_product_contract_template_collection_model.to_dict()
        assert data_product_contract_template_collection_model_json2 == data_product_contract_template_collection_model_json


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
        data_product_custom_workflow_definition_model = DataProductCustomWorkflowDefinition.from_dict(data_product_custom_workflow_definition_model_json)
        assert data_product_custom_workflow_definition_model != False

        # Construct a model instance of DataProductCustomWorkflowDefinition by calling from_dict on the json representation
        data_product_custom_workflow_definition_model_dict = DataProductCustomWorkflowDefinition.from_dict(data_product_custom_workflow_definition_model_json).__dict__
        data_product_custom_workflow_definition_model2 = DataProductCustomWorkflowDefinition(**data_product_custom_workflow_definition_model_dict)

        # Verify the model instances are equivalent
        assert data_product_custom_workflow_definition_model == data_product_custom_workflow_definition_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_custom_workflow_definition_model_json2 = data_product_custom_workflow_definition_model.to_dict()
        assert data_product_custom_workflow_definition_model_json2 == data_product_custom_workflow_definition_model_json


class TestModel_DataProductDomain:
    """
    Test Class for DataProductDomain
    """

    def test_data_product_domain_serialization(self):
        """
        Test serialization/deserialization for DataProductDomain
        """

        # Construct dict forms of any model objects needed in order to build this model.

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        error_extra_resource_model = {}  # ErrorExtraResource
        error_extra_resource_model['id'] = 'testString'
        error_extra_resource_model['timestamp'] = '2019-01-01T12:00:00Z'
        error_extra_resource_model['environment_name'] = 'testString'
        error_extra_resource_model['http_status'] = 0
        error_extra_resource_model['source_cluster'] = 0
        error_extra_resource_model['source_component'] = 0
        error_extra_resource_model['transaction_id'] = 0

        error_model_resource_model = {}  # ErrorModelResource
        error_model_resource_model['code'] = 'request_body_error'
        error_model_resource_model['message'] = 'testString'
        error_model_resource_model['extra'] = error_extra_resource_model
        error_model_resource_model['more_info'] = 'testString'

        member_roles_schema_model = {}  # MemberRolesSchema
        member_roles_schema_model['user_iam_id'] = 'testString'
        member_roles_schema_model['roles'] = ['testString']

        properties_schema_model = {}  # PropertiesSchema
        properties_schema_model['value'] = 'testString'

        initialize_sub_domain_model = {}  # InitializeSubDomain
        initialize_sub_domain_model['name'] = 'Operations'
        initialize_sub_domain_model['id'] = 'testString'
        initialize_sub_domain_model['description'] = 'testString'

        # Construct a json representation of a DataProductDomain model
        data_product_domain_model_json = {}
        data_product_domain_model_json['container'] = container_reference_model
        data_product_domain_model_json['trace'] = 'testString'
        data_product_domain_model_json['errors'] = [error_model_resource_model]
        data_product_domain_model_json['name'] = 'Operations'
        data_product_domain_model_json['description'] = 'This is a description of the data product domain.'
        data_product_domain_model_json['id'] = 'testString'
        data_product_domain_model_json['member_roles'] = member_roles_schema_model
        data_product_domain_model_json['properties'] = properties_schema_model
        data_product_domain_model_json['sub_domains'] = [initialize_sub_domain_model]

        # Construct a model instance of DataProductDomain by calling from_dict on the json representation
        data_product_domain_model = DataProductDomain.from_dict(data_product_domain_model_json)
        assert data_product_domain_model != False

        # Construct a model instance of DataProductDomain by calling from_dict on the json representation
        data_product_domain_model_dict = DataProductDomain.from_dict(data_product_domain_model_json).__dict__
        data_product_domain_model2 = DataProductDomain(**data_product_domain_model_dict)

        # Verify the model instances are equivalent
        assert data_product_domain_model == data_product_domain_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_domain_model_json2 = data_product_domain_model.to_dict()
        assert data_product_domain_model_json2 == data_product_domain_model_json


class TestModel_DataProductDomainCollection:
    """
    Test Class for DataProductDomainCollection
    """

    def test_data_product_domain_collection_serialization(self):
        """
        Test serialization/deserialization for DataProductDomainCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        error_extra_resource_model = {}  # ErrorExtraResource
        error_extra_resource_model['id'] = 'testString'
        error_extra_resource_model['timestamp'] = '2019-01-01T12:00:00Z'
        error_extra_resource_model['environment_name'] = 'testString'
        error_extra_resource_model['http_status'] = 0
        error_extra_resource_model['source_cluster'] = 0
        error_extra_resource_model['source_component'] = 0
        error_extra_resource_model['transaction_id'] = 0

        error_model_resource_model = {}  # ErrorModelResource
        error_model_resource_model['code'] = 'request_body_error'
        error_model_resource_model['message'] = 'testString'
        error_model_resource_model['extra'] = error_extra_resource_model
        error_model_resource_model['more_info'] = 'testString'

        member_roles_schema_model = {}  # MemberRolesSchema
        member_roles_schema_model['user_iam_id'] = 'testString'
        member_roles_schema_model['roles'] = ['testString']

        properties_schema_model = {}  # PropertiesSchema
        properties_schema_model['value'] = 'testString'

        initialize_sub_domain_model = {}  # InitializeSubDomain
        initialize_sub_domain_model['name'] = 'Operations'
        initialize_sub_domain_model['id'] = 'testString'
        initialize_sub_domain_model['description'] = 'testString'

        data_product_domain_model = {}  # DataProductDomain
        data_product_domain_model['container'] = container_reference_model
        data_product_domain_model['trace'] = 'testString'
        data_product_domain_model['errors'] = [error_model_resource_model]
        data_product_domain_model['name'] = 'Operations'
        data_product_domain_model['description'] = 'This is a description of the data product domain.'
        data_product_domain_model['id'] = 'testString'
        data_product_domain_model['member_roles'] = member_roles_schema_model
        data_product_domain_model['properties'] = properties_schema_model
        data_product_domain_model['sub_domains'] = [initialize_sub_domain_model]

        # Construct a json representation of a DataProductDomainCollection model
        data_product_domain_collection_model_json = {}
        data_product_domain_collection_model_json['domains'] = [data_product_domain_model]

        # Construct a model instance of DataProductDomainCollection by calling from_dict on the json representation
        data_product_domain_collection_model = DataProductDomainCollection.from_dict(data_product_domain_collection_model_json)
        assert data_product_domain_collection_model != False

        # Construct a model instance of DataProductDomainCollection by calling from_dict on the json representation
        data_product_domain_collection_model_dict = DataProductDomainCollection.from_dict(data_product_domain_collection_model_json).__dict__
        data_product_domain_collection_model2 = DataProductDomainCollection(**data_product_domain_collection_model_dict)

        # Verify the model instances are equivalent
        assert data_product_domain_collection_model == data_product_domain_collection_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_domain_collection_model_json2 = data_product_domain_collection_model.to_dict()
        assert data_product_domain_collection_model_json2 == data_product_domain_collection_model_json


class TestModel_DataProductDraft:
    """
    Test Class for DataProductDraft
    """

    def test_data_product_draft_serialization(self):
        """
        Test serialization/deserialization for DataProductDraft
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_product_draft_version_release_model = {}  # DataProductDraftVersionRelease
        data_product_draft_version_release_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        data_product_draft_data_product_model = {}  # DataProductDraftDataProduct
        data_product_draft_data_product_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_draft_data_product_model['release'] = data_product_draft_version_release_model
        data_product_draft_data_product_model['container'] = container_reference_model

        use_case_model = {}  # UseCase
        use_case_model['id'] = 'testString'
        use_case_model['name'] = 'testString'
        use_case_model['container'] = container_reference_model

        asset_reference_model = {}  # AssetReference
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['name'] = 'testString'
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

        domain_model = {}  # Domain
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        overview_model = {}  # Overview
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = '0.0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        contract_terms_more_info_model = {}  # ContractTermsMoreInfo
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://moreinfo.example.com'

        description_model = {}  # Description
        description_model['purpose'] = 'Used for customer behavior analysis.'
        description_model['limitations'] = 'Data cannot be used for marketing.'
        description_model['usage'] = 'Data should be used only for analytics.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = '{"property1":"value1"}'

        contract_template_organization_model = {}  # ContractTemplateOrganization
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        roles_model = {}  # Roles
        roles_model['role'] = 'owner'

        pricing_model = {}  # Pricing
        pricing_model['amount'] = '100.0'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        contract_template_sla_property_model = {}  # ContractTemplateSLAProperty
        contract_template_sla_property_model['property'] = 'Uptime Guarantee'
        contract_template_sla_property_model['value'] = '99.9'

        contract_template_sla_model = {}  # ContractTemplateSLA
        contract_template_sla_model['default_element'] = 'Standard SLA Policy'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        contract_template_support_and_communication_model = {}  # ContractTemplateSupportAndCommunication
        contract_template_support_and_communication_model['channel'] = 'Email Support'
        contract_template_support_and_communication_model['url'] = 'https://support.example.com'

        contract_template_custom_property_model = {}  # ContractTemplateCustomProperty
        contract_template_custom_property_model['key'] = 'customPropertyKey'
        contract_template_custom_property_model['value'] = 'customPropertyValue'

        contract_test_model = {}  # ContractTest
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        contract_schema_property_type_model = {}  # ContractSchemaPropertyType
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        contract_schema_property_model = {}  # ContractSchemaProperty
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        contract_schema_model = {}  # ContractSchema
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        contract_terms_model = {}  # ContractTerms
        contract_terms_model['asset'] = asset_reference_model
        contract_terms_model['id'] = 'testString'
        contract_terms_model['documents'] = [contract_terms_document_model]
        contract_terms_model['error_msg'] = 'testString'
        contract_terms_model['overview'] = overview_model
        contract_terms_model['description'] = description_model
        contract_terms_model['organization'] = [contract_template_organization_model]
        contract_terms_model['roles'] = [roles_model]
        contract_terms_model['price'] = pricing_model
        contract_terms_model['sla'] = [contract_template_sla_model]
        contract_terms_model['support_and_communication'] = [contract_template_support_and_communication_model]
        contract_terms_model['custom_properties'] = [contract_template_custom_property_model]
        contract_terms_model['contract_test'] = contract_test_model
        contract_terms_model['schema'] = [contract_schema_model]

        asset_part_reference_model = {}  # AssetPartReference
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['name'] = 'testString'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        engine_details_model_model = {}  # EngineDetailsModel
        engine_details_model_model['display_name'] = 'Iceberg Engine'
        engine_details_model_model['engine_id'] = 'presto767'
        engine_details_model_model['engine_port'] = '34567'
        engine_details_model_model['engine_host'] = 'a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud'
        engine_details_model_model['associated_catalogs'] = ['testString']

        producer_input_model_model = {}  # ProducerInputModel
        producer_input_model_model['engine_details'] = engine_details_model_model

        delivery_method_properties_model_model = {}  # DeliveryMethodPropertiesModel
        delivery_method_properties_model_model['producer_input'] = producer_input_model_model

        delivery_method_model = {}  # DeliveryMethod
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model
        delivery_method_model['getproperties'] = delivery_method_properties_model_model

        data_product_part_model = {}  # DataProductPart
        data_product_part_model['asset'] = asset_part_reference_model
        data_product_part_model['delivery_methods'] = [delivery_method_model]

        data_product_custom_workflow_definition_model = {}  # DataProductCustomWorkflowDefinition
        data_product_custom_workflow_definition_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        data_product_order_access_request_model = {}  # DataProductOrderAccessRequest
        data_product_order_access_request_model['task_assignee_users'] = ['testString']
        data_product_order_access_request_model['pre_approved_users'] = ['testString']
        data_product_order_access_request_model['custom_workflow_definition'] = data_product_custom_workflow_definition_model

        data_product_workflows_model = {}  # DataProductWorkflows
        data_product_workflows_model['order_access_request'] = data_product_order_access_request_model

        asset_list_access_control_model = {}  # AssetListAccessControl
        asset_list_access_control_model['owner'] = 'IBMid-696000KYV9'

        visualization_model = {}  # Visualization
        visualization_model['id'] = 'testString'
        visualization_model['name'] = 'testString'

        error_message_model = {}  # ErrorMessage
        error_message_model['code'] = 'testString'
        error_message_model['message'] = 'testString'

        data_asset_relationship_model = {}  # DataAssetRelationship
        data_asset_relationship_model['visualization'] = visualization_model
        data_asset_relationship_model['asset'] = asset_reference_model
        data_asset_relationship_model['related_asset'] = asset_reference_model
        data_asset_relationship_model['error'] = error_message_model

        # Construct a json representation of a DataProductDraft model
        data_product_draft_model_json = {}
        data_product_draft_model_json['version'] = '1.0.0'
        data_product_draft_model_json['state'] = 'draft'
        data_product_draft_model_json['data_product'] = data_product_draft_data_product_model
        data_product_draft_model_json['name'] = 'My Data Product'
        data_product_draft_model_json['description'] = 'This is a description of My Data Product.'
        data_product_draft_model_json['tags'] = ['testString']
        data_product_draft_model_json['use_cases'] = [use_case_model]
        data_product_draft_model_json['types'] = ['data']
        data_product_draft_model_json['contract_terms'] = [contract_terms_model]
        data_product_draft_model_json['domain'] = domain_model
        data_product_draft_model_json['parts_out'] = [data_product_part_model]
        data_product_draft_model_json['workflows'] = data_product_workflows_model
        data_product_draft_model_json['dataview_enabled'] = True
        data_product_draft_model_json['comments'] = 'Comments by a producer that are provided either at the time of data product version creation or retiring'
        data_product_draft_model_json['access_control'] = asset_list_access_control_model
        data_product_draft_model_json['last_updated_at'] = '2019-01-01T12:00:00Z'
        data_product_draft_model_json['is_restricted'] = True
        data_product_draft_model_json['id'] = '2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd'
        data_product_draft_model_json['asset'] = asset_reference_model
        data_product_draft_model_json['published_by'] = 'testString'
        data_product_draft_model_json['published_at'] = '2019-01-01T12:00:00Z'
        data_product_draft_model_json['created_by'] = 'testString'
        data_product_draft_model_json['created_at'] = '2019-01-01T12:00:00Z'
        data_product_draft_model_json['properties'] = {'anyKey': 'anyValue'}
        data_product_draft_model_json['visualization_errors'] = [data_asset_relationship_model]

        # Construct a model instance of DataProductDraft by calling from_dict on the json representation
        data_product_draft_model = DataProductDraft.from_dict(data_product_draft_model_json)
        assert data_product_draft_model != False

        # Construct a model instance of DataProductDraft by calling from_dict on the json representation
        data_product_draft_model_dict = DataProductDraft.from_dict(data_product_draft_model_json).__dict__
        data_product_draft_model2 = DataProductDraft(**data_product_draft_model_dict)

        # Verify the model instances are equivalent
        assert data_product_draft_model == data_product_draft_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_draft_model_json2 = data_product_draft_model.to_dict()
        assert data_product_draft_model_json2 == data_product_draft_model_json


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

        data_product_draft_summary_data_product_model = {}  # DataProductDraftSummaryDataProduct
        data_product_draft_summary_data_product_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_draft_summary_data_product_model['release'] = data_product_draft_version_release_model
        data_product_draft_summary_data_product_model['container'] = container_reference_model

        use_case_model = {}  # UseCase
        use_case_model['id'] = 'testString'
        use_case_model['name'] = 'testString'
        use_case_model['container'] = container_reference_model

        asset_reference_model = {}  # AssetReference
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['name'] = 'testString'
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

        domain_model = {}  # Domain
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        overview_model = {}  # Overview
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = '0.0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        contract_terms_more_info_model = {}  # ContractTermsMoreInfo
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://moreinfo.example.com'

        description_model = {}  # Description
        description_model['purpose'] = 'Used for customer behavior analysis.'
        description_model['limitations'] = 'Data cannot be used for marketing.'
        description_model['usage'] = 'Data should be used only for analytics.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = '{"property1":"value1"}'

        contract_template_organization_model = {}  # ContractTemplateOrganization
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        roles_model = {}  # Roles
        roles_model['role'] = 'owner'

        pricing_model = {}  # Pricing
        pricing_model['amount'] = '100.0'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        contract_template_sla_property_model = {}  # ContractTemplateSLAProperty
        contract_template_sla_property_model['property'] = 'Uptime Guarantee'
        contract_template_sla_property_model['value'] = '99.9'

        contract_template_sla_model = {}  # ContractTemplateSLA
        contract_template_sla_model['default_element'] = 'Standard SLA Policy'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        contract_template_support_and_communication_model = {}  # ContractTemplateSupportAndCommunication
        contract_template_support_and_communication_model['channel'] = 'Email Support'
        contract_template_support_and_communication_model['url'] = 'https://support.example.com'

        contract_template_custom_property_model = {}  # ContractTemplateCustomProperty
        contract_template_custom_property_model['key'] = 'customPropertyKey'
        contract_template_custom_property_model['value'] = 'customPropertyValue'

        contract_test_model = {}  # ContractTest
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        contract_schema_property_type_model = {}  # ContractSchemaPropertyType
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        contract_schema_property_model = {}  # ContractSchemaProperty
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        contract_schema_model = {}  # ContractSchema
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        contract_terms_model = {}  # ContractTerms
        contract_terms_model['asset'] = asset_reference_model
        contract_terms_model['id'] = 'testString'
        contract_terms_model['documents'] = [contract_terms_document_model]
        contract_terms_model['error_msg'] = 'testString'
        contract_terms_model['overview'] = overview_model
        contract_terms_model['description'] = description_model
        contract_terms_model['organization'] = [contract_template_organization_model]
        contract_terms_model['roles'] = [roles_model]
        contract_terms_model['price'] = pricing_model
        contract_terms_model['sla'] = [contract_template_sla_model]
        contract_terms_model['support_and_communication'] = [contract_template_support_and_communication_model]
        contract_terms_model['custom_properties'] = [contract_template_custom_property_model]
        contract_terms_model['contract_test'] = contract_test_model
        contract_terms_model['schema'] = [contract_schema_model]

        asset_part_reference_model = {}  # AssetPartReference
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['name'] = 'testString'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        engine_details_model_model = {}  # EngineDetailsModel
        engine_details_model_model['display_name'] = 'Iceberg Engine'
        engine_details_model_model['engine_id'] = 'presto767'
        engine_details_model_model['engine_port'] = '34567'
        engine_details_model_model['engine_host'] = 'a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud'
        engine_details_model_model['associated_catalogs'] = ['testString']

        producer_input_model_model = {}  # ProducerInputModel
        producer_input_model_model['engine_details'] = engine_details_model_model

        delivery_method_properties_model_model = {}  # DeliveryMethodPropertiesModel
        delivery_method_properties_model_model['producer_input'] = producer_input_model_model

        delivery_method_model = {}  # DeliveryMethod
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model
        delivery_method_model['getproperties'] = delivery_method_properties_model_model

        data_product_part_model = {}  # DataProductPart
        data_product_part_model['asset'] = asset_part_reference_model
        data_product_part_model['delivery_methods'] = [delivery_method_model]

        data_product_custom_workflow_definition_model = {}  # DataProductCustomWorkflowDefinition
        data_product_custom_workflow_definition_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        data_product_order_access_request_model = {}  # DataProductOrderAccessRequest
        data_product_order_access_request_model['task_assignee_users'] = ['testString']
        data_product_order_access_request_model['pre_approved_users'] = ['testString']
        data_product_order_access_request_model['custom_workflow_definition'] = data_product_custom_workflow_definition_model

        data_product_workflows_model = {}  # DataProductWorkflows
        data_product_workflows_model['order_access_request'] = data_product_order_access_request_model

        asset_list_access_control_model = {}  # AssetListAccessControl
        asset_list_access_control_model['owner'] = 'IBMid-696000KYV9'

        data_product_draft_summary_model = {}  # DataProductDraftSummary
        data_product_draft_summary_model['version'] = '1.0.0'
        data_product_draft_summary_model['state'] = 'draft'
        data_product_draft_summary_model['data_product'] = data_product_draft_summary_data_product_model
        data_product_draft_summary_model['name'] = 'My Data Product'
        data_product_draft_summary_model['description'] = 'This is a description of My Data Product.'
        data_product_draft_summary_model['tags'] = ['testString']
        data_product_draft_summary_model['use_cases'] = [use_case_model]
        data_product_draft_summary_model['types'] = ['data']
        data_product_draft_summary_model['contract_terms'] = [contract_terms_model]
        data_product_draft_summary_model['domain'] = domain_model
        data_product_draft_summary_model['parts_out'] = [data_product_part_model]
        data_product_draft_summary_model['workflows'] = data_product_workflows_model
        data_product_draft_summary_model['dataview_enabled'] = True
        data_product_draft_summary_model['comments'] = 'Comments by a producer that are provided either at the time of data product version creation or retiring'
        data_product_draft_summary_model['access_control'] = asset_list_access_control_model
        data_product_draft_summary_model['last_updated_at'] = '2019-01-01T12:00:00Z'
        data_product_draft_summary_model['is_restricted'] = True
        data_product_draft_summary_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd'
        data_product_draft_summary_model['asset'] = asset_reference_model

        # Construct a json representation of a DataProductDraftCollection model
        data_product_draft_collection_model_json = {}
        data_product_draft_collection_model_json['limit'] = 200
        data_product_draft_collection_model_json['first'] = first_page_model
        data_product_draft_collection_model_json['next'] = next_page_model
        data_product_draft_collection_model_json['total_results'] = 200
        data_product_draft_collection_model_json['drafts'] = [data_product_draft_summary_model]

        # Construct a model instance of DataProductDraftCollection by calling from_dict on the json representation
        data_product_draft_collection_model = DataProductDraftCollection.from_dict(data_product_draft_collection_model_json)
        assert data_product_draft_collection_model != False

        # Construct a model instance of DataProductDraftCollection by calling from_dict on the json representation
        data_product_draft_collection_model_dict = DataProductDraftCollection.from_dict(data_product_draft_collection_model_json).__dict__
        data_product_draft_collection_model2 = DataProductDraftCollection(**data_product_draft_collection_model_dict)

        # Verify the model instances are equivalent
        assert data_product_draft_collection_model == data_product_draft_collection_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_draft_collection_model_json2 = data_product_draft_collection_model.to_dict()
        assert data_product_draft_collection_model_json2 == data_product_draft_collection_model_json


class TestModel_DataProductDraftDataProduct:
    """
    Test Class for DataProductDraftDataProduct
    """

    def test_data_product_draft_data_product_serialization(self):
        """
        Test serialization/deserialization for DataProductDraftDataProduct
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_product_draft_version_release_model = {}  # DataProductDraftVersionRelease
        data_product_draft_version_release_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Construct a json representation of a DataProductDraftDataProduct model
        data_product_draft_data_product_model_json = {}
        data_product_draft_data_product_model_json['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_draft_data_product_model_json['release'] = data_product_draft_version_release_model
        data_product_draft_data_product_model_json['container'] = container_reference_model

        # Construct a model instance of DataProductDraftDataProduct by calling from_dict on the json representation
        data_product_draft_data_product_model = DataProductDraftDataProduct.from_dict(data_product_draft_data_product_model_json)
        assert data_product_draft_data_product_model != False

        # Construct a model instance of DataProductDraftDataProduct by calling from_dict on the json representation
        data_product_draft_data_product_model_dict = DataProductDraftDataProduct.from_dict(data_product_draft_data_product_model_json).__dict__
        data_product_draft_data_product_model2 = DataProductDraftDataProduct(**data_product_draft_data_product_model_dict)

        # Verify the model instances are equivalent
        assert data_product_draft_data_product_model == data_product_draft_data_product_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_draft_data_product_model_json2 = data_product_draft_data_product_model.to_dict()
        assert data_product_draft_data_product_model_json2 == data_product_draft_data_product_model_json


class TestModel_DataProductDraftPrototype:
    """
    Test Class for DataProductDraftPrototype
    """

    def test_data_product_draft_prototype_serialization(self):
        """
        Test serialization/deserialization for DataProductDraftPrototype
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
        asset_reference_model['name'] = 'testString'
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

        domain_model = {}  # Domain
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        overview_model = {}  # Overview
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = '0.0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        contract_terms_more_info_model = {}  # ContractTermsMoreInfo
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://moreinfo.example.com'

        description_model = {}  # Description
        description_model['purpose'] = 'Used for customer behavior analysis.'
        description_model['limitations'] = 'Data cannot be used for marketing.'
        description_model['usage'] = 'Data should be used only for analytics.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = '{"property1":"value1"}'

        contract_template_organization_model = {}  # ContractTemplateOrganization
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        roles_model = {}  # Roles
        roles_model['role'] = 'owner'

        pricing_model = {}  # Pricing
        pricing_model['amount'] = '100.0'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        contract_template_sla_property_model = {}  # ContractTemplateSLAProperty
        contract_template_sla_property_model['property'] = 'Uptime Guarantee'
        contract_template_sla_property_model['value'] = '99.9'

        contract_template_sla_model = {}  # ContractTemplateSLA
        contract_template_sla_model['default_element'] = 'Standard SLA Policy'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        contract_template_support_and_communication_model = {}  # ContractTemplateSupportAndCommunication
        contract_template_support_and_communication_model['channel'] = 'Email Support'
        contract_template_support_and_communication_model['url'] = 'https://support.example.com'

        contract_template_custom_property_model = {}  # ContractTemplateCustomProperty
        contract_template_custom_property_model['key'] = 'customPropertyKey'
        contract_template_custom_property_model['value'] = 'customPropertyValue'

        contract_test_model = {}  # ContractTest
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        contract_schema_property_type_model = {}  # ContractSchemaPropertyType
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        contract_schema_property_model = {}  # ContractSchemaProperty
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        contract_schema_model = {}  # ContractSchema
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        contract_terms_model = {}  # ContractTerms
        contract_terms_model['asset'] = asset_reference_model
        contract_terms_model['id'] = 'testString'
        contract_terms_model['documents'] = [contract_terms_document_model]
        contract_terms_model['error_msg'] = 'testString'
        contract_terms_model['overview'] = overview_model
        contract_terms_model['description'] = description_model
        contract_terms_model['organization'] = [contract_template_organization_model]
        contract_terms_model['roles'] = [roles_model]
        contract_terms_model['price'] = pricing_model
        contract_terms_model['sla'] = [contract_template_sla_model]
        contract_terms_model['support_and_communication'] = [contract_template_support_and_communication_model]
        contract_terms_model['custom_properties'] = [contract_template_custom_property_model]
        contract_terms_model['contract_test'] = contract_test_model
        contract_terms_model['schema'] = [contract_schema_model]

        asset_part_reference_model = {}  # AssetPartReference
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['name'] = 'testString'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        engine_details_model_model = {}  # EngineDetailsModel
        engine_details_model_model['display_name'] = 'Iceberg Engine'
        engine_details_model_model['engine_id'] = 'presto767'
        engine_details_model_model['engine_port'] = '34567'
        engine_details_model_model['engine_host'] = 'a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud'
        engine_details_model_model['associated_catalogs'] = ['testString']

        producer_input_model_model = {}  # ProducerInputModel
        producer_input_model_model['engine_details'] = engine_details_model_model

        delivery_method_properties_model_model = {}  # DeliveryMethodPropertiesModel
        delivery_method_properties_model_model['producer_input'] = producer_input_model_model

        delivery_method_model = {}  # DeliveryMethod
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model
        delivery_method_model['getproperties'] = delivery_method_properties_model_model

        data_product_part_model = {}  # DataProductPart
        data_product_part_model['asset'] = asset_part_reference_model
        data_product_part_model['delivery_methods'] = [delivery_method_model]

        data_product_custom_workflow_definition_model = {}  # DataProductCustomWorkflowDefinition
        data_product_custom_workflow_definition_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        data_product_order_access_request_model = {}  # DataProductOrderAccessRequest
        data_product_order_access_request_model['task_assignee_users'] = ['testString']
        data_product_order_access_request_model['pre_approved_users'] = ['testString']
        data_product_order_access_request_model['custom_workflow_definition'] = data_product_custom_workflow_definition_model

        data_product_workflows_model = {}  # DataProductWorkflows
        data_product_workflows_model['order_access_request'] = data_product_order_access_request_model

        asset_list_access_control_model = {}  # AssetListAccessControl
        asset_list_access_control_model['owner'] = 'IBMid-696000KYV9'

        container_identity_model = {}  # ContainerIdentity
        container_identity_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'

        asset_prototype_model = {}  # AssetPrototype
        asset_prototype_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_prototype_model['container'] = container_identity_model

        # Construct a json representation of a DataProductDraftPrototype model
        data_product_draft_prototype_model_json = {}
        data_product_draft_prototype_model_json['version'] = '1.0.0'
        data_product_draft_prototype_model_json['state'] = 'draft'
        data_product_draft_prototype_model_json['data_product'] = data_product_identity_model
        data_product_draft_prototype_model_json['name'] = 'My Data Product'
        data_product_draft_prototype_model_json['description'] = 'This is a description of My Data Product.'
        data_product_draft_prototype_model_json['tags'] = ['testString']
        data_product_draft_prototype_model_json['use_cases'] = [use_case_model]
        data_product_draft_prototype_model_json['types'] = ['data']
        data_product_draft_prototype_model_json['contract_terms'] = [contract_terms_model]
        data_product_draft_prototype_model_json['domain'] = domain_model
        data_product_draft_prototype_model_json['parts_out'] = [data_product_part_model]
        data_product_draft_prototype_model_json['workflows'] = data_product_workflows_model
        data_product_draft_prototype_model_json['dataview_enabled'] = True
        data_product_draft_prototype_model_json['comments'] = 'Comments by a producer that are provided either at the time of data product version creation or retiring'
        data_product_draft_prototype_model_json['access_control'] = asset_list_access_control_model
        data_product_draft_prototype_model_json['last_updated_at'] = '2019-01-01T12:00:00Z'
        data_product_draft_prototype_model_json['is_restricted'] = True
        data_product_draft_prototype_model_json['asset'] = asset_prototype_model

        # Construct a model instance of DataProductDraftPrototype by calling from_dict on the json representation
        data_product_draft_prototype_model = DataProductDraftPrototype.from_dict(data_product_draft_prototype_model_json)
        assert data_product_draft_prototype_model != False

        # Construct a model instance of DataProductDraftPrototype by calling from_dict on the json representation
        data_product_draft_prototype_model_dict = DataProductDraftPrototype.from_dict(data_product_draft_prototype_model_json).__dict__
        data_product_draft_prototype_model2 = DataProductDraftPrototype(**data_product_draft_prototype_model_dict)

        # Verify the model instances are equivalent
        assert data_product_draft_prototype_model == data_product_draft_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_draft_prototype_model_json2 = data_product_draft_prototype_model.to_dict()
        assert data_product_draft_prototype_model_json2 == data_product_draft_prototype_model_json


class TestModel_DataProductDraftSummary:
    """
    Test Class for DataProductDraftSummary
    """

    def test_data_product_draft_summary_serialization(self):
        """
        Test serialization/deserialization for DataProductDraftSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_product_draft_version_release_model = {}  # DataProductDraftVersionRelease
        data_product_draft_version_release_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        data_product_draft_summary_data_product_model = {}  # DataProductDraftSummaryDataProduct
        data_product_draft_summary_data_product_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_draft_summary_data_product_model['release'] = data_product_draft_version_release_model
        data_product_draft_summary_data_product_model['container'] = container_reference_model

        use_case_model = {}  # UseCase
        use_case_model['id'] = 'testString'
        use_case_model['name'] = 'testString'
        use_case_model['container'] = container_reference_model

        asset_reference_model = {}  # AssetReference
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['name'] = 'testString'
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

        domain_model = {}  # Domain
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        overview_model = {}  # Overview
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = '0.0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        contract_terms_more_info_model = {}  # ContractTermsMoreInfo
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://moreinfo.example.com'

        description_model = {}  # Description
        description_model['purpose'] = 'Used for customer behavior analysis.'
        description_model['limitations'] = 'Data cannot be used for marketing.'
        description_model['usage'] = 'Data should be used only for analytics.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = '{"property1":"value1"}'

        contract_template_organization_model = {}  # ContractTemplateOrganization
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        roles_model = {}  # Roles
        roles_model['role'] = 'owner'

        pricing_model = {}  # Pricing
        pricing_model['amount'] = '100.0'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        contract_template_sla_property_model = {}  # ContractTemplateSLAProperty
        contract_template_sla_property_model['property'] = 'Uptime Guarantee'
        contract_template_sla_property_model['value'] = '99.9'

        contract_template_sla_model = {}  # ContractTemplateSLA
        contract_template_sla_model['default_element'] = 'Standard SLA Policy'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        contract_template_support_and_communication_model = {}  # ContractTemplateSupportAndCommunication
        contract_template_support_and_communication_model['channel'] = 'Email Support'
        contract_template_support_and_communication_model['url'] = 'https://support.example.com'

        contract_template_custom_property_model = {}  # ContractTemplateCustomProperty
        contract_template_custom_property_model['key'] = 'customPropertyKey'
        contract_template_custom_property_model['value'] = 'customPropertyValue'

        contract_test_model = {}  # ContractTest
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        contract_schema_property_type_model = {}  # ContractSchemaPropertyType
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        contract_schema_property_model = {}  # ContractSchemaProperty
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        contract_schema_model = {}  # ContractSchema
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        contract_terms_model = {}  # ContractTerms
        contract_terms_model['asset'] = asset_reference_model
        contract_terms_model['id'] = 'testString'
        contract_terms_model['documents'] = [contract_terms_document_model]
        contract_terms_model['error_msg'] = 'testString'
        contract_terms_model['overview'] = overview_model
        contract_terms_model['description'] = description_model
        contract_terms_model['organization'] = [contract_template_organization_model]
        contract_terms_model['roles'] = [roles_model]
        contract_terms_model['price'] = pricing_model
        contract_terms_model['sla'] = [contract_template_sla_model]
        contract_terms_model['support_and_communication'] = [contract_template_support_and_communication_model]
        contract_terms_model['custom_properties'] = [contract_template_custom_property_model]
        contract_terms_model['contract_test'] = contract_test_model
        contract_terms_model['schema'] = [contract_schema_model]

        asset_part_reference_model = {}  # AssetPartReference
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['name'] = 'testString'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        engine_details_model_model = {}  # EngineDetailsModel
        engine_details_model_model['display_name'] = 'Iceberg Engine'
        engine_details_model_model['engine_id'] = 'presto767'
        engine_details_model_model['engine_port'] = '34567'
        engine_details_model_model['engine_host'] = 'a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud'
        engine_details_model_model['associated_catalogs'] = ['testString']

        producer_input_model_model = {}  # ProducerInputModel
        producer_input_model_model['engine_details'] = engine_details_model_model

        delivery_method_properties_model_model = {}  # DeliveryMethodPropertiesModel
        delivery_method_properties_model_model['producer_input'] = producer_input_model_model

        delivery_method_model = {}  # DeliveryMethod
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model
        delivery_method_model['getproperties'] = delivery_method_properties_model_model

        data_product_part_model = {}  # DataProductPart
        data_product_part_model['asset'] = asset_part_reference_model
        data_product_part_model['delivery_methods'] = [delivery_method_model]

        data_product_custom_workflow_definition_model = {}  # DataProductCustomWorkflowDefinition
        data_product_custom_workflow_definition_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        data_product_order_access_request_model = {}  # DataProductOrderAccessRequest
        data_product_order_access_request_model['task_assignee_users'] = ['testString']
        data_product_order_access_request_model['pre_approved_users'] = ['testString']
        data_product_order_access_request_model['custom_workflow_definition'] = data_product_custom_workflow_definition_model

        data_product_workflows_model = {}  # DataProductWorkflows
        data_product_workflows_model['order_access_request'] = data_product_order_access_request_model

        asset_list_access_control_model = {}  # AssetListAccessControl
        asset_list_access_control_model['owner'] = 'IBMid-696000KYV9'

        # Construct a json representation of a DataProductDraftSummary model
        data_product_draft_summary_model_json = {}
        data_product_draft_summary_model_json['version'] = '1.0.0'
        data_product_draft_summary_model_json['state'] = 'draft'
        data_product_draft_summary_model_json['data_product'] = data_product_draft_summary_data_product_model
        data_product_draft_summary_model_json['name'] = 'My Data Product'
        data_product_draft_summary_model_json['description'] = 'This is a description of My Data Product.'
        data_product_draft_summary_model_json['tags'] = ['testString']
        data_product_draft_summary_model_json['use_cases'] = [use_case_model]
        data_product_draft_summary_model_json['types'] = ['data']
        data_product_draft_summary_model_json['contract_terms'] = [contract_terms_model]
        data_product_draft_summary_model_json['domain'] = domain_model
        data_product_draft_summary_model_json['parts_out'] = [data_product_part_model]
        data_product_draft_summary_model_json['workflows'] = data_product_workflows_model
        data_product_draft_summary_model_json['dataview_enabled'] = True
        data_product_draft_summary_model_json['comments'] = 'Comments by a producer that are provided either at the time of data product version creation or retiring'
        data_product_draft_summary_model_json['access_control'] = asset_list_access_control_model
        data_product_draft_summary_model_json['last_updated_at'] = '2019-01-01T12:00:00Z'
        data_product_draft_summary_model_json['is_restricted'] = True
        data_product_draft_summary_model_json['id'] = '2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd'
        data_product_draft_summary_model_json['asset'] = asset_reference_model

        # Construct a model instance of DataProductDraftSummary by calling from_dict on the json representation
        data_product_draft_summary_model = DataProductDraftSummary.from_dict(data_product_draft_summary_model_json)
        assert data_product_draft_summary_model != False

        # Construct a model instance of DataProductDraftSummary by calling from_dict on the json representation
        data_product_draft_summary_model_dict = DataProductDraftSummary.from_dict(data_product_draft_summary_model_json).__dict__
        data_product_draft_summary_model2 = DataProductDraftSummary(**data_product_draft_summary_model_dict)

        # Verify the model instances are equivalent
        assert data_product_draft_summary_model == data_product_draft_summary_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_draft_summary_model_json2 = data_product_draft_summary_model.to_dict()
        assert data_product_draft_summary_model_json2 == data_product_draft_summary_model_json


class TestModel_DataProductDraftSummaryDataProduct:
    """
    Test Class for DataProductDraftSummaryDataProduct
    """

    def test_data_product_draft_summary_data_product_serialization(self):
        """
        Test serialization/deserialization for DataProductDraftSummaryDataProduct
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_product_draft_version_release_model = {}  # DataProductDraftVersionRelease
        data_product_draft_version_release_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Construct a json representation of a DataProductDraftSummaryDataProduct model
        data_product_draft_summary_data_product_model_json = {}
        data_product_draft_summary_data_product_model_json['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_draft_summary_data_product_model_json['release'] = data_product_draft_version_release_model
        data_product_draft_summary_data_product_model_json['container'] = container_reference_model

        # Construct a model instance of DataProductDraftSummaryDataProduct by calling from_dict on the json representation
        data_product_draft_summary_data_product_model = DataProductDraftSummaryDataProduct.from_dict(data_product_draft_summary_data_product_model_json)
        assert data_product_draft_summary_data_product_model != False

        # Construct a model instance of DataProductDraftSummaryDataProduct by calling from_dict on the json representation
        data_product_draft_summary_data_product_model_dict = DataProductDraftSummaryDataProduct.from_dict(data_product_draft_summary_data_product_model_json).__dict__
        data_product_draft_summary_data_product_model2 = DataProductDraftSummaryDataProduct(**data_product_draft_summary_data_product_model_dict)

        # Verify the model instances are equivalent
        assert data_product_draft_summary_data_product_model == data_product_draft_summary_data_product_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_draft_summary_data_product_model_json2 = data_product_draft_summary_data_product_model.to_dict()
        assert data_product_draft_summary_data_product_model_json2 == data_product_draft_summary_data_product_model_json


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
        data_product_draft_version_release_model = DataProductDraftVersionRelease.from_dict(data_product_draft_version_release_model_json)
        assert data_product_draft_version_release_model != False

        # Construct a model instance of DataProductDraftVersionRelease by calling from_dict on the json representation
        data_product_draft_version_release_model_dict = DataProductDraftVersionRelease.from_dict(data_product_draft_version_release_model_json).__dict__
        data_product_draft_version_release_model2 = DataProductDraftVersionRelease(**data_product_draft_version_release_model_dict)

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
        data_product_order_access_request_model_json['custom_workflow_definition'] = data_product_custom_workflow_definition_model

        # Construct a model instance of DataProductOrderAccessRequest by calling from_dict on the json representation
        data_product_order_access_request_model = DataProductOrderAccessRequest.from_dict(data_product_order_access_request_model_json)
        assert data_product_order_access_request_model != False

        # Construct a model instance of DataProductOrderAccessRequest by calling from_dict on the json representation
        data_product_order_access_request_model_dict = DataProductOrderAccessRequest.from_dict(data_product_order_access_request_model_json).__dict__
        data_product_order_access_request_model2 = DataProductOrderAccessRequest(**data_product_order_access_request_model_dict)

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
        asset_part_reference_model['name'] = 'testString'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        engine_details_model_model = {}  # EngineDetailsModel
        engine_details_model_model['display_name'] = 'Iceberg Engine'
        engine_details_model_model['engine_id'] = 'presto767'
        engine_details_model_model['engine_port'] = '34567'
        engine_details_model_model['engine_host'] = 'a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud'
        engine_details_model_model['associated_catalogs'] = ['testString']

        producer_input_model_model = {}  # ProducerInputModel
        producer_input_model_model['engine_details'] = engine_details_model_model

        delivery_method_properties_model_model = {}  # DeliveryMethodPropertiesModel
        delivery_method_properties_model_model['producer_input'] = producer_input_model_model

        delivery_method_model = {}  # DeliveryMethod
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model
        delivery_method_model['getproperties'] = delivery_method_properties_model_model

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


class TestModel_DataProductRelease:
    """
    Test Class for DataProductRelease
    """

    def test_data_product_release_serialization(self):
        """
        Test serialization/deserialization for DataProductRelease
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_product_draft_version_release_model = {}  # DataProductDraftVersionRelease
        data_product_draft_version_release_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        data_product_release_data_product_model = {}  # DataProductReleaseDataProduct
        data_product_release_data_product_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_release_data_product_model['release'] = data_product_draft_version_release_model
        data_product_release_data_product_model['container'] = container_reference_model

        use_case_model = {}  # UseCase
        use_case_model['id'] = 'testString'
        use_case_model['name'] = 'testString'
        use_case_model['container'] = container_reference_model

        asset_reference_model = {}  # AssetReference
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['name'] = 'testString'
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

        domain_model = {}  # Domain
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        overview_model = {}  # Overview
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = '0.0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        contract_terms_more_info_model = {}  # ContractTermsMoreInfo
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://moreinfo.example.com'

        description_model = {}  # Description
        description_model['purpose'] = 'Used for customer behavior analysis.'
        description_model['limitations'] = 'Data cannot be used for marketing.'
        description_model['usage'] = 'Data should be used only for analytics.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = '{"property1":"value1"}'

        contract_template_organization_model = {}  # ContractTemplateOrganization
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        roles_model = {}  # Roles
        roles_model['role'] = 'owner'

        pricing_model = {}  # Pricing
        pricing_model['amount'] = '100.0'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        contract_template_sla_property_model = {}  # ContractTemplateSLAProperty
        contract_template_sla_property_model['property'] = 'Uptime Guarantee'
        contract_template_sla_property_model['value'] = '99.9'

        contract_template_sla_model = {}  # ContractTemplateSLA
        contract_template_sla_model['default_element'] = 'Standard SLA Policy'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        contract_template_support_and_communication_model = {}  # ContractTemplateSupportAndCommunication
        contract_template_support_and_communication_model['channel'] = 'Email Support'
        contract_template_support_and_communication_model['url'] = 'https://support.example.com'

        contract_template_custom_property_model = {}  # ContractTemplateCustomProperty
        contract_template_custom_property_model['key'] = 'customPropertyKey'
        contract_template_custom_property_model['value'] = 'customPropertyValue'

        contract_test_model = {}  # ContractTest
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        contract_schema_property_type_model = {}  # ContractSchemaPropertyType
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        contract_schema_property_model = {}  # ContractSchemaProperty
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        contract_schema_model = {}  # ContractSchema
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        contract_terms_model = {}  # ContractTerms
        contract_terms_model['asset'] = asset_reference_model
        contract_terms_model['id'] = 'testString'
        contract_terms_model['documents'] = [contract_terms_document_model]
        contract_terms_model['error_msg'] = 'testString'
        contract_terms_model['overview'] = overview_model
        contract_terms_model['description'] = description_model
        contract_terms_model['organization'] = [contract_template_organization_model]
        contract_terms_model['roles'] = [roles_model]
        contract_terms_model['price'] = pricing_model
        contract_terms_model['sla'] = [contract_template_sla_model]
        contract_terms_model['support_and_communication'] = [contract_template_support_and_communication_model]
        contract_terms_model['custom_properties'] = [contract_template_custom_property_model]
        contract_terms_model['contract_test'] = contract_test_model
        contract_terms_model['schema'] = [contract_schema_model]

        asset_part_reference_model = {}  # AssetPartReference
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['name'] = 'testString'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        engine_details_model_model = {}  # EngineDetailsModel
        engine_details_model_model['display_name'] = 'Iceberg Engine'
        engine_details_model_model['engine_id'] = 'presto767'
        engine_details_model_model['engine_port'] = '34567'
        engine_details_model_model['engine_host'] = 'a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud'
        engine_details_model_model['associated_catalogs'] = ['testString']

        producer_input_model_model = {}  # ProducerInputModel
        producer_input_model_model['engine_details'] = engine_details_model_model

        delivery_method_properties_model_model = {}  # DeliveryMethodPropertiesModel
        delivery_method_properties_model_model['producer_input'] = producer_input_model_model

        delivery_method_model = {}  # DeliveryMethod
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model
        delivery_method_model['getproperties'] = delivery_method_properties_model_model

        data_product_part_model = {}  # DataProductPart
        data_product_part_model['asset'] = asset_part_reference_model
        data_product_part_model['delivery_methods'] = [delivery_method_model]

        data_product_custom_workflow_definition_model = {}  # DataProductCustomWorkflowDefinition
        data_product_custom_workflow_definition_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        data_product_order_access_request_model = {}  # DataProductOrderAccessRequest
        data_product_order_access_request_model['task_assignee_users'] = ['testString']
        data_product_order_access_request_model['pre_approved_users'] = ['testString']
        data_product_order_access_request_model['custom_workflow_definition'] = data_product_custom_workflow_definition_model

        data_product_workflows_model = {}  # DataProductWorkflows
        data_product_workflows_model['order_access_request'] = data_product_order_access_request_model

        asset_list_access_control_model = {}  # AssetListAccessControl
        asset_list_access_control_model['owner'] = 'IBMid-696000KYV9'

        visualization_model = {}  # Visualization
        visualization_model['id'] = 'testString'
        visualization_model['name'] = 'testString'

        error_message_model = {}  # ErrorMessage
        error_message_model['code'] = 'testString'
        error_message_model['message'] = 'testString'

        data_asset_relationship_model = {}  # DataAssetRelationship
        data_asset_relationship_model['visualization'] = visualization_model
        data_asset_relationship_model['asset'] = asset_reference_model
        data_asset_relationship_model['related_asset'] = asset_reference_model
        data_asset_relationship_model['error'] = error_message_model

        # Construct a json representation of a DataProductRelease model
        data_product_release_model_json = {}
        data_product_release_model_json['version'] = '1.0.0'
        data_product_release_model_json['state'] = 'draft'
        data_product_release_model_json['data_product'] = data_product_release_data_product_model
        data_product_release_model_json['name'] = 'My Data Product'
        data_product_release_model_json['description'] = 'This is a description of My Data Product.'
        data_product_release_model_json['tags'] = ['testString']
        data_product_release_model_json['use_cases'] = [use_case_model]
        data_product_release_model_json['types'] = ['data']
        data_product_release_model_json['contract_terms'] = [contract_terms_model]
        data_product_release_model_json['domain'] = domain_model
        data_product_release_model_json['parts_out'] = [data_product_part_model]
        data_product_release_model_json['workflows'] = data_product_workflows_model
        data_product_release_model_json['dataview_enabled'] = True
        data_product_release_model_json['comments'] = 'Comments by a producer that are provided either at the time of data product version creation or retiring'
        data_product_release_model_json['access_control'] = asset_list_access_control_model
        data_product_release_model_json['last_updated_at'] = '2019-01-01T12:00:00Z'
        data_product_release_model_json['is_restricted'] = True
        data_product_release_model_json['id'] = '2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd'
        data_product_release_model_json['asset'] = asset_reference_model
        data_product_release_model_json['published_by'] = 'testString'
        data_product_release_model_json['published_at'] = '2019-01-01T12:00:00Z'
        data_product_release_model_json['created_by'] = 'testString'
        data_product_release_model_json['created_at'] = '2019-01-01T12:00:00Z'
        data_product_release_model_json['properties'] = {'anyKey': 'anyValue'}
        data_product_release_model_json['visualization_errors'] = [data_asset_relationship_model]

        # Construct a model instance of DataProductRelease by calling from_dict on the json representation
        data_product_release_model = DataProductRelease.from_dict(data_product_release_model_json)
        assert data_product_release_model != False

        # Construct a model instance of DataProductRelease by calling from_dict on the json representation
        data_product_release_model_dict = DataProductRelease.from_dict(data_product_release_model_json).__dict__
        data_product_release_model2 = DataProductRelease(**data_product_release_model_dict)

        # Verify the model instances are equivalent
        assert data_product_release_model == data_product_release_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_release_model_json2 = data_product_release_model.to_dict()
        assert data_product_release_model_json2 == data_product_release_model_json


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

        data_product_release_summary_data_product_model = {}  # DataProductReleaseSummaryDataProduct
        data_product_release_summary_data_product_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_release_summary_data_product_model['release'] = data_product_draft_version_release_model
        data_product_release_summary_data_product_model['container'] = container_reference_model

        use_case_model = {}  # UseCase
        use_case_model['id'] = 'testString'
        use_case_model['name'] = 'testString'
        use_case_model['container'] = container_reference_model

        asset_reference_model = {}  # AssetReference
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['name'] = 'testString'
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

        domain_model = {}  # Domain
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        overview_model = {}  # Overview
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = '0.0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        contract_terms_more_info_model = {}  # ContractTermsMoreInfo
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://moreinfo.example.com'

        description_model = {}  # Description
        description_model['purpose'] = 'Used for customer behavior analysis.'
        description_model['limitations'] = 'Data cannot be used for marketing.'
        description_model['usage'] = 'Data should be used only for analytics.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = '{"property1":"value1"}'

        contract_template_organization_model = {}  # ContractTemplateOrganization
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        roles_model = {}  # Roles
        roles_model['role'] = 'owner'

        pricing_model = {}  # Pricing
        pricing_model['amount'] = '100.0'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        contract_template_sla_property_model = {}  # ContractTemplateSLAProperty
        contract_template_sla_property_model['property'] = 'Uptime Guarantee'
        contract_template_sla_property_model['value'] = '99.9'

        contract_template_sla_model = {}  # ContractTemplateSLA
        contract_template_sla_model['default_element'] = 'Standard SLA Policy'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        contract_template_support_and_communication_model = {}  # ContractTemplateSupportAndCommunication
        contract_template_support_and_communication_model['channel'] = 'Email Support'
        contract_template_support_and_communication_model['url'] = 'https://support.example.com'

        contract_template_custom_property_model = {}  # ContractTemplateCustomProperty
        contract_template_custom_property_model['key'] = 'customPropertyKey'
        contract_template_custom_property_model['value'] = 'customPropertyValue'

        contract_test_model = {}  # ContractTest
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        contract_schema_property_type_model = {}  # ContractSchemaPropertyType
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        contract_schema_property_model = {}  # ContractSchemaProperty
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        contract_schema_model = {}  # ContractSchema
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        contract_terms_model = {}  # ContractTerms
        contract_terms_model['asset'] = asset_reference_model
        contract_terms_model['id'] = 'testString'
        contract_terms_model['documents'] = [contract_terms_document_model]
        contract_terms_model['error_msg'] = 'testString'
        contract_terms_model['overview'] = overview_model
        contract_terms_model['description'] = description_model
        contract_terms_model['organization'] = [contract_template_organization_model]
        contract_terms_model['roles'] = [roles_model]
        contract_terms_model['price'] = pricing_model
        contract_terms_model['sla'] = [contract_template_sla_model]
        contract_terms_model['support_and_communication'] = [contract_template_support_and_communication_model]
        contract_terms_model['custom_properties'] = [contract_template_custom_property_model]
        contract_terms_model['contract_test'] = contract_test_model
        contract_terms_model['schema'] = [contract_schema_model]

        asset_part_reference_model = {}  # AssetPartReference
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['name'] = 'testString'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        engine_details_model_model = {}  # EngineDetailsModel
        engine_details_model_model['display_name'] = 'Iceberg Engine'
        engine_details_model_model['engine_id'] = 'presto767'
        engine_details_model_model['engine_port'] = '34567'
        engine_details_model_model['engine_host'] = 'a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud'
        engine_details_model_model['associated_catalogs'] = ['testString']

        producer_input_model_model = {}  # ProducerInputModel
        producer_input_model_model['engine_details'] = engine_details_model_model

        delivery_method_properties_model_model = {}  # DeliveryMethodPropertiesModel
        delivery_method_properties_model_model['producer_input'] = producer_input_model_model

        delivery_method_model = {}  # DeliveryMethod
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model
        delivery_method_model['getproperties'] = delivery_method_properties_model_model

        data_product_part_model = {}  # DataProductPart
        data_product_part_model['asset'] = asset_part_reference_model
        data_product_part_model['delivery_methods'] = [delivery_method_model]

        data_product_custom_workflow_definition_model = {}  # DataProductCustomWorkflowDefinition
        data_product_custom_workflow_definition_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        data_product_order_access_request_model = {}  # DataProductOrderAccessRequest
        data_product_order_access_request_model['task_assignee_users'] = ['testString']
        data_product_order_access_request_model['pre_approved_users'] = ['testString']
        data_product_order_access_request_model['custom_workflow_definition'] = data_product_custom_workflow_definition_model

        data_product_workflows_model = {}  # DataProductWorkflows
        data_product_workflows_model['order_access_request'] = data_product_order_access_request_model

        asset_list_access_control_model = {}  # AssetListAccessControl
        asset_list_access_control_model['owner'] = 'IBMid-696000KYV9'

        data_product_release_summary_model = {}  # DataProductReleaseSummary
        data_product_release_summary_model['version'] = '1.0.0'
        data_product_release_summary_model['state'] = 'draft'
        data_product_release_summary_model['data_product'] = data_product_release_summary_data_product_model
        data_product_release_summary_model['name'] = 'My Data Product'
        data_product_release_summary_model['description'] = 'This is a description of My Data Product.'
        data_product_release_summary_model['tags'] = ['testString']
        data_product_release_summary_model['use_cases'] = [use_case_model]
        data_product_release_summary_model['types'] = ['data']
        data_product_release_summary_model['contract_terms'] = [contract_terms_model]
        data_product_release_summary_model['domain'] = domain_model
        data_product_release_summary_model['parts_out'] = [data_product_part_model]
        data_product_release_summary_model['workflows'] = data_product_workflows_model
        data_product_release_summary_model['dataview_enabled'] = True
        data_product_release_summary_model['comments'] = 'Comments by a producer that are provided either at the time of data product version creation or retiring'
        data_product_release_summary_model['access_control'] = asset_list_access_control_model
        data_product_release_summary_model['last_updated_at'] = '2019-01-01T12:00:00Z'
        data_product_release_summary_model['is_restricted'] = True
        data_product_release_summary_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd'
        data_product_release_summary_model['asset'] = asset_reference_model

        # Construct a json representation of a DataProductReleaseCollection model
        data_product_release_collection_model_json = {}
        data_product_release_collection_model_json['limit'] = 200
        data_product_release_collection_model_json['first'] = first_page_model
        data_product_release_collection_model_json['next'] = next_page_model
        data_product_release_collection_model_json['total_results'] = 200
        data_product_release_collection_model_json['releases'] = [data_product_release_summary_model]

        # Construct a model instance of DataProductReleaseCollection by calling from_dict on the json representation
        data_product_release_collection_model = DataProductReleaseCollection.from_dict(data_product_release_collection_model_json)
        assert data_product_release_collection_model != False

        # Construct a model instance of DataProductReleaseCollection by calling from_dict on the json representation
        data_product_release_collection_model_dict = DataProductReleaseCollection.from_dict(data_product_release_collection_model_json).__dict__
        data_product_release_collection_model2 = DataProductReleaseCollection(**data_product_release_collection_model_dict)

        # Verify the model instances are equivalent
        assert data_product_release_collection_model == data_product_release_collection_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_release_collection_model_json2 = data_product_release_collection_model.to_dict()
        assert data_product_release_collection_model_json2 == data_product_release_collection_model_json


class TestModel_DataProductReleaseDataProduct:
    """
    Test Class for DataProductReleaseDataProduct
    """

    def test_data_product_release_data_product_serialization(self):
        """
        Test serialization/deserialization for DataProductReleaseDataProduct
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_product_draft_version_release_model = {}  # DataProductDraftVersionRelease
        data_product_draft_version_release_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Construct a json representation of a DataProductReleaseDataProduct model
        data_product_release_data_product_model_json = {}
        data_product_release_data_product_model_json['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_release_data_product_model_json['release'] = data_product_draft_version_release_model
        data_product_release_data_product_model_json['container'] = container_reference_model

        # Construct a model instance of DataProductReleaseDataProduct by calling from_dict on the json representation
        data_product_release_data_product_model = DataProductReleaseDataProduct.from_dict(data_product_release_data_product_model_json)
        assert data_product_release_data_product_model != False

        # Construct a model instance of DataProductReleaseDataProduct by calling from_dict on the json representation
        data_product_release_data_product_model_dict = DataProductReleaseDataProduct.from_dict(data_product_release_data_product_model_json).__dict__
        data_product_release_data_product_model2 = DataProductReleaseDataProduct(**data_product_release_data_product_model_dict)

        # Verify the model instances are equivalent
        assert data_product_release_data_product_model == data_product_release_data_product_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_release_data_product_model_json2 = data_product_release_data_product_model.to_dict()
        assert data_product_release_data_product_model_json2 == data_product_release_data_product_model_json


class TestModel_DataProductReleaseSummary:
    """
    Test Class for DataProductReleaseSummary
    """

    def test_data_product_release_summary_serialization(self):
        """
        Test serialization/deserialization for DataProductReleaseSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_product_draft_version_release_model = {}  # DataProductDraftVersionRelease
        data_product_draft_version_release_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        data_product_release_summary_data_product_model = {}  # DataProductReleaseSummaryDataProduct
        data_product_release_summary_data_product_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_release_summary_data_product_model['release'] = data_product_draft_version_release_model
        data_product_release_summary_data_product_model['container'] = container_reference_model

        use_case_model = {}  # UseCase
        use_case_model['id'] = 'testString'
        use_case_model['name'] = 'testString'
        use_case_model['container'] = container_reference_model

        asset_reference_model = {}  # AssetReference
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['name'] = 'testString'
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

        domain_model = {}  # Domain
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        overview_model = {}  # Overview
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = '0.0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        contract_terms_more_info_model = {}  # ContractTermsMoreInfo
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://moreinfo.example.com'

        description_model = {}  # Description
        description_model['purpose'] = 'Used for customer behavior analysis.'
        description_model['limitations'] = 'Data cannot be used for marketing.'
        description_model['usage'] = 'Data should be used only for analytics.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = '{"property1":"value1"}'

        contract_template_organization_model = {}  # ContractTemplateOrganization
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        roles_model = {}  # Roles
        roles_model['role'] = 'owner'

        pricing_model = {}  # Pricing
        pricing_model['amount'] = '100.0'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        contract_template_sla_property_model = {}  # ContractTemplateSLAProperty
        contract_template_sla_property_model['property'] = 'Uptime Guarantee'
        contract_template_sla_property_model['value'] = '99.9'

        contract_template_sla_model = {}  # ContractTemplateSLA
        contract_template_sla_model['default_element'] = 'Standard SLA Policy'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        contract_template_support_and_communication_model = {}  # ContractTemplateSupportAndCommunication
        contract_template_support_and_communication_model['channel'] = 'Email Support'
        contract_template_support_and_communication_model['url'] = 'https://support.example.com'

        contract_template_custom_property_model = {}  # ContractTemplateCustomProperty
        contract_template_custom_property_model['key'] = 'customPropertyKey'
        contract_template_custom_property_model['value'] = 'customPropertyValue'

        contract_test_model = {}  # ContractTest
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        contract_schema_property_type_model = {}  # ContractSchemaPropertyType
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        contract_schema_property_model = {}  # ContractSchemaProperty
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        contract_schema_model = {}  # ContractSchema
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        contract_terms_model = {}  # ContractTerms
        contract_terms_model['asset'] = asset_reference_model
        contract_terms_model['id'] = 'testString'
        contract_terms_model['documents'] = [contract_terms_document_model]
        contract_terms_model['error_msg'] = 'testString'
        contract_terms_model['overview'] = overview_model
        contract_terms_model['description'] = description_model
        contract_terms_model['organization'] = [contract_template_organization_model]
        contract_terms_model['roles'] = [roles_model]
        contract_terms_model['price'] = pricing_model
        contract_terms_model['sla'] = [contract_template_sla_model]
        contract_terms_model['support_and_communication'] = [contract_template_support_and_communication_model]
        contract_terms_model['custom_properties'] = [contract_template_custom_property_model]
        contract_terms_model['contract_test'] = contract_test_model
        contract_terms_model['schema'] = [contract_schema_model]

        asset_part_reference_model = {}  # AssetPartReference
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['name'] = 'testString'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        engine_details_model_model = {}  # EngineDetailsModel
        engine_details_model_model['display_name'] = 'Iceberg Engine'
        engine_details_model_model['engine_id'] = 'presto767'
        engine_details_model_model['engine_port'] = '34567'
        engine_details_model_model['engine_host'] = 'a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud'
        engine_details_model_model['associated_catalogs'] = ['testString']

        producer_input_model_model = {}  # ProducerInputModel
        producer_input_model_model['engine_details'] = engine_details_model_model

        delivery_method_properties_model_model = {}  # DeliveryMethodPropertiesModel
        delivery_method_properties_model_model['producer_input'] = producer_input_model_model

        delivery_method_model = {}  # DeliveryMethod
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model
        delivery_method_model['getproperties'] = delivery_method_properties_model_model

        data_product_part_model = {}  # DataProductPart
        data_product_part_model['asset'] = asset_part_reference_model
        data_product_part_model['delivery_methods'] = [delivery_method_model]

        data_product_custom_workflow_definition_model = {}  # DataProductCustomWorkflowDefinition
        data_product_custom_workflow_definition_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        data_product_order_access_request_model = {}  # DataProductOrderAccessRequest
        data_product_order_access_request_model['task_assignee_users'] = ['testString']
        data_product_order_access_request_model['pre_approved_users'] = ['testString']
        data_product_order_access_request_model['custom_workflow_definition'] = data_product_custom_workflow_definition_model

        data_product_workflows_model = {}  # DataProductWorkflows
        data_product_workflows_model['order_access_request'] = data_product_order_access_request_model

        asset_list_access_control_model = {}  # AssetListAccessControl
        asset_list_access_control_model['owner'] = 'IBMid-696000KYV9'

        # Construct a json representation of a DataProductReleaseSummary model
        data_product_release_summary_model_json = {}
        data_product_release_summary_model_json['version'] = '1.0.0'
        data_product_release_summary_model_json['state'] = 'draft'
        data_product_release_summary_model_json['data_product'] = data_product_release_summary_data_product_model
        data_product_release_summary_model_json['name'] = 'My Data Product'
        data_product_release_summary_model_json['description'] = 'This is a description of My Data Product.'
        data_product_release_summary_model_json['tags'] = ['testString']
        data_product_release_summary_model_json['use_cases'] = [use_case_model]
        data_product_release_summary_model_json['types'] = ['data']
        data_product_release_summary_model_json['contract_terms'] = [contract_terms_model]
        data_product_release_summary_model_json['domain'] = domain_model
        data_product_release_summary_model_json['parts_out'] = [data_product_part_model]
        data_product_release_summary_model_json['workflows'] = data_product_workflows_model
        data_product_release_summary_model_json['dataview_enabled'] = True
        data_product_release_summary_model_json['comments'] = 'Comments by a producer that are provided either at the time of data product version creation or retiring'
        data_product_release_summary_model_json['access_control'] = asset_list_access_control_model
        data_product_release_summary_model_json['last_updated_at'] = '2019-01-01T12:00:00Z'
        data_product_release_summary_model_json['is_restricted'] = True
        data_product_release_summary_model_json['id'] = '2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd'
        data_product_release_summary_model_json['asset'] = asset_reference_model

        # Construct a model instance of DataProductReleaseSummary by calling from_dict on the json representation
        data_product_release_summary_model = DataProductReleaseSummary.from_dict(data_product_release_summary_model_json)
        assert data_product_release_summary_model != False

        # Construct a model instance of DataProductReleaseSummary by calling from_dict on the json representation
        data_product_release_summary_model_dict = DataProductReleaseSummary.from_dict(data_product_release_summary_model_json).__dict__
        data_product_release_summary_model2 = DataProductReleaseSummary(**data_product_release_summary_model_dict)

        # Verify the model instances are equivalent
        assert data_product_release_summary_model == data_product_release_summary_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_release_summary_model_json2 = data_product_release_summary_model.to_dict()
        assert data_product_release_summary_model_json2 == data_product_release_summary_model_json


class TestModel_DataProductReleaseSummaryDataProduct:
    """
    Test Class for DataProductReleaseSummaryDataProduct
    """

    def test_data_product_release_summary_data_product_serialization(self):
        """
        Test serialization/deserialization for DataProductReleaseSummaryDataProduct
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_product_draft_version_release_model = {}  # DataProductDraftVersionRelease
        data_product_draft_version_release_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Construct a json representation of a DataProductReleaseSummaryDataProduct model
        data_product_release_summary_data_product_model_json = {}
        data_product_release_summary_data_product_model_json['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_release_summary_data_product_model_json['release'] = data_product_draft_version_release_model
        data_product_release_summary_data_product_model_json['container'] = container_reference_model

        # Construct a model instance of DataProductReleaseSummaryDataProduct by calling from_dict on the json representation
        data_product_release_summary_data_product_model = DataProductReleaseSummaryDataProduct.from_dict(data_product_release_summary_data_product_model_json)
        assert data_product_release_summary_data_product_model != False

        # Construct a model instance of DataProductReleaseSummaryDataProduct by calling from_dict on the json representation
        data_product_release_summary_data_product_model_dict = DataProductReleaseSummaryDataProduct.from_dict(data_product_release_summary_data_product_model_json).__dict__
        data_product_release_summary_data_product_model2 = DataProductReleaseSummaryDataProduct(**data_product_release_summary_data_product_model_dict)

        # Verify the model instances are equivalent
        assert data_product_release_summary_data_product_model == data_product_release_summary_data_product_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_release_summary_data_product_model_json2 = data_product_release_summary_data_product_model.to_dict()
        assert data_product_release_summary_data_product_model_json2 == data_product_release_summary_data_product_model_json


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
        data_product_summary_model_json['name'] = 'testString'

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


class TestModel_DataProductVersionCollection:
    """
    Test Class for DataProductVersionCollection
    """

    def test_data_product_version_collection_serialization(self):
        """
        Test serialization/deserialization for DataProductVersionCollection
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
        asset_reference_model['name'] = 'testString'
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

        domain_model = {}  # Domain
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        overview_model = {}  # Overview
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = '0.0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        contract_terms_more_info_model = {}  # ContractTermsMoreInfo
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://moreinfo.example.com'

        description_model = {}  # Description
        description_model['purpose'] = 'Used for customer behavior analysis.'
        description_model['limitations'] = 'Data cannot be used for marketing.'
        description_model['usage'] = 'Data should be used only for analytics.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = '{"property1":"value1"}'

        contract_template_organization_model = {}  # ContractTemplateOrganization
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        roles_model = {}  # Roles
        roles_model['role'] = 'owner'

        pricing_model = {}  # Pricing
        pricing_model['amount'] = '100.0'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        contract_template_sla_property_model = {}  # ContractTemplateSLAProperty
        contract_template_sla_property_model['property'] = 'Uptime Guarantee'
        contract_template_sla_property_model['value'] = '99.9'

        contract_template_sla_model = {}  # ContractTemplateSLA
        contract_template_sla_model['default_element'] = 'Standard SLA Policy'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        contract_template_support_and_communication_model = {}  # ContractTemplateSupportAndCommunication
        contract_template_support_and_communication_model['channel'] = 'Email Support'
        contract_template_support_and_communication_model['url'] = 'https://support.example.com'

        contract_template_custom_property_model = {}  # ContractTemplateCustomProperty
        contract_template_custom_property_model['key'] = 'customPropertyKey'
        contract_template_custom_property_model['value'] = 'customPropertyValue'

        contract_test_model = {}  # ContractTest
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        contract_schema_property_type_model = {}  # ContractSchemaPropertyType
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        contract_schema_property_model = {}  # ContractSchemaProperty
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        contract_schema_model = {}  # ContractSchema
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        contract_terms_model = {}  # ContractTerms
        contract_terms_model['asset'] = asset_reference_model
        contract_terms_model['id'] = 'testString'
        contract_terms_model['documents'] = [contract_terms_document_model]
        contract_terms_model['error_msg'] = 'testString'
        contract_terms_model['overview'] = overview_model
        contract_terms_model['description'] = description_model
        contract_terms_model['organization'] = [contract_template_organization_model]
        contract_terms_model['roles'] = [roles_model]
        contract_terms_model['price'] = pricing_model
        contract_terms_model['sla'] = [contract_template_sla_model]
        contract_terms_model['support_and_communication'] = [contract_template_support_and_communication_model]
        contract_terms_model['custom_properties'] = [contract_template_custom_property_model]
        contract_terms_model['contract_test'] = contract_test_model
        contract_terms_model['schema'] = [contract_schema_model]

        asset_part_reference_model = {}  # AssetPartReference
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['name'] = 'testString'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        engine_details_model_model = {}  # EngineDetailsModel
        engine_details_model_model['display_name'] = 'Iceberg Engine'
        engine_details_model_model['engine_id'] = 'presto767'
        engine_details_model_model['engine_port'] = '34567'
        engine_details_model_model['engine_host'] = 'a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud'
        engine_details_model_model['associated_catalogs'] = ['testString']

        producer_input_model_model = {}  # ProducerInputModel
        producer_input_model_model['engine_details'] = engine_details_model_model

        delivery_method_properties_model_model = {}  # DeliveryMethodPropertiesModel
        delivery_method_properties_model_model['producer_input'] = producer_input_model_model

        delivery_method_model = {}  # DeliveryMethod
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model
        delivery_method_model['getproperties'] = delivery_method_properties_model_model

        data_product_part_model = {}  # DataProductPart
        data_product_part_model['asset'] = asset_part_reference_model
        data_product_part_model['delivery_methods'] = [delivery_method_model]

        data_product_custom_workflow_definition_model = {}  # DataProductCustomWorkflowDefinition
        data_product_custom_workflow_definition_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        data_product_order_access_request_model = {}  # DataProductOrderAccessRequest
        data_product_order_access_request_model['task_assignee_users'] = ['testString']
        data_product_order_access_request_model['pre_approved_users'] = ['testString']
        data_product_order_access_request_model['custom_workflow_definition'] = data_product_custom_workflow_definition_model

        data_product_workflows_model = {}  # DataProductWorkflows
        data_product_workflows_model['order_access_request'] = data_product_order_access_request_model

        asset_list_access_control_model = {}  # AssetListAccessControl
        asset_list_access_control_model['owner'] = 'IBMid-696000KYV9'

        data_product_version_summary_model = {}  # DataProductVersionSummary
        data_product_version_summary_model['version'] = '1.0.0'
        data_product_version_summary_model['state'] = 'draft'
        data_product_version_summary_model['data_product'] = data_product_version_summary_data_product_model
        data_product_version_summary_model['name'] = 'My Data Product'
        data_product_version_summary_model['description'] = 'This is a description of My Data Product.'
        data_product_version_summary_model['tags'] = ['testString']
        data_product_version_summary_model['use_cases'] = [use_case_model]
        data_product_version_summary_model['types'] = ['data']
        data_product_version_summary_model['contract_terms'] = [contract_terms_model]
        data_product_version_summary_model['domain'] = domain_model
        data_product_version_summary_model['parts_out'] = [data_product_part_model]
        data_product_version_summary_model['workflows'] = data_product_workflows_model
        data_product_version_summary_model['dataview_enabled'] = True
        data_product_version_summary_model['comments'] = 'Comments by a producer that are provided either at the time of data product version creation or retiring'
        data_product_version_summary_model['access_control'] = asset_list_access_control_model
        data_product_version_summary_model['last_updated_at'] = '2019-01-01T12:00:00Z'
        data_product_version_summary_model['is_restricted'] = True
        data_product_version_summary_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd'
        data_product_version_summary_model['asset'] = asset_reference_model

        # Construct a json representation of a DataProductVersionCollection model
        data_product_version_collection_model_json = {}
        data_product_version_collection_model_json['limit'] = 200
        data_product_version_collection_model_json['first'] = first_page_model
        data_product_version_collection_model_json['next'] = next_page_model
        data_product_version_collection_model_json['total_results'] = 200
        data_product_version_collection_model_json['data_product_versions'] = [data_product_version_summary_model]

        # Construct a model instance of DataProductVersionCollection by calling from_dict on the json representation
        data_product_version_collection_model = DataProductVersionCollection.from_dict(data_product_version_collection_model_json)
        assert data_product_version_collection_model != False

        # Construct a model instance of DataProductVersionCollection by calling from_dict on the json representation
        data_product_version_collection_model_dict = DataProductVersionCollection.from_dict(data_product_version_collection_model_json).__dict__
        data_product_version_collection_model2 = DataProductVersionCollection(**data_product_version_collection_model_dict)

        # Verify the model instances are equivalent
        assert data_product_version_collection_model == data_product_version_collection_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_version_collection_model_json2 = data_product_version_collection_model.to_dict()
        assert data_product_version_collection_model_json2 == data_product_version_collection_model_json


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
        asset_reference_model['name'] = 'testString'
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

        domain_model = {}  # Domain
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        overview_model = {}  # Overview
        overview_model['api_version'] = 'v3.0.1'
        overview_model['kind'] = 'DataContract'
        overview_model['name'] = 'Sample Data Contract'
        overview_model['version'] = '0.0.0'
        overview_model['domain'] = domain_model
        overview_model['more_info'] = 'List of links to sources that provide more details on the data contract.'

        contract_terms_more_info_model = {}  # ContractTermsMoreInfo
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://moreinfo.example.com'

        description_model = {}  # Description
        description_model['purpose'] = 'Used for customer behavior analysis.'
        description_model['limitations'] = 'Data cannot be used for marketing.'
        description_model['usage'] = 'Data should be used only for analytics.'
        description_model['more_info'] = [contract_terms_more_info_model]
        description_model['custom_properties'] = '{"property1":"value1"}'

        contract_template_organization_model = {}  # ContractTemplateOrganization
        contract_template_organization_model['user_id'] = 'IBMid-691000IN4G'
        contract_template_organization_model['role'] = 'owner'

        roles_model = {}  # Roles
        roles_model['role'] = 'owner'

        pricing_model = {}  # Pricing
        pricing_model['amount'] = '100.0'
        pricing_model['currency'] = 'USD'
        pricing_model['unit'] = 'megabyte'

        contract_template_sla_property_model = {}  # ContractTemplateSLAProperty
        contract_template_sla_property_model['property'] = 'Uptime Guarantee'
        contract_template_sla_property_model['value'] = '99.9'

        contract_template_sla_model = {}  # ContractTemplateSLA
        contract_template_sla_model['default_element'] = 'Standard SLA Policy'
        contract_template_sla_model['properties'] = [contract_template_sla_property_model]

        contract_template_support_and_communication_model = {}  # ContractTemplateSupportAndCommunication
        contract_template_support_and_communication_model['channel'] = 'Email Support'
        contract_template_support_and_communication_model['url'] = 'https://support.example.com'

        contract_template_custom_property_model = {}  # ContractTemplateCustomProperty
        contract_template_custom_property_model['key'] = 'customPropertyKey'
        contract_template_custom_property_model['value'] = 'customPropertyValue'

        contract_test_model = {}  # ContractTest
        contract_test_model['status'] = 'pass'
        contract_test_model['last_tested_time'] = 'testString'
        contract_test_model['message'] = 'testString'

        contract_schema_property_type_model = {}  # ContractSchemaPropertyType
        contract_schema_property_type_model['type'] = 'testString'
        contract_schema_property_type_model['length'] = 'testString'
        contract_schema_property_type_model['scale'] = 'testString'
        contract_schema_property_type_model['nullable'] = 'testString'
        contract_schema_property_type_model['signed'] = 'testString'
        contract_schema_property_type_model['native_type'] = 'testString'

        contract_schema_property_model = {}  # ContractSchemaProperty
        contract_schema_property_model['name'] = 'testString'
        contract_schema_property_model['type'] = contract_schema_property_type_model

        contract_schema_model = {}  # ContractSchema
        contract_schema_model['name'] = 'testString'
        contract_schema_model['description'] = 'testString'
        contract_schema_model['physical_type'] = 'testString'
        contract_schema_model['properties'] = [contract_schema_property_model]

        contract_terms_model = {}  # ContractTerms
        contract_terms_model['asset'] = asset_reference_model
        contract_terms_model['id'] = 'testString'
        contract_terms_model['documents'] = [contract_terms_document_model]
        contract_terms_model['error_msg'] = 'testString'
        contract_terms_model['overview'] = overview_model
        contract_terms_model['description'] = description_model
        contract_terms_model['organization'] = [contract_template_organization_model]
        contract_terms_model['roles'] = [roles_model]
        contract_terms_model['price'] = pricing_model
        contract_terms_model['sla'] = [contract_template_sla_model]
        contract_terms_model['support_and_communication'] = [contract_template_support_and_communication_model]
        contract_terms_model['custom_properties'] = [contract_template_custom_property_model]
        contract_terms_model['contract_test'] = contract_test_model
        contract_terms_model['schema'] = [contract_schema_model]

        asset_part_reference_model = {}  # AssetPartReference
        asset_part_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_part_reference_model['name'] = 'testString'
        asset_part_reference_model['container'] = container_reference_model
        asset_part_reference_model['type'] = 'data_asset'

        engine_details_model_model = {}  # EngineDetailsModel
        engine_details_model_model['display_name'] = 'Iceberg Engine'
        engine_details_model_model['engine_id'] = 'presto767'
        engine_details_model_model['engine_port'] = '34567'
        engine_details_model_model['engine_host'] = 'a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud'
        engine_details_model_model['associated_catalogs'] = ['testString']

        producer_input_model_model = {}  # ProducerInputModel
        producer_input_model_model['engine_details'] = engine_details_model_model

        delivery_method_properties_model_model = {}  # DeliveryMethodPropertiesModel
        delivery_method_properties_model_model['producer_input'] = producer_input_model_model

        delivery_method_model = {}  # DeliveryMethod
        delivery_method_model['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model['container'] = container_reference_model
        delivery_method_model['getproperties'] = delivery_method_properties_model_model

        data_product_part_model = {}  # DataProductPart
        data_product_part_model['asset'] = asset_part_reference_model
        data_product_part_model['delivery_methods'] = [delivery_method_model]

        data_product_custom_workflow_definition_model = {}  # DataProductCustomWorkflowDefinition
        data_product_custom_workflow_definition_model['id'] = '18bdbde1-918e-4ecf-aa23-6727bf319e14'

        data_product_order_access_request_model = {}  # DataProductOrderAccessRequest
        data_product_order_access_request_model['task_assignee_users'] = ['testString']
        data_product_order_access_request_model['pre_approved_users'] = ['testString']
        data_product_order_access_request_model['custom_workflow_definition'] = data_product_custom_workflow_definition_model

        data_product_workflows_model = {}  # DataProductWorkflows
        data_product_workflows_model['order_access_request'] = data_product_order_access_request_model

        asset_list_access_control_model = {}  # AssetListAccessControl
        asset_list_access_control_model['owner'] = 'IBMid-696000KYV9'

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
        data_product_version_summary_model_json['contract_terms'] = [contract_terms_model]
        data_product_version_summary_model_json['domain'] = domain_model
        data_product_version_summary_model_json['parts_out'] = [data_product_part_model]
        data_product_version_summary_model_json['workflows'] = data_product_workflows_model
        data_product_version_summary_model_json['dataview_enabled'] = True
        data_product_version_summary_model_json['comments'] = 'Comments by a producer that are provided either at the time of data product version creation or retiring'
        data_product_version_summary_model_json['access_control'] = asset_list_access_control_model
        data_product_version_summary_model_json['last_updated_at'] = '2019-01-01T12:00:00Z'
        data_product_version_summary_model_json['is_restricted'] = True
        data_product_version_summary_model_json['id'] = '2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd'
        data_product_version_summary_model_json['asset'] = asset_reference_model

        # Construct a model instance of DataProductVersionSummary by calling from_dict on the json representation
        data_product_version_summary_model = DataProductVersionSummary.from_dict(data_product_version_summary_model_json)
        assert data_product_version_summary_model != False

        # Construct a model instance of DataProductVersionSummary by calling from_dict on the json representation
        data_product_version_summary_model_dict = DataProductVersionSummary.from_dict(data_product_version_summary_model_json).__dict__
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
        data_product_version_summary_data_product_model = DataProductVersionSummaryDataProduct.from_dict(data_product_version_summary_data_product_model_json)
        assert data_product_version_summary_data_product_model != False

        # Construct a model instance of DataProductVersionSummaryDataProduct by calling from_dict on the json representation
        data_product_version_summary_data_product_model_dict = DataProductVersionSummaryDataProduct.from_dict(data_product_version_summary_data_product_model_json).__dict__
        data_product_version_summary_data_product_model2 = DataProductVersionSummaryDataProduct(**data_product_version_summary_data_product_model_dict)

        # Verify the model instances are equivalent
        assert data_product_version_summary_data_product_model == data_product_version_summary_data_product_model2

        # Convert model instance back to dict and verify no loss of data
        data_product_version_summary_data_product_model_json2 = data_product_version_summary_data_product_model.to_dict()
        assert data_product_version_summary_data_product_model_json2 == data_product_version_summary_data_product_model_json


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
        data_product_order_access_request_model['custom_workflow_definition'] = data_product_custom_workflow_definition_model

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

        engine_details_model_model = {}  # EngineDetailsModel
        engine_details_model_model['display_name'] = 'Iceberg Engine'
        engine_details_model_model['engine_id'] = 'presto767'
        engine_details_model_model['engine_port'] = '34567'
        engine_details_model_model['engine_host'] = 'a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud'
        engine_details_model_model['associated_catalogs'] = ['testString']

        producer_input_model_model = {}  # ProducerInputModel
        producer_input_model_model['engine_details'] = engine_details_model_model

        delivery_method_properties_model_model = {}  # DeliveryMethodPropertiesModel
        delivery_method_properties_model_model['producer_input'] = producer_input_model_model

        # Construct a json representation of a DeliveryMethod model
        delivery_method_model_json = {}
        delivery_method_model_json['id'] = '09cf5fcc-cb9d-4995-a8e4-16517b25229f'
        delivery_method_model_json['container'] = container_reference_model
        delivery_method_model_json['getproperties'] = delivery_method_properties_model_model

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


class TestModel_DeliveryMethodPropertiesModel:
    """
    Test Class for DeliveryMethodPropertiesModel
    """

    def test_delivery_method_properties_model_serialization(self):
        """
        Test serialization/deserialization for DeliveryMethodPropertiesModel
        """

        # Construct dict forms of any model objects needed in order to build this model.

        engine_details_model_model = {}  # EngineDetailsModel
        engine_details_model_model['display_name'] = 'Iceberg Engine'
        engine_details_model_model['engine_id'] = 'presto767'
        engine_details_model_model['engine_port'] = '34567'
        engine_details_model_model['engine_host'] = 'a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud'
        engine_details_model_model['associated_catalogs'] = ['testString']

        producer_input_model_model = {}  # ProducerInputModel
        producer_input_model_model['engine_details'] = engine_details_model_model

        # Construct a json representation of a DeliveryMethodPropertiesModel model
        delivery_method_properties_model_model_json = {}
        delivery_method_properties_model_model_json['producer_input'] = producer_input_model_model

        # Construct a model instance of DeliveryMethodPropertiesModel by calling from_dict on the json representation
        delivery_method_properties_model_model = DeliveryMethodPropertiesModel.from_dict(delivery_method_properties_model_model_json)
        assert delivery_method_properties_model_model != False

        # Construct a model instance of DeliveryMethodPropertiesModel by calling from_dict on the json representation
        delivery_method_properties_model_model_dict = DeliveryMethodPropertiesModel.from_dict(delivery_method_properties_model_model_json).__dict__
        delivery_method_properties_model_model2 = DeliveryMethodPropertiesModel(**delivery_method_properties_model_model_dict)

        # Verify the model instances are equivalent
        assert delivery_method_properties_model_model == delivery_method_properties_model_model2

        # Convert model instance back to dict and verify no loss of data
        delivery_method_properties_model_model_json2 = delivery_method_properties_model_model.to_dict()
        assert delivery_method_properties_model_model_json2 == delivery_method_properties_model_model_json


class TestModel_Description:
    """
    Test Class for Description
    """

    def test_description_serialization(self):
        """
        Test serialization/deserialization for Description
        """

        # Construct dict forms of any model objects needed in order to build this model.

        contract_terms_more_info_model = {}  # ContractTermsMoreInfo
        contract_terms_more_info_model['type'] = 'privacy-statement'
        contract_terms_more_info_model['url'] = 'https://moreinfo.example.com'

        # Construct a json representation of a Description model
        description_model_json = {}
        description_model_json['purpose'] = 'Used for customer behavior analysis.'
        description_model_json['limitations'] = 'Data cannot be used for marketing.'
        description_model_json['usage'] = 'Data should be used only for analytics.'
        description_model_json['more_info'] = [contract_terms_more_info_model]
        description_model_json['custom_properties'] = '{"property1":"value1"}'

        # Construct a model instance of Description by calling from_dict on the json representation
        description_model = Description.from_dict(description_model_json)
        assert description_model != False

        # Construct a model instance of Description by calling from_dict on the json representation
        description_model_dict = Description.from_dict(description_model_json).__dict__
        description_model2 = Description(**description_model_dict)

        # Verify the model instances are equivalent
        assert description_model == description_model2

        # Convert model instance back to dict and verify no loss of data
        description_model_json2 = description_model.to_dict()
        assert description_model_json2 == description_model_json


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


class TestModel_EngineDetailsModel:
    """
    Test Class for EngineDetailsModel
    """

    def test_engine_details_model_serialization(self):
        """
        Test serialization/deserialization for EngineDetailsModel
        """

        # Construct a json representation of a EngineDetailsModel model
        engine_details_model_model_json = {}
        engine_details_model_model_json['display_name'] = 'Iceberg Engine'
        engine_details_model_model_json['engine_id'] = 'presto767'
        engine_details_model_model_json['engine_port'] = '34567'
        engine_details_model_model_json['engine_host'] = 'a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud'
        engine_details_model_model_json['associated_catalogs'] = ['testString']

        # Construct a model instance of EngineDetailsModel by calling from_dict on the json representation
        engine_details_model_model = EngineDetailsModel.from_dict(engine_details_model_model_json)
        assert engine_details_model_model != False

        # Construct a model instance of EngineDetailsModel by calling from_dict on the json representation
        engine_details_model_model_dict = EngineDetailsModel.from_dict(engine_details_model_model_json).__dict__
        engine_details_model_model2 = EngineDetailsModel(**engine_details_model_model_dict)

        # Verify the model instances are equivalent
        assert engine_details_model_model == engine_details_model_model2

        # Convert model instance back to dict and verify no loss of data
        engine_details_model_model_json2 = engine_details_model_model.to_dict()
        assert engine_details_model_model_json2 == engine_details_model_model_json


class TestModel_ErrorExtraResource:
    """
    Test Class for ErrorExtraResource
    """

    def test_error_extra_resource_serialization(self):
        """
        Test serialization/deserialization for ErrorExtraResource
        """

        # Construct a json representation of a ErrorExtraResource model
        error_extra_resource_model_json = {}
        error_extra_resource_model_json['id'] = 'testString'
        error_extra_resource_model_json['timestamp'] = '2019-01-01T12:00:00Z'
        error_extra_resource_model_json['environment_name'] = 'testString'
        error_extra_resource_model_json['http_status'] = 0
        error_extra_resource_model_json['source_cluster'] = 0
        error_extra_resource_model_json['source_component'] = 0
        error_extra_resource_model_json['transaction_id'] = 0

        # Construct a model instance of ErrorExtraResource by calling from_dict on the json representation
        error_extra_resource_model = ErrorExtraResource.from_dict(error_extra_resource_model_json)
        assert error_extra_resource_model != False

        # Construct a model instance of ErrorExtraResource by calling from_dict on the json representation
        error_extra_resource_model_dict = ErrorExtraResource.from_dict(error_extra_resource_model_json).__dict__
        error_extra_resource_model2 = ErrorExtraResource(**error_extra_resource_model_dict)

        # Verify the model instances are equivalent
        assert error_extra_resource_model == error_extra_resource_model2

        # Convert model instance back to dict and verify no loss of data
        error_extra_resource_model_json2 = error_extra_resource_model.to_dict()
        assert error_extra_resource_model_json2 == error_extra_resource_model_json


class TestModel_ErrorMessage:
    """
    Test Class for ErrorMessage
    """

    def test_error_message_serialization(self):
        """
        Test serialization/deserialization for ErrorMessage
        """

        # Construct a json representation of a ErrorMessage model
        error_message_model_json = {}
        error_message_model_json['code'] = 'testString'
        error_message_model_json['message'] = 'testString'

        # Construct a model instance of ErrorMessage by calling from_dict on the json representation
        error_message_model = ErrorMessage.from_dict(error_message_model_json)
        assert error_message_model != False

        # Construct a model instance of ErrorMessage by calling from_dict on the json representation
        error_message_model_dict = ErrorMessage.from_dict(error_message_model_json).__dict__
        error_message_model2 = ErrorMessage(**error_message_model_dict)

        # Verify the model instances are equivalent
        assert error_message_model == error_message_model2

        # Convert model instance back to dict and verify no loss of data
        error_message_model_json2 = error_message_model.to_dict()
        assert error_message_model_json2 == error_message_model_json


class TestModel_ErrorModelResource:
    """
    Test Class for ErrorModelResource
    """

    def test_error_model_resource_serialization(self):
        """
        Test serialization/deserialization for ErrorModelResource
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_extra_resource_model = {}  # ErrorExtraResource
        error_extra_resource_model['id'] = 'testString'
        error_extra_resource_model['timestamp'] = '2019-01-01T12:00:00Z'
        error_extra_resource_model['environment_name'] = 'testString'
        error_extra_resource_model['http_status'] = 0
        error_extra_resource_model['source_cluster'] = 0
        error_extra_resource_model['source_component'] = 0
        error_extra_resource_model['transaction_id'] = 0

        # Construct a json representation of a ErrorModelResource model
        error_model_resource_model_json = {}
        error_model_resource_model_json['code'] = 'request_body_error'
        error_model_resource_model_json['message'] = 'testString'
        error_model_resource_model_json['extra'] = error_extra_resource_model
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

        error_extra_resource_model = {}  # ErrorExtraResource
        error_extra_resource_model['id'] = 'testString'
        error_extra_resource_model['timestamp'] = '2019-01-01T12:00:00Z'
        error_extra_resource_model['environment_name'] = 'testString'
        error_extra_resource_model['http_status'] = 0
        error_extra_resource_model['source_cluster'] = 0
        error_extra_resource_model['source_component'] = 0
        error_extra_resource_model['transaction_id'] = 0

        error_model_resource_model = {}  # ErrorModelResource
        error_model_resource_model['code'] = 'request_body_error'
        error_model_resource_model['message'] = 'testString'
        error_model_resource_model['extra'] = error_extra_resource_model
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
        initialize_resource_model_json['href'] = 'https://api.example.com/configuration/initialize/status?catalog_id=d29c42eb-7100-4b7a-8257-c196dbcca1cd'
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


class TestModel_InitializeSubDomain:
    """
    Test Class for InitializeSubDomain
    """

    def test_initialize_sub_domain_serialization(self):
        """
        Test serialization/deserialization for InitializeSubDomain
        """

        # Construct a json representation of a InitializeSubDomain model
        initialize_sub_domain_model_json = {}
        initialize_sub_domain_model_json['name'] = 'Operations'
        initialize_sub_domain_model_json['id'] = 'testString'
        initialize_sub_domain_model_json['description'] = 'testString'

        # Construct a model instance of InitializeSubDomain by calling from_dict on the json representation
        initialize_sub_domain_model = InitializeSubDomain.from_dict(initialize_sub_domain_model_json)
        assert initialize_sub_domain_model != False

        # Construct a model instance of InitializeSubDomain by calling from_dict on the json representation
        initialize_sub_domain_model_dict = InitializeSubDomain.from_dict(initialize_sub_domain_model_json).__dict__
        initialize_sub_domain_model2 = InitializeSubDomain(**initialize_sub_domain_model_dict)

        # Verify the model instances are equivalent
        assert initialize_sub_domain_model == initialize_sub_domain_model2

        # Convert model instance back to dict and verify no loss of data
        initialize_sub_domain_model_json2 = initialize_sub_domain_model.to_dict()
        assert initialize_sub_domain_model_json2 == initialize_sub_domain_model_json


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


class TestModel_MemberRolesSchema:
    """
    Test Class for MemberRolesSchema
    """

    def test_member_roles_schema_serialization(self):
        """
        Test serialization/deserialization for MemberRolesSchema
        """

        # Construct a json representation of a MemberRolesSchema model
        member_roles_schema_model_json = {}
        member_roles_schema_model_json['user_iam_id'] = 'testString'
        member_roles_schema_model_json['roles'] = ['testString']

        # Construct a model instance of MemberRolesSchema by calling from_dict on the json representation
        member_roles_schema_model = MemberRolesSchema.from_dict(member_roles_schema_model_json)
        assert member_roles_schema_model != False

        # Construct a model instance of MemberRolesSchema by calling from_dict on the json representation
        member_roles_schema_model_dict = MemberRolesSchema.from_dict(member_roles_schema_model_json).__dict__
        member_roles_schema_model2 = MemberRolesSchema(**member_roles_schema_model_dict)

        # Verify the model instances are equivalent
        assert member_roles_schema_model == member_roles_schema_model2

        # Convert model instance back to dict and verify no loss of data
        member_roles_schema_model_json2 = member_roles_schema_model.to_dict()
        assert member_roles_schema_model_json2 == member_roles_schema_model_json


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


class TestModel_Overview:
    """
    Test Class for Overview
    """

    def test_overview_serialization(self):
        """
        Test serialization/deserialization for Overview
        """

        # Construct dict forms of any model objects needed in order to build this model.

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        domain_model = {}  # Domain
        domain_model['id'] = 'testString'
        domain_model['name'] = 'testString'
        domain_model['container'] = container_reference_model

        # Construct a json representation of a Overview model
        overview_model_json = {}
        overview_model_json['api_version'] = 'v3.0.1'
        overview_model_json['kind'] = 'DataContract'
        overview_model_json['name'] = 'Sample Data Contract'
        overview_model_json['version'] = '0.0.0'
        overview_model_json['domain'] = domain_model
        overview_model_json['more_info'] = 'List of links to sources that provide more details on the data contract.'

        # Construct a model instance of Overview by calling from_dict on the json representation
        overview_model = Overview.from_dict(overview_model_json)
        assert overview_model != False

        # Construct a model instance of Overview by calling from_dict on the json representation
        overview_model_dict = Overview.from_dict(overview_model_json).__dict__
        overview_model2 = Overview(**overview_model_dict)

        # Verify the model instances are equivalent
        assert overview_model == overview_model2

        # Convert model instance back to dict and verify no loss of data
        overview_model_json2 = overview_model.to_dict()
        assert overview_model_json2 == overview_model_json


class TestModel_Pricing:
    """
    Test Class for Pricing
    """

    def test_pricing_serialization(self):
        """
        Test serialization/deserialization for Pricing
        """

        # Construct a json representation of a Pricing model
        pricing_model_json = {}
        pricing_model_json['amount'] = '100.0'
        pricing_model_json['currency'] = 'USD'
        pricing_model_json['unit'] = 'megabyte'

        # Construct a model instance of Pricing by calling from_dict on the json representation
        pricing_model = Pricing.from_dict(pricing_model_json)
        assert pricing_model != False

        # Construct a model instance of Pricing by calling from_dict on the json representation
        pricing_model_dict = Pricing.from_dict(pricing_model_json).__dict__
        pricing_model2 = Pricing(**pricing_model_dict)

        # Verify the model instances are equivalent
        assert pricing_model == pricing_model2

        # Convert model instance back to dict and verify no loss of data
        pricing_model_json2 = pricing_model.to_dict()
        assert pricing_model_json2 == pricing_model_json


class TestModel_ProducerInputModel:
    """
    Test Class for ProducerInputModel
    """

    def test_producer_input_model_serialization(self):
        """
        Test serialization/deserialization for ProducerInputModel
        """

        # Construct dict forms of any model objects needed in order to build this model.

        engine_details_model_model = {}  # EngineDetailsModel
        engine_details_model_model['display_name'] = 'Iceberg Engine'
        engine_details_model_model['engine_id'] = 'presto767'
        engine_details_model_model['engine_port'] = '34567'
        engine_details_model_model['engine_host'] = 'a109e0f6-2dfc-4954-a0ff-343d70f7da7b.someId.lakehouse.appdomain.cloud'
        engine_details_model_model['associated_catalogs'] = ['testString']

        # Construct a json representation of a ProducerInputModel model
        producer_input_model_model_json = {}
        producer_input_model_model_json['engine_details'] = engine_details_model_model

        # Construct a model instance of ProducerInputModel by calling from_dict on the json representation
        producer_input_model_model = ProducerInputModel.from_dict(producer_input_model_model_json)
        assert producer_input_model_model != False

        # Construct a model instance of ProducerInputModel by calling from_dict on the json representation
        producer_input_model_model_dict = ProducerInputModel.from_dict(producer_input_model_model_json).__dict__
        producer_input_model_model2 = ProducerInputModel(**producer_input_model_model_dict)

        # Verify the model instances are equivalent
        assert producer_input_model_model == producer_input_model_model2

        # Convert model instance back to dict and verify no loss of data
        producer_input_model_model_json2 = producer_input_model_model.to_dict()
        assert producer_input_model_model_json2 == producer_input_model_model_json


class TestModel_PropertiesSchema:
    """
    Test Class for PropertiesSchema
    """

    def test_properties_schema_serialization(self):
        """
        Test serialization/deserialization for PropertiesSchema
        """

        # Construct a json representation of a PropertiesSchema model
        properties_schema_model_json = {}
        properties_schema_model_json['value'] = 'testString'

        # Construct a model instance of PropertiesSchema by calling from_dict on the json representation
        properties_schema_model = PropertiesSchema.from_dict(properties_schema_model_json)
        assert properties_schema_model != False

        # Construct a model instance of PropertiesSchema by calling from_dict on the json representation
        properties_schema_model_dict = PropertiesSchema.from_dict(properties_schema_model_json).__dict__
        properties_schema_model2 = PropertiesSchema(**properties_schema_model_dict)

        # Verify the model instances are equivalent
        assert properties_schema_model == properties_schema_model2

        # Convert model instance back to dict and verify no loss of data
        properties_schema_model_json2 = properties_schema_model.to_dict()
        assert properties_schema_model_json2 == properties_schema_model_json


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
        provided_catalog_workflows_model_dict = ProvidedCatalogWorkflows.from_dict(provided_catalog_workflows_model_json).__dict__
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
        provided_workflow_resource_model_dict = ProvidedWorkflowResource.from_dict(provided_workflow_resource_model_json).__dict__
        provided_workflow_resource_model2 = ProvidedWorkflowResource(**provided_workflow_resource_model_dict)

        # Verify the model instances are equivalent
        assert provided_workflow_resource_model == provided_workflow_resource_model2

        # Convert model instance back to dict and verify no loss of data
        provided_workflow_resource_model_json2 = provided_workflow_resource_model.to_dict()
        assert provided_workflow_resource_model_json2 == provided_workflow_resource_model_json


class TestModel_Roles:
    """
    Test Class for Roles
    """

    def test_roles_serialization(self):
        """
        Test serialization/deserialization for Roles
        """

        # Construct a json representation of a Roles model
        roles_model_json = {}
        roles_model_json['role'] = 'owner'

        # Construct a model instance of Roles by calling from_dict on the json representation
        roles_model = Roles.from_dict(roles_model_json)
        assert roles_model != False

        # Construct a model instance of Roles by calling from_dict on the json representation
        roles_model_dict = Roles.from_dict(roles_model_json).__dict__
        roles_model2 = Roles(**roles_model_dict)

        # Verify the model instances are equivalent
        assert roles_model == roles_model2

        # Convert model instance back to dict and verify no loss of data
        roles_model_json2 = roles_model.to_dict()
        assert roles_model_json2 == roles_model_json


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
        service_id_credentials_model_json['created_at'] = '2019-01-01T12:00:00Z'

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


class TestModel_Visualization:
    """
    Test Class for Visualization
    """

    def test_visualization_serialization(self):
        """
        Test serialization/deserialization for Visualization
        """

        # Construct a json representation of a Visualization model
        visualization_model_json = {}
        visualization_model_json['id'] = 'testString'
        visualization_model_json['name'] = 'testString'

        # Construct a model instance of Visualization by calling from_dict on the json representation
        visualization_model = Visualization.from_dict(visualization_model_json)
        assert visualization_model != False

        # Construct a model instance of Visualization by calling from_dict on the json representation
        visualization_model_dict = Visualization.from_dict(visualization_model_json).__dict__
        visualization_model2 = Visualization(**visualization_model_dict)

        # Verify the model instances are equivalent
        assert visualization_model == visualization_model2

        # Convert model instance back to dict and verify no loss of data
        visualization_model_json2 = visualization_model.to_dict()
        assert visualization_model_json2 == visualization_model_json


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
        workflow_definition_reference_model = WorkflowDefinitionReference.from_dict(workflow_definition_reference_model_json)
        assert workflow_definition_reference_model != False

        # Construct a model instance of WorkflowDefinitionReference by calling from_dict on the json representation
        workflow_definition_reference_model_dict = WorkflowDefinitionReference.from_dict(workflow_definition_reference_model_json).__dict__
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
