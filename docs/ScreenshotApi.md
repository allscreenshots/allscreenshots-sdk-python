# allscreenshots_sdk.ScreenshotApi

All URIs are relative to *https://api.allscreenshots.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**capture_sync**](ScreenshotApi.md#capture_sync) | **POST** /v1/screenshots | 
[**get_sync_capture_output_result**](ScreenshotApi.md#get_sync_capture_output_result) | **GET** /v1/screenshots/captures/{id}/result/{outputId} | 
[**get_sync_capture_result**](ScreenshotApi.md#get_sync_capture_result) | **GET** /v1/screenshots/captures/{id}/result | 
[**submission_status**](ScreenshotApi.md#submission_status) | **GET** /v1/screenshots/submissions/{key} | 


# **capture_sync**
> bytes capture_sync(screenshot_request, idempotency_key=idempotency_key)

### Example

* Api Key Authentication (ApiKey):

```python
import allscreenshots_sdk
from allscreenshots_sdk.models.screenshot_request import ScreenshotRequest
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
    api_instance = allscreenshots_sdk.ScreenshotApi(api_client)
    screenshot_request = allscreenshots_sdk.ScreenshotRequest() # ScreenshotRequest | 
    idempotency_key = 'idempotency_key_example' # str | Unique submission key. Supported for responseType=url; reuse with the same body to recover the original result. (optional)

    try:
        api_response = api_instance.capture_sync(screenshot_request, idempotency_key=idempotency_key)
        print("The response of ScreenshotApi->capture_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScreenshotApi->capture_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screenshot_request** | [**ScreenshotRequest**](ScreenshotRequest.md)|  | 
 **idempotency_key** | **str**| Unique submission key. Supported for responseType&#x3D;url; reuse with the same body to recover the original result. | [optional] 

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
**200** | Binary capture or JSON, according to responseType and outputs |  -  |
**400** | API error |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**404** | API error |  -  |
**409** | API error |  -  |
**422** | API error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_capture_output_result**
> bytes get_sync_capture_output_result(id, output_id)

### Example

* Api Key Authentication (ApiKey):

```python
import allscreenshots_sdk
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
    api_instance = allscreenshots_sdk.ScreenshotApi(api_client)
    id = 'id_example' # str | 
    output_id = 'output_id_example' # str | 

    try:
        api_response = api_instance.get_sync_capture_output_result(id, output_id)
        print("The response of ScreenshotApi->get_sync_capture_output_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScreenshotApi->get_sync_capture_output_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **output_id** | **str**|  | 

### Return type

**bytes**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stored capture output |  -  |
**400** | API error |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**404** | API error |  -  |
**409** | API error |  -  |
**422** | API error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_capture_result**
> bytes get_sync_capture_result(id)

### Example

* Api Key Authentication (ApiKey):

```python
import allscreenshots_sdk
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
    api_instance = allscreenshots_sdk.ScreenshotApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_sync_capture_result(id)
        print("The response of ScreenshotApi->get_sync_capture_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScreenshotApi->get_sync_capture_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**bytes**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stored capture output |  -  |
**400** | API error |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**404** | API error |  -  |
**409** | API error |  -  |
**422** | API error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submission_status**
> object submission_status(key)

### Example

* Api Key Authentication (ApiKey):

```python
import allscreenshots_sdk
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
    api_instance = allscreenshots_sdk.ScreenshotApi(api_client)
    key = 'key_example' # str | 

    try:
        api_response = api_instance.submission_status(key)
        print("The response of ScreenshotApi->submission_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScreenshotApi->submission_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 

### Return type

**object**

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

