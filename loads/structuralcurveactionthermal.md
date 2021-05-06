# StructuralCurveActionThermal

## Thermal load on the beam

The thermal load on the line elements \([StructuralCurveMember](../structural-analysis-elements/structuralcurvemember.md#1d-member-beam-column), [StructuralCurveMemberRib](../structural-analysis-elements/structuralcurvememberrib.md#2d-member-rib)\). The variation of the thermal load can be constant or linear over the cross-section of the beam.

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
      <td style="text-align:center">LT1</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Human readable unique name of the load</td>
    </tr>
    <tr>
      <td style="text-align:center">Force action</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>On beam</p>
        <p></p>
        <p>On rib</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Specifies on which type of object the load acts.</td>
    </tr>
    <tr>
      <td style="text-align:center">Variation</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>Constant</p>
        <p></p>
        <p>Linear</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">
        <p>Specifies how the temperature varies</p>
        <p>Constant: The load is defined by means of a single value deltaT. The value
          specifies the warming to which the 1D member is subject to.</p>
        <p>Linear: The load is defined by means of a set of four values. The individual
          values specify the temperature at individual sides (left, right, top, bottom)
          of the 1D member.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">deltaT [&#xB0;C]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">5</td>
      <td style="text-align:center">yes; if Variation = Constant</td>
      <td style="text-align:left">
        <p>Temperature delta in Celsius/Fahrenheit on the centre line of the member.</p>
        <p>*See note to clarify the position.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">TempL [&#xB0;C]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">5</td>
      <td style="text-align:center">yes, if Variation = Linear</td>
      <td style="text-align:left">
        <p>The temperature on the left side of the beam surface in Celsius/Fahrenheit.
          Refers to LCS of 1D member.</p>
        <p>*See note to clarify the position.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">TempR [&#xB0;C]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">18</td>
      <td style="text-align:center">yes, if Variation = Linear</td>
      <td style="text-align:left">
        <p>Temperature on right side of the beam surface in Celsius/Fahrenheit. Refers
          to LCS of 1D member.</p>
        <p>*See note to clarify the position.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">TempT [&#xB0;C]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">5</td>
      <td style="text-align:center">yes, if Variation = Linear</td>
      <td style="text-align:left">
        <p>Temperature on top side of the beam surface in Celsius/Fahrenheit. Refers
          to LCS of 1D member.</p>
        <p>*See note to clarify the position.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">TempB [&#xB0;C]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">5</td>
      <td style="text-align:center">yes, if Variation = Linear</td>
      <td style="text-align:left">
        <p>Temperature on bottom side of the beam surface in Celsius/Fahrenheit.
          Refers to LCS of 1D member.</p>
        <p>*See note to clarify the position.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Member</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">B11</td>
      <td style="text-align:center">yes, if Force action = On beam</td>
      <td style="text-align:left">The name of the <a href="../structural-analysis-elements/structuralcurvemember.md#1d-member-beam-column">StructuralCurveMember </a>on
        which the load is applied</td>
    </tr>
    <tr>
      <td style="text-align:center">Member Rib</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">B10</td>
      <td style="text-align:center">yes, if Force action = On rib</td>
      <td style="text-align:left">The name of the <a href="../structural-analysis-elements/structuralcurvememberrib.md#2d-member-rib">StructuralCurveMemberRib </a>on
        which the load is applied</td>
    </tr>
    <tr>
      <td style="text-align:center">Load case</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">LC1</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">The name of the load case to which the load belongs</td>
    </tr>
    <tr>
      <td style="text-align:center">Coordinate definition</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>Absolute</p>
        <p></p>
        <p>Relative</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Selects the coordinate system that is used to define the length of the
        line load. Relative means without units. To define length of the load in
        meters input absolute</td>
    </tr>
    <tr>
      <td style="text-align:center">Origin</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>From start</p>
        <p></p>
        <p>From end</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Specifies the origin of the coordinate system used for the definition
        of the length of the load</td>
    </tr>
    <tr>
      <td style="text-align:center">Start point [m]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">
        <p>value in meters for Coordinate definition = Absolute</p>
        <p>0,0</p>
        <p>value in percentage for Coordinate definition = Relative</p>
        <p>0,0</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Defines the position of the start point of the load in relative or absolute
        coordinates</td>
    </tr>
    <tr>
      <td style="text-align:center">End point [m]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">
        <p>value in meters for Coordinate definition = Absolute</p>
        <p>5,25</p>
        <p>value in percentage for Coordinate definition = Relative</p>
        <p>1,0</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Defines the position of the end point of the load in relative or absolute
        coordinates</td>
    </tr>
    <tr>
      <td style="text-align:center">Parent ID</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">67b35d84-3d04-47aa-aa4a-dc1263982320</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">
        <p>Is filled for objects created be dividing curved geometry to series of
          straight line objects.
          <br />
          <br />Parent ID will ensure that curved edge is imported as straight parts to
          nonsupporting application, and back to original supporting application
          as curved geometry.</p>
        <p>To ensure successful round trip of segmented objects and their related
          objects, Parent ID needs to be present in both directions.</p>
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

## Notes

{% hint style="info" %}
Reference to surfaces of cross-section where linear temperature can be applied. View is towards the direction of center axis \(looking from end point towards start point\).
{% endhint %}



