# StructuralPointMoment

## Moment force in node/on beam

A node or a beam of the structure may be subject to a moment load. The load is defined by the direction and size of the moment and in case of the moment force on beam it can be repeated along the member.

![](../.gitbook/assets/32_structuralpointmoment.png)

Specification in the excel:

<table>
  <thead>
    <tr>
      <th style="text-align:center">Name of the column header</th>
      <th style="text-align:center">Type of data</th>
      <th style="text-align:center">Value example or enum definition</th>
      <th style="text-align:center">Required value</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:center">Name</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">PF3</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Human readable unique name of the force</td>
    </tr>
    <tr>
      <td style="text-align:center">Type</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">Standard</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">This property defines what the load is caused by, E.g. Standard, Wind,
        Snow, Self weight, Hoar Frost, Predefined, Plane Load, Water Pond, Water
        Pressure, Soil Pressure, Generated Water, Generated Soil</td>
    </tr>
    <tr>
      <td style="text-align:center">Direction</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>Mx</p>
        <p></p>
        <p>My</p>
        <p></p>
        <p>Mz</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Specifies the base direction of the load</td>
    </tr>
    <tr>
      <td style="text-align:center">Force action</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>On beam</p>
        <p></p>
        <p>In node</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Specifies on which type of object the force acts</td>
    </tr>
    <tr>
      <td style="text-align:center">Reference node</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">N3</td>
      <td style="text-align:center">yes if Force action = In node</td>
      <td style="text-align:left">The name of the reference node</td>
    </tr>
    <tr>
      <td style="text-align:center">Reference member</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">B1</td>
      <td style="text-align:center">yes if Force action =On beam</td>
      <td style="text-align:left">The name of the reference beam</td>
    </tr>
    <tr>
      <td style="text-align:center">Value [kNm]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">-10</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Specifies the size of the load in kiloNewtonmeters.</td>
    </tr>
    <tr>
      <td style="text-align:center">Load case</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">LC5</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">The name of the load case to which the force belongs</td>
    </tr>
    <tr>
      <td style="text-align:center">Coordinate system</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>Global</p>
        <p>Local</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Defines co-ordinate system in which the load is applied</td>
    </tr>
    <tr>
      <td style="text-align:center">Origin</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>From start</p>
        <p></p>
        <p>From end</p>
      </td>
      <td style="text-align:center">yes, if Force action = On beam</td>
      <td style="text-align:left">Specifies where the origin for the position co-ordinate measurement is</td>
    </tr>
    <tr>
      <td style="text-align:center">Coordinate definition</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>Absolute</p>
        <p></p>
        <p>Relative</p>
      </td>
      <td style="text-align:center">yes, if Force action = On beam</td>
      <td style="text-align:left">Specifies the definition of the position. It may be absolute or relative</td>
    </tr>
    <tr>
      <td style="text-align:center">Position x [m]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">
        <p>value in meters for Coordinate definition = Absolute</p>
        <p>5,25</p>
        <p>value in percentage for Coordinate definition = Relative</p>
        <p>1,0</p>
      </td>
      <td style="text-align:center">yes, if Force action = On beam</td>
      <td style="text-align:left">Defines the position of the load on the 1D member in local coordinate
        system in relative or in absolute coordinates [m]</td>
    </tr>
    <tr>
      <td style="text-align:center">Repeat (n)</td>
      <td style="text-align:center">Integer</td>
      <td style="text-align:center">1</td>
      <td style="text-align:center">yes, if Force action = On beam</td>
      <td style="text-align:left">Defines the number of forces acting on the beam. If the number is greater
        than 1, the forces are distributed uniformly over the 1D member</td>
    </tr>
    <tr>
      <td style="text-align:center">Delta x [m]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">0,3</td>
      <td style="text-align:center">yes, if Repeat (n) &gt; 1</td>
      <td style="text-align:left">
        <p>Defines the distance between forces acting on the 1D member in relative
          or in absolute coordinates [m]</p>
        <p>(only applicable when ForceAction=OnBeam)</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Id</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">39f238a5-01d0-45cf-a2eb-958170fd4f39</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Unique attribute designation</td>
    </tr>
  </tbody>
</table>

