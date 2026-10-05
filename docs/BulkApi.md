# allscreenshots_sdk.BulkApi

All URIs are relative to *https://api.allscreenshots.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_bulk_job**](BulkApi.md#cancel_bulk_job) | **POST** /v1/screenshots/bulk/{id}/cancel | 
[**create_bulk_job**](BulkApi.md#create_bulk_job) | **POST** /v1/screenshots/bulk | 
[**get_bulk_job_status**](BulkApi.md#get_bulk_job_status) | **GET** /v1/screenshots/bulk/{id} | 
[**list_bulk_jobs**](BulkApi.md#list_bulk_jobs) | **GET** /v1/screenshots/bulk | 


# **cancel_bulk_job**
> BulkJobSummary cancel_bulk_job(id)

### Example

* Api Key Authentication (ApiKey):

```python
import allscreenshots_sdk
from allscreenshots_sdk.models.bulk_job_summary import BulkJobSummary
from allscreenshots_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.allscreenshots.com
# See configuration.py for a list of all supported configuration parameters.
configuration = allscreenshots_sdk.Configuration(
    host = "https://api.allscreenshots.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with allscreenshots_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = allscreenshots_sdk.BulkApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.cancel_bulk_job(id)
        print("The response of BulkApi->cancel_bulk_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkApi->cancel_bulk_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BulkJobSummary**](BulkJobSummary.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | API error |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**404** | API error |  -  |
**409** | API error |  -  |
**422** | API error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bulk_job**
> BulkResponse create_bulk_job(bulk_request)

### Example

* Api Key Authentication (ApiKey):

```python
import allscreenshots_sdk
from allscreenshots_sdk.models.bulk_request import BulkRequest
from allscreenshots_sdk.models.bulk_response import BulkResponse
from allscreenshots_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.allscreenshots.com
# See configuration.py for a list of all supported configuration parameters.
configuration = allscreenshots_sdk.Configuration(
    host = "https://api.allscreenshots.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with allscreenshots_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = allscreenshots_sdk.BulkApi(api_client)
    bulk_request = allscreenshots_sdk.BulkRequest() # BulkRequest | 

    try:
        api_response = api_instance.create_bulk_job(bulk_request)
        print("The response of BulkApi->create_bulk_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkApi->create_bulk_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_request** | [**BulkRequest**](BulkRequest.md)|  | 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | OK |  -  |
**400** | API error |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**404** | API error |  -  |
**409** | API error |  -  |
**422** | API error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bulk_job_status**
> BulkStatusResponse get_bulk_job_status(id)

### Example

* Api Key Authentication (ApiKey):

```python
import allscreenshots_sdk
from allscreenshots_sdk.models.bulk_status_response import BulkStatusResponse
from allscreenshots_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.allscreenshots.com
# See configuration.py for a list of all supported configuration parameters.
configuration = allscreenshots_sdk.Configuration(
    host = "https://api.allscreenshots.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with allscreenshots_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = allscreenshots_sdk.BulkApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_bulk_job_status(id)
        print("The response of BulkApi->get_bulk_job_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkApi->get_bulk_job_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BulkStatusResponse**](BulkStatusResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | API error |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**404** | API error |  -  |
**409** | API error |  -  |
**422** | API error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bulk_jobs**
> List[BulkJobSummary] list_bulk_jobs()

### Example

* Api Key Authentication (ApiKey):

```python
import allscreenshots_sdk
from allscreenshots_sdk.models.bulk_job_summary import BulkJobSummary
from allscreenshots_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.allscreenshots.com
# See configuration.py for a list of all supported configuration parameters.
configuration = allscreenshots_sdk.Configuration(
    host = "https://api.allscreenshots.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with allscreenshots_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = allscreenshots_sdk.BulkApi(api_client)

    try:
        api_response = api_instance.list_bulk_jobs()
        print("The response of BulkApi->list_bulk_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkApi->list_bulk_jobs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BulkJobSummary]**](BulkJobSummary.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | API error |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**404** | API error |  -  |
**409** | API error |  -  |
**422** | API error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

