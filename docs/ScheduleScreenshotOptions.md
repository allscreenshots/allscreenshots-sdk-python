# ScheduleScreenshotOptions


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
**freeze_fixed** | **bool** |  | [optional] [default to True]
**full_page** | **bool** |  | [optional] [default to False]
**full_page_mode** | **str** |  | [optional] [default to 'stitch']
**hide_selectors** | **List[str]** |  | [optional] 
**max_height** | **int** |  | [optional] 
**max_sections** | **int** |  | [optional] [default to 50]
**outputs** | [**List[OutputSpec]**](OutputSpec.md) |  | [optional] 
**quality** | **int** |  | [optional] [default to 80]
**scroll_interval** | **int** |  | [optional] [default to 150]
**selector** | **str** |  | [optional] 
**stealth_mode** | **bool** |  | [optional] [default to False]
**timeout** | **int** |  | [optional] [default to 30000]
**viewport** | [**ViewportConfig**](ViewportConfig.md) |  | [optional] 
**wait_for** | **str** |  | [optional] 
**wait_until** | **str** |  | [optional] [default to 'domcontentloaded']

## Example

```python
from allscreenshots_sdk.models.schedule_screenshot_options import ScheduleScreenshotOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleScreenshotOptions from a JSON string
schedule_screenshot_options_instance = ScheduleScreenshotOptions.from_json(json)
# print the JSON string representation of the object
print(ScheduleScreenshotOptions.to_json())

# convert the object into a dict
schedule_screenshot_options_dict = schedule_screenshot_options_instance.to_dict()
# create an instance of ScheduleScreenshotOptions from a dict
schedule_screenshot_options_from_dict = ScheduleScreenshotOptions.from_dict(schedule_screenshot_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


