# PlacementPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **int** |  | 
**index** | **int** |  | 
**label** | **str** |  | [optional] 
**width** | **int** |  | 
**x** | **int** |  | 
**y** | **int** |  | 

## Example

```python
from allscreenshots_sdk.models.placement_preview import PlacementPreview

# TODO update the JSON string below
json = "{}"
# create an instance of PlacementPreview from a JSON string
placement_preview_instance = PlacementPreview.from_json(json)
# print the JSON string representation of the object
print(PlacementPreview.to_json())

# convert the object into a dict
placement_preview_dict = placement_preview_instance.to_dict()
# create an instance of PlacementPreview from a dict
placement_preview_from_dict = PlacementPreview.from_dict(placement_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


