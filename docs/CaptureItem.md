# CaptureItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dark_mode** | **bool** |  | [optional] 
**delay** | **int** |  | [optional] 
**device** | **str** |  | [optional] 
**full_page** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**url** | **str** |  | 
**viewport** | [**ViewportConfig**](ViewportConfig.md) |  | [optional] 

## Example

```python
from allscreenshots_sdk.models.capture_item import CaptureItem

# TODO update the JSON string below
json = "{}"
# create an instance of CaptureItem from a JSON string
capture_item_instance = CaptureItem.from_json(json)
# print the JSON string representation of the object
print(CaptureItem.to_json())

# convert the object into a dict
capture_item_dict = capture_item_instance.to_dict()
# create an instance of CaptureItem from a dict
capture_item_from_dict = CaptureItem.from_dict(capture_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


