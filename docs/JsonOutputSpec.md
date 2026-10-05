# JsonOutputSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**var_schema** | [**Dict[str, JsonFieldSpec]**](JsonFieldSpec.md) |  | 
**type** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.json_output_spec import JsonOutputSpec

# TODO update the JSON string below
json = "{}"
# create an instance of JsonOutputSpec from a JSON string
json_output_spec_instance = JsonOutputSpec.from_json(json)
# print the JSON string representation of the object
print(JsonOutputSpec.to_json())

# convert the object into a dict
json_output_spec_dict = json_output_spec_instance.to_dict()
# create an instance of JsonOutputSpec from a dict
json_output_spec_from_dict = JsonOutputSpec.from_dict(json_output_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


