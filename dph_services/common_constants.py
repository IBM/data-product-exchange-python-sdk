# Dph Api Paths
URL_GET_INITIALIZE_STATUS = '/data_product_exchange/v1/configuration/initialize/status'
URL_GET_SERVICEID_CREDENTIALS = '/data_product_exchange/v1/configuration/credentials'
URL_INITIALIZE = '/data_product_exchange/v1/configuration/initialize'
URL_MANAGE_APIKEYS = '/data_product_exchange/v1/configuration/rotate_credentials'
URL_LIST_DATA_PRODUCTS = '/data_product_exchange/v1/data_products'
URL_CREATE_DATA_PRODUCT = '/data_product_exchange/v1/data_products'
URL_GET_DATA_PRODUCT = '/data_product_exchange/v1/data_products/{data_product_id}'
URL_COMPLETE_DRAFT_CONTRACT_TERMS_DOCUMENT = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/contract_terms/{contract_terms_id}/documents/{document_id}/complete'
URL_LIST_DATA_PRODUCT_DRAFTS = '/data_product_exchange/v1/data_products/{data_product_id}/drafts'
URL_CREATE_DATA_PRODUCT_DRAFT = '/data_product_exchange/v1/data_products/{data_product_id}/drafts'
URL_CREATE_DRAFT_CONTRACT_TERMS_DOCUMENT = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/contract_terms/{contract_terms_id}/documents'
URL_GET_DATA_PRODUCT_DRAFT = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}'
URL_GET_DRAFT_CONTRACT_TERMS_DOCUMENT = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/contract_terms/{contract_terms_id}/documents/{document_id}'
URL_PUBLISH_DATA_PRODUCT_DRAFT = '/data_product_exchange/v1/data_products/{data_product_id}/drafts/{draft_id}/publish'
URL_GET_DATA_PRODUCT_RELEASE = '/data_product_exchange/v1/data_products/{data_product_id}/releases/{release_id}'
URL_UPDATE_DATA_PRODUCT_RELEASE = '/data_product_exchange/v1/data_products/{data_product_id}/releases/{release_id}'
URL_GET_RELEASE_CONTRACT_TERMS_DOCUMENT = '/data_product_exchange/v1/data_products/{data_product_id}/releases/{release_id}/contract_terms/{contract_terms_id}/documents/{document_id}'
URL_LIST_DATA_PRODUCT_RELEASES = '/data_product_exchange/v1/data_products/{data_product_id}/releases'
URL_RETIRE_DATA_PRODUCT_RELEASE = '/data_product_exchange/v1/data_products/{data_product_id}/releases/{release_id}/retire'

# Dph Api Headers
CONTENT_TYPE_JSON = 'application/json'
CONTENT_TYPE_PATCH_JSON = 'application/json-patch+json'

SERVICE_NAME = 'data_product_hub_api_service'
SERVICE_VERSION = 'V1'

