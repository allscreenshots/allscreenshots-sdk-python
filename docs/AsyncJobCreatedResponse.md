# AsyncJobCreatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**status** | **str** |  | 
**status_url** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.async_job_created_response import AsyncJobCreatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncJobCreatedResponse from a JSON string
async_job_created_response_instance = AsyncJobCreatedResponse.from_json(json)
# print the JSON string representation of the object
print(AsyncJobCreatedResponse.to_json())

# convert the object into a dict
async_job_created_response_dict = async_job_created_response_instance.to_dict()
# create an instance of AsyncJobCreatedResponse from a dict
async_job_created_response_from_dict = AsyncJobCreatedResponse.from_dict(async_job_created_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


