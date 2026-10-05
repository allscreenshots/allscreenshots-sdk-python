# BulkUrlOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[PageAction]**](PageAction.md) |  | [optional] 
**block_ads** | **bool** |  | [optional] 
**block_cookie_banners** | **bool** |  | [optional] 
**block_level** | **str** |  | [optional] 
**block_popups** | **bool** |  | [optional] 
**custom_css** | **str** |  | [optional] 
**dark_mode** | **bool** |  | [optional] 
**delay** | **int** |  | [optional] 
**device** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**full_page** | **bool** |  | [optional] 
**outputs** | [**List[OutputSpec]**](OutputSpec.md) |  | [optional] 
**quality** | **int** |  | [optional] 
**stealth_mode** | **bool** |  | [optional] 
**viewport** | [**ViewportConfig**](ViewportConfig.md) |  | [optional] 
**wait_for** | **str** |  | [optional] 
**wait_until** | **str** |  | [optional] 

## Example

```python
from allscreenshots_sdk.models.bulk_url_options import BulkUrlOptions

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUrlOptions from a JSON string
bulk_url_options_instance = BulkUrlOptions.from_json(json)
# print the JSON string representation of the object
print(BulkUrlOptions.to_json())

# convert the object into a dict
bulk_url_options_dict = bulk_url_options_instance.to_dict()
# create an instance of BulkUrlOptions from a dict
bulk_url_options_from_dict = BulkUrlOptions.from_dict(bulk_url_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


