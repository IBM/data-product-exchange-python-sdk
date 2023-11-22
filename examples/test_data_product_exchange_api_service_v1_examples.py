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
Examples for DataProductExchangeApiServiceV1
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from ibm_dpx_services.data_product_exchange_api_service_v1 import *

#
# This file provides an example of how to use the Data Product Exchange API Service service.
#
# The following configuration properties are assumed to be defined:
# DATA_PRODUCT_EXCHANGE_API_SERVICE_URL=<service base url>
# DATA_PRODUCT_EXCHANGE_API_SERVICE_AUTH_TYPE=iam
# DATA_PRODUCT_EXCHANGE_API_SERVICE_APIKEY=<IAM apikey>
# DATA_PRODUCT_EXCHANGE_API_SERVICE_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'data_product_exchange_api_service_v1.env'

data_product_exchange_api_service_service = None

config = None

# Variables to hold link values
create_data_product_version_by_catalog_id_link = None
delete_data_product_version_by_user_id_link = None
deliver_data_product_version_by_user_id_link = None
get_data_product_by_user_id_link = None
get_data_product_version_by_user_id_link = None
get_list_of_data_product_by_catalog_id_link = None
get_status_by_catalog_id_link = None
update_data_product_version_by_user_id_link = None


##############################################################################
# Start of Examples for Service: DataProductExchangeApiServiceV1
##############################################################################
# region
class TestDataProductExchangeApiServiceV1Examples:
    """
    Example Test Class for DataProductExchangeApiServiceV1
    """

    @classmethod
    def setup_class(cls):
        global data_product_exchange_api_service_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            data_product_exchange_api_service_service = DataProductExchangeApiServiceV1.new_instance()

            # end-common
            assert data_product_exchange_api_service_service is not None

            # Load the configuration
            global config
            config = read_external_sources(DataProductExchangeApiServiceV1.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_initialize_example(self):
        """
        initialize request example
        """
        try:
            print('\ninitialize() result:')
            # begin-initialize

            response = data_product_exchange_api_service_service.initialize(
                include=['delivery_methods', 'data_product_samples', 'domains_multi_industry'],
            )
            initialize_resource = response.get_result()

            print(json.dumps(initialize_resource, indent=2))

            # end-initialize

            global create_data_product_version_by_catalog_id_link
            create_data_product_version_by_catalog_id_link = initialize_resource['container']['id']
            global get_status_by_catalog_id_link
            get_status_by_catalog_id_link = initialize_resource['container']['id']
            global get_list_of_data_product_by_catalog_id_link
            get_list_of_data_product_by_catalog_id_link = initialize_resource['container']['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_data_product_version_example(self):
        """
        create_data_product_version request example
        """
        try:
            print('\ncreate_data_product_version() result:')
            # begin-create_data_product_version

            container_reference_model = {
                # 'id': 'd29c42eb-7100-4b7a-8257-c196dbcca1cd',
                'id': create_data_product_version_by_catalog_id_link,
                'type': 'catalog',
            }

            response = data_product_exchange_api_service_service.create_data_product_version(
                container=container_reference_model,
                name='My New Data Product',
            )
            data_product_version = response.get_result()

            print(json.dumps(data_product_version, indent=2))

            # end-create_data_product_version

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
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_initialize_status_example(self):
        """
        get_initialize_status request example
        """
        try:
            print('\nget_initialize_status() result:')
            # begin-get_initialize_status

            response = data_product_exchange_api_service_service.get_initialize_status()
            initialize_resource = response.get_result()

            print(json.dumps(initialize_resource, indent=2))

            # end-get_initialize_status

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_data_product_example(self):
        """
        get_data_product request example
        """
        try:
            print('\nget_data_product() result:')
            # begin-get_data_product

            response = data_product_exchange_api_service_service.get_data_product(
                id=get_data_product_by_user_id_link,
            )
            data_product = response.get_result()

            print(json.dumps(data_product, indent=2))

            # end-get_data_product

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_data_products_example(self):
        """
        list_data_products request example
        """
        try:
            print('\nlist_data_products() result:')
            # begin-list_data_products

            all_results = []
            pager = DataProductsPager(
                client=data_product_exchange_api_service_service,
                limit=10,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_data_products
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_data_product_versions_example(self):
        """
        list_data_product_versions request example
        """
        try:
            print('\nlist_data_product_versions() result:')
            # begin-list_data_product_versions

            all_results = []
            pager = DataProductVersionsPager(
                client=data_product_exchange_api_service_service,
                asset_container_id=get_list_of_data_product_by_catalog_id_link,
                # data_product='testString',
                # state='draft',
                # version='testString',
                limit=10,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_data_product_versions
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_data_product_version_example(self):
        """
        get_data_product_version request example
        """
        try:
            print('\nget_data_product_version() result:')
            # begin-get_data_product_version

            response = data_product_exchange_api_service_service.get_data_product_version(
                id=get_data_product_version_by_user_id_link,
            )
            data_product_version = response.get_result()

            print(json.dumps(data_product_version, indent=2))

            # end-get_data_product_version

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_data_product_version_example(self):
        """
        update_data_product_version request example
        """
        try:
            print('\nupdate_data_product_version() result:')
            # begin-update_data_product_version

            json_patch_operation_model = {
                'op': 'replace',
                'path': '/description',
            }

            response = data_product_exchange_api_service_service.update_data_product_version(
                id=update_data_product_version_by_user_id_link,
                json_patch_instructions=[json_patch_operation_model],
            )
            data_product_version = response.get_result()

            print(json.dumps(data_product_version, indent=2))

            # end-update_data_product_version

        except ApiException as e:
            pytest.fail(str(e))

    # @needscredentials
    # def test_deliver_data_product_version_example(self):
    #     """
    #     deliver_data_product_version request example
    #     """
    #     try:
    #         print('\ndeliver_data_product_version() result:')
    #         # begin-deliver_data_product_version

    #         item_reference_model = {
    #             'id': 'd29c42eb-7100-4b7a-8257-c196dbcca1cd',
    #         }

    #         order_reference_model = {
    #             'id': '4705e047-1808-459a-805f-d5d13c947637',
    #             'items': [item_reference_model],
    #         }

    #         response = data_product_exchange_api_service_service.deliver_data_product_version(
    #             id=deliver_data_product_version_by_user_id_link,
    #             order=order_reference_model,
    #         )
    #         delivery_resource = response.get_result()

    #         print(json.dumps(delivery_resource, indent=2))

    #         # end-deliver_data_product_version

    #     except ApiException as e:
    #         pytest.fail(str(e))

    @needscredentials
    def test_delete_data_product_version_example(self):
        """
        delete_data_product_version request example
        """
        try:
            # begin-delete_data_product_version

            response = data_product_exchange_api_service_service.delete_data_product_version(
                id=delete_data_product_version_by_user_id_link,
            )

            # end-delete_data_product_version
            print('\ndelete_data_product_version() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: DataProductExchangeApiServiceV1
##############################################################################
