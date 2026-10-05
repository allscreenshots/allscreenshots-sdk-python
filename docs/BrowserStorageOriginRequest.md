# BrowserStorageOriginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_storage** | **Dict[str, str]** |  | [optional] 
**origin** | **str** |  | 
**session_storage** | **Dict[str, str]** |  | [optional] 

## Example

```python
from allscreenshots_sdk.models.browser_storage_origin_request import BrowserStorageOriginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserStorageOriginRequest from a JSON string
browser_storage_origin_request_instance = BrowserStorageOriginRequest.from_json(json)
# print the JSON string representation of the object
print(BrowserStorageOriginRequest.to_json())

# convert the object into a dict
browser_storage_origin_request_dict = browser_storage_origin_request_instance.to_dict()
# create an instance of BrowserStorageOriginRequest from a dict
browser_storage_origin_request_from_dict = BrowserStorageOriginRequest.from_dict(browser_storage_origin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


