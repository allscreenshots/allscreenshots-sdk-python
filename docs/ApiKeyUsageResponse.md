# ApiKeyUsageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[ApiKeyUsageDetail]**](ApiKeyUsageDetail.md) |  | 
**period_end** | **str** |  | 
**period_start** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.api_key_usage_response import ApiKeyUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyUsageResponse from a JSON string
api_key_usage_response_instance = ApiKeyUsageResponse.from_json(json)
# print the JSON string representation of the object
print(ApiKeyUsageResponse.to_json())

# convert the object into a dict
api_key_usage_response_dict = api_key_usage_response_instance.to_dict()
# create an instance of ApiKeyUsageResponse from a dict
api_key_usage_response_from_dict = ApiKeyUsageResponse.from_dict(api_key_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


