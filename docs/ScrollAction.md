# ScrollAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**optional** | **bool** |  | [optional] [default to False]
**selector** | **str** |  | [optional] 
**timeout** | **int** |  | [optional] 
**to_bottom** | **bool** |  | [optional] [default to False]
**type** | **str** |  | 
**y** | **int** |  | [optional] 

## Example

```python
from allscreenshots_sdk.models.scroll_action import ScrollAction

# TODO update the JSON string below
json = "{}"
# create an instance of ScrollAction from a JSON string
scroll_action_instance = ScrollAction.from_json(json)
# print the JSON string representation of the object
print(ScrollAction.to_json())

# convert the object into a dict
scroll_action_dict = scroll_action_instance.to_dict()
# create an instance of ScrollAction from a dict
scroll_action_from_dict = ScrollAction.from_dict(scroll_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


