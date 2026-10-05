# LabelConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background** | **str** |  | [optional] [default to '#ffffff']
**font_color** | **str** |  | [optional] [default to '#333333']
**font_size** | **int** |  | [optional] [default to 14]
**padding** | **int** |  | [optional] [default to 8]
**position** | **str** |  | [optional] [default to 'bottom']
**show** | **bool** |  | [optional] [default to True]

## Example

```python
from allscreenshots_sdk.models.label_config import LabelConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LabelConfig from a JSON string
label_config_instance = LabelConfig.from_json(json)
# print the JSON string representation of the object
print(LabelConfig.to_json())

# convert the object into a dict
label_config_dict = label_config_instance.to_dict()
# create an instance of LabelConfig from a dict
label_config_from_dict = LabelConfig.from_dict(label_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


