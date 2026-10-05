# QuotaStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidth** | [**BandwidthQuotaResponse**](BandwidthQuotaResponse.md) |  | 
**period_ends** | **str** |  | [optional] 
**screenshots** | [**QuotaDetailResponse**](QuotaDetailResponse.md) |  | 
**tier** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.quota_status_response import QuotaStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaStatusResponse from a JSON string
quota_status_response_instance = QuotaStatusResponse.from_json(json)
# print the JSON string representation of the object
print(QuotaStatusResponse.to_json())

# convert the object into a dict
quota_status_response_dict = quota_status_response_instance.to_dict()
# create an instance of QuotaStatusResponse from a dict
quota_status_response_from_dict = QuotaStatusResponse.from_dict(quota_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


