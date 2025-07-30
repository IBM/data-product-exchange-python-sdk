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
Integration Tests for DphV1
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from dph_services.dph_v1 import *

# Config file name
config_file = 'dph_v1.env'

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
create_contract_template_id = None
create_data_product_domain_id = None


class TestDphV1:
    """
    Integration Test Class for DphV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.dph_service = DphV1.new_instance(
            )
            assert cls.dph_service is not None

            cls.config = read_external_sources(DphV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.dph_service.enable_retries()

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
            'id': 'a7ca67e8-1fac-4061-ae9b-7604e15c4ab3',
            'type': 'catalog',
        }

        response = self.dph_service.initialize(
            container=container_reference_model,
            include=['delivery_methods', 'domains_multi_industry', 'data_product_samples', 'workflows', 'project', 'catalog_configurations'],
        )

        assert response.get_status_code() == 202
        initialize_resource = response.get_result()
        assert initialize_resource is not None

        create_draft_by_container_id_link = initialize_resource['container']['id']
        create_data_product_by_catalog_id_link = initialize_resource['container']['id']
        get_status_by_catalog_id_link = initialize_resource['container']['id']

    @pytest.mark.dependency(depends=["test_initialize"])
    @needscredentials
    def test_get_initialize_status(self):
        response = self.dph_service.get_initialize_status(
            container_id=get_status_by_catalog_id_link,
        )

        assert response.get_status_code() == 200
        initialize_resource = response.get_result()
        assert initialize_resource is not None

    @pytest.mark.dependency(depends=["test_get_initialize_status"])
    @needscredentials
    def test_get_service_id_credentials(self):
        response = self.dph_service.get_service_id_credentials()

        assert response.get_status_code() == 200
        service_id_credentials = response.get_result()
        assert service_id_credentials is not None

    @pytest.mark.dependency(depends=["test_get_service_id_credentials"])
    @needscredentials
    def test_manage_api_keys(self):
        response = self.dph_service.manage_api_keys()

        assert response.get_status_code() == 204

    @pytest.mark.dependency(depends=["test_manage_api_keys"])
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
        global get_draft_by_draft_id_link
        global create_a_contract_terms_doc_by_contract_terms_id_link
        global get_a_release_contract_terms_by_contract_terms_id_link
        global create_a_contract_terms_doc_by_draft_id_link

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {
            'id': create_data_product_by_catalog_id_link,
            'type': 'catalog',
        }

        # Construct a dict representation of a ContainerIdentity model
        container_identity_model = {
            'id': create_data_product_by_catalog_id_link,
        }
        # Construct a dict representation of a AssetPrototype model
        asset_prototype_model = {
            'id': '2b0bf220-079c-11ee-be56-0242ac120002',
            'container': container_identity_model,
        }
        # Construct a dict representation of a Domain model
        domain_model = {
            'id': 'ccacbfb4-7180-4632-b1ed-6709c7001f1e',
            'name': 'Customer Management',
            'container': container_reference_model,
        }
        # Construct a dict representation of a AssetPartReference model
        asset_part_reference_model = {
            'id': '16a8f683-f947-48d9-a92c-b81758b1a5f5',
            'container': container_reference_model,
            'type': 'data_asset',
        }
        # Construct a dict representation of a DeliveryMethod model
        delivery_method_model = {
            'id': '8848fd43-7384-4435-aff3-6a9f113768c4',
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
            'name': 'My New Data Product using Python SDK',
            'description': 'My Data Product generation using Python SDK.',
            'types': ['data'],
            'asset': asset_prototype_model,
            'domain': domain_model,
            'parts_out': [data_product_part_model],
        }

        response = self.dph_service.create_data_product(
            drafts=[data_product_version_prototype_model],
        )

        assert response.get_status_code() == 201
        data_product = response.get_result()
        assert data_product is not None

        print(data_product)
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
        create_a_contract_terms_doc_by_contract_terms_id_link = data_product['drafts'][0]['contract_terms'][0]['id']
        get_a_release_contract_terms_by_contract_terms_id_link = data_product['drafts'][0]['contract_terms'][0]['id']
        create_a_contract_terms_doc_by_draft_id_link = data_product['drafts'][0]['id']
        get_draft_by_draft_id_link = data_product['drafts'][0]['id']

    @pytest.mark.dependency(depends=["test_create_data_product"])
    @needscredentials
    def test_get_data_product(self):
        response = self.dph_service.get_data_product(
            data_product_id=get_data_product_by_data_product_id_link,
        )

        assert response.get_status_code() == 200
        data_product = response.get_result()
        assert data_product is not None

    @pytest.mark.dependency(depends=["test_get_data_product"])
    @needscredentials
    def test_list_data_products(self):
        response = self.dph_service.list_data_products(
            limit=200,
        )

        assert response.get_status_code() == 200
        data_product_collection = response.get_result()
        assert data_product_collection is not None

    @pytest.mark.dependency(depends=["test_list_data_products"])
    @needscredentials
    def test_list_data_products_with_pager(self):
        all_results = []

        # Test get_next().
        pager = DataProductsPager(
            client=self.dph_service,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = DataProductsPager(
            client=self.dph_service,
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_data_products() returned a total of {len(all_results)} items(s) using DataProductsPager.')
  
    @pytest.mark.dependency(depends=["test_list_data_products_with_pager"])
    @needscredentials
    def test_get_data_product_draft(self):
        response = self.dph_service.get_data_product_draft(
            data_product_id='-',
            draft_id=get_draft_by_draft_id_link,
        )

        assert response.get_status_code() == 200
        data_product_draft = response.get_result()
        assert data_product_draft is not None

    @pytest.mark.dependency(depends=["test_get_data_product_draft"])
    @needscredentials
    def test_update_data_product_draft(self):
        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {
            'op': 'replace',
            'path': '/description',
            'value': 'Updated the description by Node SDK.',
        }

        response = self.dph_service.update_data_product_draft(
            data_product_id='-',
            draft_id=create_a_contract_terms_doc_by_draft_id_link,
            json_patch_instructions=[json_patch_operation_model],
        )

        assert response.get_status_code() == 200
        data_product_draft = response.get_result()
        assert data_product_draft is not None

    @pytest.mark.dependency(depends=["test_update_data_product_draft"])
    @needscredentials
    def test_create_draft_contract_terms_document(self):
        global get_release_contract_document_by_document_id_link
        global delete_contract_terms_document_by_document_id_link
        global get_contract_terms_document_by_id_document_id_link
        global update_contract_terms_document_by_document_id_link
        global complete_contract_terms_document_by_document_id_link

        response = self.dph_service.create_draft_contract_terms_document(
            data_product_id=upload_contract_terms_doc_by_data_product_id_link,
            draft_id=create_a_contract_terms_doc_by_draft_id_link,
            contract_terms_id=create_a_contract_terms_doc_by_contract_terms_id_link,
            type='terms_and_conditions',
            name='Terms and conditions document',
            url='https://www.ibm.com/contract_document',
        )

        assert response.get_status_code() == 201
        contract_terms_document = response.get_result()
        assert contract_terms_document is not None

        get_release_contract_document_by_document_id_link = contract_terms_document['id']
        delete_contract_terms_document_by_document_id_link = contract_terms_document['id']
        get_contract_terms_document_by_id_document_id_link = contract_terms_document['id']
        update_contract_terms_document_by_document_id_link = contract_terms_document['id']
        complete_contract_terms_document_by_document_id_link = contract_terms_document['id']

    @pytest.mark.dependency(depends=["test_create_draft_contract_terms_document"])
    @needscredentials
    def test_get_draft_contract_terms_document(self):
        response = self.dph_service.get_draft_contract_terms_document(
            data_product_id=get_contract_document_by_data_product_id_link,
            draft_id=create_a_contract_terms_doc_by_draft_id_link,
            contract_terms_id=create_a_contract_terms_doc_by_contract_terms_id_link,
            document_id=get_contract_terms_document_by_id_document_id_link,
        )

        assert response.get_status_code() == 200
        contract_terms_document = response.get_result()
        assert contract_terms_document is not None

    @pytest.mark.dependency(depends=["test_get_draft_contract_terms_document"])
    @needscredentials
    def test_update_draft_contract_terms_document(self):
        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {
            'op': 'add',
            'path': '/name',
            'value': 'updated Terms and Conditions',
        }

        response = self.dph_service.update_draft_contract_terms_document(
            data_product_id=get_contract_document_by_data_product_id_link,
            draft_id=create_a_contract_terms_doc_by_draft_id_link,
            contract_terms_id=create_a_contract_terms_doc_by_contract_terms_id_link,
            document_id=get_contract_terms_document_by_id_document_id_link,
            json_patch_instructions=[json_patch_operation_model],
        )

        assert response.get_status_code() == 200
        contract_terms_document = response.get_result()
        assert contract_terms_document is not None

    @pytest.mark.dependency(depends=["test_update_draft_contract_terms_document"])
    @needscredentials
    def test_get_data_product_draft_contract_terms(self):
        response = self.dph_service.get_data_product_draft_contract_terms(
            data_product_id=get_contract_document_by_data_product_id_link,
            draft_id=create_a_contract_terms_doc_by_draft_id_link,
            contract_terms_id=create_a_contract_terms_doc_by_contract_terms_id_link,
            include_contract_documents=True,
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @pytest.mark.dependency(depends=["test_get_data_product_draft_contract_terms"])
    @needscredentials
    def test_publish_data_product_draft(self):
        global update_a_release_by_release_id_link
        global get_a_release_contract_terms_by_release_id_link
        global retire_a_release_contract_terms_by_release_id_link
        global get_a_release_by_release_id_link

        response = self.dph_service.publish_data_product_draft(
            data_product_id=publish_a_draft_of_data_product_by_data_product_id_link,
            draft_id=get_draft_by_draft_id_link,
        )

        assert response.get_status_code() == 200
        data_product_release = response.get_result()
        assert data_product_release is not None

        update_a_release_by_release_id_link = data_product_release['id']
        get_a_release_contract_terms_by_release_id_link = data_product_release['id']
        retire_a_release_contract_terms_by_release_id_link = data_product_release['id']
        get_a_release_by_release_id_link = data_product_release['id']

    @pytest.mark.dependency(depends=["test_publish_data_product_draft"])
    @needscredentials
    def test_get_data_product_release(self):
        response = self.dph_service.get_data_product_release(
            data_product_id=get_a_release_of_data_product_by_data_product_id_link,
            release_id=get_a_release_by_release_id_link,
            check_caller_approval=False,
        )

        assert response.get_status_code() == 200
        data_product_release = response.get_result()
        assert data_product_release is not None

    @pytest.mark.dependency(depends=["test_get_data_product_release"])
    @needscredentials
    def test_update_data_product_release(self):
        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {
            'op': 'replace',
            'path': '/description',
            'value': 'New description for my data product',
        }

        response = self.dph_service.update_data_product_release(
            data_product_id=update_release_of_data_product_by_data_product_id_link,
            release_id=get_a_release_by_release_id_link,
            json_patch_instructions=[json_patch_operation_model],
        )

        assert response.get_status_code() == 200
        data_product_release = response.get_result()
        assert data_product_release is not None

    @pytest.mark.dependency(depends=["test_update_data_product_release"])
    @needscredentials
    def test_get_release_contract_terms_document(self):
        response = self.dph_service.get_release_contract_terms_document(
            data_product_id=get_release_contract_document_by_data_product_id_link,
            release_id=get_a_release_contract_terms_by_release_id_link,
            contract_terms_id=get_a_release_contract_terms_by_contract_terms_id_link,
            document_id=get_release_contract_document_by_document_id_link,
        )

        assert response.get_status_code() == 200
        contract_terms_document = response.get_result()
        assert contract_terms_document is not None

    @pytest.mark.dependency(depends=["test_get_release_contract_terms_document"])
    @needscredentials
    def test_replace_data_product_draft_contract_terms(self):

        # Construct a dict representation of a ContractTermsDocumentAttachment model
        contract_terms_document_attachment_model = {
            'id': get_contract_terms_document_by_id_document_id_link,
        }
        # Construct a dict representation of a ContractTermsDocument model
        contract_terms_document_model = {
            'url': 'https://ibm.com/document',
            'type': 'terms_and_conditions',
            'name': 'Terms and Conditions',
            'id': 'b38df608-d34b-4d58-8136-ed25e6c6684e',
            'attachment': contract_terms_document_attachment_model,
        }
        # Construct a dict representation of a Domain model
        domain_model = {
            'id': 'b38df608-d34b-4d58-8136-ed25e6c6684e',
            'name': 'domain_name',
        }
        # Construct a dict representation of a Overview model
        overview_model = {
            'api_version': 'v3.0.1',
            'kind': 'DataContract',
            'name': 'Sample Data Contract',
            'version': 'v0.0',
            'domain': domain_model,
            'more_info': 'List of links to sources that provide more details on the data contract.',
        }
        # Construct a dict representation of a ContractTermsMoreInfo model
        contract_terms_more_info_model = {
            'type': 'privacy-statement',
            'url': 'https://www.moreinfo.example.coms',
        }
        # Construct a dict representation of a Description model
        description_model = {
            'purpose': 'Intended purpose for the provided data.',
            'limitations': 'Technical, compliance, and legal limitations for data use.',
            'usage': 'Recommended usage of the data.',
            'more_info': [contract_terms_more_info_model],
            'custom_properties': 'Custom properties that are not part of the standard.',
        }
        # Construct a dict representation of a ContractTemplateOrganization model
        contract_template_organization_model = {
            'user_id': 'IBMid-691000IN4G',
            'role': 'owner',
        }
        # Construct a dict representation of a Roles model
        roles_model = {
            'role': 'IAM Role',
        }
        # Construct a dict representation of a Pricing model
        pricing_model = {
            'amount': '100.0',
            'currency': 'USD',
            'unit': 'megabyte',
        }
        # Construct a dict representation of a ContractTemplateSLAProperty model
        contract_template_sla_property_model = {
            'property': 'slaproperty',
            'value': 'slavalue',
        }
        # Construct a dict representation of a ContractTemplateSLA model
        contract_template_sla_model = {
            'default_element': 'sladefaultelement',
            'properties': [contract_template_sla_property_model],
        }
        # Construct a dict representation of a ContractTemplateSupportAndCommunication model
        contract_template_support_and_communication_model = {
            'channel': 'channel',
            'url': 'https://www.example.coms',
        }
        # Construct a dict representation of a ContractTemplateCustomProperty model
        contract_template_custom_property_model = {
            'key': 'The name of the key.',
            'value': 'The value of the key.',
        }
        # Construct a dict representation of a ContractTest model
        contract_test_model = {
            'status': 'pass',
            'last_tested_time': 'testString',
            'message': 'testString',
        }

        response = self.dph_service.replace_data_product_draft_contract_terms(
            data_product_id=get_contract_document_by_data_product_id_link,
            draft_id=create_a_contract_terms_doc_by_draft_id_link,
            contract_terms_id=create_a_contract_terms_doc_by_contract_terms_id_link,
            documents=[contract_terms_document_model],
            error_msg='testString',
            overview=overview_model,
            description=description_model,
            organization=[contract_template_organization_model],
            roles=[roles_model],
            price=pricing_model,
            sla=[contract_template_sla_model],
            support_and_communication=[contract_template_support_and_communication_model],
            custom_properties=[contract_template_custom_property_model],
            contract_test=contract_test_model,
        )

        assert response.get_status_code() == 200
        contract_terms = response.get_result()
        assert contract_terms is not None

    @pytest.mark.dependency(depends=["test_replace_data_product_draft_contract_terms"])
    @needscredentials
    def test_update_data_product_draft_contract_terms(self):
        
        # Construct a dict representation of a Domain model
        domain_model = {
            'id': 'b38df608-d34b-4d58-8136-ed25e6c6684e',
            'name': 'domain_name',
        }
        
        # Construct a dict representation of a Overview model
        overview_model = {
            'api_version': 'v3.0.1',
            'kind': 'DataContract',
            'name': 'Sample Data Contract',
            'version': 'v0.0',
            'domain': domain_model,
            'more_info': 'List of links to sources that provide more details on the data contract.',
        }
        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {
            'op': 'replace',
            'path': '/overview',
            'value': overview_model,
        }

        response = self.dph_service.update_data_product_draft_contract_terms(
            data_product_id=get_contract_document_by_data_product_id_link,
            draft_id=create_a_contract_terms_doc_by_draft_id_link,
            contract_terms_id=create_a_contract_terms_doc_by_contract_terms_id_link,
            json_patch_instructions=[json_patch_operation_model],
        )

        assert response.get_status_code() == 200
        contract_terms = response.get_result()
        assert contract_terms is not None

    @pytest.mark.dependency(depends=["test_update_data_product_draft_contract_terms"])
    @needscredentials
    def test_list_data_product_releases(self):
        response = self.dph_service.list_data_product_releases(
            data_product_id=get_list_of_releases_of_data_product_by_data_product_id_link,
            asset_container_id=create_data_product_by_catalog_id_link,
            state=['available'],
            limit=200,
        )

        assert response.get_status_code() == 200
        data_product_release_collection = response.get_result()
        assert data_product_release_collection is not None

    @pytest.mark.dependency(depends=["test_list_data_product_releases"])
    @needscredentials
    def test_list_data_product_releases_with_pager(self):
        all_results = []

        # Test get_next().
        pager = DataProductReleasesPager(
            client=self.dph_service,
            data_product_id=get_list_of_releases_of_data_product_by_data_product_id_link,
            asset_container_id=create_data_product_by_catalog_id_link,
            state=['available'],
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = DataProductReleasesPager(
            client=self.dph_service,
            data_product_id=get_list_of_releases_of_data_product_by_data_product_id_link,
            asset_container_id=create_data_product_by_catalog_id_link,
            state=['available'],
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_data_product_releases() returned a total of {len(all_results)} items(s) using DataProductReleasesPager.')

    @pytest.mark.dependency(depends=["test_list_data_product_releases_with_pager"])
    @needscredentials
    def test_retire_data_product_release(self):
        response = self.dph_service.retire_data_product_release(
            data_product_id=retire_a_releases_of_data_product_by_data_product_id_link,
            release_id=retire_a_release_contract_terms_by_release_id_link,
            revoke_access=False,
        )

        assert response.get_status_code() == 200
        data_product_release = response.get_result()
        assert data_product_release is not None

    @pytest.mark.dependency(depends=["test_retire_data_product_release"])
    @needscredentials
    def test_create_data_asset_visualization(self):
        # Construct a dict representation of a Visualization model
        visualization_model = {
            'id': 'testString',
            'name': 'testString',
        }
        # Construct a dict representation of a ContainerReference model
        container_reference_model = {
            'id': '2be8f727-c5d2-4cb0-9216-f9888f428048',
            'type': 'catalog',
        }
        # Construct a dict representation of a AssetReference model
        asset_reference_model = {
            'id': 'caeee3f3-756e-47d5-846d-da4600809e22',
            'name': 'testString',
            'container': container_reference_model,
        }
        # Construct a dict representation of a ErrorMessage model
        error_message_model = {
            'code': 'testString',
            'message': 'testString',
        }
        # Construct a dict representation of a DataAssetRelationship model
        data_asset_relationship_model = {
            'visualization': visualization_model,
            'asset': asset_reference_model,
            'related_asset': asset_reference_model,
            'error': error_message_model,
        }

        response = self.dph_service.create_data_asset_visualization(
            assets=[data_asset_relationship_model],
        )

        assert response.get_status_code() == 201
        data_asset_visualization_res = response.get_result()
        assert data_asset_visualization_res is not None

    @pytest.mark.dependency(depends=["test_create_data_asset_visualization"])
    @needscredentials
    def test_reinitiate_data_asset_visualization(self):
        # Construct a dict representation of a Visualization model
        visualization_model = {
            'id': 'testString',
            'name': 'testString',
        }
        # Construct a dict representation of a ContainerReference model
        container_reference_model = {
            'id': '2be8f727-c5d2-4cb0-9216-f9888f428048',
            'type': 'catalog',
        }
        # Construct a dict representation of a AssetReference model
        asset_reference_model = {
            'id': 'caeee3f3-756e-47d5-846d-da4600809e22',
            'name': 'testString',
            'container': container_reference_model,
        }
        # Construct a dict representation of a ErrorMessage model
        error_message_model = {
            'code': 'testString',
            'message': 'testString',
        }
        # Construct a dict representation of a DataAssetRelationship model
        data_asset_relationship_model = {
            'visualization': visualization_model,
            'asset': asset_reference_model,
            'related_asset': asset_reference_model,
            'error': error_message_model,
        }

        response = self.dph_service.reinitiate_data_asset_visualization(
            assets=[data_asset_relationship_model],
        )

        assert response.get_status_code() == 200
        data_asset_visualization_res = response.get_result()
        assert data_asset_visualization_res is not None

    @pytest.mark.dependency(depends=["test_reinitiate_data_asset_visualization"])
    @needscredentials
    def test_create_contract_template(self):
        global create_contract_template_id
        # Construct a dict representation of a ContainerReference model
        container_reference_model = {
            'id': get_status_by_catalog_id_link,
            'type': 'catalog',
        }
        # Construct a dict representation of a ErrorMessage model
        error_message_model = {
            'code': 'testString',
            'message': 'testString',
        }
        # Construct a dict representation of a AssetReference model
        asset_reference_model = {
            'id': '2b0bf220-079c-11ee-be56-0242ac120002',
            'name': 'testString',
            'container': container_reference_model,
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
        # Construct a dict representation of a Domain model
        domain_model = {
            'id': 'b38df608-d34b-4d58-8136-ed25e6c6684e',
            'name': 'domain_name',
            'container': container_reference_model,
        }
        # Construct a dict representation of a Overview model
        overview_model = {
            'api_version': 'v3.0.1',
            'kind': 'DataContract',
            'name': 'Sample Data Contract',
            'version': '0.0.0',
            'domain': domain_model,
            'more_info': 'List of links to sources that provide more details on the data contract.',
        }
        # Construct a dict representation of a ContractTermsMoreInfo model
        contract_terms_more_info_model = {
            'type': 'privacy-statement',
            'url': 'https://www.moreinfo.example.coms',
        }
        # Construct a dict representation of a Description model
        description_model = {
            'purpose': 'Intended purpose for the provided data.',
            'limitations': 'Technical, compliance, and legal limitations for data use.',
            'usage': 'Recommended usage of the data.',
            'more_info': [contract_terms_more_info_model],
            'custom_properties': 'Custom properties that are not part of the standard.',
        }
        # Construct a dict representation of a ContractTemplateOrganization model
        contract_template_organization_model = {
            'user_id': 'IBMid-691000IN4G',
            'role': 'owner',
        }
        # Construct a dict representation of a Roles model
        roles_model = {
            'role': 'IAM Role',
        }
        # Construct a dict representation of a Pricing model
        pricing_model = {
            'amount': '100.00',
            'currency': 'USD',
            'unit': 'megabyte',
        }
        # Construct a dict representation of a ContractTemplateSLAProperty model
        contract_template_sla_property_model = {
            'property': 'slaproperty',
            'value': 'slavalue',
        }
        # Construct a dict representation of a ContractTemplateSLA model
        contract_template_sla_model = {
            'default_element': 'sladefaultelement',
            'properties': [contract_template_sla_property_model],
        }
        # Construct a dict representation of a ContractTemplateSupportAndCommunication model
        contract_template_support_and_communication_model = {
            'channel': 'channel',
            'url': 'https://www.example.coms',
        }
        # Construct a dict representation of a ContractTemplateCustomProperty model
        contract_template_custom_property_model = {
            'key': 'propertykey',
            'value': 'propertyvalue',
        }
        # Construct a dict representation of a ContractTest model
        contract_test_model = {
            'status': 'pass',
            'last_tested_time': 'testString',
            'message': 'testString',
        }
        # Construct a dict representation of a ContractSchemaPropertyType model
        contract_schema_property_type_model = {
            'type': 'testString',
            'length': 'testString',
            'scale': 'testString',
            'nullable': 'testString',
            'signed': 'testString',
            'native_type': 'testString',
        }
        # Construct a dict representation of a ContractSchemaProperty model
        contract_schema_property_model = {
            'name': 'testString',
            'type': contract_schema_property_type_model,
        }
        # Construct a dict representation of a ContractSchema model
        contract_schema_model = {
            'name': 'testString',
            'description': 'testString',
            'physical_type': 'testString',
            'properties': [contract_schema_property_model],
        }
        # Construct a dict representation of a ContractTerms model
        contract_terms_model = {
            'overview': overview_model,
            'description': description_model,
            'organization': [contract_template_organization_model],
            'roles': [roles_model],
            'price': pricing_model,
            'sla': [contract_template_sla_model],
            'support_and_communication': [contract_template_support_and_communication_model],
            'custom_properties': [contract_template_custom_property_model],
            'contract_test': contract_test_model,
            'schema': [contract_schema_model],
        }

        response = self.dph_service.create_contract_template(
            container=container_reference_model,
            name='Sample Data Contract Template',
            contract_terms=contract_terms_model,
            container_id=get_status_by_catalog_id_link,
            contract_template_name='testString',
        )

        assert response.get_status_code() == 201
        data_product_contract_template = response.get_result()
        create_contract_template_id = data_product_contract_template['id']
        
        assert data_product_contract_template is not None

    @pytest.mark.dependency(depends=["test_create_contract_template"])
    @needscredentials
    def test_get_contract_template(self):
        response = self.dph_service.get_contract_template(
            contract_template_id=create_contract_template_id,
            container_id=get_status_by_catalog_id_link,
        )

        assert response.get_status_code() == 200
        data_product_contract_template = response.get_result()
        assert data_product_contract_template is not None

    @pytest.mark.dependency(depends=["test_get_contract_template"])
    @needscredentials
    def test_update_data_product_contract_template(self):
        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {
            'op': 'replace',
            'path': '/name',
            'value': 'contract template name',
        }

        response = self.dph_service.update_data_product_contract_template(
            contract_template_id=create_contract_template_id,
            container_id=get_status_by_catalog_id_link,
            json_patch_instructions=[json_patch_operation_model],
        )

        assert response.get_status_code() == 200
        data_product_contract_template = response.get_result()
        assert data_product_contract_template is not None

    @pytest.mark.dependency(depends=["test_update_data_product_contract_template"])
    @needscredentials
    def test_list_data_product_contract_template(self):
        response = self.dph_service.list_data_product_contract_template(
            container_id=get_status_by_catalog_id_link,
            contract_template_name='testString',
        )

        assert response.get_status_code() == 200
        data_product_contract_template_collection = response.get_result()
        assert data_product_contract_template_collection is not None

    @pytest.mark.dependency(depends=["test_list_data_product_contract_template"])
    @needscredentials
    def test_delete_data_product_contract_template(self):
        response = self.dph_service.delete_data_product_contract_template(
            contract_template_id=create_contract_template_id,
            container_id=get_status_by_catalog_id_link,
        )

        assert response.get_status_code() == 204

    @pytest.mark.dependency(depends=["test_delete_data_product_contract_template"])
    @needscredentials
    def test_create_data_product_draft(self):
        global delete_a_contract_document_by_draft_id_link
        global delete_a_draft_by_contract_terms_id_link
        global create_a_contract_terms_doc_by_contract_terms_id_link
        global delete_a_draft_by_draft_id_link
        global create_a_contract_terms_doc_by_draft_id_link

        # Construct a dict representation of a ContainerReference model
        container_reference_model = {
            'id': create_data_product_by_catalog_id_link,
            'type': 'catalog',
        }

        # Construct a dict representation of a ContainerIdentity model
        container_identity_model = {
            'id': create_data_product_by_catalog_id_link,
        }
        # Construct a dict representation of a AssetPrototype model
        asset_prototype_model = {
            'id': '2b0bf220-079c-11ee-be56-0242ac120002',
            'container': container_identity_model,
        }
        # Construct a dict representation of a Domain model
        domain_model = {
            'id': 'ccacbfb4-7180-4632-b1ed-6709c7001f1e',
            'name': 'Customer Management',
            'container': container_reference_model,
        }
        # Construct a dict representation of a AssetPartReference model
        asset_part_reference_model = {
            'id': '16a8f683-f947-48d9-a92c-b81758b1a5f5',
            'container': container_reference_model,
            'type': 'data_asset',
        }
        # Construct a dict representation of a DeliveryMethod model
        delivery_method_model = {
            'id': '8848fd43-7384-4435-aff3-6a9f113768c4',
            'container': container_reference_model,
        }
        # Construct a dict representation of a DataProductPart model
        data_product_part_model = {
            'asset': asset_part_reference_model,
            'delivery_methods': [delivery_method_model],
        }

        # Construct a dict representation of a DataProductVersionPrototype model
        data_product_version_prototype_model = {
            'version': '2.0.0',
            'state': 'draft',
            'name': 'New Delete Draft DP using Python SDK',
            'description': 'This is a description of My Data Product which will get deleted using Python SDK.',
            'types': ['data'],
            'asset': asset_prototype_model,
            'domain': domain_model,
            'parts_out': [data_product_part_model],
        }

        response = self.dph_service.create_data_product(
            drafts=[data_product_version_prototype_model],
        )

        assert response.get_status_code() == 201
        data_product = response.get_result()
        assert data_product is not None

        print(data_product)
        delete_a_contract_document_by_draft_id_link = data_product["drafts"][0]["id"]
        delete_a_draft_by_contract_terms_id_link = data_product["drafts"][0]["contract_terms"][0]["id"]
        create_a_contract_terms_doc_by_contract_terms_id_link = data_product["drafts"][0]["contract_terms"][0]["id"]
        delete_a_draft_by_draft_id_link = data_product["drafts"][0]["id"]
        create_a_contract_terms_doc_by_draft_id_link = data_product["drafts"][0]["id"]

    @pytest.mark.dependency(depends=["test_create_data_product_draft"])
    @needscredentials
    def test_list_data_product_drafts(self):
        response = self.dph_service.list_data_product_drafts(
            data_product_id=get_list_of_data_product_drafts_by_data_product_id_link,
            asset_container_id=create_data_product_by_catalog_id_link,
            limit=200,
        )

        assert response.get_status_code() == 200
        data_product_draft_collection = response.get_result()
        assert data_product_draft_collection is not None

    @pytest.mark.dependency(depends=["test_list_data_product_drafts"])
    @needscredentials
    def test_list_data_product_drafts_with_pager(self):
        all_results = []

        # Test get_next().
        pager = DataProductDraftsPager(
            client=self.dph_service,
            data_product_id=get_list_of_data_product_drafts_by_data_product_id_link,
            asset_container_id=get_status_by_catalog_id_link,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = DataProductDraftsPager(
            client=self.dph_service,
            data_product_id=get_list_of_data_product_drafts_by_data_product_id_link,
            asset_container_id=get_status_by_catalog_id_link,
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_data_product_drafts() returned a total of {len(all_results)} items(s) using DataProductDraftsPager.')

    @pytest.mark.dependency(depends=["test_list_data_product_drafts_with_pager"])
    @needscredentials
    def test_create_draft_contract_terms_document_for_delete_op(self):
        global get_release_contract_document_by_document_id_link
        global delete_contract_terms_document_by_document_id_link
        global get_contract_terms_document_by_id_document_id_link
        global update_contract_terms_document_by_document_id_link
        global complete_contract_terms_document_by_document_id_link

        response = self.dph_service.create_draft_contract_terms_document(
            data_product_id='-',
            draft_id=create_a_contract_terms_doc_by_draft_id_link,
            contract_terms_id=create_a_contract_terms_doc_by_contract_terms_id_link,
            type='terms_and_conditions',
            name='Terms and conditions document',
            url='https://data.un.org/Host.aspx?Content=UNdataUse',
        )

        assert response.get_status_code() == 201
        contract_terms_document = response.get_result()
        assert contract_terms_document is not None

        get_release_contract_document_by_document_id_link = contract_terms_document['id']
        delete_contract_terms_document_by_document_id_link = contract_terms_document['id']
        get_contract_terms_document_by_id_document_id_link = contract_terms_document['id']
        update_contract_terms_document_by_document_id_link = contract_terms_document['id']
        complete_contract_terms_document_by_document_id_link = contract_terms_document['id']

    @pytest.mark.dependency(depends=["test_create_draft_contract_terms_document_for_delete_op"])
    @needscredentials
    def test_delete_draft_contract_terms_document(self):
        response = self.dph_service.delete_draft_contract_terms_document(
            data_product_id='-',
            draft_id=delete_a_contract_document_by_draft_id_link,
            contract_terms_id=delete_a_draft_by_contract_terms_id_link,
            document_id=delete_contract_terms_document_by_document_id_link,
        )

        assert response.get_status_code() == 204

    @pytest.mark.dependency(depends=["test_delete_draft_contract_terms_document"])
    @needscredentials
    def test_list_data_product_domains(self):
        response = self.dph_service.list_data_product_domains(
            container_id=get_status_by_catalog_id_link,
        )

        assert response.get_status_code() == 200
        data_product_domain_collection = response.get_result()
        assert data_product_domain_collection is not None

    @pytest.mark.dependency(depends=["test_list_data_product_domains"])
    @needscredentials
    def test_create_data_product_domain(self):
        global create_data_product_domain_id
        # Construct a dict representation of a ContainerReference model
        container_reference_model = {
            'id': get_status_by_catalog_id_link,
            'type': 'catalog',
        }

        # Construct a dict representation of a InitializeSubDomain model
        initialize_sub_domain_model = {
            'name': 'Sub domain 1',
            'id': 'testString',
            'description': 'New sub domain 1',
        }

        response = self.dph_service.create_data_product_domain(
            container=container_reference_model,
            name='Test domain - python sdk',
            description='The sample description for new domain',
            sub_domains=[initialize_sub_domain_model],
            container_id=get_status_by_catalog_id_link,
        )

        assert response.get_status_code() == 201
        data_product_domain = response.get_result()
        create_data_product_domain_id = data_product_domain['id']
        assert data_product_domain is not None

    @pytest.mark.dependency(depends=["test_create_data_product_domain"])
    @needscredentials
    def test_create_data_product_subdomain(self):
        response = self.dph_service.create_data_product_subdomain(
            domain_id=create_data_product_domain_id,
            container_id=get_status_by_catalog_id_link,
            name='Sub domain 2',
            description='New sub domain 2',
        )

        assert response.get_status_code() == 201
        initialize_sub_domain = response.get_result()
        assert initialize_sub_domain is not None

    @pytest.mark.dependency(depends=["test_create_data_product_subdomain"])
    @needscredentials
    def test_get_domain(self):
        response = self.dph_service.get_domain(
            domain_id=create_data_product_domain_id,
        )

        assert response.get_status_code() == 200
        data_product_domain = response.get_result()
        assert data_product_domain is not None

    @pytest.mark.dependency(depends=["test_get_domain"])
    @needscredentials
    def test_update_data_product_domain(self):
        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {
            'op': 'replace',
            'path': '/name',
            'value': 'Updated domain name',
        }

        response = self.dph_service.update_data_product_domain(
            domain_id=create_data_product_domain_id,
            container_id=get_status_by_catalog_id_link,
            json_patch_instructions=[json_patch_operation_model],
        )

        assert response.get_status_code() == 200
        data_product_domain = response.get_result()
        assert data_product_domain is not None

    @pytest.mark.dependency(depends=["test_update_data_product_domain"])
    @needscredentials
    def test_get_data_product_by_domain(self):
        response = self.dph_service.get_data_product_by_domain(
            domain_id=create_data_product_domain_id,
            container_id=get_status_by_catalog_id_link,
        )

        assert response.get_status_code() == 200
        data_product_version_collection = response.get_result()
        assert data_product_version_collection is not None

    @pytest.mark.dependency(depends=["test_get_data_product_by_domain"])
    @needscredentials
    def test_delete_domain(self):
        response = self.dph_service.delete_domain(
            domain_id=create_data_product_domain_id,
        )

        assert response.get_status_code() == 204

    @pytest.mark.skip(reason="Skipping unneccesary creation of bucket")
    def test_create_s3_bucket(self):
        response = self.dph_service.create_s3_bucket(
            is_shared=True,
        )

        assert response.get_status_code() == 201
        bucket_response = response.get_result()
        assert bucket_response is not None

    @pytest.mark.skip(reason="Skipping bucket validation")
    def test_get_s3_bucket_validation(self):
        response = self.dph_service.get_s3_bucket_validation(
            bucket_name='testString',
        )

        assert response.get_status_code() == 200
        bucket_validation_response = response.get_result()
        assert bucket_validation_response is not None

    @pytest.mark.dependency(depends=["test_delete_domain"])
    @needscredentials
    def test_delete_data_product_draft(self):
        response = self.dph_service.delete_data_product_draft(
            data_product_id='-',
            draft_id=delete_a_draft_by_draft_id_link,
        )

        assert response.get_status_code() == 204


