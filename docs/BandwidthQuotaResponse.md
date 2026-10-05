# BandwidthQuotaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit_bytes** | **int** |  | 
**limit_formatted** | **str** |  | 
**percent_used** | **int** |  | 
**remaining_bytes** | **int** |  | 
**remaining_formatted** | **str** |  | 
**used_bytes** | **int** |  | 
**used_formatted** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.bandwidth_quota_response import BandwidthQuotaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BandwidthQuotaResponse from a JSON string
bandwidth_quota_response_instance = BandwidthQuotaResponse.from_json(json)
# print the JSON string representation of the object
print(BandwidthQuotaResponse.to_json())

# convert the object into a dict
bandwidth_quota_response_dict = bandwidth_quota_response_instance.to_dict()
# create an instance of BandwidthQuotaResponse from a dict
bandwidth_quota_response_from_dict = BandwidthQuotaResponse.from_dict(bandwidth_quota_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


