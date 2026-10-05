# ScheduleHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executions** | [**List[ScheduleExecutionResponse]**](ScheduleExecutionResponse.md) |  | 
**schedule_id** | **str** |  | 
**total_executions** | **int** |  | 

## Example

```python
from allscreenshots_sdk.models.schedule_history_response import ScheduleHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleHistoryResponse from a JSON string
schedule_history_response_instance = ScheduleHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(ScheduleHistoryResponse.to_json())

# convert the object into a dict
schedule_history_response_dict = schedule_history_response_instance.to_dict()
# create an instance of ScheduleHistoryResponse from a dict
schedule_history_response_from_dict = ScheduleHistoryResponse.from_dict(schedule_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


