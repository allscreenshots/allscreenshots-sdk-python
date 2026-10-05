# BrowserHeaderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**origin** | **str** |  | [optional] 
**value** | **str** |  | [optional] [default to '']

## Example

```python
from allscreenshots_sdk.models.browser_header_request import BrowserHeaderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserHeaderRequest from a JSON string
browser_header_request_instance = BrowserHeaderRequest.from_json(json)
# print the JSON string representation of the object
print(BrowserHeaderRequest.to_json())

# convert the object into a dict
browser_header_request_dict = browser_header_request_instance.to_dict()
# create an instance of BrowserHeaderRequest from a dict
browser_header_request_from_dict = BrowserHeaderRequest.from_dict(browser_header_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


