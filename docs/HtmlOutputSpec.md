# HtmlOutputSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clean** | **bool** |  | [optional] [default to True]
**id** | **str** |  | [optional] 
**main_content_only** | **bool** |  | [optional] [default to False]
**type** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.html_output_spec import HtmlOutputSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HtmlOutputSpec from a JSON string
html_output_spec_instance = HtmlOutputSpec.from_json(json)
# print the JSON string representation of the object
print(HtmlOutputSpec.to_json())

# convert the object into a dict
html_output_spec_dict = html_output_spec_instance.to_dict()
# create an instance of HtmlOutputSpec from a dict
html_output_spec_from_dict = HtmlOutputSpec.from_dict(html_output_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


