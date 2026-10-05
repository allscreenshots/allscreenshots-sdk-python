# ScheduleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_on_failure** | **bool** |  | 
**auto_pause_after_failures** | **int** |  | [optional] 
**consecutive_failures** | **int** |  | 
**created_at** | **datetime** |  | 
**destinations** | [**List[DeliveryDestination]**](DeliveryDestination.md) |  | [optional] 
**diff_threshold** | **float** |  | [optional] 
**ends_at** | **datetime** |  | [optional] 
**execution_count** | **int** |  | 
**failure_count** | **int** |  | 
**id** | **str** |  | 
**last_executed_at** | **datetime** |  | [optional] 
**name** | **str** |  | 
**next_execution_at** | **datetime** |  | [optional] 
**only_on_change** | **bool** |  | 
**options** | **Dict[str, object]** |  | [optional] 
**retention_days** | **int** |  | 
**schedule** | **str** |  | 
**schedule_description** | **str** |  | 
**starts_at** | **datetime** |  | [optional] 
**status** | **str** |  | 
**success_count** | **int** |  | 
**timezone** | **str** |  | 
**updated_at** | **datetime** |  | 
**url** | **str** |  | 
**webhook_url** | **str** |  | [optional] 

## Example

```python
from allscreenshots_sdk.models.schedule_response import ScheduleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleResponse from a JSON string
schedule_response_instance = ScheduleResponse.from_json(json)
# print the JSON string representation of the object
print(ScheduleResponse.to_json())

# convert the object into a dict
schedule_response_dict = schedule_response_instance.to_dict()
# create an instance of ScheduleResponse from a dict
schedule_response_from_dict = ScheduleResponse.from_dict(schedule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


