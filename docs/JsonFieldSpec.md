# JsonFieldSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** |  | [optional] 
**multiple** | **bool** |  | [optional] [default to False]
**selector** | **str** |  | 
**type** | **str** |  | [optional] [default to 'text']

## Example

```python
from allscreenshots_sdk.models.json_field_spec import JsonFieldSpec

# TODO update the JSON string below
json = "{}"
# create an instance of JsonFieldSpec from a JSON string
json_field_spec_instance = JsonFieldSpec.from_json(json)
# print the JSON string representation of the object
print(JsonFieldSpec.to_json())

# convert the object into a dict
json_field_spec_dict = json_field_spec_instance.to_dict()
# create an instance of JsonFieldSpec from a dict
json_field_spec_from_dict = JsonFieldSpec.from_dict(json_field_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


