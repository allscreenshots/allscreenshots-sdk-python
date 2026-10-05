# CaptureInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **int** |  | 
**id** | **str** |  | 
**label** | **str** |  | [optional] 
**original_height** | **int** |  | 
**original_width** | **int** |  | 
**url** | **str** |  | 
**width** | **int** |  | 
**x** | **int** |  | 
**y** | **int** |  | 

## Example

```python
from allscreenshots_sdk.models.capture_info import CaptureInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CaptureInfo from a JSON string
capture_info_instance = CaptureInfo.from_json(json)
# print the JSON string representation of the object
print(CaptureInfo.to_json())

# convert the object into a dict
capture_info_dict = capture_info_instance.to_dict()
# create an instance of CaptureInfo from a dict
capture_info_from_dict = CaptureInfo.from_dict(capture_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


