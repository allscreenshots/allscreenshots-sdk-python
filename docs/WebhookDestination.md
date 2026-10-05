# WebhookDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**only_on_change** | **bool** |  | [optional] 
**secret** | **str** |  | [optional] 
**type** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.webhook_destination import WebhookDestination

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDestination from a JSON string
webhook_destination_instance = WebhookDestination.from_json(json)
# print the JSON string representation of the object
print(WebhookDestination.to_json())

# convert the object into a dict
webhook_destination_dict = webhook_destination_instance.to_dict()
# create an instance of WebhookDestination from a dict
webhook_destination_from_dict = WebhookDestination.from_dict(webhook_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


