# ComposeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_async** | **bool** |  | [optional] 
**captures** | [**List[CaptureItem]**](CaptureItem.md) |  | [optional] 
**captures_mode** | **bool** |  | [optional] 
**defaults** | [**CaptureDefaults**](CaptureDefaults.md) |  | [optional] 
**output** | [**ComposeOutputConfig**](ComposeOutputConfig.md) |  | [optional] 
**url** | **str** |  | [optional] 
**variants** | [**List[VariantConfig]**](VariantConfig.md) |  | [optional] 
**variants_mode** | **bool** |  | [optional] 
**webhook_secret** | **str** |  | [optional] 
**webhook_url** | **str** |  | [optional] 

## Example

```python
from allscreenshots_sdk.models.compose_request import ComposeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComposeRequest from a JSON string
compose_request_instance = ComposeRequest.from_json(json)
# print the JSON string representation of the object
print(ComposeRequest.to_json())

# convert the object into a dict
compose_request_dict = compose_request_instance.to_dict()
# create an instance of ComposeRequest from a dict
compose_request_from_dict = ComposeRequest.from_dict(compose_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


