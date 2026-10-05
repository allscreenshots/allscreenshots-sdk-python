# LayoutPreviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canvas_height** | **int** |  | 
**canvas_width** | **int** |  | 
**layout** | **str** |  | 
**metadata** | **Dict[str, object]** |  | 
**placements** | [**List[PlacementPreview]**](PlacementPreview.md) |  | 
**resolved_layout** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.layout_preview_response import LayoutPreviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LayoutPreviewResponse from a JSON string
layout_preview_response_instance = LayoutPreviewResponse.from_json(json)
# print the JSON string representation of the object
print(LayoutPreviewResponse.to_json())

# convert the object into a dict
layout_preview_response_dict = layout_preview_response_instance.to_dict()
# create an instance of LayoutPreviewResponse from a dict
layout_preview_response_from_dict = LayoutPreviewResponse.from_dict(layout_preview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


