# ComposeJobSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_at** | **datetime** |  | [optional] 
**completed_captures** | **int** |  | 
**created_at** | **datetime** |  | 
**failed_captures** | **int** |  | 
**job_id** | **str** |  | 
**layout_type** | **str** |  | 
**progress** | **int** |  | 
**status** | **str** |  | 
**total_captures** | **int** |  | 

## Example

```python
from allscreenshots_sdk.models.compose_job_summary_response import ComposeJobSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComposeJobSummaryResponse from a JSON string
compose_job_summary_response_instance = ComposeJobSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(ComposeJobSummaryResponse.to_json())

# convert the object into a dict
compose_job_summary_response_dict = compose_job_summary_response_instance.to_dict()
# create an instance of ComposeJobSummaryResponse from a dict
compose_job_summary_response_from_dict = ComposeJobSummaryResponse.from_dict(compose_job_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


