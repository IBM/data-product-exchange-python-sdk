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
Integration Tests for DataProductHubApiServiceV1
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from dph_services.data_product_hub_api_service_v1 import *
from pytest_depends import *


# Config file name
config_file = 'data_product_hub_api_service_v1.env'

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


class TestDataProductHubApiServiceV1:
    """
    Integration Test Class for DataProductHubApiServiceV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.data_product_hub_api_service = DataProductHubApiServiceV1.new_instance()
            assert cls.data_product_hub_api_service is not None

            cls.config = read_external_sources(DataProductHubApiServiceV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.data_product_hub_api_service.enable_retries()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_initialize(self):
        global create_draft_by_container_id_link
        global create_data_product_by_catalog_id_link
        global get_status_by_catalog_id_link

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {
            'id': '78c6e2f0-d6ed-46c0-8dee-2c2bd578d58b',
            'type': 'catalog',
        }

        response = self.data_product_hub_api_service.initialize(
            container=container_reference_model,
            include=['delivery_methods', 'domains_multi_industry', 'data_product_samples', 'workflows', 'project'],
        )

        assert response.get_status_code() == 202
        initialize_resource = response.get_result()
        assert initialize_resource is not None

        create_draft_by_container_id_link = initialize_resource['container']['id']
        create_data_product_by_catalog_id_link = initialize_resource['container']['id']
        get_status_by_catalog_id_link = initialize_resource['container']['id']

    @pytest.mark.dependency(depends=["test_initialize"])
    @needscredentials
    def test_create_data_product(self):
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

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {
            'id': '78c6e2f0-d6ed-46c0-8dee-2c2bd578d58b',
            'type': 'catalog',
        }

        # Construct a dict representation of a AssetReference model
        asset_reference_model = {
            'id': 'd6241f2b-cde1-42d7-9912-0348eccd5159',
            'container': container_reference_model,
        }
        # Construct a dict representation of a ContractTermsDocumentAttachment model
        contract_terms_document_attachment_model = {
            'id': 'fd55bb14-81a5-44a3-b578-2c9acc8a0c0d',
        }
        # Construct a dict representation of a ContractTermsDocument model
        contract_terms_document_model = {
            'url': 'https://data.un.org/Host.aspx?Content=UNdataUse',
            'type': 'terms_and_conditions',
            'name': 'Contract Terms Documents',
            'id': 'fd55bb14-81a5-44a3-b578-2c9acc8a0c0d',
            'attachment': contract_terms_document_attachment_model,
            'upload_url': 'https://data.un.org/Host.aspx?Content=UNdataUse',
        }
        # Construct a dict representation of a DataProductContractTerms model
        data_product_contract_terms_model = {
            'asset': asset_reference_model,
            'id': 'b483b37d-c3cb-412c-8045-854672027ed8@78c6e2f0-d6ed-46c0-8dee-2c2bd578d58b',
            'documents': [contract_terms_document_model],
        }
        # Construct a dict representation of a ContainerIdentity model
        container_identity_model = {
            'id': '78c6e2f0-d6ed-46c0-8dee-2c2bd578d58b',
        }
        # Construct a dict representation of a AssetPrototype model
        asset_prototype_model = {
            'id': 'd6241f2b-cde1-42d7-9912-0348eccd5159',
            'container': container_identity_model,
        }
        # Construct a dict representation of a Domain model
        domain_model = {
            'id': '352c8ccc-950d-4881-8139-9dc641fa87cd',
            'name': 'Human Resources',
            'container': container_reference_model,
        }
        # Construct a dict representation of a AssetPartReference model
        asset_part_reference_model = {
            'id': 'd6241f2b-cde1-42d7-9912-0348eccd5159',
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
            'delivery_methods': [delivery_method_model],
        }

        # Construct a dict representation of a DataProductVersionPrototype model
        data_product_version_prototype_model = {
            'version': '1.0.0',
            'state': 'draft',
            'name': 'My New Data Product',
            'description': 'This is a description of My Data Product.',
            'types': ['data'],
            'contract_terms': [data_product_contract_terms_model],
            'is_restricted': True,
            'asset': asset_prototype_model,
            'domain': domain_model,
            'parts_out': [data_product_part_model],
        }

        response = self.data_product_hub_api_service.create_data_product(
            drafts=[data_product_version_prototype_model],
        )

        assert response.get_status_code() == 201
        data_product = response.get_result()
        assert data_product is not None

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

    @needscredentials
    @pytest.mark.dependency(depends=["test_create_data_product"])
    def test_get_data_product(self):
        response = self.data_product_hub_api_service.get_data_product(
            data_product_id=get_data_product_by_data_product_id_link,
        )

        assert response.get_status_code() == 200
        data_product = response.get_result()
        assert data_product is not None

    @needscredentials
    @pytest.mark.dependency(depends=["test_get_data_product"])
    def test_list_data_products(self):
        response = self.data_product_hub_api_service.list_data_products(
            limit=200,
        )

        assert response.get_status_code() == 200
        data_product_summary_collection = response.get_result()
        assert data_product_summary_collection is not None

    @needscredentials
    @pytest.mark.dependency(depends=["test_list_data_products"])
    def test_list_data_products_with_pager(self):
        all_results = []

        # Test get_next().
        pager = DataProductsPager(
            client=self.data_product_hub_api_service,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = DataProductsPager(
            client=self.data_product_hub_api_service,
            limit=200,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_data_products() returned a total of {len(all_results)} items(s) using DataProductsPager.')

    @needscredentials
    @pytest.mark.dependency(depends=["test_list_data_products_with_pager"])
    def test_create_data_product_draft(self):
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

        # Construct a dict representation of a ContainerIdentity model
        container_identity_model = {
            'id': '78c6e2f0-d6ed-46c0-8dee-2c2bd578d58b',
        }
        # Construct a dict representation of a AssetPrototype model
        asset_prototype_model = {
            'container': container_identity_model,
        }
        # Construct a dict representation of a DataProductIdentity model
        data_product_identity_model = {
            'id': get_data_product_by_data_product_id_link,
        }
        # Construct a dict representation of a ContainerReference model
        container_reference_model = {
            'id': '78c6e2f0-d6ed-46c0-8dee-2c2bd578d58b',
            'type': 'catalog',
        }

        # Construct a dict representation of a AssetReference model
        asset_reference_model = {
            'container': container_reference_model,
        }
        # Construct a dict representation of a ContractTermsDocumentAttachment model
        contract_terms_document_attachment_model = {
            'id': 'fd55bb14-81a5-44a3-b578-2c9acc8a0c0d',
        }
        # Construct a dict representation of a ContractTermsDocument model
        contract_terms_document_model = {
            'url': 'https://data.un.org/Host.aspx?Content=UNdataUse',
            'type': 'terms_and_conditions',
            'name': 'Terms and Conditions',
            'id': 'fd55bb14-81a5-44a3-b578-2c9acc8a0c0d',
            'attachment': contract_terms_document_attachment_model,
            'upload_url': 'https://data.un.org/Host.aspx?Content=UNdataUse',
        }
        # Construct a dict representation of a DataProductContractTerms model
        data_product_contract_terms_model = {
            'asset': asset_reference_model,
            'id': 'b483b37d-c3cb-412c-8045-854672027ed8@78c6e2f0-d6ed-46c0-8dee-2c2bd578d58b',
            'documents': [contract_terms_document_model],
        }
        # Construct a dict representation of a Domain model
        domain_model = {
            'id': '352c8ccc-950d-4881-8139-9dc641fa87cd',
            'name': 'Human Resources',
            'container': container_reference_model,
        }
        # Construct a dict representation of a AssetPartReference model
        asset_part_reference_model = {
            'id': 'd6241f2b-cde1-42d7-9912-0348eccd5159',
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
            'delivery_methods': [delivery_method_model],
        }

        response = self.data_product_hub_api_service.create_data_product_draft(
            data_product_id=get_data_product_by_data_product_id_link,
            asset=asset_prototype_model,
            version='1.3.0',
            state='draft',
            data_product=data_product_identity_model,
            name='New DP Draft created from IntegrationTest',
            description='New Data Product Draft Created',
            types=['data'],
            contract_terms=[data_product_contract_terms_model],
            is_restricted=True,
            domain=domain_model,
            parts_out=[data_product_part_model],
        )

        assert response.get_status_code() == 201
        data_product_version = response.get_result()
        assert data_product_version is not None

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

    @needscredentials
    @pytest.mark.dependency(depends=["test_create_data_product_draft"])
    def test_get_data_product_draft(self):
        response = self.data_product_hub_api_service.get_data_product_draft(
            data_product_id=get_a_draft_of_data_product_by_data_product_id_link,
            draft_id=get_draft_by_draft_id_link,
        )

        assert response.get_status_code() == 200
        data_product_version = response.get_result()
        assert data_product_version is not None

    @needscredentials
    @pytest.mark.dependency(depends=["test_get_data_product_draft"])
    def test_update_data_product_draft(self):
        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {
            'op': 'replace',
            'path': '/description',
            'value': 'Updated Data Product Draft',
        }

        response = self.data_product_hub_api_service.update_data_product_draft(
            data_product_id=update_draft_of_data_product_by_data_product_id_link,
            draft_id=update_a_draft_by_draft_id_link,
            json_patch_instructions=[json_patch_operation_model],
        )

        assert response.get_status_code() == 200
        data_product_version = response.get_result()
        assert data_product_version is not None

    @needscredentials
    @pytest.mark.dependency(depends=["test_update_data_product_draft"])
    def test_create_draft_contract_terms_document(self):
        global get_release_contract_document_by_document_id_link
        global delete_contract_terms_document_by_document_id_link
        global get_contract_terms_document_by_id_document_id_link
        global update_contract_terms_document_by_document_id_link
        global complete_contract_terms_document_by_document_id_link

        # Construct a dict representation of a ContractTermsDocumentAttachment model
        contract_terms_document_attachment_model = {
            'id': 'fd55bb14-81a5-44a3-b578-2c9acc8a0c0d',
        }

        response = self.data_product_hub_api_service.create_draft_contract_terms_document(
            data_product_id=upload_contract_terms_doc_by_data_product_id_link,
            draft_id=create_a_contract_terms_doc_by_draft_id_link,
            contract_terms_id=create_a_contract_terms_doc_by_contract_terms_id_link,
            type='terms_and_conditions',
            name='Terms and conditions document',
            id='b38df608-d34b-4d58-8136-ed25e6c6684e',
            url='https://data.un.org/Host.aspx?Content=UNdataUse',
            attachment=contract_terms_document_attachment_model,
            upload_url='https://data.un.org/Host.aspx?Content=UNdataUse',
        )

        assert response.get_status_code() == 201
        contract_terms_document = response.get_result()
        assert contract_terms_document is not None

        get_release_contract_document_by_document_id_link = contract_terms_document['id']
        delete_contract_terms_document_by_document_id_link = contract_terms_document['id']
        get_contract_terms_document_by_id_document_id_link = contract_terms_document['id']
        update_contract_terms_document_by_document_id_link = contract_terms_document['id']
        complete_contract_terms_document_by_document_id_link = contract_terms_document['id']

    @needscredentials
    @pytest.mark.dependency(depends=["test_create_draft_contract_terms_document"])
    def test_get_draft_contract_terms_document(self):
        response = self.data_product_hub_api_service.get_draft_contract_terms_document(
            data_product_id=get_contract_document_by_data_product_id_link,
            draft_id=get_a_draft_contract_document_by_draft_id_link,
            contract_terms_id=get_a_draft_by_contract_terms_id_link,
            document_id=get_contract_terms_document_by_id_document_id_link,
        )

        assert response.get_status_code() == 200
        contract_terms_document = response.get_result()
        assert contract_terms_document is not None

    @needscredentials
    @pytest.mark.dependency(depends=["test_get_draft_contract_terms_document"])
    def test_update_draft_contract_terms_document(self):
        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {
            'op': 'replace',
            'path': '/type',
            'value': 'terms_and_conditions',
        }

        response = self.data_product_hub_api_service.update_draft_contract_terms_document(
            data_product_id=update_contract_document_by_data_product_id_link,
            draft_id=update_contract_document_by_draft_id_link,
            contract_terms_id=update_a_draft_by_contract_terms_id_link,
            document_id=update_contract_terms_document_by_document_id_link,
            json_patch_instructions=[json_patch_operation_model],
        )

        assert response.get_status_code() == 200
        contract_terms_document = response.get_result()
        assert contract_terms_document is not None

    @needscredentials
    @pytest.mark.dependency(depends=["test_update_draft_contract_terms_document"])
    def test_publish_data_product_draft(self):
        global update_a_release_by_release_id_link
        global get_a_release_contract_terms_by_release_id_link
        global retire_a_release_contract_terms_by_release_id_link
        global get_a_release_by_release_id_link

        response = self.data_product_hub_api_service.publish_data_product_draft(
            data_product_id=publish_a_draft_of_data_product_by_data_product_id_link,
            draft_id=publish_a_draft_by_draft_id_link,
        )

        assert response.get_status_code() == 200
        data_product_version = response.get_result()
        assert data_product_version is not None

        update_a_release_by_release_id_link = data_product_version['id']
        get_a_release_contract_terms_by_release_id_link = data_product_version['id']
        retire_a_release_contract_terms_by_release_id_link = data_product_version['id']
        get_a_release_by_release_id_link = data_product_version['id']

    @needscredentials
    @pytest.mark.dependency(depends=["test_publish_data_product_draft"])
    def test_list_data_product_drafts(self):
        response = self.data_product_hub_api_service.list_data_product_drafts(
            data_product_id=get_list_of_data_product_drafts_by_data_product_id_link,
            version='1.3.0',
            limit=10,
        )

        assert response.get_status_code() == 200
        data_product_draft_collection = response.get_result()
        assert data_product_draft_collection is not None

    @needscredentials
    @pytest.mark.dependency(depends=["test_list_data_product_drafts"])
    def test_list_data_product_drafts_with_pager(self):
        all_results = []

        # Test get_next().
        pager = DataProductDraftsPager(
            client=self.data_product_hub_api_service,
            data_product_id=get_list_of_data_product_drafts_by_data_product_id_link,
            version='1.3.0',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = DataProductDraftsPager(
            client=self.data_product_hub_api_service,
            data_product_id=get_list_of_data_product_drafts_by_data_product_id_link,
            version='1.3.0',
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(
            f'\nlist_data_product_drafts() returned a total of {len(all_results)} items(s) using DataProductDraftsPager.'
        )

    @needscredentials
    @pytest.mark.dependency(depends=["test_list_data_product_drafts_with_pager"])
    def test_get_initialize_status(self):
        response = self.data_product_hub_api_service.get_initialize_status(
            container_id=get_status_by_catalog_id_link,
        )

        assert response.get_status_code() == 200
        initialize_resource = response.get_result()
        assert initialize_resource is not None

    @needscredentials
    @pytest.mark.dependency(depends=["test_get_initialize_status"])
    def test_get_service_id_credentials(self):
        response = self.data_product_hub_api_service.get_service_id_credentials()

        assert response.get_status_code() == 200
        service_id_credentials = response.get_result()
        assert service_id_credentials is not None

    @needscredentials
    @pytest.mark.dependency(depends=["test_get_service_id_credentials"])
    def test_manage_api_keys(self):
        response = self.data_product_hub_api_service.manage_api_keys()
        assert response.get_status_code() == 204

    @needscredentials
    @pytest.mark.dependency(depends=["test_manage_api_keys"])
    def test_get_data_product_release(self):
        response = self.data_product_hub_api_service.get_data_product_release(
            data_product_id=get_a_release_of_data_product_by_data_product_id_link,
            release_id=get_a_release_by_release_id_link,
        )

        assert response.get_status_code() == 200
        data_product_version = response.get_result()
        assert data_product_version is not None

    @needscredentials
    @pytest.mark.dependency(depends=["test_get_data_product_release"])
    def test_update_data_product_release(self):
        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {
            'op': 'replace',
            'path': '/description',
            'value': 'Updated Data Product Release',
        }

        response = self.data_product_hub_api_service.update_data_product_release(
            data_product_id=update_release_of_data_product_by_data_product_id_link,
            release_id=get_a_release_by_release_id_link,
            json_patch_instructions=[json_patch_operation_model],
        )

        assert response.get_status_code() == 200
        data_product_version = response.get_result()
        assert data_product_version is not None

    @needscredentials
    @pytest.mark.dependency(depends=["test_update_data_product_release"])
    def test_get_release_contract_terms_document(self):
        response = self.data_product_hub_api_service.get_release_contract_terms_document(
            data_product_id=get_release_contract_document_by_data_product_id_link,
            release_id=get_a_release_contract_terms_by_release_id_link,
            contract_terms_id=get_a_release_contract_terms_by_contract_terms_id_link,
            document_id=get_release_contract_document_by_document_id_link,
        )

        assert response.get_status_code() == 200
        contract_terms_document = response.get_result()
        assert contract_terms_document is not None

    @needscredentials
    @pytest.mark.dependency(depends=["test_get_release_contract_terms_document"])
    def test_list_data_product_releases(self):
        response = self.data_product_hub_api_service.list_data_product_releases(
            data_product_id=get_list_of_releases_of_data_product_by_data_product_id_link,
            state=['available'],
            version='1.3.0',
            limit=200,
        )

        assert response.get_status_code() == 200
        data_product_release_collection = response.get_result()
        assert data_product_release_collection is not None

    @needscredentials
    @pytest.mark.dependency(depends=["test_list_data_product_releases"])
    def test_list_data_product_releases_with_pager(self):
        all_results = []

        # Test get_next().
        pager = DataProductReleasesPager(
            client=self.data_product_hub_api_service,
            data_product_id=get_list_of_releases_of_data_product_by_data_product_id_link,
            state=['available'],
            limit=200,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = DataProductReleasesPager(
            client=self.data_product_hub_api_service,
            data_product_id=get_list_of_releases_of_data_product_by_data_product_id_link,
            state=['available'],
            limit=200,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(
            f'\nlist_data_product_releases() returned a total of {len(all_results)} items(s) using DataProductReleasesPager.'
        )

    @needscredentials
    def test_delete_data_product_draft(self):
        response = self.data_product_hub_api_service.delete_data_product_draft(
            data_product_id=delete_draft_of_data_product_by_data_product_id_link,
            draft_id=delete_a_draft_by_draft_id_link,
        )
        assert response.get_status_code() == 204
