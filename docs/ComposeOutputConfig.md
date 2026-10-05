# ComposeOutputConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alignment** | **str** |  | [optional] [default to 'center']
**background** | **str** |  | [optional] [default to '#ffffff']
**border** | [**BorderConfig**](BorderConfig.md) |  | [optional] 
**columns** | **int** |  | [optional] 
**format** | **str** |  | [optional] [default to 'png']
**labels** | [**LabelConfig**](LabelConfig.md) |  | [optional] 
**layout** | **str** |  | [optional] [default to 'AUTO']
**max_height** | **int** |  | [optional] 
**max_width** | **int** |  | [optional] 
**padding** | **int** |  | [optional] [default to 0]
**quality** | **int** |  | [optional] [default to 90]
**shadow** | [**ShadowConfig**](ShadowConfig.md) |  | [optional] 
**spacing** | **int** |  | [optional] [default to 10]
**thumbnail_width** | **int** |  | [optional] 

## Example

```python
from allscreenshots_sdk.models.compose_output_config import ComposeOutputConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ComposeOutputConfig from a JSON string
compose_output_config_instance = ComposeOutputConfig.from_json(json)
# print the JSON string representation of the object
print(ComposeOutputConfig.to_json())

# convert the object into a dict
compose_output_config_dict = compose_output_config_instance.to_dict()
# create an instance of ComposeOutputConfig from a dict
compose_output_config_from_dict = ComposeOutputConfig.from_dict(compose_output_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


