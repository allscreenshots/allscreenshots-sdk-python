# ClickAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**optional** | **bool** |  | [optional] [default to False]
**selector** | **str** |  | 
**timeout** | **int** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.click_action import ClickAction

# TODO update the JSON string below
json = "{}"
# create an instance of ClickAction from a JSON string
click_action_instance = ClickAction.from_json(json)
# print the JSON string representation of the object
print(ClickAction.to_json())

# convert the object into a dict
click_action_dict = click_action_instance.to_dict()
# create an instance of ClickAction from a dict
click_action_from_dict = ClickAction.from_dict(click_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


