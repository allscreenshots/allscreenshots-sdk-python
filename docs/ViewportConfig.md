# ViewportConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_scale_factor** | **int** |  | [optional] [default to 1]
**height** | **int** |  | [optional] [default to 1080]
**width** | **int** |  | [optional] [default to 1920]

## Example

```python
from allscreenshots_sdk.models.viewport_config import ViewportConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ViewportConfig from a JSON string
viewport_config_instance = ViewportConfig.from_json(json)
# print the JSON string representation of the object
print(ViewportConfig.to_json())

# convert the object into a dict
viewport_config_dict = viewport_config_instance.to_dict()
# create an instance of ViewportConfig from a dict
viewport_config_from_dict = ViewportConfig.from_dict(viewport_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


