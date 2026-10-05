# ComposeJobStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_at** | **datetime** |  | [optional] 
**completed_captures** | **int** |  | 
**created_at** | **datetime** |  | 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**job_id** | **str** |  | 
**progress** | **int** |  | 
**result** | [**ComposeResponse**](ComposeResponse.md) |  | [optional] 
**status** | **str** |  | 
**total_captures** | **int** |  | 

## Example

```python
from allscreenshots_sdk.models.compose_job_status_response import ComposeJobStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComposeJobStatusResponse from a JSON string
compose_job_status_response_instance = ComposeJobStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ComposeJobStatusResponse.to_json())

# convert the object into a dict
compose_job_status_response_dict = compose_job_status_response_instance.to_dict()
# create an instance of ComposeJobStatusResponse from a dict
compose_job_status_response_from_dict = ComposeJobStatusResponse.from_dict(compose_job_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


