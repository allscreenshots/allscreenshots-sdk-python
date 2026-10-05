# ScreenshotRequest


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
**response_type** | **str** |  | [optional] [default to 'BINARY']
**scroll_interval** | **int** |  | [optional] [default to 150]
**selector** | **str** |  | [optional] 
**session** | [**BrowserSessionRequest**](BrowserSessionRequest.md) |  | [optional] 
**stealth_mode** | **bool** |  | [optional] [default to False]
**timeout** | **int** |  | [optional] [default to 30000]
**url** | **str** |  | 
**viewport** | [**ViewportConfig**](ViewportConfig.md) |  | [optional] 
**wait_for** | **str** |  | [optional] 
**wait_until** | **str** |  | [optional] [default to 'domcontentloaded']
**webhook_secret** | **str** |  | [optional] 
**webhook_url** | **str** |  | [optional] 

## Example

```python
from allscreenshots_sdk.models.screenshot_request import ScreenshotRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScreenshotRequest from a JSON string
screenshot_request_instance = ScreenshotRequest.from_json(json)
# print the JSON string representation of the object
print(ScreenshotRequest.to_json())

# convert the object into a dict
screenshot_request_dict = screenshot_request_instance.to_dict()
# create an instance of ScreenshotRequest from a dict
screenshot_request_from_dict = ScreenshotRequest.from_dict(screenshot_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


