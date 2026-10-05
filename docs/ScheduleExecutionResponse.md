# ScheduleExecutionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed** | **bool** |  | [optional] 
**deliveries** | **List[Dict[str, object]]** |  | [optional] 
**diff_score** | **float** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**executed_at** | **datetime** |  | 
**expires_at** | **datetime** |  | [optional] 
**file_size** | **int** |  | [optional] 
**id** | **str** |  | 
**outputs** | **Dict[str, object]** |  | [optional] 
**render_time_ms** | **int** |  | [optional] 
**result_url** | **str** |  | [optional] 
**run_id** | **str** |  | [optional] 
**status** | **str** |  | 
**storage_url** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from allscreenshots_sdk.models.schedule_execution_response import ScheduleExecutionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleExecutionResponse from a JSON string
schedule_execution_response_instance = ScheduleExecutionResponse.from_json(json)
# print the JSON string representation of the object
print(ScheduleExecutionResponse.to_json())

# convert the object into a dict
schedule_execution_response_dict = schedule_execution_response_instance.to_dict()
# create an instance of ScheduleExecutionResponse from a dict
schedule_execution_response_from_dict = ScheduleExecutionResponse.from_dict(schedule_execution_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


