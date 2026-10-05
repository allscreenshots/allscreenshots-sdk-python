# UpdateScheduleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_on_failure** | **bool** |  | [optional] 
**auto_pause_after_failures** | **int** |  | [optional] 
**destinations** | [**List[DeliveryDestination]**](DeliveryDestination.md) |  | [optional] 
**diff_threshold** | **float** |  | [optional] 
**ends_at** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**only_on_change** | **bool** |  | [optional] 
**options** | [**ScheduleScreenshotOptions**](ScheduleScreenshotOptions.md) |  | [optional] 
**retention_days** | **int** |  | [optional] 
**schedule** | **str** |  | [optional] 
**starts_at** | **datetime** |  | [optional] 
**timezone** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**webhook_secret** | **str** |  | [optional] 
**webhook_url** | **str** |  | [optional] 

## Example

```python
from allscreenshots_sdk.models.update_schedule_request import UpdateScheduleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateScheduleRequest from a JSON string
update_schedule_request_instance = UpdateScheduleRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateScheduleRequest.to_json())

# convert the object into a dict
update_schedule_request_dict = update_schedule_request_instance.to_dict()
# create an instance of UpdateScheduleRequest from a dict
update_schedule_request_from_dict = UpdateScheduleRequest.from_dict(update_schedule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


