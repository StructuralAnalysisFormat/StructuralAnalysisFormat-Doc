# StructuralStorey

**Storey, Floor levels...**

StructuralStorey object describes definition of floor levels/storeys in structural model.

```{image} ../.gitbook/assets/17\_structuralstorey\_1.png
:width: 1000px
```

```{image} ../.gitbook/assets/17\_structuralstorey\_2.png
:width: 600px
```

## Specification in the excel

| **Name of the column header** | **Type of data** | **Value example or enum definition** | **Required value** | **Description**                                                                                                        |
| ----------------------------- | ---------------- | ------------------------------------ | ------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| Name                          | String           | FL1                                  | yes                | Human readable unique name of the Arbitrary definition                                                                 |
| Height level \[m]             | Double           | -2.000                               | yes                | <p>Height level [m] or [m] of the floor.<br>Zero height level refers to horizontal plane of GCS (mostly XY plane).</p> |
| Id                            | String           | 39f238a5-01d0-45cf-a2eb-958170fd4f39 | no                 | Unique attribute designation                                                                                           |
