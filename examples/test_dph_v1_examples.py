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
Examples for DphV1
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import os
import pytest
from dph_services.dph_v1 import *

#
# This file provides an example of how to use the DPH service.
#
# The following configuration properties are assumed to be defined:
# DPH_URL=<service base url>
# DPH_AUTH_TYPE=iam
# DPH_APIKEY=<IAM apikey>
# DPH_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'dph_v1.env'

dph_service = None

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
# Start of Examples for Service: DphV1
##############################################################################
# region
class TestDphV1Examples:
    """
    Example Test Class for DphV1
    """

    @classmethod
    def setup_class(cls):
        global dph_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            dph_service = DphV1.new_instance(
            )

            # end-common
            assert dph_service is not None

            # Load the configuration
            global config
            config = read_external_sources(DphV1.DEFAULT_SERVICE_NAME)

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

            response = dph_service.initialize(
                include=['delivery_methods', 'domains_multi_industry', 'data_product_samples', 'workflows', 'project', 'catalog_configurations'],
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

            data_product_draft_prototype_model = {
                'name': 'My New Data Product',
                'asset': asset_prototype_model,
            }

            response = dph_service.create_data_product(
                drafts=[data_product_draft_prototype_model],
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

            data_product_draft_version_release_model = {
                'id': '8bf83660-11fe-4427-a72a-8d8359af24e3',
            }

            data_product_identity_model = {
                'id': 'b38df608-d34b-4d58-8136-ed25e6c6684e',
                'release': data_product_draft_version_release_model,
            }

            response = dph_service.create_data_product_draft(
                data_product_id=create_new_draft_by_data_product_id_link,
                asset=asset_prototype_model,
                version='1.2.0',
                data_product=data_product_identity_model,
            )
            data_product_draft = response.get_result()

            print(json.dumps(data_product_draft, indent=2))

            # end-create_data_product_draft

            get_a_draft_contract_document_by_draft_id_link = data_product_draft['id']
            update_a_draft_by_contract_terms_id_link = data_product_draft['contract_terms'][0]['id']
            create_a_contract_terms_doc_by_contract_terms_id_link = data_product_draft['contract_terms'][0]['id']
            update_contract_document_by_draft_id_link = data_product_draft['id']
            get_a_release_contract_terms_by_contract_terms_id_link = data_product_draft['contract_terms'][0]['id']
            complete_a_draft_by_contract_terms_id_link = data_product_draft['contract_terms'][0]['id']
            get_draft_by_draft_id_link = data_product_draft['id']
            publish_a_draft_by_draft_id_link = data_product_draft['id']
            update_a_draft_by_draft_id_link = data_product_draft['id']
            create_a_contract_terms_doc_by_draft_id_link = data_product_draft['id']
            delete_a_contract_document_by_draft_id_link = data_product_draft['id']
            delete_a_draft_by_contract_terms_id_link = data_product_draft['contract_terms'][0]['id']
            delete_a_draft_by_draft_id_link = data_product_draft['id']
            complete_a_draft_by_draft_id_link = data_product_draft['id']
            get_a_draft_by_contract_terms_id_link = data_product_draft['contract_terms'][0]['id']
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

            response = dph_service.create_draft_contract_terms_document(
                data_product_id=upload_contract_terms_doc_by_data_product_id_link,
                draft_id=create_a_contract_terms_doc_by_draft_id_link,
                contract_terms_id=create_a_contract_terms_doc_by_contract_terms_id_link,
                type='terms_and_conditions',
                name='Terms and conditions document',
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

            response = dph_service.publish_data_product_draft(
                data_product_id=publish_a_draft_of_data_product_by_data_product_id_link,
                draft_id=publish_a_draft_by_draft_id_link,
            )
            data_product_release = response.get_result()

            print(json.dumps(data_product_release, indent=2))

            # end-publish_data_product_draft

            update_a_release_by_release_id_link = data_product_release['id']
            get_a_release_contract_terms_by_release_id_link = data_product_release['id']
            retire_a_release_contract_terms_by_release_id_link = data_product_release['id']
            get_a_release_by_release_id_link = data_product_release['id']
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

            response = dph_service.get_initialize_status()
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

            response = dph_service.get_service_id_credentials()
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

            response = dph_service.manage_api_keys()

            # end-manage_api_keys
            print('\nmanage_api_keys() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_data_asset_visualization_example(self):
        """
        create_data_asset_visualization request example
        """
        try:
            print('\ncreate_data_asset_visualization() result:')

            # begin-create_data_asset_visualization

            container_reference_model = {
                'id': '2be8f727-c5d2-4cb0-9216-f9888f428048',
                'type': 'catalog',
            }

            asset_reference_model = {
                'id': 'caeee3f3-756e-47d5-846d-da4600809e22',
                'container': container_reference_model,
            }

            data_asset_relationship_model = {
                'asset': asset_reference_model,
                'related_asset': asset_reference_model,
            }

            response = dph_service.create_data_asset_visualization(
                assets=[data_asset_relationship_model],
            )
            data_asset_visualization_res = response.get_result()

            print(json.dumps(data_asset_visualization_res, indent=2))

            # end-create_data_asset_visualization

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_reinitiate_data_asset_visualization_example(self):
        """
        reinitiate_data_asset_visualization request example
        """
        try:
            print('\nreinitiate_data_asset_visualization() result:')

            # begin-reinitiate_data_asset_visualization

            container_reference_model = {
                'id': '2be8f727-c5d2-4cb0-9216-f9888f428048',
                'type': 'catalog',
            }

            asset_reference_model = {
                'id': 'caeee3f3-756e-47d5-846d-da4600809e22',
                'container': container_reference_model,
            }

            data_asset_relationship_model = {
                'asset': asset_reference_model,
                'related_asset': asset_reference_model,
            }

            response = dph_service.reinitiate_data_asset_visualization(
                assets=[data_asset_relationship_model],
            )
            data_asset_visualization_res = response.get_result()

            print(json.dumps(data_asset_visualization_res, indent=2))

            # end-reinitiate_data_asset_visualization

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
                client=dph_service,
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

            response = dph_service.get_data_product(
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

            response = dph_service.complete_draft_contract_terms_document(
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
                client=dph_service,
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

            response = dph_service.get_data_product_draft(
                data_product_id=get_a_draft_of_data_product_by_data_product_id_link,
                draft_id=get_draft_by_draft_id_link,
            )
            data_product_draft = response.get_result()

            print(json.dumps(data_product_draft, indent=2))

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

            response = dph_service.update_data_product_draft(
                data_product_id=update_draft_of_data_product_by_data_product_id_link,
                draft_id=update_a_draft_by_draft_id_link,
                json_patch_instructions=[json_patch_operation_model],
            )
            data_product_draft = response.get_result()

            print(json.dumps(data_product_draft, indent=2))

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

            response = dph_service.get_draft_contract_terms_document(
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

            response = dph_service.update_draft_contract_terms_document(
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
    def test_get_data_product_draft_contract_terms_example(self):
        """
        get_data_product_draft_contract_terms request example
        """
        try:
            print('\nget_data_product_draft_contract_terms() result:')

            # begin-get_data_product_draft_contract_terms

            response = dph_service.get_data_product_draft_contract_terms(
                data_product_id='testString',
                draft_id='testString',
                contract_terms_id='testString',
            )
            result = response.get_result()

            with open('/tmp/result.out', 'wb') as fp:
                fp.write(result)

            # end-get_data_product_draft_contract_terms

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_data_product_draft_contract_terms_example(self):
        """
        replace_data_product_draft_contract_terms request example
        """
        try:
            print('\nreplace_data_product_draft_contract_terms() result:')

            # begin-replace_data_product_draft_contract_terms

            contract_terms_document_model = {
                'url': 'https://ibm.com/document',
                'type': 'terms_and_conditions',
                'name': 'Terms and Conditions',
                'id': 'b38df608-d34b-4d58-8136-ed25e6c6684e',
            }

            domain_model = {
                'id': 'b38df608-d34b-4d58-8136-ed25e6c6684e',
                'name': 'domain_name',
            }

            overview_model = {
                'name': 'Sample Data Contract',
                'version': 'v0.0',
                'domain': domain_model,
                'more_info': 'List of links to sources that provide more details on the data contract.',
            }

            contract_terms_more_info_model = {
                'type': 'privacy-statement',
                'url': 'https://www.moreinfo.example.coms',
            }

            description_model = {
                'purpose': 'Intended purpose for the provided data.',
                'limitations': 'Technical, compliance, and legal limitations for data use.',
                'usage': 'Recommended usage of the data.',
                'more_info': [contract_terms_more_info_model],
                'custom_properties': 'Custom properties that are not part of the standard.',
            }

            contract_template_organization_model = {
                'user_id': 'IBMid-691000IN4G',
                'role': 'owner',
            }

            roles_model = {
                'role': 'IAM Role',
            }

            contract_template_sla_property_model = {
                'property': 'slaproperty',
                'value': 'slavalue',
            }

            contract_template_sla_model = {
                'default_element': 'sladefaultelement',
                'properties': [contract_template_sla_property_model],
            }

            contract_template_support_and_communication_model = {
                'channel': 'channel',
                'url': 'https://www.example.coms',
            }

            contract_template_custom_property_model = {
                'key': 'The name of the key.',
                'value': 'The value of the key.',
            }

            response = dph_service.replace_data_product_draft_contract_terms(
                data_product_id='testString',
                draft_id='testString',
                contract_terms_id='testString',
                documents=[contract_terms_document_model],
                overview=overview_model,
                description=description_model,
                organization=[contract_template_organization_model],
                roles=[roles_model],
                sla=[contract_template_sla_model],
                support_and_communication=[contract_template_support_and_communication_model],
                custom_properties=[contract_template_custom_property_model],
            )
            contract_terms = response.get_result()

            print(json.dumps(contract_terms, indent=2))

            # end-replace_data_product_draft_contract_terms

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_data_product_draft_contract_terms_example(self):
        """
        update_data_product_draft_contract_terms request example
        """
        try:
            print('\nupdate_data_product_draft_contract_terms() result:')

            # begin-update_data_product_draft_contract_terms

            json_patch_operation_model = {
                'op': 'add',
                'path': 'testString',
            }

            response = dph_service.update_data_product_draft_contract_terms(
                data_product_id='testString',
                draft_id='testString',
                contract_terms_id='testString',
                json_patch_instructions=[json_patch_operation_model],
            )
            contract_terms = response.get_result()

            print(json.dumps(contract_terms, indent=2))

            # end-update_data_product_draft_contract_terms

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

            response = dph_service.get_data_product_release(
                data_product_id=get_a_release_of_data_product_by_data_product_id_link,
                release_id=get_a_release_by_release_id_link,
            )
            data_product_release = response.get_result()

            print(json.dumps(data_product_release, indent=2))

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

            response = dph_service.update_data_product_release(
                data_product_id=update_release_of_data_product_by_data_product_id_link,
                release_id='testString',
                json_patch_instructions=[json_patch_operation_model],
            )
            data_product_release = response.get_result()

            print(json.dumps(data_product_release, indent=2))

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

            response = dph_service.get_release_contract_terms_document(
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
                client=dph_service,
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

            response = dph_service.retire_data_product_release(
                data_product_id=retire_a_releases_of_data_product_by_data_product_id_link,
                release_id=retire_a_release_contract_terms_by_release_id_link,
            )
            data_product_release = response.get_result()

            print(json.dumps(data_product_release, indent=2))

            # end-retire_data_product_release

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_data_product_contract_template_example(self):
        """
        list_data_product_contract_template request example
        """
        try:
            print('\nlist_data_product_contract_template() result:')

            # begin-list_data_product_contract_template

            response = dph_service.list_data_product_contract_template()
            data_product_contract_template_collection = response.get_result()

            print(json.dumps(data_product_contract_template_collection, indent=2))

            # end-list_data_product_contract_template

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_contract_template_example(self):
        """
        create_contract_template request example
        """
        try:
            print('\ncreate_contract_template() result:')

            # begin-create_contract_template

            container_reference_model = {
                'id': 'f531f74a-01c8-4e91-8e29-b018db683c86',
                'type': 'catalog',
            }

            domain_model = {
                'id': 'b38df608-d34b-4d58-8136-ed25e6c6684e',
                'name': 'domain_name',
            }

            overview_model = {
                'name': 'Sample Data Contract',
                'version': '0.0.0',
                'domain': domain_model,
                'more_info': 'List of links to sources that provide more details on the data contract.',
            }

            contract_terms_more_info_model = {
                'type': 'privacy-statement',
                'url': 'https://www.moreinfo.example.coms',
            }

            description_model = {
                'purpose': 'Intended purpose for the provided data.',
                'limitations': 'Technical, compliance, and legal limitations for data use.',
                'usage': 'Recommended usage of the data.',
                'more_info': [contract_terms_more_info_model],
                'custom_properties': 'Custom properties that are not part of the standard.',
            }

            contract_template_organization_model = {
                'user_id': 'IBMid-691000IN4G',
                'role': 'owner',
            }

            roles_model = {
                'role': 'IAM Role',
            }

            pricing_model = {
                'amount': '100.00',
                'currency': 'USD',
                'unit': 'megabyte',
            }

            contract_template_sla_property_model = {
                'property': 'slaproperty',
                'value': 'slavalue',
            }

            contract_template_sla_model = {
                'default_element': 'sladefaultelement',
                'properties': [contract_template_sla_property_model],
            }

            contract_template_support_and_communication_model = {
                'channel': 'channel',
                'url': 'https://www.example.coms',
            }

            contract_template_custom_property_model = {
                'key': 'propertykey',
                'value': 'propertyvalue',
            }

            contract_terms_model = {
                'overview': overview_model,
                'description': description_model,
                'organization': [contract_template_organization_model],
                'roles': [roles_model],
                'price': pricing_model,
                'sla': [contract_template_sla_model],
                'support_and_communication': [contract_template_support_and_communication_model],
                'custom_properties': [contract_template_custom_property_model],
            }

            response = dph_service.create_contract_template(
                container=container_reference_model,
                name='Sample Data Contract Template',
                contract_terms=contract_terms_model,
            )
            data_product_contract_template = response.get_result()

            print(json.dumps(data_product_contract_template, indent=2))

            # end-create_contract_template

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_contract_template_example(self):
        """
        get_contract_template request example
        """
        try:
            print('\nget_contract_template() result:')

            # begin-get_contract_template

            response = dph_service.get_contract_template(
                contract_template_id='testString',
                container_id='testString',
            )
            data_product_contract_template = response.get_result()

            print(json.dumps(data_product_contract_template, indent=2))

            # end-get_contract_template

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_data_product_contract_template_example(self):
        """
        update_data_product_contract_template request example
        """
        try:
            print('\nupdate_data_product_contract_template() result:')

            # begin-update_data_product_contract_template

            json_patch_operation_model = {
                'op': 'add',
                'path': 'testString',
            }

            response = dph_service.update_data_product_contract_template(
                contract_template_id='testString',
                container_id='testString',
                json_patch_instructions=[json_patch_operation_model],
            )
            data_product_contract_template = response.get_result()

            print(json.dumps(data_product_contract_template, indent=2))

            # end-update_data_product_contract_template

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_data_product_domains_example(self):
        """
        list_data_product_domains request example
        """
        try:
            print('\nlist_data_product_domains() result:')

            # begin-list_data_product_domains

            response = dph_service.list_data_product_domains()
            data_product_domain_collection = response.get_result()

            print(json.dumps(data_product_domain_collection, indent=2))

            # end-list_data_product_domains

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_data_product_domain_example(self):
        """
        create_data_product_domain request example
        """
        try:
            print('\ncreate_data_product_domain() result:')

            # begin-create_data_product_domain

            container_reference_model = {
                'id': 'ed580171-a6e4-4b93-973f-ae2f2f62991b',
                'type': 'catalog',
            }

            initialize_sub_domain_model = {
                'name': 'Sub domain 1',
                'description': 'New sub domain 1',
            }

            response = dph_service.create_data_product_domain(
                container=container_reference_model,
                name='Test domain',
                description='The sample description for new domain',
                sub_domains=[initialize_sub_domain_model],
            )
            data_product_domain = response.get_result()

            print(json.dumps(data_product_domain, indent=2))

            # end-create_data_product_domain

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_data_product_subdomain_example(self):
        """
        create_data_product_subdomain request example
        """
        try:
            print('\ncreate_data_product_subdomain() result:')

            # begin-create_data_product_subdomain

            response = dph_service.create_data_product_subdomain(
                domain_id='testString',
                container_id='testString',
                name='Sub domain 1',
                description='New sub domain 1',
            )
            initialize_sub_domain = response.get_result()

            print(json.dumps(initialize_sub_domain, indent=2))

            # end-create_data_product_subdomain

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_domain_example(self):
        """
        get_domain request example
        """
        try:
            print('\nget_domain() result:')

            # begin-get_domain

            response = dph_service.get_domain(
                domain_id='testString',
            )
            data_product_domain = response.get_result()

            print(json.dumps(data_product_domain, indent=2))

            # end-get_domain

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_data_product_domain_example(self):
        """
        update_data_product_domain request example
        """
        try:
            print('\nupdate_data_product_domain() result:')

            # begin-update_data_product_domain

            json_patch_operation_model = {
                'op': 'add',
                'path': 'testString',
            }

            response = dph_service.update_data_product_domain(
                domain_id='testString',
                container_id='testString',
                json_patch_instructions=[json_patch_operation_model],
            )
            data_product_domain = response.get_result()

            print(json.dumps(data_product_domain, indent=2))

            # end-update_data_product_domain

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_data_product_by_domain_example(self):
        """
        get_data_product_by_domain request example
        """
        try:
            print('\nget_data_product_by_domain() result:')

            # begin-get_data_product_by_domain

            response = dph_service.get_data_product_by_domain(
                domain_id='testString',
                container_id='testString',
            )
            data_product_version_collection = response.get_result()

            print(json.dumps(data_product_version_collection, indent=2))

            # end-get_data_product_by_domain

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_s3_bucket_example(self):
        """
        create_s3_bucket request example
        """
        try:
            print('\ncreate_s3_bucket() result:')

            # begin-create_s3_bucket

            response = dph_service.create_s3_bucket(
                is_shared=True,
            )
            bucket_response = response.get_result()

            print(json.dumps(bucket_response, indent=2))

            # end-create_s3_bucket

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_s3_bucket_validation_example(self):
        """
        get_s3_bucket_validation request example
        """
        try:
            print('\nget_s3_bucket_validation() result:')

            # begin-get_s3_bucket_validation

            response = dph_service.get_s3_bucket_validation(
                bucket_name='testString',
            )
            bucket_validation_response = response.get_result()

            print(json.dumps(bucket_validation_response, indent=2))

            # end-get_s3_bucket_validation

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_draft_contract_terms_document_example(self):
        """
        delete_draft_contract_terms_document request example
        """
        try:
            # begin-delete_draft_contract_terms_document

            response = dph_service.delete_draft_contract_terms_document(
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

            response = dph_service.delete_data_product_draft(
                data_product_id=delete_draft_of_data_product_by_data_product_id_link,
                draft_id=delete_a_draft_by_draft_id_link,
            )

            # end-delete_data_product_draft
            print('\ndelete_data_product_draft() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_data_product_contract_template_example(self):
        """
        delete_data_product_contract_template request example
        """
        try:
            # begin-delete_data_product_contract_template

            response = dph_service.delete_data_product_contract_template(
                contract_template_id='testString',
                container_id='testString',
            )

            # end-delete_data_product_contract_template
            print('\ndelete_data_product_contract_template() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_domain_example(self):
        """
        delete_domain request example
        """
        try:
            # begin-delete_domain

            response = dph_service.delete_domain(
                domain_id='testString',
            )

            # end-delete_domain
            print('\ndelete_domain() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: DphV1
##############################################################################
