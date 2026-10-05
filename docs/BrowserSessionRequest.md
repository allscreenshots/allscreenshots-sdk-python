# BrowserSessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookies** | [**List[BrowserCookieRequest]**](BrowserCookieRequest.md) |  | [optional] 
**headers** | [**List[BrowserHeaderRequest]**](BrowserHeaderRequest.md) |  | [optional] 
**storage** | [**List[BrowserStorageOriginRequest]**](BrowserStorageOriginRequest.md) |  | [optional] 

## Example

```python
from allscreenshots_sdk.models.browser_session_request import BrowserSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserSessionRequest from a JSON string
browser_session_request_instance = BrowserSessionRequest.from_json(json)
# print the JSON string representation of the object
print(BrowserSessionRequest.to_json())

# convert the object into a dict
browser_session_request_dict = browser_session_request_instance.to_dict()
# create an instance of BrowserSessionRequest from a dict
browser_session_request_from_dict = BrowserSessionRequest.from_dict(browser_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


