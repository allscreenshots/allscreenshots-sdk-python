# CaptureDefaults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[PageAction]**](PageAction.md) |  | [optional] 
**block_ads** | **bool** |  | [optional] [default to True]
**block_cookie_banners** | **bool** |  | [optional] [default to True]
**block_level** | **str** |  | [optional] [default to 'none']
**block_popups** | **bool** |  | [optional] [default to True]
**custom_css** | **str** |  | [optional] 
**dark_mode** | **bool** |  | [optional] [default to False]
**delay** | **int** |  | [optional] [default to 0]
**device** | **str** |  | [optional] 
**format** | **str** |  | [optional] [default to 'png']
**full_page** | **bool** |  | [optional] [default to False]
**hide_selectors** | **List[str]** |  | [optional] 
**quality** | **int** |  | [optional] [default to 80]
**stealth_mode** | **bool** |  | [optional] [default to False]
**timeout** | **int** |  | [optional] [default to 30000]
**viewport** | [**ViewportConfig**](ViewportConfig.md) |  | [optional] 
**wait_for** | **str** |  | [optional] 
**wait_until** | **str** |  | [optional] [default to 'domcontentloaded']

## Example

```python
from allscreenshots_sdk.models.capture_defaults import CaptureDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of CaptureDefaults from a JSON string
capture_defaults_instance = CaptureDefaults.from_json(json)
# print the JSON string representation of the object
print(CaptureDefaults.to_json())

# convert the object into a dict
capture_defaults_dict = capture_defaults_instance.to_dict()
# create an instance of CaptureDefaults from a dict
capture_defaults_from_dict = CaptureDefaults.from_dict(capture_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


