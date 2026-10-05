# JobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**id** | **str** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 
**outputs** | [**Dict[str, OutputInfo]**](OutputInfo.md) |  | [optional] 
**result_url** | **str** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**status** | **str** |  | 
**storage_url** | **str** |  | [optional] 
**url** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.job_response import JobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobResponse from a JSON string
job_response_instance = JobResponse.from_json(json)
# print the JSON string representation of the object
print(JobResponse.to_json())

# convert the object into a dict
job_response_dict = job_response_instance.to_dict()
# create an instance of JobResponse from a dict
job_response_from_dict = JobResponse.from_dict(job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


