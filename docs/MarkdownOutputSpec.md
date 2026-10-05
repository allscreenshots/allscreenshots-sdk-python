# MarkdownOutputSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**main_content_only** | **bool** |  | [optional] [default to True]
**type** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.markdown_output_spec import MarkdownOutputSpec

# TODO update the JSON string below
json = "{}"
# create an instance of MarkdownOutputSpec from a JSON string
markdown_output_spec_instance = MarkdownOutputSpec.from_json(json)
# print the JSON string representation of the object
print(MarkdownOutputSpec.to_json())

# convert the object into a dict
markdown_output_spec_dict = markdown_output_spec_instance.to_dict()
# create an instance of MarkdownOutputSpec from a dict
markdown_output_spec_from_dict = MarkdownOutputSpec.from_dict(markdown_output_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


