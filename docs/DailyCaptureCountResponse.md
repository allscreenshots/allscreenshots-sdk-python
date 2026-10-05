# DailyCaptureCountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**var_date** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.daily_capture_count_response import DailyCaptureCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DailyCaptureCountResponse from a JSON string
daily_capture_count_response_instance = DailyCaptureCountResponse.from_json(json)
# print the JSON string representation of the object
print(DailyCaptureCountResponse.to_json())

# convert the object into a dict
daily_capture_count_response_dict = daily_capture_count_response_instance.to_dict()
# create an instance of DailyCaptureCountResponse from a dict
daily_capture_count_response_from_dict = DailyCaptureCountResponse.from_dict(daily_capture_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


