# BorderConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] [default to '#cccccc']
**radius** | **int** |  | [optional] [default to 0]
**width** | **int** |  | [optional] [default to 1]

## Example

```python
from allscreenshots_sdk.models.border_config import BorderConfig

# TODO update the JSON string below
json = "{}"
# create an instance of BorderConfig from a JSON string
border_config_instance = BorderConfig.from_json(json)
# print the JSON string representation of the object
print(BorderConfig.to_json())

# convert the object into a dict
border_config_dict = border_config_instance.to_dict()
# create an instance of BorderConfig from a dict
border_config_from_dict = BorderConfig.from_dict(border_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


