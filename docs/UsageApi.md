# allscreenshots_sdk.UsageApi

All URIs are relative to *https://api.allscreenshots.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_activity**](UsageApi.md#get_activity) | **GET** /v1/usage/activity | 
[**get_quota**](UsageApi.md#get_quota) | **GET** /v1/usage/quota | 
[**get_usage**](UsageApi.md#get_usage) | **GET** /v1/usage | 
[**get_usage_by_key**](UsageApi.md#get_usage_by_key) | **GET** /v1/usage/keys | 


# **get_activity**
> List[DailyCaptureCountResponse] get_activity(days=days, api_key_ids=api_key_ids)

### Example

* Api Key Authentication (ApiKey):

```python
import allscreenshots_sdk
from allscreenshots_sdk.models.daily_capture_count_response import DailyCaptureCountResponse
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
    api_instance = allscreenshots_sdk.UsageApi(api_client)
    days = 120 # int |  (optional) (default to 120)
    api_key_ids = ['api_key_ids_example'] # List[str] |  (optional)

    try:
        api_response = api_instance.get_activity(days=days, api_key_ids=api_key_ids)
        print("The response of UsageApi->get_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**|  | [optional] [default to 120]
 **api_key_ids** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[DailyCaptureCountResponse]**](DailyCaptureCountResponse.md)

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

# **get_quota**
> QuotaStatusResponse get_quota()

### Example

* Api Key Authentication (ApiKey):

```python
import allscreenshots_sdk
from allscreenshots_sdk.models.quota_status_response import QuotaStatusResponse
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
    api_instance = allscreenshots_sdk.UsageApi(api_client)

    try:
        api_response = api_instance.get_quota()
        print("The response of UsageApi->get_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_quota: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**QuotaStatusResponse**](QuotaStatusResponse.md)

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

# **get_usage**
> UsageResponse get_usage()

### Example

* Api Key Authentication (ApiKey):

```python
import allscreenshots_sdk
from allscreenshots_sdk.models.usage_response import UsageResponse
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
    api_instance = allscreenshots_sdk.UsageApi(api_client)

    try:
        api_response = api_instance.get_usage()
        print("The response of UsageApi->get_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_usage: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UsageResponse**](UsageResponse.md)

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

# **get_usage_by_key**
> ApiKeyUsageResponse get_usage_by_key()

### Example

* Api Key Authentication (ApiKey):

```python
import allscreenshots_sdk
from allscreenshots_sdk.models.api_key_usage_response import ApiKeyUsageResponse
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
    api_instance = allscreenshots_sdk.UsageApi(api_client)

    try:
        api_response = api_instance.get_usage_by_key()
        print("The response of UsageApi->get_usage_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_usage_by_key: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiKeyUsageResponse**](ApiKeyUsageResponse.md)

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

