# VariantConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_css** | **str** |  | [optional] 
**dark_mode** | **bool** |  | [optional] 
**delay** | **int** |  | [optional] 
**device** | **str** |  | [optional] 
**full_page** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**viewport** | [**ViewportConfig**](ViewportConfig.md) |  | [optional] 

## Example

```python
from allscreenshots_sdk.models.variant_config import VariantConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VariantConfig from a JSON string
variant_config_instance = VariantConfig.from_json(json)
# print the JSON string representation of the object
print(VariantConfig.to_json())

# convert the object into a dict
variant_config_dict = variant_config_instance.to_dict()
# create an instance of VariantConfig from a dict
variant_config_from_dict = VariantConfig.from_dict(variant_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


