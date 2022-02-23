# StructuralProxyElement

**General solids**

StrucutralProxyElements are solid objects described by their boundary representation (faces of objects). The common use for StrucutralProxyElements can be found for complex part of structures (garage ramps for example), which are difficult to describe with [StructuralCurveMember](structuralcurvemember.md) and [StrucuturalSurfaceMemeber](structuralsurfacemember.md) or for massive parts of structures with difficult geometry such as foundations. With StrucuralProxyElement all important parts of the structure can be transferred via SAF format no matter the complexity.

```{warning}
|Structural proxy element is not structural analysis object and will not be considered in structural analysis calculation.
|It is just a geometrical reference object.
```

![](../.gitbook/assets/18\_structuralproxyelement.png)

## StructuralProxyElement

Sheet StrucutralProxyElement is a list of all StructuralProxyElements defined in the SAF file. Every row represents one solid object.

### Specification in the excel

| Column header| Data type | Example / enum definition | Required | Description |
| :---------------------------: | :--------------: | :----------------------------------: | :----------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              Name             |      String      |                 SPE1                 |         Yes        | Human readable unique name of the StructuralProxyElement                                                                                                                                       |
|            Material           |      String      |                C20/25                |         Yes        | The reference to the "Name" of defined material in [StructuralMaterial](structuralmaterial.md)                                                                                        |
|             Color             |      String      |                #FFFF00               |         no         | Defines colour and transparency of the object. Colour is defined by Hex format #AARRGGBB. Transparency is controlled by the alpha channel AA. If no colour is set then default colour is used. |
|             Layer             |      String      |        StructuralProxyElement        |         no         | Custom created layer. The layer can thus comprise entities that have something in common (e.g. one floor, columns of one floor, columns of the same length, etc.)                              |
|               Id              |      String      | bba1ede8-4106-47fd-b5e1-48637ab87f47 |         no         | Unique attribute designation                                                                                                                                                                   |

## StructuralProxyElementVertices

Sheet StructuralProxyElementVertices is a list of all vertices that are used for defining the StrucutralProxyElements. Each row is one vertex of StructuralProxyElements.

### Specification in the excel

| Column header| Data type | Example / enum definition | Required | Description |
| ------------------------ | :--------------: | ------------------------------------ | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Structural proxy element |      String      | SPE1                                 | Yes                | Name reference to existing StructuralProxyElement in the sheet StructuralProxyElelement.                                                                                                                                                                                                                                                                         |
| Index                    |      Integer     | 0                                    | Yes                | <p>The index of the vertex of the StrucutralProxyElement. The indexing is starting with 0. The Index is used as the reference for StructuralProxyElementFaces.</p><p></p><p>Every StructuralProxyElement has it owns set of vertecies indexed from 0 to n. Where n ∈ N (natural numbers)</p><p></p><p>Every StructuralProxyElement has at least 4 vertecies.</p> |
| X \[m]                   |      Double      | 32.569                               | Yes                | Coordinates of vertex in X direction                                                                                                                                                                                                                                                                                                                             |
| Y \[m]                   |      Double      | 12.761                               | Yes                | Coordinates of vertex in Y direction                                                                                                                                                                                                                                                                                                                             |
| Z \[m]                   |      Double      | 7.200                                | Yes                | Coordinates of vertex in Z direction                                                                                                                                                                                                                                                                                                                             |

## StructuralProxyElementFaces

Sheet StructuralProxyElementFaces is used for defining faces of every StructuralProxyElement presented. Each row represents one face of StructuralProxyElements.

### Specification in the excel

| Column header| Data type | Example / enum definition | Required | Description |
| ------------------------ | ---------------- | :----------------------------------: | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Structural proxy element | String           |                 SPE1                 | Yes                | Human readable unique name of the StructuralProxyElement                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Index                    | Integer          |                   0                  | Yes                | <p>The index of the face of the StrucutralProxyElement. The indexing is starting with 0. The Index is used as an identifier of faces among all faces of StructuralProxyElement.</p><p></p><p>Every StructuralProxyElement has it owns set of faces indexed from 0 to n. Where n ∈ N (natural numbers)</p><p></p><p>Face is defined with polygon consisting of at least 3 vertecies. These vertecies are defining a plane.</p><p></p><p>StrucutralProxyElement is defined with at least 4 faces. .</p> |
| Definition               | String           |         (11,8,1,2,13,12,5,6)         | yes                | <p>List of ordered vertecies defining the face. Face is defined with polygons.</p><p></p><p>Polygons are defined by set of vertices in brackets and vertices are divided by comma.</p>                                                                                                                                                                                                                                                                                                                |

## Notes

>Example of simple StrucutralProxyElement\
>vertices:\
>**v**0\[0,0,0], **v**1\[2,0,0], **v**2\[1,2,0], **v**3\[1,1,2]\
>faces:\
>f0(v0,v1,v3), **f**1(v2,v3,v1), **f**2(v3,v2,v0), f3(v1,v0,v2).\
>![](../.gitbook/assets/18\_structuralproxyelement2.png)
>
>It is recommended to define the edge common for two faces with the opposite polygons.
>
>Face **f**0 is in the picture defined as (v0,**v**1,**v**3) so the face **f**1 will be defined (v2,**v**3,**v**1). The common edge is defined as (**v**1,**v**3) for face **f**1 and (**v**3,**v**1) for face **f**2.

> Maximum number of rows in excel is 1,048,575, this number is not a limitation for SAF though. If more space is required, the table can continue on the right side of the first table with one empty column in between. The headers are repeated as well. 
>```{image} ../.gitbook/assets/18_limitation_of_excel.png
>:width: 800px
>```
