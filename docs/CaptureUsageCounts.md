# CaptureUsageCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidth_bytes** | **int** |  | 
**screenshots_count** | **int** |  | 

## Example

```python
from allscreenshots_sdk.models.capture_usage_counts import CaptureUsageCounts

# TODO update the JSON string below
json = "{}"
# create an instance of CaptureUsageCounts from a JSON string
capture_usage_counts_instance = CaptureUsageCounts.from_json(json)
# print the JSON string representation of the object
print(CaptureUsageCounts.to_json())

# convert the object into a dict
capture_usage_counts_dict = capture_usage_counts_instance.to_dict()
# create an instance of CaptureUsageCounts from a dict
capture_usage_counts_from_dict = CaptureUsageCounts.from_dict(capture_usage_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


