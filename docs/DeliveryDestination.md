# DeliveryDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**only_on_change** | **bool** |  | [optional] 
**subject** | **str** |  | [optional] 
**to** | **List[str]** |  | 
**type** | **str** |  | 
**secret** | **str** |  | [optional] 
**url** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.delivery_destination import DeliveryDestination

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryDestination from a JSON string
delivery_destination_instance = DeliveryDestination.from_json(json)
# print the JSON string representation of the object
print(DeliveryDestination.to_json())

# convert the object into a dict
delivery_destination_dict = delivery_destination_instance.to_dict()
# create an instance of DeliveryDestination from a dict
delivery_destination_from_dict = DeliveryDestination.from_dict(delivery_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


