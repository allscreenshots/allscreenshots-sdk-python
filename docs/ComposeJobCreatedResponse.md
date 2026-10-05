# ComposeJobCreatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**job_id** | **str** |  | 
**status** | **str** |  | 
**status_url** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.compose_job_created_response import ComposeJobCreatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComposeJobCreatedResponse from a JSON string
compose_job_created_response_instance = ComposeJobCreatedResponse.from_json(json)
# print the JSON string representation of the object
print(ComposeJobCreatedResponse.to_json())

# convert the object into a dict
compose_job_created_response_dict = compose_job_created_response_instance.to_dict()
# create an instance of ComposeJobCreatedResponse from a dict
compose_job_created_response_from_dict = ComposeJobCreatedResponse.from_dict(compose_job_created_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


