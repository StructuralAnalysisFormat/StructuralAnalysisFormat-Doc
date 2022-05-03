# StructuralPointDeformation

## Specification in the excel

| Column header | Data type | Example / enum definition | Required | Description |
|---|---|---|---|---|
| Name | String | RS1 | yes | Human readable unique name of the deformation |
| Support in a node | String | Sn6 | yes |  |
| Direction | Enum | X<br>Y<br>Z<br>Rx<br>Ry<br>Rz | yes |  |
| Translation value [mm] | Double | -10 | yes, if Direction = X, Y, Z |  |
| Rotation value [mrad] | Double | -50 | yes, if Direction = Rx, Ry, Rz |  |
| Load case | String | LC5 | yes |  |
| Id | String | 39f238a5-01d0-45cf-a2eb-958170fd4f39 | no |  |

## Notes