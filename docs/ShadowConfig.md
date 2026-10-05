# ShadowConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blur** | **int** |  | [optional] [default to 10]
**color** | **str** |  | [optional] [default to 'rgba(0,0,0,0.2)']
**enabled** | **bool** |  | [optional] [default to True]
**offset_x** | **int** |  | [optional] [default to 0]
**offset_y** | **int** |  | [optional] [default to 4]

## Example

```python
from allscreenshots_sdk.models.shadow_config import ShadowConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ShadowConfig from a JSON string
shadow_config_instance = ShadowConfig.from_json(json)
# print the JSON string representation of the object
print(ShadowConfig.to_json())

# convert the object into a dict
shadow_config_dict = shadow_config_instance.to_dict()
# create an instance of ShadowConfig from a dict
shadow_config_from_dict = ShadowConfig.from_dict(shadow_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


