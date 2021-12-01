# StructuralMaterial

**Material**

Material is the basic entity affecting the behaviour of the structure. It is subsequently applied to a chosen profile ([StructuralCrossSection](structuralcrosssection.md)). The user can use a pre-defined material or change the properties to get a custom one. The predefined materials correspond to materials defined in particular technical codes.The specification in excel:

## Specification in excel:

| Header | Data type | Example | Required? | Description |
| --- | --- | --- | --- | --- |
| Name | String | S235 | yes | Human readable unique name of the material \*see notes |
| Type | Enum | <p>Concrete<br></p><p>Steel<br></p><p>Timber<br></p><p>Aluminium<br></p><p>Masonry<br></p><p>Other</p> | yes | The type of material |
| Subtype | String | Hot rolled | no | The subtype of the material, e.g. hot rolled, cold formed, stainless steel, prestressed concrete, fiber-reinforced concrete, UHPC etc. |
| Quality | String | S235 | yes | <p>The quality grade of the material. Use a commonly known naming of grades of specific structural material. Example:</p><p>Steel - S235, S275, S355...</p><p>Concrete - C16/20, C25/30, C30/35...</p><p>Timber - C18, C22, D18...</p> |
| Unit mass \[kg/m3] | Double | 7850 | no | Self-weight of the material |
| E modulus \[MPa] | Double | 210000 | no | Young's modulus of elasticity |
| G modulus \[MPa] | Double | 12500 | no | Shear modulus |
| Poisson Coefficient | Double | 0,2 | no | Poisson coefficient |
| Thermal expansion \[1/K] | Double | 0,000012 | no | The coefficient of thermal expansion of the material |
| Design properties | String | 1\|1.1; 2\|4.8; 9\|1100 | no | Custom design characteristics of the material. The format of the data has to follow this convention: "label of the design property" "\|" "value of the design property" The list of available properties with indexes can be found in Annex. |
| Id | String | 6bbd256e-0225-4ee5-91e5-c7ef791a33cb | no | Unique attribute designation |

## Notes


>"**Name**" is recommended to set the same as the "**Quality**" of the defined material.

