# PdfOutputSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**landscape** | **bool** |  | [optional] [default to False]
**print_background** | **bool** |  | [optional] [default to True]
**type** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.pdf_output_spec import PdfOutputSpec

# TODO update the JSON string below
json = "{}"
# create an instance of PdfOutputSpec from a JSON string
pdf_output_spec_instance = PdfOutputSpec.from_json(json)
# print the JSON string representation of the object
print(PdfOutputSpec.to_json())

# convert the object into a dict
pdf_output_spec_dict = pdf_output_spec_instance.to_dict()
# create an instance of PdfOutputSpec from a dict
pdf_output_spec_from_dict = PdfOutputSpec.from_dict(pdf_output_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


