# StructuralPointActionFree

**Free point load**

The Free point load is related to slabs. The load is not defined by the entity it acts on, but by a specific load point. Free loads are defined by means of "loading entities" that may overlap or affect one or more slabs.

```{image} ../.gitbook/assets/38\_structuralpointactionfree.png
:width: 600px
```


## Specification in the excel

| Column header| Data type | Example / enum definition | Required | Description |
| :---------------------------: | :--------------: | :--------------------------------------------------------: | :--------------------------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              Name             |      String      |                             FF1                            |              yes             | Human readable unique name of the force                                                                                                                                                                  |
|              Type             |      String      |                          Standard                          |              no              | This property defines what the load is caused by, E.g. Standard, Wind, Snow, Self weight, Hoar Frost, Predefined, Plane Load, Water Pond, Water Pressure, Soil Pressure, Generated Water, Generated Soil |
|           Direction           |       Enum       | <p>X</p><p></p><p>Y</p><p></p><p>Z</p><p></p><p>Vector</p> |              yes             | <p>Specifies the base direction of the load</p><p>X, Y, Z - action will be applied in one of these directions</p><p>Vector - size and direction calculated from vector</p>                               |
|          Value \[kN]          |      Double      |                             -1                             | yes, if Direction = X,Y or Z | Specifies the size of the load                                                                                                                                                                           |
|      Vector (X;Y;Z) \[kN]     |      String      |                          (10;10;0)                         |  yes, if Direction = Vector  | Specifies the size of the load in , direction by vector                                                                                                                                                  |
|           Load case           |      String      |                             LC2                            |              yes             | The name of the load case to which the force belongs                                                                                                                                                     |
|       Coordinate X \[m]       |      Double      |                           -1,000                           |              yes             | The X coordinate of the point force                                                                                                                                                                      |
|       Coordinate Y \[m]       |      Double      |                            1,000                           |              yes             | The Y coordinate of the point force                                                                                                                                                                      |
|       Coordinate Z \[m]       |      Double      |                            3,250                           |              yes             | The Z coordinate of the point force                                                                                                                                                                      |
|       Coordinate system       |      String      |                           Global                           |              yes             | Defines the co-ordinate system of the member in which the load is applied. Only global coordinate system is supported for free point loads                                                               |
|               Id              |      String      |            39f238a5-01d0-45cf-a2eb-958170fd4f39            |              no              | Unique attribute designation                                                                                                                                                                             |
