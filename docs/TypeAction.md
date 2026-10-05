# TypeAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clear** | **bool** |  | [optional] [default to True]
**optional** | **bool** |  | [optional] [default to False]
**selector** | **str** |  | 
**text** | **str** |  | 
**timeout** | **int** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.type_action import TypeAction

# TODO update the JSON string below
json = "{}"
# create an instance of TypeAction from a JSON string
type_action_instance = TypeAction.from_json(json)
# print the JSON string representation of the object
print(TypeAction.to_json())

# convert the object into a dict
type_action_dict = type_action_instance.to_dict()
# create an instance of TypeAction from a dict
type_action_from_dict = TypeAction.from_dict(type_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


