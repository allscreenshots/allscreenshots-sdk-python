# BulkDefaults


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
**outputs** | [**List[OutputSpec]**](OutputSpec.md) |  | [optional] 
**quality** | **int** |  | [optional] [default to 80]
**stealth_mode** | **bool** |  | [optional] [default to False]
**timeout** | **int** |  | [optional] [default to 30000]
**viewport** | [**ViewportConfig**](ViewportConfig.md) |  | [optional] 
**wait_for** | **str** |  | [optional] 
**wait_until** | **str** |  | [optional] [default to 'domcontentloaded']

## Example

```python
from allscreenshots_sdk.models.bulk_defaults import BulkDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDefaults from a JSON string
bulk_defaults_instance = BulkDefaults.from_json(json)
# print the JSON string representation of the object
print(BulkDefaults.to_json())

# convert the object into a dict
bulk_defaults_dict = bulk_defaults_instance.to_dict()
# create an instance of BulkDefaults from a dict
bulk_defaults_from_dict = BulkDefaults.from_dict(bulk_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


