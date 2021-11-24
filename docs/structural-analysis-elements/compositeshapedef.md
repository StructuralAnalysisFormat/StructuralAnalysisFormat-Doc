# CompositeShapeDef

## Composite Shape Definition

Composite Shape definition is **required** when the cross-section type in [StructuralCrossSection](structuralcrosssection.md#cross-section) sheet is set as "General".

For **manufactured** types of a cross-section, Composite Shape Definition is **optional**, offering the possibility to share detailed shape definition, for better classification of the profile.

### Specification in excel:

| **Name of the column header** | **Type of data** |          **Value example or enum definition**         |       **Required value**       | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| :---------------------------: | :--------------: | :---------------------------------------------------: | :----------------------------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              Name             |      String      |                         GEN\_1                        |               yes              | Name of the profile from the [StructuralCrossSection](structuralcrosssection.md#cross-section) object sheet                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|        Material name #        |      String      |                         MAT\_1                        | yes, if polygon is not opening | Name reference to the existing [StructuralMaterial](structuralmaterial.md#material) object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|       Polygon contour #       |      String      | -75.0; 105.0\| -175.0; 5.0\| 175.0; 5.0\| 75.0; 105.0 |       yes (at least one)       | <p>This attribute is used to define the cross-section geometry as a polygon contour.</p><p>One cross-section shape can consist of more polygons.</p><p><strong>Openings</strong> contour are defined clockwise.</p><p><strong>Common polygons</strong> counterclockwise.</p><p>The format of the data is:</p><p>y1; z1\|y2; z2\|y3; z3\|yi; zi\|yi+1; zi+1</p><p>The coordinates of the vertices are divided by ";" and each vertex separated by "\|"</p><p>Keep in mind: enter dimensions in millimeters [mm] or inches [inch] (based on System of units set in <a href="../getting-started/project-and-model-specifications/#model">Project and model</a> specifications)</p> |
|               Id              |      String      |          39f238a5-01d0-45cf-a2eb-958170fd4f39         |               no               | Unique attribute designation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Notes

{% hint style="info" %}
The symbol "#" means indexing of the name columns, depends on how many polygons is used, starts from 1

The contour defined clockwise is opening

The contour defined counter clockwise is polygon of the general cross-section (relation between LCS and counter clockwise direction is shown below)
{% endhint %}

![](../.gitbook/assets/8\_compositeshapedef\_counterclockwise.png)

{% hint style="info" %}
Each polygon has a defined material which is name reference to existing material in [StructuralMaterial](structuralmaterial.md#material) sheet

* The opening has no material definition
* Each polygon contour has to be closed
* The set of all polygons and openings defines one general cross-section (one row in the Excel table)
* The number of polygons is limited to 99. The definition of the general shape has to consist of at least one polygon which is not the opening.
* CompositeShapeDef example with opening is shown below. A,B,C,D are defining the contour of cross-section (counter clockwise polygon) and E,F,K,L are defining the opening (clockwise polygon).
{% endhint %}

![](../.gitbook/assets/8\_compositeshapedef\_animation.gif)