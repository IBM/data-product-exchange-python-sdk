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
Integration Tests for DpxV1
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from ibm_dpx_services.dpx_v1 import *

# Config file name
config_file = 'dpx_v1.env'

# Variables to hold link values
container_id_link = None
contract_terms_id_link = None
data_product_id_link = None
document_id_link = None
draft_id_link = None
optional_data_product_id_link = None
release_id_link = None


class TestDpxV1:
    """
    Integration Test Class for DpxV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.dpx_service = DpxV1.new_instance()
            assert cls.dpx_service is not None

            cls.config = read_external_sources(DpxV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.dpx_service.enable_retries()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_initialize(self):
        global container_id_link

        # Construct a dict representation of a ContainerReference model
        # container_reference_model = {
        #     'id': container_id_link,
        #     'type': 'catalog',
        # }

        response = self.dpx_service.initialize(
            container=None,
            include=['delivery_methods', 'data_product_samples', 'domains_multi_industry'],
        )

        assert response.get_status_code() == 202
        initialize_resource = response.get_result()
        assert initialize_resource is not None

        container_id_link = initialize_resource['container']['id']

    @needscredentials
    def test_create_data_product(self):
        global optional_data_product_id_link
        global data_product_id_link

        # Construct a dict representation of a DataProductIdentity model
        data_product_identity_model = {
            'id': 'b38df608-d34b-4d58-8136-ed25e6c6684e',
        }
        # Construct a dict representation of a ContainerReference model
        container_reference_model = {
            'id': container_id_link,
            'type': 'catalog',
        }
        # Construct a dict representation of a AssetReference model
        asset_reference_model = {
            'id': '2b0bf220-079c-11ee-be56-0242ac120002',
            'container': container_reference_model,
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
        # Construct a dict representation of a ContractTermsDocumentAttachment model
        contract_terms_document_attachment_model = {
            'id': 'testString',
        }
        # Construct a dict representation of a ContractTermsDocument model
        contract_terms_document_model = {
            'url': 'testString',
            'type': 'terms_and_conditions',
            'name': 'testString',
            'id': '2b0bf220-079c-11ee-be56-0242ac120002',
            'attachment': contract_terms_document_attachment_model,
            'upload_url': 'testString',
        }
        # Construct a dict representation of a DataProductContractTerms model
        data_product_contract_terms_model = {
            'asset': asset_reference_model,
            'id': contract_terms_id_link,
            'documents': [contract_terms_document_model],
        }
        # Construct a dict representation of a DataProductVersionPrototype model
        data_product_version_prototype_model = {
            'name': 'My New Data Product',
            'description': 'This is a description of My Data Product.',
            'asset': asset_reference_model,
            'types': ['data'],
        }

        response = self.dpx_service.create_data_product(
            drafts=[data_product_version_prototype_model],
        )

        assert response.get_status_code() == 200
        data_product = response.get_result()
        assert data_product is not None

        optional_data_product_id_link = data_product['id']
        data_product_id_link = data_product['id']
        print("optional_data_product_id_link:", optional_data_product_id_link)
        print("data_product_id_link:", data_product_id_link)

    @needscredentials
    def test_create_data_product_draft(self):
        global draft_id_link
        global contract_terms_id_link

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {
            'id': container_id_link,
            'type': 'catalog',
        }
        # Construct a dict representation of a AssetReference model
        asset_reference_model = {
            'id': '2b0bf220-079c-11ee-be56-0242ac120002',
            'container': container_reference_model,
        }
        # Construct a dict representation of a DataProductIdentity model
        data_product_identity_model = {
            'id': data_product_id_link,
        }
        # Construct a dict representation of a UseCase model
        use_case_model = {
            'id': 'testString',
            'name': 'testString',
            'container': container_reference_model,
        }
        # Construct a dict representation of a Domain model
        domain_model = {
            'id': '918c0bfd-6943-4468-b74f-bc111018e0d1',
            'name': 'Customer Service',
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
        # Construct a dict representation of a ContractTermsDocumentAttachment model
        contract_terms_document_attachment_model = {
            'id': 'testString',
        }
        # Construct a dict representation of a ContractTermsDocument model
        contract_terms_document_model = {
            'url': 'testString',
            'type': 'terms_and_conditions',
            'name': 'testString',
            'id': '2b0bf220-079c-11ee-be56-0242ac120002',
            'attachment': contract_terms_document_attachment_model,
            'upload_url': 'testString',
        }
        # Construct a dict representation of a DataProductContractTerms model
        data_product_contract_terms_model = {
            'asset': asset_reference_model,
            'id': contract_terms_id_link,
            'documents': [contract_terms_document_model],
        }

        response = self.dpx_service.create_data_product_draft(
            data_product_id=data_product_id_link,
            asset=asset_reference_model,
            version='1.2.0',
            data_product=data_product_identity_model,
            name='data_product_test',
            description='testString',
            domain=domain_model,
            types=['data'],
            is_restricted=True,
        )

        assert response.get_status_code() == 201
        data_product_version = response.get_result()
        assert data_product_version is not None

        draft_id_link = data_product_version['id']
        contract_terms_id_link = data_product_version['contract_terms'][0]['id']

    @needscredentials
    def test_delete_data_product_draft(self):
        response = self.dpx_service.delete_data_product_draft(
            data_product_id=optional_data_product_id_link,
            draft_id=draft_id_link,
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_create_data_product_draft_again(self):
        global draft_id_link
        global contract_terms_id_link

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {
            'id': container_id_link,
            'type': 'catalog',
        }
        # Construct a dict representation of a AssetReference model
        asset_reference_model = {
            'id': '2b0bf220-079c-11ee-be56-0242ac120002',
            'container': container_reference_model,
        }
        # Construct a dict representation of a DataProductIdentity model
        data_product_identity_model = {
            'id': data_product_id_link,
        }
        # Construct a dict representation of a UseCase model
        use_case_model = {
            'id': 'testString',
            'name': 'testString',
            'container': container_reference_model,
        }
        # Construct a dict representation of a Domain model
        domain_model = {
            'id': '918c0bfd-6943-4468-b74f-bc111018e0d1',
            'name': 'Customer Service',
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
        # Construct a dict representation of a ContractTermsDocumentAttachment model
        contract_terms_document_attachment_model = {
            'id': 'testString',
        }
        # Construct a dict representation of a ContractTermsDocument model
        contract_terms_document_model = {
            'url': 'testString',
            'type': 'terms_and_conditions',
            'name': 'testString',
            'id': '2b0bf220-079c-11ee-be56-0242ac120002',
            'attachment': contract_terms_document_attachment_model,
            'upload_url': 'testString',
        }
        # Construct a dict representation of a DataProductContractTerms model
        data_product_contract_terms_model = {
            'asset': asset_reference_model,
            'id': contract_terms_id_link,
            'documents': [contract_terms_document_model],
        }

        response = self.dpx_service.create_data_product_draft(
            data_product_id=data_product_id_link,
            asset=asset_reference_model,
            version='1.2.0',
            data_product=data_product_identity_model,
            name='data_product_test',
            description='testString',
            domain=domain_model,
            types=['data'],
            is_restricted=True,
        )

        assert response.get_status_code() == 201
        data_product_version = response.get_result()
        assert data_product_version is not None

        draft_id_link = data_product_version['id']
        contract_terms_id_link = data_product_version['contract_terms'][0]['id']

    @needscredentials
    def test_create_draft_contract_terms_document(self):
        global document_id_link

        # Construct a dict representation of a ContractTermsDocumentAttachment model
        contract_terms_document_attachment_model = {
            'id': 'testString',
        }

        response = self.dpx_service.create_draft_contract_terms_document(
            data_product_id=optional_data_product_id_link,
            draft_id=draft_id_link,
            contract_terms_id=contract_terms_id_link,
            type='terms_and_conditions',
            name='Terms and conditions document',
            id='b38df608-d34b-4d58-8136-ed25e6c6684e',
            url='https://www.google.com',
        )

        assert response.get_status_code() == 201
        contract_terms_document = response.get_result()
        assert contract_terms_document is not None

        document_id_link = contract_terms_document['id']

    @needscredentials
    def test_delete_draft_contract_terms_document(self):
        response = self.dpx_service.delete_draft_contract_terms_document(
            data_product_id=optional_data_product_id_link,
            draft_id=draft_id_link,
            contract_terms_id=contract_terms_id_link,
            document_id=document_id_link,
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_create_draft_contract_terms_document_again(self):
        global document_id_link

        # Construct a dict representation of a ContractTermsDocumentAttachment model
        contract_terms_document_attachment_model = {
            'id': 'testString',
        }

        response = self.dpx_service.create_draft_contract_terms_document(
            data_product_id=optional_data_product_id_link,
            draft_id=draft_id_link,
            contract_terms_id=contract_terms_id_link,
            type='terms_and_conditions',
            name='Terms and conditions document',
            id='b38df608-d34b-4d58-8136-ed25e6c6684e',
            url='https://www.google.com',
        )

        assert response.get_status_code() == 201
        contract_terms_document = response.get_result()
        assert contract_terms_document is not None

        document_id_link = contract_terms_document['id']

    @needscredentials
    def test_update_data_product_draft(self):
        # Construct the asset object
        asset_string = '{"id":"669a570b-31f7-4c84-bfd1-851282ab5b86","container":{"id":"b6eb50b4-ace4-4dab-b2c4-318bb4c032a6","type":"catalog"}}'

        # Parse the JSON string to a dictionary
        asset_map = json.loads(asset_string)

        # Create a list to hold the asset object
        parts_out_list = [{"asset": asset_map}]
        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {
            'op': 'add',
            'path': '/parts_out',
            # 'from': 'testString',
            'value': parts_out_list,
        }

        response = self.dpx_service.update_data_product_draft(
            data_product_id=optional_data_product_id_link,
            draft_id=draft_id_link,
            json_patch_instructions=[json_patch_operation_model],
        )

        assert response.get_status_code() == 200
        data_product_version = response.get_result()
        assert data_product_version is not None

    @needscredentials
    def test_get_data_product_draft(self):
        response = self.dpx_service.get_data_product_draft(
            data_product_id=optional_data_product_id_link,
            draft_id=draft_id_link,
        )

        assert response.get_status_code() == 200
        data_product_version = response.get_result()
        assert data_product_version is not None

    @needscredentials
    def test_update_draft_contract_terms_document(self):
        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {
            'op': 'replace',
            'path': '/url',
            'value': 'https://google.com',
        }

        response = self.dpx_service.update_draft_contract_terms_document(
            data_product_id=optional_data_product_id_link,
            draft_id=draft_id_link,
            contract_terms_id=contract_terms_id_link,
            document_id=document_id_link,
            json_patch_instructions=[json_patch_operation_model],
        )

        assert response.get_status_code() == 200
        contract_terms_document = response.get_result()
        assert contract_terms_document is not None

    @needscredentials
    def test_get_initialize_status(self):
        response = self.dpx_service.get_initialize_status(
            container_id=container_id_link,
        )

        assert response.get_status_code() == 200
        initialize_resource = response.get_result()
        assert initialize_resource is not None

    @needscredentials
    def test_get_draft_contract_terms_document(self):
        response = self.dpx_service.get_draft_contract_terms_document(
            data_product_id=optional_data_product_id_link,
            draft_id=draft_id_link,
            contract_terms_id=contract_terms_id_link,
            document_id=document_id_link,
        )

        assert response.get_status_code() == 200
        contract_terms_document = response.get_result()
        assert contract_terms_document is not None

    @needscredentials
    def test_publish_data_product_draft(self):
        global release_id_link

        response = self.dpx_service.publish_data_product_draft(
            data_product_id=optional_data_product_id_link,
            draft_id=draft_id_link,
        )

        assert response.get_status_code() == 200
        data_product_version = response.get_result()
        assert data_product_version is not None

        release_id_link = data_product_version['id']

    @needscredentials
    def test_manage_api_keys(self):
        response = self.dpx_service.manage_api_keys()

        assert response.get_status_code() == 204

    @needscredentials
    def test_list_data_products(self):
        response = self.dpx_service.list_data_products(
            limit=200,
        )

        assert response.get_status_code() == 200
        data_product_summary_collection = response.get_result()
        assert data_product_summary_collection is not None

    @needscredentials
    def test_list_data_products_with_pager(self):
        all_results = []

        # Test get_next().
        pager = DataProductsPager(
            client=self.dpx_service,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = DataProductsPager(
            client=self.dpx_service,
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_data_products() returned a total of {len(all_results)} items(s) using DataProductsPager.')

    @needscredentials
    def test_get_data_product(self):
        response = self.dpx_service.get_data_product(
            data_product_id=data_product_id_link,
        )

        assert response.get_status_code() == 200
        data_product = response.get_result()
        assert data_product is not None

    @needscredentials
    def test_complete_draft_contract_terms_document(self):
        response = self.dpx_service.complete_draft_contract_terms_document(
            data_product_id=optional_data_product_id_link,
            draft_id=draft_id_link,
            contract_terms_id=contract_terms_id_link,
            document_id=document_id_link,
        )

        assert response.get_status_code() == 200
        contract_terms_document = response.get_result()
        assert contract_terms_document is not None

    @needscredentials
    def test_list_data_product_drafts(self):
        response = self.dpx_service.list_data_product_drafts(
            data_product_id=optional_data_product_id_link,
            limit=200,
        )

        assert response.get_status_code() == 200
        data_product_draft_collection = response.get_result()
        assert data_product_draft_collection is not None

    @needscredentials
    def test_list_data_product_drafts_with_pager(self):
        all_results = []

        # Test get_next().
        pager = DataProductDraftsPager(
            client=self.dpx_service,
            data_product_id=optional_data_product_id_link,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = DataProductDraftsPager(
            client=self.dpx_service,
            data_product_id=optional_data_product_id_link,
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(
            f'\nlist_data_product_drafts() returned a total of {len(all_results)} items(s) using DataProductDraftsPager.'
        )

    @needscredentials
    def test_get_data_product_release(self):
        response = self.dpx_service.get_data_product_release(
            data_product_id=optional_data_product_id_link,
            release_id=release_id_link,
        )

        assert response.get_status_code() == 200
        data_product_version = response.get_result()
        assert data_product_version is not None

    @needscredentials
    def test_update_data_product_release(self):
        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {
            'op': 'replace',
            'path': '/description',
            'value': '"New Description',
        }

        response = self.dpx_service.update_data_product_release(
            data_product_id=optional_data_product_id_link,
            release_id=release_id_link,
            json_patch_instructions=[json_patch_operation_model],
        )

        assert response.get_status_code() == 200
        data_product_version = response.get_result()
        assert data_product_version is not None

    @needscredentials
    def test_get_release_contract_terms_document(self):
        response = self.dpx_service.get_release_contract_terms_document(
            data_product_id=optional_data_product_id_link,
            release_id=release_id_link,
            contract_terms_id=contract_terms_id_link,
            document_id=document_id_link,
        )

        assert response.get_status_code() == 200
        contract_terms_document = response.get_result()
        assert contract_terms_document is not None

    @needscredentials
    def test_list_data_product_releases(self):
        response = self.dpx_service.list_data_product_releases(
            data_product_id=optional_data_product_id_link,
            limit=200,
        )

        assert response.get_status_code() == 200
        data_product_release_collection = response.get_result()
        assert data_product_release_collection is not None

    @needscredentials
    def test_list_data_product_releases_with_pager(self):
        all_results = []

        # Test get_next().
        pager = DataProductReleasesPager(
            client=self.dpx_service,
            data_product_id=optional_data_product_id_link,
            state=['available'],
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = DataProductReleasesPager(
            client=self.dpx_service,
            data_product_id=optional_data_product_id_link,
            state=['available'],
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(
            f'\nlist_data_product_releases() returned a total of {len(all_results)} items(s) using DataProductReleasesPager.'
        )

    @needscredentials
    def test_retire_data_product_release(self):
        response = self.dpx_service.retire_data_product_release(
            data_product_id=optional_data_product_id_link,
            release_id=release_id_link,
        )

        assert response.get_status_code() == 200
        data_product_version = response.get_result()
        assert data_product_version is not None
