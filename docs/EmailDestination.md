# EmailDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**only_on_change** | **bool** |  | [optional] 
**subject** | **str** |  | [optional] 
**to** | **List[str]** |  | 
**type** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.email_destination import EmailDestination

# TODO update the JSON string below
json = "{}"
# create an instance of EmailDestination from a JSON string
email_destination_instance = EmailDestination.from_json(json)
# print the JSON string representation of the object
print(EmailDestination.to_json())

# convert the object into a dict
email_destination_dict = email_destination_instance.to_dict()
# create an instance of EmailDestination from a dict
email_destination_from_dict = EmailDestination.from_dict(email_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


