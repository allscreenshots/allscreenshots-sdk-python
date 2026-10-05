# MultiOutputResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outputs** | **Dict[str, object]** |  | 
**render_time_ms** | **int** |  | 
**url** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.multi_output_response import MultiOutputResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MultiOutputResponse from a JSON string
multi_output_response_instance = MultiOutputResponse.from_json(json)
# print the JSON string representation of the object
print(MultiOutputResponse.to_json())

# convert the object into a dict
multi_output_response_dict = multi_output_response_instance.to_dict()
# create an instance of MultiOutputResponse from a dict
multi_output_response_from_dict = MultiOutputResponse.from_dict(multi_output_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


