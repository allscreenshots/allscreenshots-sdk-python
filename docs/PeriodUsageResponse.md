# PeriodUsageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidth_bytes** | **int** |  | 
**bandwidth_formatted** | **str** |  | 
**period_end** | **str** |  | 
**period_start** | **str** |  | 
**screenshots_count** | **int** |  | 

## Example

```python
from allscreenshots_sdk.models.period_usage_response import PeriodUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodUsageResponse from a JSON string
period_usage_response_instance = PeriodUsageResponse.from_json(json)
# print the JSON string representation of the object
print(PeriodUsageResponse.to_json())

# convert the object into a dict
period_usage_response_dict = period_usage_response_instance.to_dict()
# create an instance of PeriodUsageResponse from a dict
period_usage_response_from_dict = PeriodUsageResponse.from_dict(period_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


