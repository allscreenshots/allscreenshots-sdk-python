# UsageOrganizationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.usage_organization_response import UsageOrganizationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsageOrganizationResponse from a JSON string
usage_organization_response_instance = UsageOrganizationResponse.from_json(json)
# print the JSON string representation of the object
print(UsageOrganizationResponse.to_json())

# convert the object into a dict
usage_organization_response_dict = usage_organization_response_instance.to_dict()
# create an instance of UsageOrganizationResponse from a dict
usage_organization_response_from_dict = UsageOrganizationResponse.from_dict(usage_organization_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


