# ComposeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** |  | 
**file_size** | **int** |  | 
**format** | **str** |  | 
**height** | **int** |  | 
**layout** | **str** |  | 
**metadata** | [**ComposeMetadata**](ComposeMetadata.md) |  | 
**render_time_ms** | **int** |  | 
**storage_url** | **str** |  | [optional] 
**url** | **str** |  | 
**width** | **int** |  | 

## Example

```python
from allscreenshots_sdk.models.compose_response import ComposeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComposeResponse from a JSON string
compose_response_instance = ComposeResponse.from_json(json)
# print the JSON string representation of the object
print(ComposeResponse.to_json())

# convert the object into a dict
compose_response_dict = compose_response_instance.to_dict()
# create an instance of ComposeResponse from a dict
compose_response_from_dict = ComposeResponse.from_dict(compose_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


