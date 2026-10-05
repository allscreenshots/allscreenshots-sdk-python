# OutputInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  | 
**result_url** | **str** |  | [optional] 
**size** | **int** |  | 
**storage_url** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.output_info import OutputInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OutputInfo from a JSON string
output_info_instance = OutputInfo.from_json(json)
# print the JSON string representation of the object
print(OutputInfo.to_json())

# convert the object into a dict
output_info_dict = output_info_instance.to_dict()
# create an instance of OutputInfo from a dict
output_info_from_dict = OutputInfo.from_dict(output_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


