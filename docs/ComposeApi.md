# allscreenshots_sdk.ComposeApi

All URIs are relative to *https://api.allscreenshots.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compose**](ComposeApi.md#compose) | **POST** /v1/screenshots/compose | 
[**get_compose_job_status**](ComposeApi.md#get_compose_job_status) | **GET** /v1/screenshots/compose/jobs/{jobId} | 
[**get_layout_preview**](ComposeApi.md#get_layout_preview) | **GET** /v1/screenshots/compose/preview | 
[**list_compose_jobs**](ComposeApi.md#list_compose_jobs) | **GET** /v1/screenshots/compose/jobs | 


# **compose**
> bytes compose(compose_request)

### Example

* Api Key Authentication (ApiKey):

```python
import allscreenshots_sdk
from allscreenshots_sdk.models.compose_request import ComposeRequest
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
    api_instance = allscreenshots_sdk.ComposeApi(api_client)
    compose_request = allscreenshots_sdk.ComposeRequest() # ComposeRequest | 

    try:
        api_response = api_instance.compose(compose_request)
        print("The response of ComposeApi->compose:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->compose: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compose_request** | [**ComposeRequest**](ComposeRequest.md)|  | 

### Return type

**bytes**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Composed image |  -  |
**202** | Composition accepted |  -  |
**400** | API error |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**404** | API error |  -  |
**409** | API error |  -  |
**422** | API error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compose_job_status**
> ComposeJobStatusResponse get_compose_job_status(job_id)

### Example

* Api Key Authentication (ApiKey):

```python
import allscreenshots_sdk
from allscreenshots_sdk.models.compose_job_status_response import ComposeJobStatusResponse
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
    api_instance = allscreenshots_sdk.ComposeApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        api_response = api_instance.get_compose_job_status(job_id)
        print("The response of ComposeApi->get_compose_job_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->get_compose_job_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**ComposeJobStatusResponse**](ComposeJobStatusResponse.md)

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

# **get_layout_preview**
> LayoutPreviewResponse get_layout_preview(layout, image_count, canvas_width=canvas_width, canvas_height=canvas_height, aspect_ratios=aspect_ratios)

### Example

* Api Key Authentication (ApiKey):

```python
import allscreenshots_sdk
from allscreenshots_sdk.models.layout_preview_response import LayoutPreviewResponse
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
    api_instance = allscreenshots_sdk.ComposeApi(api_client)
    layout = 'layout_example' # str | 
    image_count = 56 # int | 
    canvas_width = 1200 # int |  (optional) (default to 1200)
    canvas_height = 800 # int |  (optional) (default to 800)
    aspect_ratios = [3.4] # List[float] |  (optional)

    try:
        api_response = api_instance.get_layout_preview(layout, image_count, canvas_width=canvas_width, canvas_height=canvas_height, aspect_ratios=aspect_ratios)
        print("The response of ComposeApi->get_layout_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->get_layout_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layout** | **str**|  | 
 **image_count** | **int**|  | 
 **canvas_width** | **int**|  | [optional] [default to 1200]
 **canvas_height** | **int**|  | [optional] [default to 800]
 **aspect_ratios** | [**List[float]**](float.md)|  | [optional] 

### Return type

[**LayoutPreviewResponse**](LayoutPreviewResponse.md)

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

# **list_compose_jobs**
> List[ComposeJobSummaryResponse] list_compose_jobs()

### Example

* Api Key Authentication (ApiKey):

```python
import allscreenshots_sdk
from allscreenshots_sdk.models.compose_job_summary_response import ComposeJobSummaryResponse
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
    api_instance = allscreenshots_sdk.ComposeApi(api_client)

    try:
        api_response = api_instance.list_compose_jobs()
        print("The response of ComposeApi->list_compose_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->list_compose_jobs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ComposeJobSummaryResponse]**](ComposeJobSummaryResponse.md)

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

