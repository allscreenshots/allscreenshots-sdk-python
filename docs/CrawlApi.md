# allscreenshots_sdk.CrawlApi

All URIs are relative to *https://api.allscreenshots.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel**](CrawlApi.md#cancel) | **POST** /v1/crawls/{id}/cancel | 
[**create**](CrawlApi.md#create) | **POST** /v1/crawls | 
[**delete**](CrawlApi.md#delete) | **DELETE** /v1/crawls/{id} | 
[**get**](CrawlApi.md#get) | **GET** /v1/crawls/{id} | 
[**list**](CrawlApi.md#list) | **GET** /v1/crawls | 
[**output**](CrawlApi.md#output) | **GET** /v1/crawls/{id}/pages/{pageId}/outputs/{output} | 
[**pages**](CrawlApi.md#pages) | **GET** /v1/crawls/{id}/pages | 


# **cancel**
> CrawlResponse cancel(id)

### Example

* Api Key Authentication (ApiKey):

```python
import allscreenshots_sdk
from allscreenshots_sdk.models.crawl_response import CrawlResponse
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
    api_instance = allscreenshots_sdk.CrawlApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.cancel(id)
        print("The response of CrawlApi->cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrawlApi->cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CrawlResponse**](CrawlResponse.md)

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

# **create**
> CrawlCreatedResponse create(crawl_request)

### Example

* Api Key Authentication (ApiKey):

```python
import allscreenshots_sdk
from allscreenshots_sdk.models.crawl_created_response import CrawlCreatedResponse
from allscreenshots_sdk.models.crawl_request import CrawlRequest
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
    api_instance = allscreenshots_sdk.CrawlApi(api_client)
    crawl_request = allscreenshots_sdk.CrawlRequest() # CrawlRequest | 

    try:
        api_response = api_instance.create(crawl_request)
        print("The response of CrawlApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrawlApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crawl_request** | [**CrawlRequest**](CrawlRequest.md)|  | 

### Return type

[**CrawlCreatedResponse**](CrawlCreatedResponse.md)

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

# **delete**
> delete(id)

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
    api_instance = allscreenshots_sdk.CrawlApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete(id)
    except Exception as e:
        print("Exception when calling CrawlApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |
**400** | API error |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**404** | API error |  -  |
**409** | API error |  -  |
**422** | API error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> CrawlResponse get(id)

### Example

* Api Key Authentication (ApiKey):

```python
import allscreenshots_sdk
from allscreenshots_sdk.models.crawl_response import CrawlResponse
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
    api_instance = allscreenshots_sdk.CrawlApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get(id)
        print("The response of CrawlApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrawlApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CrawlResponse**](CrawlResponse.md)

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

# **list**
> CrawlListResponse list(page=page, page_size=page_size)

### Example

* Api Key Authentication (ApiKey):

```python
import allscreenshots_sdk
from allscreenshots_sdk.models.crawl_list_response import CrawlListResponse
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
    api_instance = allscreenshots_sdk.CrawlApi(api_client)
    page = 0 # int |  (optional) (default to 0)
    page_size = 20 # int |  (optional) (default to 20)

    try:
        api_response = api_instance.list(page=page, page_size=page_size)
        print("The response of CrawlApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrawlApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 20]

### Return type

[**CrawlListResponse**](CrawlListResponse.md)

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

# **output**
> bytes output(id, page_id, output)

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
    api_instance = allscreenshots_sdk.CrawlApi(api_client)
    id = 'id_example' # str | 
    page_id = 'page_id_example' # str | 
    output = 'output_example' # str | 

    try:
        api_response = api_instance.output(id, page_id, output)
        print("The response of CrawlApi->output:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrawlApi->output: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **page_id** | **str**|  | 
 **output** | **str**|  | 

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

# **pages**
> CrawlPagesResponse pages(id, page=page, page_size=page_size)

### Example

* Api Key Authentication (ApiKey):

```python
import allscreenshots_sdk
from allscreenshots_sdk.models.crawl_pages_response import CrawlPagesResponse
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
    api_instance = allscreenshots_sdk.CrawlApi(api_client)
    id = 'id_example' # str | 
    page = 0 # int |  (optional) (default to 0)
    page_size = 100 # int |  (optional) (default to 100)

    try:
        api_response = api_instance.pages(id, page=page, page_size=page_size)
        print("The response of CrawlApi->pages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrawlApi->pages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]

### Return type

[**CrawlPagesResponse**](CrawlPagesResponse.md)

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

