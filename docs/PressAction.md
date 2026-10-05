# PressAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**optional** | **bool** |  | [optional] [default to False]
**selector** | **str** |  | [optional] 
**timeout** | **int** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.press_action import PressAction

# TODO update the JSON string below
json = "{}"
# create an instance of PressAction from a JSON string
press_action_instance = PressAction.from_json(json)
# print the JSON string representation of the object
print(PressAction.to_json())

# convert the object into a dict
press_action_dict = press_action_instance.to_dict()
# create an instance of PressAction from a dict
press_action_from_dict = PressAction.from_dict(press_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


