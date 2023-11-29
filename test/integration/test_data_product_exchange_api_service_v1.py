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
Integration Tests for DataProductExchangeApiServiceV1
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from ibm_dpx_services.data_product_exchange_api_service_v1 import *

# Config file name
config_file = 'data_product_exchange_api_service_v1.env'

# Variables to hold link values
create_data_product_version_by_catalog_id_link = None
delete_data_product_version_by_user_id_link = None
deliver_data_product_version_by_user_id_link = None
get_data_product_by_user_id_link = None
get_data_product_version_by_user_id_link = None
get_list_of_data_product_by_catalog_id_link = None
get_status_by_catalog_id_link = None
update_data_product_version_by_user_id_link = None


class TestDataProductExchangeApiServiceV1:
    """
    Integration Test Class for DataProductExchangeApiServiceV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.data_product_exchange_api_service_service = DataProductExchangeApiServiceV1.new_instance()
            assert cls.data_product_exchange_api_service_service is not None

            cls.config = read_external_sources(DataProductExchangeApiServiceV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.data_product_exchange_api_service_service.enable_retries()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_initialize(self):
        # Construct a dict representation of a ContainerReference model
        # container_reference_model = {
        #     'id': 'd29c42eb-7100-4b7a-8257-c196dbcca1cd',
        #     'type': 'catalog',
        # }

        response = self.data_product_exchange_api_service_service.initialize(
            container=None,
            include=['delivery_methods', 'data_product_samples', 'domains_multi_industry'],
        )

        assert response.get_status_code() == 202
        initialize_resource = response.get_result()
        assert initialize_resource is not None

        global create_data_product_version_by_catalog_id_link
        create_data_product_version_by_catalog_id_link = initialize_resource['container']['id']
        global get_status_by_catalog_id_link
        get_status_by_catalog_id_link = initialize_resource['container']['id']
        global get_list_of_data_product_by_catalog_id_link
        get_list_of_data_product_by_catalog_id_link = initialize_resource['container']['id']

    @needscredentials
    def test_create_data_product_version(self):
        # Construct a dict representation of a ContainerReference model
        container_reference_model = {
            'id': create_data_product_version_by_catalog_id_link,
            'type': 'catalog',
        }
        # Construct a dict representation of a DataProductIdentity model
        data_product_identity_model = {
            'id': 'b38df608-d34b-4d58-8136-ed25e6c6684e',
        }
        # Construct a dict representation of a UseCase model
        use_case_model = {
            'id': 'testString',
            'name': 'testString',
            'container': container_reference_model,
        }
        # Construct a dict representation of a Domain model
        domain_model = {
            'id': 'testString',
            'name': 'testString',
            'container': container_reference_model,
        }
        # Construct a dict representation of a AssetPartReference model
        asset_part_reference_model = {
            'id': '2b0bf220-079c-11ee-be56-0242ac120002',
            'container': container_reference_model,
            'type': 'data_asset',
        }
        # Construct a dict representation of a DeliveryMethod model
        delivery_method_model = {
            'id': '09cf5fcc-cb9d-4995-a8e4-16517b25229f',
            'container': container_reference_model,
        }
        # Construct a dict representation of a DataProductPart model
        data_product_part_model = {
            'asset': asset_part_reference_model,
            'revision': 1,
            'updated_at': '2023-07-01T22:22:34.876Z',
            'delivery_methods': [delivery_method_model],
        }

        response = self.data_product_exchange_api_service_service.create_data_product_version(
            container=container_reference_model,
            name='My New Data Product',
            description='testString',
            type=['data'],
        )

        assert response.get_status_code() == 201
        data_product_version = response.get_result()
        assert data_product_version is not None

        global get_data_product_version_by_user_id_link
        get_data_product_version_by_user_id_link = data_product_version['id']
        global update_data_product_version_by_user_id_link
        update_data_product_version_by_user_id_link = data_product_version['id']
        global delete_data_product_version_by_user_id_link
        delete_data_product_version_by_user_id_link = data_product_version['id']
        global get_data_product_by_user_id_link
        get_data_product_by_user_id_link = data_product_version['data_product']['id']
        global deliver_data_product_version_by_user_id_link
        deliver_data_product_version_by_user_id_link = data_product_version['id']

    @needscredentials
    def test_get_initialize_status(self):
        response = self.data_product_exchange_api_service_service.get_initialize_status(
            container_id=get_status_by_catalog_id_link,
        )

        assert response.get_status_code() == 200
        initialize_resource = response.get_result()
        assert initialize_resource is not None

    @needscredentials
    def test_get_data_product(self):
        response = self.data_product_exchange_api_service_service.get_data_product(
            id=get_data_product_by_user_id_link,
        )

        assert response.get_status_code() == 200
        data_product = response.get_result()
        assert data_product is not None

    @needscredentials
    def test_list_data_products(self):
        response = self.data_product_exchange_api_service_service.list_data_products(
            limit=200,
        )

        assert response.get_status_code() == 200
        data_product_collection = response.get_result()
        assert data_product_collection is not None

    @needscredentials
    def test_list_data_products_with_pager(self):
        all_results = []

        # Test get_next().
        pager = DataProductsPager(
            client=self.data_product_exchange_api_service_service,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = DataProductsPager(
            client=self.data_product_exchange_api_service_service,
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_data_products() returned a total of {len(all_results)} items(s) using DataProductsPager.')

    @needscredentials
    def test_list_data_product_versions(self):
        response = self.data_product_exchange_api_service_service.list_data_product_versions(
            asset_container_id=get_list_of_data_product_by_catalog_id_link,
            limit=200,
        )

        assert response.get_status_code() == 200
        data_product_version_collection = response.get_result()
        assert data_product_version_collection is not None

    @needscredentials
    def test_list_data_product_versions_with_pager(self):
        all_results = []

        # Test get_next().
        pager = DataProductVersionsPager(
            client=self.data_product_exchange_api_service_service,
            asset_container_id=get_list_of_data_product_by_catalog_id_link,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = DataProductVersionsPager(
            client=self.data_product_exchange_api_service_service,
            asset_container_id=get_list_of_data_product_by_catalog_id_link,
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(
            f'\nlist_data_product_versions() returned a total of {len(all_results)} items(s) using DataProductVersionsPager.'
        )

    @needscredentials
    def test_get_data_product_version(self):
        response = self.data_product_exchange_api_service_service.get_data_product_version(
            id=get_data_product_version_by_user_id_link,
        )

        assert response.get_status_code() == 200
        data_product_version = response.get_result()
        assert data_product_version is not None

    @needscredentials
    def test_update_data_product_version(self):
        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {
            'op': 'replace',
            'path': '/description',
            'value': 'This is the updated description from python SDK',
        }

        response = self.data_product_exchange_api_service_service.update_data_product_version(
            id=update_data_product_version_by_user_id_link,
            json_patch_instructions=[json_patch_operation_model],
        )

        assert response.get_status_code() == 200
        data_product_version = response.get_result()
        assert data_product_version is not None

    # @needscredentials
    # def test_deliver_data_product_version(self):
    #     # Construct a dict representation of a ItemReference model
    #     item_reference_model = {
    #         'id': 'd29c42eb-7100-4b7a-8257-c196dbcca1cd',
    #     }
    #     # Construct a dict representation of a OrderReference model
    #     order_reference_model = {
    #         'id': '4705e047-1808-459a-805f-d5d13c947637',
    #         'items': [item_reference_model],
    #     }

    #     response = self.data_product_exchange_api_service_service.deliver_data_product_version(
    #         id=deliver_data_product_version_by_user_id_link,
    #         order=order_reference_model,
    #     )

    #     assert response.get_status_code() == 202
    #     delivery_resource = response.get_result()
    #     assert delivery_resource is not None

    @needscredentials
    def test_delete_data_product_version(self):
        response = self.data_product_exchange_api_service_service.delete_data_product_version(
            id=delete_data_product_version_by_user_id_link,
        )

        assert response.get_status_code() == 204
