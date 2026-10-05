# QuotaDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | 
**percent_used** | **int** |  | 
**remaining** | **int** |  | 
**used** | **int** |  | 

## Example

```python
from allscreenshots_sdk.models.quota_detail_response import QuotaDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaDetailResponse from a JSON string
quota_detail_response_instance = QuotaDetailResponse.from_json(json)
# print the JSON string representation of the object
print(QuotaDetailResponse.to_json())

# convert the object into a dict
quota_detail_response_dict = quota_detail_response_instance.to_dict()
# create an instance of QuotaDetailResponse from a dict
quota_detail_response_from_dict = QuotaDetailResponse.from_dict(quota_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


