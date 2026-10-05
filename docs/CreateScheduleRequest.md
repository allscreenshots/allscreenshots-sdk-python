# CreateScheduleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_on_failure** | **bool** |  | [optional] [default to False]
**auto_pause_after_failures** | **int** |  | [optional] 
**destinations** | [**List[DeliveryDestination]**](DeliveryDestination.md) |  | [optional] 
**diff_threshold** | **float** |  | [optional] 
**ends_at** | **datetime** |  | [optional] 
**name** | **str** |  | 
**only_on_change** | **bool** |  | [optional] [default to False]
**options** | [**ScheduleScreenshotOptions**](ScheduleScreenshotOptions.md) |  | [optional] 
**retention_days** | **int** |  | [optional] [default to 30]
**schedule** | **str** |  | 
**starts_at** | **datetime** |  | [optional] 
**timezone** | **str** |  | [optional] [default to 'UTC']
**url** | **str** |  | 
**webhook_secret** | **str** |  | [optional] 
**webhook_url** | **str** |  | [optional] 

## Example

```python
from allscreenshots_sdk.models.create_schedule_request import CreateScheduleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScheduleRequest from a JSON string
create_schedule_request_instance = CreateScheduleRequest.from_json(json)
# print the JSON string representation of the object
print(CreateScheduleRequest.to_json())

# convert the object into a dict
create_schedule_request_dict = create_schedule_request_instance.to_dict()
# create an instance of CreateScheduleRequest from a dict
create_schedule_request_from_dict = CreateScheduleRequest.from_dict(create_schedule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


