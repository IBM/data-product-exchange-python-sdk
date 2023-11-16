# -*- coding: utf-8 -*-
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

"""
Unit Tests for DataProductExchangeApiServiceV1
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
from dph_services.data_product_exchange_api_service_v1 import *


_service = DataProductExchangeApiServiceV1(
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
    # First, unquote the path since it might have some quoted/escaped characters in it
    # due to how the generator inserts the operation paths into the unit test code.
    operation_path = urllib.parse.unquote(operation_path)

    # Next, quote the path using urllib so that we approximate what will
    # happen during request processing.
    operation_path = urllib.parse.quote(operation_path, safe='/')

    # Finally, form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if re.fullmatch('.*/+', request_url) is None:
        return request_url
    else:
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

        service = DataProductExchangeApiServiceV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DataProductExchangeApiServiceV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DataProductExchangeApiServiceV1.new_instance(
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
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "href": "http://api.example.com/configuration/initialize/status?catalog_id=d29c42eb-7100-4b7a-8257-c196dbcca1cd", "status": "not_started", "trace": "trace", "errors": [{"code": "code", "target": {"type": "field", "name": "name"}, "message": "message", "more_info": "more_info"}], "last_started_at": "2023-08-21T15:24:06.021Z", "last_finished_at": "2023-08-21T20:24:34.450Z", "initialized_options": [{"name": "name", "version": 1}]}'
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
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "href": "http://api.example.com/configuration/initialize/status?catalog_id=d29c42eb-7100-4b7a-8257-c196dbcca1cd", "status": "not_started", "trace": "trace", "errors": [{"code": "code", "target": {"type": "field", "name": "name"}, "message": "message", "more_info": "more_info"}], "last_started_at": "2023-08-21T15:24:06.021Z", "last_finished_at": "2023-08-21T20:24:34.450Z", "initialized_options": [{"name": "name", "version": 1}]}'
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
        mock_response = '{"container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "href": "http://api.example.com/configuration/initialize/status?catalog_id=d29c42eb-7100-4b7a-8257-c196dbcca1cd", "status": "not_started", "trace": "trace", "errors": [{"code": "code", "target": {"type": "field", "name": "name"}, "message": "message", "more_info": "more_info"}], "last_started_at": "2023-08-21T15:24:06.021Z", "last_finished_at": "2023-08-21T20:24:34.450Z", "initialized_options": [{"name": "name", "version": 1}]}'
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
        include = ['delivery_methods', 'data_product_samples', 'domains_multi_industry']

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
        assert req_body['include'] == ['delivery_methods', 'data_product_samples', 'domains_multi_industry']

    def test_initialize_all_params_with_retries(self):
        # Enable retries and run test_initialize_all_params.
        _service.enable_retries()
        self.test_initialize_all_params()

        # Disable retries and run test_initialize_all_params.
        _service.disable_retries()
        self.test_initialize_all_params()


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

        service = DataProductExchangeApiServiceV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DataProductExchangeApiServiceV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DataProductExchangeApiServiceV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


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
        mock_response = '{"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "name": "Sample Data Product"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.get_data_product(
            id,
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
        mock_response = '{"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "name": "Sample Data Product"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
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
        mock_response = '{"limit": 200, "first": {"href": "http://api.example.com/collection"}, "next": {"href": "http://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "data_products": [{"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "name": "Sample Data Product"}]}'
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
        mock_response = '{"limit": 200, "first": {"href": "http://api.example.com/collection"}, "next": {"href": "http://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "data_products": [{"id": "b38df608-d34b-4d58-8136-ed25e6c6684e", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "name": "Sample Data Product"}]}'
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
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"data_products":[{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"name":"Sample Data Product"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"data_products":[{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"name":"Sample Data Product"}]}'
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
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"data_products":[{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"name":"Sample Data Product"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"data_products":[{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"},"name":"Sample Data Product"}]}'
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


# endregion
##############################################################################
# End of Service: DataProducts
##############################################################################

##############################################################################
# Start of Service: DataProductVersions
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

        service = DataProductExchangeApiServiceV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DataProductExchangeApiServiceV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DataProductExchangeApiServiceV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListDataProductVersions:
    """
    Test Class for list_data_product_versions
    """

    @responses.activate
    def test_list_data_product_versions_all_params(self):
        """
        list_data_product_versions()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_product_versions')
        mock_response = '{"limit": 200, "first": {"href": "http://api.example.com/collection"}, "next": {"href": "http://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "data_product_versions": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e"}, "name": "My Data Product", "description": "This is a description of My Data Product.", "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        asset_container_id = 'testString'
        data_product = 'testString'
        state = 'draft'
        version = 'testString'
        limit = 200
        start = 'testString'

        # Invoke method
        response = _service.list_data_product_versions(
            asset_container_id=asset_container_id,
            data_product=data_product,
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
        assert 'data_product={}'.format(data_product) in query_string
        assert 'state={}'.format(state) in query_string
        assert 'version={}'.format(version) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_data_product_versions_all_params_with_retries(self):
        # Enable retries and run test_list_data_product_versions_all_params.
        _service.enable_retries()
        self.test_list_data_product_versions_all_params()

        # Disable retries and run test_list_data_product_versions_all_params.
        _service.disable_retries()
        self.test_list_data_product_versions_all_params()

    @responses.activate
    def test_list_data_product_versions_required_params(self):
        """
        test_list_data_product_versions_required_params()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_product_versions')
        mock_response = '{"limit": 200, "first": {"href": "http://api.example.com/collection"}, "next": {"href": "http://api.example.com/collection?start=eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9", "start": "eyJvZmZzZXQiOjAsImRvbmUiOnRydWV9"}, "data_product_versions": [{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e"}, "name": "My Data Product", "description": "This is a description of My Data Product.", "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_data_product_versions()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_data_product_versions_required_params_with_retries(self):
        # Enable retries and run test_list_data_product_versions_required_params.
        _service.enable_retries()
        self.test_list_data_product_versions_required_params()

        # Disable retries and run test_list_data_product_versions_required_params.
        _service.disable_retries()
        self.test_list_data_product_versions_required_params()

    @responses.activate
    def test_list_data_product_versions_with_pager_get_next(self):
        """
        test_list_data_product_versions_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/data_product_exchange/v1/data_product_versions')
        mock_response1 = '{"next":{"start":"1"},"data_product_versions":[{"version":"1.0.0","state":"draft","data_product":{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e"},"name":"My Data Product","description":"This is a description of My Data Product.","id":"2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd","asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}}],"total_count":2,"limit":1}'
        mock_response2 = '{"data_product_versions":[{"version":"1.0.0","state":"draft","data_product":{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e"},"name":"My Data Product","description":"This is a description of My Data Product.","id":"2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd","asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}}],"total_count":2,"limit":1}'
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
        pager = DataProductVersionsPager(
            client=_service,
            asset_container_id='testString',
            data_product='testString',
            state='draft',
            version='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_data_product_versions_with_pager_get_all(self):
        """
        test_list_data_product_versions_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/data_product_exchange/v1/data_product_versions')
        mock_response1 = '{"next":{"start":"1"},"data_product_versions":[{"version":"1.0.0","state":"draft","data_product":{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e"},"name":"My Data Product","description":"This is a description of My Data Product.","id":"2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd","asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}}],"total_count":2,"limit":1}'
        mock_response2 = '{"data_product_versions":[{"version":"1.0.0","state":"draft","data_product":{"id":"b38df608-d34b-4d58-8136-ed25e6c6684e"},"name":"My Data Product","description":"This is a description of My Data Product.","id":"2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd","asset":{"id":"2b0bf220-079c-11ee-be56-0242ac120002","container":{"id":"d29c42eb-7100-4b7a-8257-c196dbcca1cd","type":"catalog"}}}],"total_count":2,"limit":1}'
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
        pager = DataProductVersionsPager(
            client=_service,
            asset_container_id='testString',
            data_product='testString',
            state='draft',
            version='testString',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateDataProductVersion:
    """
    Test Class for create_data_product_version
    """

    @responses.activate
    def test_create_data_product_version_all_params(self):
        """
        create_data_product_version()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_product_versions')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e"}, "name": "My Data Product", "description": "This is a description of My Data Product.", "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "type": ["data"], "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "revision": 1, "updated_at": "2023-07-01T22:22:34.876Z", "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}], "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {}
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Construct a dict representation of a DataProductIdentity model
        data_product_identity_model = {}
        data_product_identity_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'

        # Construct a dict representation of a UseCase model
        use_case_model = {}
        use_case_model['id'] = 'testString'
        use_case_model['name'] = 'testString'
        use_case_model['container'] = container_reference_model

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
        data_product_part_model['revision'] = 1
        data_product_part_model['updated_at'] = '2023-07-01T22:22:34.876000Z'
        data_product_part_model['delivery_methods'] = [delivery_method_model]

        # Set up parameter values
        container = container_reference_model
        version = 'testString'
        state = 'draft'
        data_product = data_product_identity_model
        name = 'My New Data Product'
        description = 'testString'
        tags = ['testString']
        use_cases = [use_case_model]
        domain = domain_model
        type = ['data']
        parts_out = [data_product_part_model]

        # Invoke method
        response = _service.create_data_product_version(
            container,
            version=version,
            state=state,
            data_product=data_product,
            name=name,
            description=description,
            tags=tags,
            use_cases=use_cases,
            domain=domain,
            type=type,
            parts_out=parts_out,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['container'] == container_reference_model
        assert req_body['version'] == 'testString'
        assert req_body['state'] == 'draft'
        assert req_body['data_product'] == data_product_identity_model
        assert req_body['name'] == 'My New Data Product'
        assert req_body['description'] == 'testString'
        assert req_body['tags'] == ['testString']
        assert req_body['use_cases'] == [use_case_model]
        assert req_body['domain'] == domain_model
        assert req_body['type'] == ['data']
        assert req_body['parts_out'] == [data_product_part_model]

    def test_create_data_product_version_all_params_with_retries(self):
        # Enable retries and run test_create_data_product_version_all_params.
        _service.enable_retries()
        self.test_create_data_product_version_all_params()

        # Disable retries and run test_create_data_product_version_all_params.
        _service.disable_retries()
        self.test_create_data_product_version_all_params()

    @responses.activate
    def test_create_data_product_version_value_error(self):
        """
        test_create_data_product_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_product_versions')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e"}, "name": "My Data Product", "description": "This is a description of My Data Product.", "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "type": ["data"], "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "revision": 1, "updated_at": "2023-07-01T22:22:34.876Z", "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}], "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {}
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Construct a dict representation of a DataProductIdentity model
        data_product_identity_model = {}
        data_product_identity_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'

        # Construct a dict representation of a UseCase model
        use_case_model = {}
        use_case_model['id'] = 'testString'
        use_case_model['name'] = 'testString'
        use_case_model['container'] = container_reference_model

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
        data_product_part_model['revision'] = 1
        data_product_part_model['updated_at'] = '2023-07-01T22:22:34.876000Z'
        data_product_part_model['delivery_methods'] = [delivery_method_model]

        # Set up parameter values
        container = container_reference_model
        version = 'testString'
        state = 'draft'
        data_product = data_product_identity_model
        name = 'My New Data Product'
        description = 'testString'
        tags = ['testString']
        use_cases = [use_case_model]
        domain = domain_model
        type = ['data']
        parts_out = [data_product_part_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "container": container,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_data_product_version(**req_copy)

    def test_create_data_product_version_value_error_with_retries(self):
        # Enable retries and run test_create_data_product_version_value_error.
        _service.enable_retries()
        self.test_create_data_product_version_value_error()

        # Disable retries and run test_create_data_product_version_value_error.
        _service.disable_retries()
        self.test_create_data_product_version_value_error()


class TestGetDataProductVersion:
    """
    Test Class for get_data_product_version
    """

    @responses.activate
    def test_get_data_product_version_all_params(self):
        """
        get_data_product_version()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_product_versions/testString')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e"}, "name": "My Data Product", "description": "This is a description of My Data Product.", "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "type": ["data"], "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "revision": 1, "updated_at": "2023-07-01T22:22:34.876Z", "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}], "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.get_data_product_version(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_data_product_version_all_params_with_retries(self):
        # Enable retries and run test_get_data_product_version_all_params.
        _service.enable_retries()
        self.test_get_data_product_version_all_params()

        # Disable retries and run test_get_data_product_version_all_params.
        _service.disable_retries()
        self.test_get_data_product_version_all_params()

    @responses.activate
    def test_get_data_product_version_value_error(self):
        """
        test_get_data_product_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_product_versions/testString')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e"}, "name": "My Data Product", "description": "This is a description of My Data Product.", "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "type": ["data"], "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "revision": 1, "updated_at": "2023-07-01T22:22:34.876Z", "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}], "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_data_product_version(**req_copy)

    def test_get_data_product_version_value_error_with_retries(self):
        # Enable retries and run test_get_data_product_version_value_error.
        _service.enable_retries()
        self.test_get_data_product_version_value_error()

        # Disable retries and run test_get_data_product_version_value_error.
        _service.disable_retries()
        self.test_get_data_product_version_value_error()


class TestDeleteDataProductVersion:
    """
    Test Class for delete_data_product_version
    """

    @responses.activate
    def test_delete_data_product_version_all_params(self):
        """
        delete_data_product_version()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_product_versions/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.delete_data_product_version(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_data_product_version_all_params_with_retries(self):
        # Enable retries and run test_delete_data_product_version_all_params.
        _service.enable_retries()
        self.test_delete_data_product_version_all_params()

        # Disable retries and run test_delete_data_product_version_all_params.
        _service.disable_retries()
        self.test_delete_data_product_version_all_params()

    @responses.activate
    def test_delete_data_product_version_value_error(self):
        """
        test_delete_data_product_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_product_versions/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_data_product_version(**req_copy)

    def test_delete_data_product_version_value_error_with_retries(self):
        # Enable retries and run test_delete_data_product_version_value_error.
        _service.enable_retries()
        self.test_delete_data_product_version_value_error()

        # Disable retries and run test_delete_data_product_version_value_error.
        _service.disable_retries()
        self.test_delete_data_product_version_value_error()


class TestUpdateDataProductVersion:
    """
    Test Class for update_data_product_version
    """

    @responses.activate
    def test_update_data_product_version_all_params(self):
        """
        update_data_product_version()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_product_versions/testString')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e"}, "name": "My Data Product", "description": "This is a description of My Data Product.", "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "type": ["data"], "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "revision": 1, "updated_at": "2023-07-01T22:22:34.876Z", "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}], "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z"}'
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
        id = 'testString'
        json_patch_instructions = [json_patch_operation_model]

        # Invoke method
        response = _service.update_data_product_version(
            id,
            json_patch_instructions,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == json_patch_instructions

    def test_update_data_product_version_all_params_with_retries(self):
        # Enable retries and run test_update_data_product_version_all_params.
        _service.enable_retries()
        self.test_update_data_product_version_all_params()

        # Disable retries and run test_update_data_product_version_all_params.
        _service.disable_retries()
        self.test_update_data_product_version_all_params()

    @responses.activate
    def test_update_data_product_version_value_error(self):
        """
        test_update_data_product_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_product_versions/testString')
        mock_response = '{"version": "1.0.0", "state": "draft", "data_product": {"id": "b38df608-d34b-4d58-8136-ed25e6c6684e"}, "name": "My Data Product", "description": "This is a description of My Data Product.", "id": "2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd", "asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "tags": ["tags"], "use_cases": [{"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}], "domain": {"id": "id", "name": "name", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}, "type": ["data"], "parts_out": [{"asset": {"id": "2b0bf220-079c-11ee-be56-0242ac120002", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}, "type": "data_asset"}, "revision": 1, "updated_at": "2023-07-01T22:22:34.876Z", "delivery_methods": [{"id": "09cf5fcc-cb9d-4995-a8e4-16517b25229f", "container": {"id": "d29c42eb-7100-4b7a-8257-c196dbcca1cd", "type": "catalog"}}]}], "published_by": "published_by", "published_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "created_at": "2019-01-01T12:00:00.000Z"}'
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
        id = 'testString'
        json_patch_instructions = [json_patch_operation_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "json_patch_instructions": json_patch_instructions,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_data_product_version(**req_copy)

    def test_update_data_product_version_value_error_with_retries(self):
        # Enable retries and run test_update_data_product_version_value_error.
        _service.enable_retries()
        self.test_update_data_product_version_value_error()

        # Disable retries and run test_update_data_product_version_value_error.
        _service.disable_retries()
        self.test_update_data_product_version_value_error()


class TestDeliverDataProductVersion:
    """
    Test Class for deliver_data_product_version
    """

    @responses.activate
    def test_deliver_data_product_version_all_params(self):
        """
        deliver_data_product_version()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_product_versions/testString/deliver')
        mock_response = '{"status": "not_started", "href": "href"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Construct a dict representation of a ItemReference model
        item_reference_model = {}
        item_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'

        # Construct a dict representation of a OrderReference model
        order_reference_model = {}
        order_reference_model['id'] = '4705e047-1808-459a-805f-d5d13c947637'
        order_reference_model['items'] = [item_reference_model]

        # Set up parameter values
        id = 'testString'
        order = order_reference_model

        # Invoke method
        response = _service.deliver_data_product_version(
            id,
            order=order,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['order'] == order_reference_model

    def test_deliver_data_product_version_all_params_with_retries(self):
        # Enable retries and run test_deliver_data_product_version_all_params.
        _service.enable_retries()
        self.test_deliver_data_product_version_all_params()

        # Disable retries and run test_deliver_data_product_version_all_params.
        _service.disable_retries()
        self.test_deliver_data_product_version_all_params()

    @responses.activate
    def test_deliver_data_product_version_value_error(self):
        """
        test_deliver_data_product_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/data_product_exchange/v1/data_product_versions/testString/deliver')
        mock_response = '{"status": "not_started", "href": "href"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Construct a dict representation of a ItemReference model
        item_reference_model = {}
        item_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'

        # Construct a dict representation of a OrderReference model
        order_reference_model = {}
        order_reference_model['id'] = '4705e047-1808-459a-805f-d5d13c947637'
        order_reference_model['items'] = [item_reference_model]

        # Set up parameter values
        id = 'testString'
        order = order_reference_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.deliver_data_product_version(**req_copy)

    def test_deliver_data_product_version_value_error_with_retries(self):
        # Enable retries and run test_deliver_data_product_version_value_error.
        _service.enable_retries()
        self.test_deliver_data_product_version_value_error()

        # Disable retries and run test_deliver_data_product_version_value_error.
        _service.disable_retries()
        self.test_deliver_data_product_version_value_error()


# endregion
##############################################################################
# End of Service: DataProductVersions
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


class TestModel_DataProduct:
    """
    Test Class for DataProduct
    """

    def test_data_product_serialization(self):
        """
        Test serialization/deserialization for DataProduct
        """

        # Construct dict forms of any model objects needed in order to build this model.

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        # Construct a json representation of a DataProduct model
        data_product_model_json = {}
        data_product_model_json['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_model_json['container'] = container_reference_model
        data_product_model_json['name'] = 'Sample Data Product'

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

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        data_product_model = {}  # DataProduct
        data_product_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'
        data_product_model['container'] = container_reference_model
        data_product_model['name'] = 'Sample Data Product'

        # Construct a json representation of a DataProductCollection model
        data_product_collection_model_json = {}
        data_product_collection_model_json['limit'] = 200
        data_product_collection_model_json['first'] = first_page_model
        data_product_collection_model_json['next'] = next_page_model
        data_product_collection_model_json['data_products'] = [data_product_model]

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


class TestModel_DataProductIdentity:
    """
    Test Class for DataProductIdentity
    """

    def test_data_product_identity_serialization(self):
        """
        Test serialization/deserialization for DataProductIdentity
        """

        # Construct a json representation of a DataProductIdentity model
        data_product_identity_model_json = {}
        data_product_identity_model_json['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'

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
        data_product_part_model_json['revision'] = 1
        data_product_part_model_json['updated_at'] = '2023-07-01T22:22:34.876000Z'
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


class TestModel_DataProductVersion:
    """
    Test Class for DataProductVersion
    """

    def test_data_product_version_serialization(self):
        """
        Test serialization/deserialization for DataProductVersion
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_product_identity_model = {}  # DataProductIdentity
        data_product_identity_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        asset_reference_model = {}  # AssetReference
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['container'] = container_reference_model

        use_case_model = {}  # UseCase
        use_case_model['id'] = 'testString'
        use_case_model['name'] = 'testString'
        use_case_model['container'] = container_reference_model

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
        data_product_part_model['revision'] = 1
        data_product_part_model['updated_at'] = '2023-07-01T22:22:34.876000Z'
        data_product_part_model['delivery_methods'] = [delivery_method_model]

        # Construct a json representation of a DataProductVersion model
        data_product_version_model_json = {}
        data_product_version_model_json['version'] = '1.0.0'
        data_product_version_model_json['state'] = 'draft'
        data_product_version_model_json['data_product'] = data_product_identity_model
        data_product_version_model_json['name'] = 'My Data Product'
        data_product_version_model_json['description'] = 'This is a description of My Data Product.'
        data_product_version_model_json['id'] = '2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd'
        data_product_version_model_json['asset'] = asset_reference_model
        data_product_version_model_json['tags'] = ['testString']
        data_product_version_model_json['use_cases'] = [use_case_model]
        data_product_version_model_json['domain'] = domain_model
        data_product_version_model_json['type'] = ['data']
        data_product_version_model_json['parts_out'] = [data_product_part_model]
        data_product_version_model_json['published_by'] = 'testString'
        data_product_version_model_json['published_at'] = '2019-01-01T12:00:00Z'
        data_product_version_model_json['created_by'] = 'testString'
        data_product_version_model_json['created_at'] = '2019-01-01T12:00:00Z'

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

        data_product_identity_model = {}  # DataProductIdentity
        data_product_identity_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        asset_reference_model = {}  # AssetReference
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['container'] = container_reference_model

        data_product_version_summary_model = {}  # DataProductVersionSummary
        data_product_version_summary_model['version'] = '1.0.0'
        data_product_version_summary_model['state'] = 'draft'
        data_product_version_summary_model['data_product'] = data_product_identity_model
        data_product_version_summary_model['name'] = 'My Data Product'
        data_product_version_summary_model['description'] = 'This is a description of My Data Product.'
        data_product_version_summary_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002@d29c42eb-7100-4b7a-8257-c196dbcca1cd'
        data_product_version_summary_model['asset'] = asset_reference_model

        # Construct a json representation of a DataProductVersionCollection model
        data_product_version_collection_model_json = {}
        data_product_version_collection_model_json['limit'] = 200
        data_product_version_collection_model_json['first'] = first_page_model
        data_product_version_collection_model_json['next'] = next_page_model
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

        data_product_identity_model = {}  # DataProductIdentity
        data_product_identity_model['id'] = 'b38df608-d34b-4d58-8136-ed25e6c6684e'

        container_reference_model = {}  # ContainerReference
        container_reference_model['id'] = 'd29c42eb-7100-4b7a-8257-c196dbcca1cd'
        container_reference_model['type'] = 'catalog'

        asset_reference_model = {}  # AssetReference
        asset_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        asset_reference_model['container'] = container_reference_model

        # Construct a json representation of a DataProductVersionSummary model
        data_product_version_summary_model_json = {}
        data_product_version_summary_model_json['version'] = '1.0.0'
        data_product_version_summary_model_json['state'] = 'draft'
        data_product_version_summary_model_json['data_product'] = data_product_identity_model
        data_product_version_summary_model_json['name'] = 'My Data Product'
        data_product_version_summary_model_json['description'] = 'This is a description of My Data Product.'
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


class TestModel_DeliveryResource:
    """
    Test Class for DeliveryResource
    """

    def test_delivery_resource_serialization(self):
        """
        Test serialization/deserialization for DeliveryResource
        """

        # Construct a json representation of a DeliveryResource model
        delivery_resource_model_json = {}
        delivery_resource_model_json['status'] = 'not_started'
        delivery_resource_model_json['href'] = 'testString'

        # Construct a model instance of DeliveryResource by calling from_dict on the json representation
        delivery_resource_model = DeliveryResource.from_dict(delivery_resource_model_json)
        assert delivery_resource_model != False

        # Construct a model instance of DeliveryResource by calling from_dict on the json representation
        delivery_resource_model_dict = DeliveryResource.from_dict(delivery_resource_model_json).__dict__
        delivery_resource_model2 = DeliveryResource(**delivery_resource_model_dict)

        # Verify the model instances are equivalent
        assert delivery_resource_model == delivery_resource_model2

        # Convert model instance back to dict and verify no loss of data
        delivery_resource_model_json2 = delivery_resource_model.to_dict()
        assert delivery_resource_model_json2 == delivery_resource_model_json


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


class TestModel_ErrorModel:
    """
    Test Class for ErrorModel
    """

    def test_error_model_serialization(self):
        """
        Test serialization/deserialization for ErrorModel
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_target_model_model = {}  # ErrorTargetModel
        error_target_model_model['type'] = 'field'
        error_target_model_model['name'] = 'testString'

        # Construct a json representation of a ErrorModel model
        error_model_model_json = {}
        error_model_model_json['code'] = 'testString'
        error_model_model_json['target'] = error_target_model_model
        error_model_model_json['message'] = 'testString'
        error_model_model_json['more_info'] = 'testString'

        # Construct a model instance of ErrorModel by calling from_dict on the json representation
        error_model_model = ErrorModel.from_dict(error_model_model_json)
        assert error_model_model != False

        # Construct a model instance of ErrorModel by calling from_dict on the json representation
        error_model_model_dict = ErrorModel.from_dict(error_model_model_json).__dict__
        error_model_model2 = ErrorModel(**error_model_model_dict)

        # Verify the model instances are equivalent
        assert error_model_model == error_model_model2

        # Convert model instance back to dict and verify no loss of data
        error_model_model_json2 = error_model_model.to_dict()
        assert error_model_model_json2 == error_model_model_json


class TestModel_ErrorTargetModel:
    """
    Test Class for ErrorTargetModel
    """

    def test_error_target_model_serialization(self):
        """
        Test serialization/deserialization for ErrorTargetModel
        """

        # Construct a json representation of a ErrorTargetModel model
        error_target_model_model_json = {}
        error_target_model_model_json['type'] = 'field'
        error_target_model_model_json['name'] = 'testString'

        # Construct a model instance of ErrorTargetModel by calling from_dict on the json representation
        error_target_model_model = ErrorTargetModel.from_dict(error_target_model_model_json)
        assert error_target_model_model != False

        # Construct a model instance of ErrorTargetModel by calling from_dict on the json representation
        error_target_model_model_dict = ErrorTargetModel.from_dict(error_target_model_model_json).__dict__
        error_target_model_model2 = ErrorTargetModel(**error_target_model_model_dict)

        # Verify the model instances are equivalent
        assert error_target_model_model == error_target_model_model2

        # Convert model instance back to dict and verify no loss of data
        error_target_model_model_json2 = error_target_model_model.to_dict()
        assert error_target_model_model_json2 == error_target_model_model_json


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

        error_target_model_model = {}  # ErrorTargetModel
        error_target_model_model['type'] = 'field'
        error_target_model_model['name'] = 'testString'

        error_model_model = {}  # ErrorModel
        error_model_model['code'] = 'testString'
        error_model_model['target'] = error_target_model_model
        error_model_model['message'] = 'testString'
        error_model_model['more_info'] = 'testString'

        initialized_option_model = {}  # InitializedOption
        initialized_option_model['name'] = 'testString'
        initialized_option_model['version'] = 1

        # Construct a json representation of a InitializeResource model
        initialize_resource_model_json = {}
        initialize_resource_model_json['container'] = container_reference_model
        initialize_resource_model_json['href'] = 'https://api.example.com/configuration/initialize/status?catalog_id=d29c42eb-7100-4b7a-8257-c196dbcca1cd'
        initialize_resource_model_json['status'] = 'not_started'
        initialize_resource_model_json['trace'] = 'testString'
        initialize_resource_model_json['errors'] = [error_model_model]
        initialize_resource_model_json['last_started_at'] = '2023-08-21T15:24:06.021000Z'
        initialize_resource_model_json['last_finished_at'] = '2023-08-21T20:24:34.450000Z'
        initialize_resource_model_json['initialized_options'] = [initialized_option_model]

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


class TestModel_ItemReference:
    """
    Test Class for ItemReference
    """

    def test_item_reference_serialization(self):
        """
        Test serialization/deserialization for ItemReference
        """

        # Construct a json representation of a ItemReference model
        item_reference_model_json = {}
        item_reference_model_json['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'

        # Construct a model instance of ItemReference by calling from_dict on the json representation
        item_reference_model = ItemReference.from_dict(item_reference_model_json)
        assert item_reference_model != False

        # Construct a model instance of ItemReference by calling from_dict on the json representation
        item_reference_model_dict = ItemReference.from_dict(item_reference_model_json).__dict__
        item_reference_model2 = ItemReference(**item_reference_model_dict)

        # Verify the model instances are equivalent
        assert item_reference_model == item_reference_model2

        # Convert model instance back to dict and verify no loss of data
        item_reference_model_json2 = item_reference_model.to_dict()
        assert item_reference_model_json2 == item_reference_model_json


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


class TestModel_OrderReference:
    """
    Test Class for OrderReference
    """

    def test_order_reference_serialization(self):
        """
        Test serialization/deserialization for OrderReference
        """

        # Construct dict forms of any model objects needed in order to build this model.

        item_reference_model = {}  # ItemReference
        item_reference_model['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'

        # Construct a json representation of a OrderReference model
        order_reference_model_json = {}
        order_reference_model_json['id'] = '2b0bf220-079c-11ee-be56-0242ac120002'
        order_reference_model_json['items'] = [item_reference_model]

        # Construct a model instance of OrderReference by calling from_dict on the json representation
        order_reference_model = OrderReference.from_dict(order_reference_model_json)
        assert order_reference_model != False

        # Construct a model instance of OrderReference by calling from_dict on the json representation
        order_reference_model_dict = OrderReference.from_dict(order_reference_model_json).__dict__
        order_reference_model2 = OrderReference(**order_reference_model_dict)

        # Verify the model instances are equivalent
        assert order_reference_model == order_reference_model2

        # Convert model instance back to dict and verify no loss of data
        order_reference_model_json2 = order_reference_model.to_dict()
        assert order_reference_model_json2 == order_reference_model_json


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


# endregion
##############################################################################
# End of Model Tests
##############################################################################
