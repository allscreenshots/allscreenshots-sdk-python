# ApiKeyUsageDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_id** | **str** |  | [optional] 
**current_period** | [**CaptureUsageCounts**](CaptureUsageCounts.md) |  | 
**key_prefix** | **str** |  | [optional] 
**name** | **str** |  | 
**totals** | [**CaptureUsageCounts**](CaptureUsageCounts.md) |  | 

## Example

```python
from allscreenshots_sdk.models.api_key_usage_detail import ApiKeyUsageDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyUsageDetail from a JSON string
api_key_usage_detail_instance = ApiKeyUsageDetail.from_json(json)
# print the JSON string representation of the object
print(ApiKeyUsageDetail.to_json())

# convert the object into a dict
api_key_usage_detail_dict = api_key_usage_detail_instance.to_dict()
# create an instance of ApiKeyUsageDetail from a dict
api_key_usage_detail_from_dict = ApiKeyUsageDetail.from_dict(api_key_usage_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


