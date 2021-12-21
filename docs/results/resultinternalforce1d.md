# ResultInternalForce1D

**Internal force 1D**


Internal forces on line, beam, member. Result in member axis (not in principal axis).

![](../.gitbook/assets/47\_resultsinternal\_force\_1.gif)

## Specification in the excel

| Column header| Data type | Example / enum definition | Required | Description |
| :---------------------------: | :--------------: | :--------------------------------------------: | :------------------------------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|           Result on           |       Enum       |       <p>On beam</p><p></p><p>On rib</p>       |                yes               | <p>Specify object where the result is</p><p></p><p>On beam - [StructuralCurveMember](../structural-analysis-elements/structuralcurvemember.md)</p><p></p><p>On rib - [StructuralCurveMemberRib](../structural-analysis-elements/structuralcurvememberrib.md)</p> |
|             Member            |      String      |                       B1                       |    yes, if Result on = On beam   | Reference to the name of 1D member - [StructuralCurveMember](../structural-analysis-elements/structuralcurvemember.md)                                                                                                                                                                               |
|           Member Rib          |      String      |                       B2                       |    yes, if Result on = On rib    | Reference to the name of 1D member - rib [StructuralCurveMemberRib](../structural-analysis-elements/structuralcurvememberrib.md)                                                                                                                                                                             |
|           Result for          |       Enum       | <p>Load case</p><p></p><p>Load combination</p> |                yes               | Specifies from where the result is coming from (from Load Case, Load Combination)                                                                                                                                                                                                                                          |
|           Load case           |      String      |                       LC1                      |  yes, if Result for = Load case  | Reference to the name of [StructuraLoadCase](../loads/structuralloadcase.md)                                                                                                                                                                                                                                     |
|        Load combination       |      String      |                      COM1                      | yes, if Result for = Combination | Reference to the name of [StructuralLoadCombination](../loads/structuralloadcombination.md)                                                                                                                                                                                                                                |
|        Combination key        |      String      | <p>1.35*LC1+1.5*LC2+1.5*LC3+1.5*LC4</p><p></p> |                no                | <p>Allows to define exact combination per result section<br><br>Structure of string:<br>"LoadFactor1*LoadCase1+LoadFactor2*LoadCase2</p><p>+LoadFactorN*LoadCaseN"<br></p><p>For envelopes and national standard (code) combinations, this column specifies for which exact combination is the result</p>                  |
|        Section at \[m]        |      Double      |                      0.100                     |                yes               | X coordinate on the beam (distance from the start node) where the result is located                                                                                                                                                                                                                                        |
|             Index             |      Integer     |                        1                       |                yes               | Index of the section on beam. See [notes](#notes).                                                                                                                                                                                                                                                 |
|            N \[kN]            |      Double      |                      3.00                      |                yes               | <p>Result value of N</p><p>(Normal force)</p>                                                                                                                                                                                                                                                                              |
|            Vy \[kN]           |      Double      |                      3.00                      |                yes               | <p>Result value of Vy</p><p>(Shear force in Y axis direction)</p>                                                                                                                                                                                                                                                          |
|            Vz \[kN]           |      Double      |                      3.00                      |                yes               | <p>Result value of Vz</p><p>(Shear force in Z axis direction)</p>                                                                                                                                                                                                                                                          |
|           Mx \[kNm]           |      Double      |                      0.000                     |                yes               | <p>Result value of Mx</p><p>(Moment around X axis)</p>                                                                                                                                                                                                                                                                     |
|           My \[kNm]           |      Double      |                      4.500                     |                yes               | <p>Result value of My</p><p>(Moment around Y axis)</p>                                                                                                                                                                                                                                                                     |
|           Mz \[kNm]           |      Double      |                      4.500                     |                yes               | Result value of Mz (Moment around Z axis)                                                                                                                                                                                                                                                                                  |

## Notes

>### Multiple tables in one sheet
>
>The amount of data can be limited due the [limitation of xlsx](https://support.microsoft.com/en-us/office/excel-specifications-and-limits-1672b34d-7043-467e-8e27-269d656771c3) format.
>
>Therefore the results can be written to SAF in a form of multiple tables. In the similiar logic as the [StructuralProxyElement](../structural-analysis-elements/structuralproxyelement.md).
>

>### **Index**&#x20;
>
>This attribute defines an order of the section on the beam, starting with 1 and increasing from the **start** to the **end** of the beam. This property helps to specify if the internal force is on the "left" or on the right side of the section.
>
>See example below:
>
>![](../.gitbook/assets/47_resultinternalforce1d_2.gif)

```{hint}
See the index 6 and 7. One section, two values for normal (N) force. \
Section with lower index (6) identifies value on the left (closer to the origin of X-axis of the beam).\
Section with a higher index (7) identifies value on the right (further from the origin of X-axis of the beam).
```