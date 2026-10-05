# HoverAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**optional** | **bool** |  | [optional] [default to False]
**selector** | **str** |  | 
**timeout** | **int** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.hover_action import HoverAction

# TODO update the JSON string below
json = "{}"
# create an instance of HoverAction from a JSON string
hover_action_instance = HoverAction.from_json(json)
# print the JSON string representation of the object
print(HoverAction.to_json())

# convert the object into a dict
hover_action_dict = hover_action_instance.to_dict()
# create an instance of HoverAction from a dict
hover_action_from_dict = HoverAction.from_dict(hover_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


