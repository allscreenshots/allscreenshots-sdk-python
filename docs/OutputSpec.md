# OutputSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** |  | [optional] 
**full_page** | **bool** |  | [optional] [default to False]
**id** | **str** |  | [optional] 
**quality** | **int** |  | [optional] [default to 80]
**selector** | **str** |  | [optional] 
**type** | **str** |  | 
**landscape** | **bool** |  | [optional] [default to False]
**print_background** | **bool** |  | [optional] [default to True]
**clean** | **bool** |  | [optional] [default to True]
**main_content_only** | **bool** |  | [optional] [default to True]
**var_schema** | [**Dict[str, JsonFieldSpec]**](JsonFieldSpec.md) |  | 

## Example

```python
from allscreenshots_sdk.models.output_spec import OutputSpec

# TODO update the JSON string below
json = "{}"
# create an instance of OutputSpec from a JSON string
output_spec_instance = OutputSpec.from_json(json)
# print the JSON string representation of the object
print(OutputSpec.to_json())

# convert the object into a dict
output_spec_dict = output_spec_instance.to_dict()
# create an instance of OutputSpec from a dict
output_spec_from_dict = OutputSpec.from_dict(output_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


