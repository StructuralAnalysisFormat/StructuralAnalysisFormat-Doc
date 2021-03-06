# StructuralCurveEdge

**Internal edge**

Internal edge (StructuralCurveEdge) is an object within a 2D Member ([StructuralSurfaceMember](structuralsurfacemember.md)) on which the line force (StructuralCurveAction) can act. 

```{warning}
If StructuralCurveEdge does not geometrically fit to the StructuralSurfaceMember it is assigned to, it is considered a logically invalid input. Cases like this one have to be solved by validation during the import of excel data to the specific software. The validation has to be implemented together with the import/export of SAF.
```

![](../.gitbook/assets/10\_structuralcurveedge.png)

### Specification in the excel

| Column header| Data type | Example / enum definition | Required | Description |
| :---------------------------: | :--------------: | :-----------------------------------------------: | :----------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              Name             |      String      |                        IE1                        |         yes        | Human readable unique name of the internal edge                                                                                                                                                                                                                                                                                                                                                                 |
|           2D member           |      String      |                         S2                        |         yes        | The name of the [StructuralSurfaceMember](structuralsurfacemember.md) (plate, wall) on which the internal edge is placed                                                                                                                                                                                                                                                                                        |
|             Nodes             |      String      |                       N1; N2                      |         yes        | <p>All nodes that belong to the curve edge and define its geometric shape.</p><p>The names of the nodes are separated by ; (semicolon) and space.</p><p>The order of the nodes has to be from beginning to end.</p>                                                                                                                                                                                             |
|            Segments           |      String      | Line; Circular Arc; Bezier; Parabolic arc; Spline |         yes        | <p>Defines the shape of the curve between two next nodes.</p><p>Supported strings are:</p><p>Line; Circular Arc; Bezier; Parabolic arc; Spline. The names are separated by ; (semicolon) and space.</p><p></p><p>Internal edge consisting of multiple segments follows rule defined in [Geometry](../getting-started/geometry.md)</p>                                                                |
|           Parent ID           |      String      |        67b35d84-3d04-47aa-aa4a-dc1263982320       |         no         | <p>Is filled for objects created be dividing curved geometry to series of straight line objects.</p><p>Parent ID will ensure that curved edge is imported as straight parts to nonsupporting application, and back to original supporting application as curved geometry. To ensure successful round trip of segmented objects and their related objects, Parent ID needs to be present in both directions.</p> |
|               Id              |      String      |        36606732-25e0-4fd7-ae35-bb8cb1bdcf46       |         no         | Unique attribute designation                                                                                                                                                                                                                                                                                                                                                                                    |

## Notes

>StructuralCurveEdge is not affected by any [StructuralSurfaceMemberRegion](structuralsurfacememberregion.md) it might go through, it is always assigned to a [StructuralSurfaceMember](structuralsurfacemember.md).
