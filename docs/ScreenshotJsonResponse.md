# ScreenshotJsonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cached** | **bool** |  | [optional] [default to False]
**content_type** | **str** |  | 
**data** | **str** |  | [optional] 
**encoding** | **str** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**format** | **str** |  | 
**height** | **int** |  | [optional] 
**render_time_ms** | **int** |  | 
**result_url** | **str** |  | [optional] 
**size** | **int** |  | 
**storage_url** | **str** |  | [optional] 
**url** | **str** |  | 
**width** | **int** |  | 

## Example

```python
from allscreenshots_sdk.models.screenshot_json_response import ScreenshotJsonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScreenshotJsonResponse from a JSON string
screenshot_json_response_instance = ScreenshotJsonResponse.from_json(json)
# print the JSON string representation of the object
print(ScreenshotJsonResponse.to_json())

# convert the object into a dict
screenshot_json_response_dict = screenshot_json_response_instance.to_dict()
# create an instance of ScreenshotJsonResponse from a dict
screenshot_json_response_from_dict = ScreenshotJsonResponse.from_dict(screenshot_json_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


