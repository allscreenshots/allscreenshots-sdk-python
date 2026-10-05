# ScreenshotOutputSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** |  | [optional] [default to 'png']
**full_page** | **bool** |  | [optional] [default to False]
**id** | **str** |  | [optional] 
**quality** | **int** |  | [optional] [default to 80]
**selector** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.screenshot_output_spec import ScreenshotOutputSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ScreenshotOutputSpec from a JSON string
screenshot_output_spec_instance = ScreenshotOutputSpec.from_json(json)
# print the JSON string representation of the object
print(ScreenshotOutputSpec.to_json())

# convert the object into a dict
screenshot_output_spec_dict = screenshot_output_spec_instance.to_dict()
# create an instance of ScreenshotOutputSpec from a dict
screenshot_output_spec_from_dict = ScreenshotOutputSpec.from_dict(screenshot_output_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


