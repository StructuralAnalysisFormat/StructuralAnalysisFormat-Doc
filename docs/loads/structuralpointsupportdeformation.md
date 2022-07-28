# StructuralPointSupportDeformation

```{warning}
New object under construction.
```

**Imposed deformation of a point support**

Displacement or rotation can be imposed on a point support. Displacement can be set in the direction of one of the axes of a support, positive displacement acts in the positive direction of the corresponding axis. Rotation can be imposed around one of the axes of a support, positive rotation acts right-handed about the corresponding positive axis. A rigid support is required in the direction of the deformation. 

```{warning}
The name of the excel sheet is **StructuralPointSupportDef** due to sheet name length limitation.
```


```{image} ../.gitbook/assets/41b_deformation_of_support.png
:width: 600px
```

## Specification in the excel

| Column header | Data type | Example / enum definition | Required | Description |
|---|---|---|---|---|
| Name | String | RS1 | yes | Human readable unique name of the deformation |
| Point support | String | Sn6 | yes | Reference to [StructuralPointSupport](../supports-and-hinges/structuralpointsupport.md) to which the deformation load is applied |
| Direction | Enum | X<br>Y<br>Z<br>Rx<br>Ry<br>Rz | yes | Specifies the direction of deformation. X, Y, Z are the directions of translation. Rx, Ry, Rz are the directions of rotation. Directions follow local axis of a [StructuralPointSupport](../supports-and-hinges/structuralpointsupport.md). See notes for current information about direction. |
| Translation value [mm] | Double | -10 | yes, if Direction = X, Y, Z | Specifies the size of translation in the chosen direction |
| Rotation value [mrad] | Double | -50 | yes, if Direction = Rx, Ry, Rz | Specifies the size of rotation around the chosen axis |
| Load case | String | LC5 | yes | The name of the load case to which the load belongs|
| Id | String | 39f238a5-01d0-45cf-a2eb-958170fd4f39 | no | Unique attribute designation |


## Notes

Local coordinate systems of supports are for now global only. Therefore all the deformation are imposed in the direction of global axes.