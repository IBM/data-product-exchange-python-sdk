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
Examples for DpxV1
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from ibm_dpx_services.dpx_v1 import *

#
# This file provides an example of how to use the DPX service.
#
# The following configuration properties are assumed to be defined:
# DPX_URL=<service base url>
# DPX_AUTH_TYPE=iam
# DPX_APIKEY=<IAM apikey>
# DPX_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'dpx_v1.env'

dpx_service = None

config = None

# Variables to hold link values
container_id_link = None
contract_terms_id_link = None
data_product_id_link = None
document_id_link = None
draft_id_link = None
optional_data_product_id_link = None
release_id_link = None


##############################################################################
# Start of Examples for Service: DpxV1
##############################################################################
# region
class TestDpxV1Examples:
    """
    Example Test Class for DpxV1
    """

    @classmethod
    def setup_class(cls):
        global dpx_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            dpx_service = DpxV1.new_instance()

            # end-common
            assert dpx_service is not None

            # Load the configuration
            global config
            config = read_external_sources(DpxV1.DEFAULT_SERVICE_NAME)

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
            global container_id_link

            print('\ninitialize() result:')

            # begin-initialize

            response = dpx_service.initialize(
                include=['delivery_methods', 'data_product_samples', 'domains_multi_industry'],
            )
            initialize_resource = response.get_result()

            print(json.dumps(initialize_resource, indent=2))

            # end-initialize

            container_id_link = initialize_resource['container']['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_data_product_example(self):
        """
        create_data_product request example
        """
        try:
            global optional_data_product_id_link
            global data_product_id_link

            print('\ncreate_data_product() result:')

            # begin-create_data_product

            container_reference_model = {
                'id': container_id_link,
            }

            asset_reference_model = {
                'container': container_reference_model,
            }

            data_product_version_prototype_model = {
                'name': 'My New Data Product',
                'asset': asset_reference_model,
            }

            response = dpx_service.create_data_product(
                drafts=[data_product_version_prototype_model],
            )
            data_product = response.get_result()

            print(json.dumps(data_product, indent=2))

            # end-create_data_product

            optional_data_product_id_link = data_product['id']
            data_product_id_link = data_product['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_data_product_draft_example(self):
        """
        create_data_product_draft request example
        """
        try:
            global draft_id_link
            global contract_terms_id_link

            print('\ncreate_data_product_draft() result:')

            # begin-create_data_product_draft

            container_reference_model = {
                'id': container_id_link,
            }

            asset_reference_model = {
                'container': container_reference_model,
            }

            data_product_identity_model = {
                'id': data_product_id_link,
            }

            domain_model = {
                'id': '918c0bfd-6943-4468-b74f-bc111018e0d1',
                'name': 'Customer Service',
                'container': container_reference_model,
            }

            response = dpx_service.create_data_product_draft(
                data_product_id=data_product_id_link,
                asset=asset_reference_model,
                version='1.2.0',
                data_product=data_product_identity_model,
                domain=domain_model,
            )
            data_product_version = response.get_result()

            print(json.dumps(data_product_version, indent=2))

            # end-create_data_product_draft

            draft_id_link = data_product_version['id']
            contract_terms_id_link = data_product_version['contract_terms'][0]['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_data_product_draft_example(self):
        """
        delete_data_product_draft request example
        """
        try:
            # begin-delete_data_product_draft

            response = dpx_service.delete_data_product_draft(
                data_product_id=optional_data_product_id_link,
                draft_id=draft_id_link,
            )

            # end-delete_data_product_draft
            print('\ndelete_data_product_draft() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_data_product_draft_example_again(self):
        """
        create_data_product_draft request example
        """
        try:
            global draft_id_link
            global contract_terms_id_link

            print('\ncreate_data_product_draft() result:')

            # begin-create_data_product_draft

            container_reference_model = {
                'id': container_id_link,
            }

            asset_reference_model = {
                'container': container_reference_model,
            }

            data_product_identity_model = {
                'id': data_product_id_link,
            }

            domain_model = {
                'id': '918c0bfd-6943-4468-b74f-bc111018e0d1',
                'name': 'Customer Service',
                'container': container_reference_model,
            }

            response = dpx_service.create_data_product_draft(
                data_product_id=data_product_id_link,
                asset=asset_reference_model,
                version='1.2.0',
                data_product=data_product_identity_model,
                domain=domain_model,
            )
            data_product_version = response.get_result()

            print(json.dumps(data_product_version, indent=2))

            # end-create_data_product_draft

            draft_id_link = data_product_version['id']
            contract_terms_id_link = data_product_version['contract_terms'][0]['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_draft_contract_terms_document_example(self):
        """
        create_draft_contract_terms_document request example
        """
        try:
            global document_id_link

            print('\ncreate_draft_contract_terms_document() result:')

            # begin-create_draft_contract_terms_document

            response = dpx_service.create_draft_contract_terms_document(
                data_product_id=optional_data_product_id_link,
                draft_id=draft_id_link,
                contract_terms_id=contract_terms_id_link,
                type='terms_and_conditions',
                name='Terms and conditions document',
                id='b38df608-d34b-4d58-8136-ed25e6c6684e',
                url='https://www.google.com',
            )
            contract_terms_document = response.get_result()

            print(json.dumps(contract_terms_document, indent=2))

            # end-create_draft_contract_terms_document

            document_id_link = contract_terms_document['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_draft_contract_terms_document_example(self):
        """
        delete_draft_contract_terms_document request example
        """
        try:
            # begin-delete_draft_contract_terms_document

            response = dpx_service.delete_draft_contract_terms_document(
                data_product_id=optional_data_product_id_link,
                draft_id=draft_id_link,
                contract_terms_id=contract_terms_id_link,
                document_id=document_id_link,
            )

            # end-delete_draft_contract_terms_document
            print('\ndelete_draft_contract_terms_document() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_draft_contract_terms_document_example_again(self):
        """
        create_draft_contract_terms_document request example
        """
        try:
            global document_id_link

            print('\ncreate_draft_contract_terms_document() result:')

            # begin-create_draft_contract_terms_document

            response = dpx_service.create_draft_contract_terms_document(
                data_product_id=optional_data_product_id_link,
                draft_id=draft_id_link,
                contract_terms_id=contract_terms_id_link,
                type='terms_and_conditions',
                name='Terms and conditions document',
                id='b38df608-d34b-4d58-8136-ed25e6c6684e',
                url='https://www.google.com',
            )
            contract_terms_document = response.get_result()

            print(json.dumps(contract_terms_document, indent=2))

            # end-create_draft_contract_terms_document

            document_id_link = contract_terms_document['id']
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

            response = dpx_service.get_data_product_draft(
                data_product_id=optional_data_product_id_link,
                draft_id=draft_id_link,
            )
            data_product_version = response.get_result()

            print(json.dumps(data_product_version, indent=2))

            # end-get_data_product_draft

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

            response = dpx_service.get_initialize_status()
            initialize_resource = response.get_result()

            print(json.dumps(initialize_resource, indent=2))

            # end-get_initialize_status

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

            # Construct the asset object
            asset_string = '{"id":"669a570b-31f7-4c84-bfd1-851282ab5b86","container":{"id":"b6eb50b4-ace4-4dab-b2c4-318bb4c032a6","type":"catalog"}}'

            # Parse the JSON string to a dictionary
            asset_map = json.loads(asset_string)

            # Create a list to hold the asset object
            parts_out_list = [{"asset": asset_map}]

            json_patch_operation_model = {
                'op': 'add',
                'path': '/parts_out',
                'value': parts_out_list,
            }

            response = dpx_service.update_data_product_draft(
                data_product_id=optional_data_product_id_link,
                draft_id=draft_id_link,
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

            response = dpx_service.get_draft_contract_terms_document(
                data_product_id=optional_data_product_id_link,
                draft_id=draft_id_link,
                contract_terms_id=contract_terms_id_link,
                document_id=document_id_link,
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
                'op': 'replace',
                'path': '/url',
                'value': 'https://google.com',
            }

            response = dpx_service.update_draft_contract_terms_document(
                data_product_id=optional_data_product_id_link,
                draft_id=draft_id_link,
                contract_terms_id=contract_terms_id_link,
                document_id=document_id_link,
                json_patch_instructions=[json_patch_operation_model],
            )
            contract_terms_document = response.get_result()

            print(json.dumps(contract_terms_document, indent=2))

            # end-update_draft_contract_terms_document

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_publish_data_product_draft_example(self):
        """
        publish_data_product_draft request example
        """
        try:
            global release_id_link

            print('\npublish_data_product_draft() result:')

            # begin-publish_data_product_draft

            response = dpx_service.publish_data_product_draft(
                data_product_id=optional_data_product_id_link,
                draft_id=draft_id_link,
            )
            data_product_version = response.get_result()

            print(json.dumps(data_product_version, indent=2))

            # end-publish_data_product_draft

            release_id_link = data_product_version['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_manage_api_keys_example(self):
        """
        manage_api_keys request example
        """
        try:
            # begin-manage_api_keys

            response = dpx_service.manage_api_keys()

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
                client=dpx_service,
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

            response = dpx_service.get_data_product(
                data_product_id=data_product_id_link,
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

            response = dpx_service.complete_draft_contract_terms_document(
                data_product_id=optional_data_product_id_link,
                draft_id=draft_id_link,
                contract_terms_id=contract_terms_id_link,
                document_id=document_id_link,
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
                client=dpx_service,
                data_product_id=optional_data_product_id_link,
                # asset_container_id='testString',
                # version='testString',
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
    def test_get_data_product_release_example(self):
        """
        get_data_product_release request example
        """
        try:
            print('\nget_data_product_release() result:')

            # begin-get_data_product_release

            response = dpx_service.get_data_product_release(
                data_product_id=optional_data_product_id_link,
                release_id=release_id_link,
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
                'op': 'replace',
                'path': '/description',
                'value': '"New Description',
            }

            response = dpx_service.update_data_product_release(
                data_product_id=optional_data_product_id_link,
                release_id=release_id_link,
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

            response = dpx_service.get_release_contract_terms_document(
                data_product_id=optional_data_product_id_link,
                release_id=release_id_link,
                contract_terms_id=contract_terms_id_link,
                document_id=document_id_link,
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
                client=dpx_service,
                data_product_id=optional_data_product_id_link,
                # asset_container_id='testString',
                state=['available'],
                # version='testString',
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

            response = dpx_service.retire_data_product_release(
                data_product_id=optional_data_product_id_link,
                release_id=release_id_link,
            )
            data_product_version = response.get_result()

            print(json.dumps(data_product_version, indent=2))

            # end-retire_data_product_release

        except ApiException as e:
            pytest.fail(str(e))


# endregion
# #############################################################################
# End of Examples for Service: DpxV1
# #############################################################################
