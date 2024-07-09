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
Examples for DataProductHubApiServiceV1
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from dph_services.data_product_hub_api_service_v1 import *

#
# This file provides an example of how to use the Data Product Hub API Service service.
#
# The following configuration properties are assumed to be defined:
# DATA_PRODUCT_HUB_API_SERVICE_URL=<service base url>
# DATA_PRODUCT_HUB_API_SERVICE_AUTH_TYPE=iam
# DATA_PRODUCT_HUB_API_SERVICE_APIKEY=<IAM apikey>
# DATA_PRODUCT_HUB_API_SERVICE_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'data_product_hub_api_service_v1.env'

data_product_hub_api_service = None

config = None

# Variables to hold link values
complete_a_draft_by_contract_terms_id_link = None
complete_a_draft_by_draft_id_link = None
complete_contract_terms_document_by_document_id_link = None
complete_draft_contract_terms_by_data_product_id_link = None
create_a_contract_terms_doc_by_contract_terms_id_link = None
create_a_contract_terms_doc_by_draft_id_link = None
create_data_product_by_catalog_id_link = None
create_draft_by_container_id_link = None
create_new_draft_by_data_product_id_link = None
delete_a_contract_document_by_draft_id_link = None
delete_a_draft_by_contract_terms_id_link = None
delete_a_draft_by_draft_id_link = None
delete_contract_document_by_data_product_id_link = None
delete_contract_terms_document_by_document_id_link = None
delete_draft_of_data_product_by_data_product_id_link = None
get_a_draft_by_contract_terms_id_link = None
get_a_draft_contract_document_by_draft_id_link = None
get_a_draft_of_data_product_by_data_product_id_link = None
get_a_release_by_release_id_link = None
get_a_release_contract_terms_by_contract_terms_id_link = None
get_a_release_contract_terms_by_release_id_link = None
get_a_release_of_data_product_by_data_product_id_link = None
get_contract_document_by_data_product_id_link = None
get_contract_terms_document_by_id_document_id_link = None
get_data_product_by_data_product_id_link = None
get_draft_by_draft_id_link = None
get_list_of_data_product_drafts_by_data_product_id_link = None
get_list_of_releases_of_data_product_by_data_product_id_link = None
get_release_contract_document_by_data_product_id_link = None
get_release_contract_document_by_document_id_link = None
get_status_by_catalog_id_link = None
publish_a_draft_by_draft_id_link = None
publish_a_draft_of_data_product_by_data_product_id_link = None
retire_a_release_contract_terms_by_release_id_link = None
retire_a_releases_of_data_product_by_data_product_id_link = None
update_a_draft_by_contract_terms_id_link = None
update_a_draft_by_draft_id_link = None
update_a_release_by_release_id_link = None
update_contract_document_by_data_product_id_link = None
update_contract_document_by_draft_id_link = None
update_contract_terms_document_by_document_id_link = None
update_draft_of_data_product_by_data_product_id_link = None
update_release_of_data_product_by_data_product_id_link = None
upload_contract_terms_doc_by_data_product_id_link = None


##############################################################################
# Start of Examples for Service: DataProductHubApiServiceV1
##############################################################################
# region
class TestDataProductHubApiServiceV1Examples:
    """
    Example Test Class for DataProductHubApiServiceV1
    """

    @classmethod
    def setup_class(cls):
        global data_product_hub_api_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            data_product_hub_api_service = DataProductHubApiServiceV1.new_instance()

            # end-common
            assert data_product_hub_api_service is not None

            # Load the configuration
            global config
            config = read_external_sources(DataProductHubApiServiceV1.DEFAULT_SERVICE_NAME)

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
            global create_draft_by_container_id_link
            global create_data_product_by_catalog_id_link
            global get_status_by_catalog_id_link

            print('\ninitialize() result:')

            # begin-initialize

            response = data_product_hub_api_service.initialize(
                include=['delivery_methods', 'domains_multi_industry', 'data_product_samples', 'workflows', 'project'],
            )
            initialize_resource = response.get_result()

            print(json.dumps(initialize_resource, indent=2))

            # end-initialize

            create_draft_by_container_id_link = initialize_resource['container']['id']
            create_data_product_by_catalog_id_link = initialize_resource['container']['id']
            get_status_by_catalog_id_link = initialize_resource['container']['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_data_product_example(self):
        """
        create_data_product request example
        """
        try:
            global create_new_draft_by_data_product_id_link
            global get_contract_document_by_data_product_id_link
            global retire_a_releases_of_data_product_by_data_product_id_link
            global get_data_product_by_data_product_id_link
            global update_draft_of_data_product_by_data_product_id_link
            global update_contract_document_by_data_product_id_link
            global delete_draft_of_data_product_by_data_product_id_link
            global get_a_release_of_data_product_by_data_product_id_link
            global complete_draft_contract_terms_by_data_product_id_link
            global delete_contract_document_by_data_product_id_link
            global get_list_of_data_product_drafts_by_data_product_id_link
            global get_a_draft_of_data_product_by_data_product_id_link
            global get_release_contract_document_by_data_product_id_link
            global publish_a_draft_of_data_product_by_data_product_id_link
            global get_list_of_releases_of_data_product_by_data_product_id_link
            global update_release_of_data_product_by_data_product_id_link
            global upload_contract_terms_doc_by_data_product_id_link

            print('\ncreate_data_product() result:')

            # begin-create_data_product

            container_identity_model = {
                'id': 'd29c42eb-7100-4b7a-8257-c196dbcca1cd',
            }

            asset_prototype_model = {
                'container': container_identity_model,
            }

            data_product_version_prototype_model = {
                'name': 'My New Data Product',
                'asset': asset_prototype_model,
            }

            response = data_product_hub_api_service.create_data_product(
                drafts=[data_product_version_prototype_model],
            )
            data_product = response.get_result()

            print(json.dumps(data_product, indent=2))

            # end-create_data_product

            create_new_draft_by_data_product_id_link = data_product['id']
            get_contract_document_by_data_product_id_link = data_product['id']
            retire_a_releases_of_data_product_by_data_product_id_link = data_product['id']
            get_data_product_by_data_product_id_link = data_product['id']
            update_draft_of_data_product_by_data_product_id_link = data_product['id']
            update_contract_document_by_data_product_id_link = data_product['id']
            delete_draft_of_data_product_by_data_product_id_link = data_product['id']
            get_a_release_of_data_product_by_data_product_id_link = data_product['id']
            complete_draft_contract_terms_by_data_product_id_link = data_product['id']
            delete_contract_document_by_data_product_id_link = data_product['id']
            get_list_of_data_product_drafts_by_data_product_id_link = data_product['id']
            get_a_draft_of_data_product_by_data_product_id_link = data_product['id']
            get_release_contract_document_by_data_product_id_link = data_product['id']
            publish_a_draft_of_data_product_by_data_product_id_link = data_product['id']
            get_list_of_releases_of_data_product_by_data_product_id_link = data_product['id']
            update_release_of_data_product_by_data_product_id_link = data_product['id']
            upload_contract_terms_doc_by_data_product_id_link = data_product['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_data_product_draft_example(self):
        """
        create_data_product_draft request example
        """
        try:
            global get_a_draft_contract_document_by_draft_id_link
            global update_a_draft_by_contract_terms_id_link
            global create_a_contract_terms_doc_by_contract_terms_id_link
            global update_contract_document_by_draft_id_link
            global get_a_release_contract_terms_by_contract_terms_id_link
            global complete_a_draft_by_contract_terms_id_link
            global get_draft_by_draft_id_link
            global publish_a_draft_by_draft_id_link
            global update_a_draft_by_draft_id_link
            global create_a_contract_terms_doc_by_draft_id_link
            global delete_a_contract_document_by_draft_id_link
            global delete_a_draft_by_contract_terms_id_link
            global delete_a_draft_by_draft_id_link
            global complete_a_draft_by_draft_id_link
            global get_a_draft_by_contract_terms_id_link

            print('\ncreate_data_product_draft() result:')

            # begin-create_data_product_draft

            container_identity_model = {
                'id': 'd29c42eb-7100-4b7a-8257-c196dbcca1cd',
            }

            asset_prototype_model = {
                'container': container_identity_model,
            }

            data_product_identity_model = {
                'id': 'b38df608-d34b-4d58-8136-ed25e6c6684e',
            }

            response = data_product_hub_api_service.create_data_product_draft(
                data_product_id=create_new_draft_by_data_product_id_link,
                asset=asset_prototype_model,
                version='1.2.0',
                data_product=data_product_identity_model,
            )
            data_product_version = response.get_result()

            print(json.dumps(data_product_version, indent=2))

            # end-create_data_product_draft

            get_a_draft_contract_document_by_draft_id_link = data_product_version['id']
            update_a_draft_by_contract_terms_id_link = data_product_version['contract_terms'][0]['id']
            create_a_contract_terms_doc_by_contract_terms_id_link = data_product_version['contract_terms'][0]['id']
            update_contract_document_by_draft_id_link = data_product_version['id']
            get_a_release_contract_terms_by_contract_terms_id_link = data_product_version['contract_terms'][0]['id']
            complete_a_draft_by_contract_terms_id_link = data_product_version['contract_terms'][0]['id']
            get_draft_by_draft_id_link = data_product_version['id']
            publish_a_draft_by_draft_id_link = data_product_version['id']
            update_a_draft_by_draft_id_link = data_product_version['id']
            create_a_contract_terms_doc_by_draft_id_link = data_product_version['id']
            delete_a_contract_document_by_draft_id_link = data_product_version['id']
            delete_a_draft_by_contract_terms_id_link = data_product_version['contract_terms'][0]['id']
            delete_a_draft_by_draft_id_link = data_product_version['id']
            complete_a_draft_by_draft_id_link = data_product_version['id']
            get_a_draft_by_contract_terms_id_link = data_product_version['contract_terms'][0]['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_draft_contract_terms_document_example(self):
        """
        create_draft_contract_terms_document request example
        """
        try:
            global get_release_contract_document_by_document_id_link
            global delete_contract_terms_document_by_document_id_link
            global get_contract_terms_document_by_id_document_id_link
            global update_contract_terms_document_by_document_id_link
            global complete_contract_terms_document_by_document_id_link

            print('\ncreate_draft_contract_terms_document() result:')

            # begin-create_draft_contract_terms_document

            response = data_product_hub_api_service.create_draft_contract_terms_document(
                data_product_id=upload_contract_terms_doc_by_data_product_id_link,
                draft_id=create_a_contract_terms_doc_by_draft_id_link,
                contract_terms_id=create_a_contract_terms_doc_by_contract_terms_id_link,
                type='terms_and_conditions',
                name='Terms and conditions document',
                id='b38df608-d34b-4d58-8136-ed25e6c6684e',
            )
            contract_terms_document = response.get_result()

            print(json.dumps(contract_terms_document, indent=2))

            # end-create_draft_contract_terms_document

            get_release_contract_document_by_document_id_link = contract_terms_document['id']
            delete_contract_terms_document_by_document_id_link = contract_terms_document['id']
            get_contract_terms_document_by_id_document_id_link = contract_terms_document['id']
            update_contract_terms_document_by_document_id_link = contract_terms_document['id']
            complete_contract_terms_document_by_document_id_link = contract_terms_document['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_publish_data_product_draft_example(self):
        """
        publish_data_product_draft request example
        """
        try:
            global update_a_release_by_release_id_link
            global get_a_release_contract_terms_by_release_id_link
            global retire_a_release_contract_terms_by_release_id_link
            global get_a_release_by_release_id_link

            print('\npublish_data_product_draft() result:')

            # begin-publish_data_product_draft

            response = data_product_hub_api_service.publish_data_product_draft(
                data_product_id=publish_a_draft_of_data_product_by_data_product_id_link,
                draft_id=publish_a_draft_by_draft_id_link,
            )
            data_product_version = response.get_result()

            print(json.dumps(data_product_version, indent=2))

            # end-publish_data_product_draft

            update_a_release_by_release_id_link = data_product_version['id']
            get_a_release_contract_terms_by_release_id_link = data_product_version['id']
            retire_a_release_contract_terms_by_release_id_link = data_product_version['id']
            get_a_release_by_release_id_link = data_product_version['id']
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

            response = data_product_hub_api_service.get_initialize_status()
            initialize_resource = response.get_result()

            print(json.dumps(initialize_resource, indent=2))

            # end-get_initialize_status

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_service_id_credentials_example(self):
        """
        get_service_id_credentials request example
        """
        try:
            print('\nget_service_id_credentials() result:')

            # begin-get_service_id_credentials

            response = data_product_hub_api_service.get_service_id_credentials()
            service_id_credentials = response.get_result()

            print(json.dumps(service_id_credentials, indent=2))

            # end-get_service_id_credentials

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_manage_api_keys_example(self):
        """
        manage_api_keys request example
        """
        try:
            # begin-manage_api_keys

            response = data_product_hub_api_service.manage_api_keys()

            # end-manage_api_keys
            print('\nmanage_api_keys() response status code: ', response.get_status_code())

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
                client=data_product_hub_api_service,
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
    def test_get_data_product_example(self):
        """
        get_data_product request example
        """
        try:
            print('\nget_data_product() result:')

            # begin-get_data_product

            response = data_product_hub_api_service.get_data_product(
                data_product_id=get_data_product_by_data_product_id_link,
            )
            data_product = response.get_result()

            print(json.dumps(data_product, indent=2))

            # end-get_data_product

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_complete_draft_contract_terms_document_example(self):
        """
        complete_draft_contract_terms_document request example
        """
        try:
            print('\ncomplete_draft_contract_terms_document() result:')

            # begin-complete_draft_contract_terms_document

            response = data_product_hub_api_service.complete_draft_contract_terms_document(
                data_product_id=complete_draft_contract_terms_by_data_product_id_link,
                draft_id=complete_a_draft_by_draft_id_link,
                contract_terms_id=complete_a_draft_by_contract_terms_id_link,
                document_id=complete_contract_terms_document_by_document_id_link,
            )
            contract_terms_document = response.get_result()

            print(json.dumps(contract_terms_document, indent=2))

            # end-complete_draft_contract_terms_document

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_data_product_drafts_example(self):
        """
        list_data_product_drafts request example
        """
        try:
            print('\nlist_data_product_drafts() result:')

            # begin-list_data_product_drafts

            all_results = []
            pager = DataProductDraftsPager(
                client=data_product_hub_api_service,
                data_product_id=get_list_of_data_product_drafts_by_data_product_id_link,
                asset_container_id='testString',
                version='testString',
                limit=10,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_data_product_drafts
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_data_product_draft_example(self):
        """
        get_data_product_draft request example
        """
        try:
            print('\nget_data_product_draft() result:')

            # begin-get_data_product_draft

            response = data_product_hub_api_service.get_data_product_draft(
                data_product_id=get_a_draft_of_data_product_by_data_product_id_link,
                draft_id=get_draft_by_draft_id_link,
            )
            data_product_version = response.get_result()

            print(json.dumps(data_product_version, indent=2))

            # end-get_data_product_draft

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_data_product_draft_example(self):
        """
        update_data_product_draft request example
        """
        try:
            print('\nupdate_data_product_draft() result:')

            # begin-update_data_product_draft

            json_patch_operation_model = {
                'op': 'add',
                'path': 'testString',
            }

            response = data_product_hub_api_service.update_data_product_draft(
                data_product_id=update_draft_of_data_product_by_data_product_id_link,
                draft_id=update_a_draft_by_draft_id_link,
                json_patch_instructions=[json_patch_operation_model],
            )
            data_product_version = response.get_result()

            print(json.dumps(data_product_version, indent=2))

            # end-update_data_product_draft

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_draft_contract_terms_document_example(self):
        """
        get_draft_contract_terms_document request example
        """
        try:
            print('\nget_draft_contract_terms_document() result:')

            # begin-get_draft_contract_terms_document

            response = data_product_hub_api_service.get_draft_contract_terms_document(
                data_product_id=get_contract_document_by_data_product_id_link,
                draft_id=get_a_draft_contract_document_by_draft_id_link,
                contract_terms_id=get_a_draft_by_contract_terms_id_link,
                document_id=get_contract_terms_document_by_id_document_id_link,
            )
            contract_terms_document = response.get_result()

            print(json.dumps(contract_terms_document, indent=2))

            # end-get_draft_contract_terms_document

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_draft_contract_terms_document_example(self):
        """
        update_draft_contract_terms_document request example
        """
        try:
            print('\nupdate_draft_contract_terms_document() result:')

            # begin-update_draft_contract_terms_document

            json_patch_operation_model = {
                'op': 'add',
                'path': 'testString',
            }

            response = data_product_hub_api_service.update_draft_contract_terms_document(
                data_product_id=update_contract_document_by_data_product_id_link,
                draft_id=update_contract_document_by_draft_id_link,
                contract_terms_id=update_a_draft_by_contract_terms_id_link,
                document_id=update_contract_terms_document_by_document_id_link,
                json_patch_instructions=[json_patch_operation_model],
            )
            contract_terms_document = response.get_result()

            print(json.dumps(contract_terms_document, indent=2))

            # end-update_draft_contract_terms_document

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_data_product_release_example(self):
        """
        get_data_product_release request example
        """
        try:
            print('\nget_data_product_release() result:')

            # begin-get_data_product_release

            response = data_product_hub_api_service.get_data_product_release(
                data_product_id=get_a_release_of_data_product_by_data_product_id_link,
                release_id=get_a_release_by_release_id_link,
            )
            data_product_version = response.get_result()

            print(json.dumps(data_product_version, indent=2))

            # end-get_data_product_release

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_data_product_release_example(self):
        """
        update_data_product_release request example
        """
        try:
            print('\nupdate_data_product_release() result:')

            # begin-update_data_product_release

            json_patch_operation_model = {
                'op': 'add',
                'path': 'testString',
            }

            response = data_product_hub_api_service.update_data_product_release(
                data_product_id=update_release_of_data_product_by_data_product_id_link,
                release_id='testString',
                json_patch_instructions=[json_patch_operation_model],
            )
            data_product_version = response.get_result()

            print(json.dumps(data_product_version, indent=2))

            # end-update_data_product_release

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_release_contract_terms_document_example(self):
        """
        get_release_contract_terms_document request example
        """
        try:
            print('\nget_release_contract_terms_document() result:')

            # begin-get_release_contract_terms_document

            response = data_product_hub_api_service.get_release_contract_terms_document(
                data_product_id=get_release_contract_document_by_data_product_id_link,
                release_id=get_a_release_contract_terms_by_release_id_link,
                contract_terms_id=get_a_release_contract_terms_by_contract_terms_id_link,
                document_id=get_release_contract_document_by_document_id_link,
            )
            contract_terms_document = response.get_result()

            print(json.dumps(contract_terms_document, indent=2))

            # end-get_release_contract_terms_document

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_data_product_releases_example(self):
        """
        list_data_product_releases request example
        """
        try:
            print('\nlist_data_product_releases() result:')

            # begin-list_data_product_releases

            all_results = []
            pager = DataProductReleasesPager(
                client=data_product_hub_api_service,
                data_product_id=get_list_of_releases_of_data_product_by_data_product_id_link,
                asset_container_id='testString',
                state=['available'],
                version='testString',
                limit=10,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_data_product_releases
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_retire_data_product_release_example(self):
        """
        retire_data_product_release request example
        """
        try:
            print('\nretire_data_product_release() result:')

            # begin-retire_data_product_release

            response = data_product_hub_api_service.retire_data_product_release(
                data_product_id=retire_a_releases_of_data_product_by_data_product_id_link,
                release_id=retire_a_release_contract_terms_by_release_id_link,
            )
            data_product_version = response.get_result()

            print(json.dumps(data_product_version, indent=2))

            # end-retire_data_product_release

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_draft_contract_terms_document_example(self):
        """
        delete_draft_contract_terms_document request example
        """
        try:
            # begin-delete_draft_contract_terms_document

            response = data_product_hub_api_service.delete_draft_contract_terms_document(
                data_product_id=delete_contract_document_by_data_product_id_link,
                draft_id=delete_a_contract_document_by_draft_id_link,
                contract_terms_id=delete_a_draft_by_contract_terms_id_link,
                document_id=delete_contract_terms_document_by_document_id_link,
            )

            # end-delete_draft_contract_terms_document
            print('\ndelete_draft_contract_terms_document() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_data_product_draft_example(self):
        """
        delete_data_product_draft request example
        """
        try:
            # begin-delete_data_product_draft

            response = data_product_hub_api_service.delete_data_product_draft(
                data_product_id=delete_draft_of_data_product_by_data_product_id_link,
                draft_id=delete_a_draft_by_draft_id_link,
            )

            # end-delete_data_product_draft
            print('\ndelete_data_product_draft() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: DataProductHubApiServiceV1
##############################################################################
