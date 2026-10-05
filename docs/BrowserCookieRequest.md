# BrowserCookieRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**expires** | **float** |  | [optional] 
**http_only** | **bool** |  | [optional] 
**name** | **str** |  | 
**path** | **str** |  | [optional] [default to '/']
**same_site** | **str** |  | [optional] 
**secure** | **bool** |  | [optional] 
**value** | **str** |  | [optional] [default to '']

## Example

```python
from allscreenshots_sdk.models.browser_cookie_request import BrowserCookieRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserCookieRequest from a JSON string
browser_cookie_request_instance = BrowserCookieRequest.from_json(json)
# print the JSON string representation of the object
print(BrowserCookieRequest.to_json())

# convert the object into a dict
browser_cookie_request_dict = browser_cookie_request_instance.to_dict()
# create an instance of BrowserCookieRequest from a dict
browser_cookie_request_from_dict = BrowserCookieRequest.from_dict(browser_cookie_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


