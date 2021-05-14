# StructuralCurveActionThermal

## Thermal load on the beam

The thermal load on the line elements \([StructuralCurveMember](../structural-analysis-elements/structuralcurvemember.md#1d-member-beam-column), [StructuralCurveMemberRib](../structural-analysis-elements/structuralcurvememberrib.md#2d-member-rib)\). The variation of the thermal load can be constant or linear over the cross-section of the beam.

### Specification in the excel

<table>
  <thead>
    <tr>
      <th style="text-align:left">Name of the column header</th>
      <th style="text-align:left">Type of data</th>
      <th style="text-align:left">Value example or enum definition</th>
      <th style="text-align:left">Required value</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">Name</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">LT1</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Human readable unique name of the load</td>
    </tr>
    <tr>
      <td style="text-align:left">Force action</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>On beam</p>
        <p>On rib</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Specifies on which type of object the load acts.</td>
    </tr>
    <tr>
      <td style="text-align:left">Variation</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>Constant</p>
        <p>Linear</p>
      </td>
      <td style="text-align:left">yes</td>
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
      <td style="text-align:left">deltaT [&#xB0;C]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">5</td>
      <td style="text-align:left">yes; if Variation = Constant</td>
      <td style="text-align:left">
        <p>Temperature delta in Celsius/Fahrenheit on the centre line of the member.</p>
        <p>*See note to clarify the position.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">TempL [&#xB0;C]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">5</td>
      <td style="text-align:left">yes, if Variation = Linear</td>
      <td style="text-align:left">
        <p>The temperature on the left side of the beam surface in Celsius/Fahrenheit.
          Refers to LCS of 1D member.</p>
        <p>*See note to clarify the position.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">TempR [&#xB0;C]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">18</td>
      <td style="text-align:left">yes, if Variation = Linear</td>
      <td style="text-align:left">
        <p>Temperature on right side of the beam surface in Celsius/Fahrenheit. Refers
          to LCS of 1D member.</p>
        <p>*See note to clarify the position.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">TempT [&#xB0;C]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">5</td>
      <td style="text-align:left">yes, if Variation = Linear</td>
      <td style="text-align:left">
        <p>Temperature on top side of the beam surface in Celsius/Fahrenheit. Refers
          to LCS of 1D member.</p>
        <p>*See note to clarify the position.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">TempB [&#xB0;C]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">5</td>
      <td style="text-align:left">yes, if Variation = Linear</td>
      <td style="text-align:left">
        <p>Temperature on bottom side of the beam surface in Celsius/Fahrenheit.
          Refers to LCS of 1D member.</p>
        <p>*See note to clarify the position.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Member</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">B11</td>
      <td style="text-align:left">yes, if Force action = On beam</td>
      <td style="text-align:left">The name of the <a href="../structural-analysis-elements/structuralcurvemember.md#1d-member-beam-column">StructuralCurveMember</a> on
        which the load is applied</td>
    </tr>
    <tr>
      <td style="text-align:left">Member Rib</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">B10</td>
      <td style="text-align:left">yes, if Force action = On rib</td>
      <td style="text-align:left">The name of the <a href="../structural-analysis-elements/structuralcurvememberrib.md#2d-member-rib">StructuralCurveMemberRib</a> on
        which the load is applied</td>
    </tr>
    <tr>
      <td style="text-align:left">Load case</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">LC1</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">The name of the load case to which the load belongs</td>
    </tr>
    <tr>
      <td style="text-align:left">Coordinate definition</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>Absolute</p>
        <p>Relative</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Selects the coordinate system that is used to define the length of the
        line load. Relative means without units. To define length of the load in
        meters input absolute</td>
    </tr>
    <tr>
      <td style="text-align:left">Origin</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>From start</p>
        <p>From end</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Specifies the origin of the coordinate system used for the definition
        of the length of the load</td>
    </tr>
    <tr>
      <td style="text-align:left">Start point [m]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">
        <p>value in meters for Coordinate definition = Absolute</p>
        <p>0,0</p>
        <p>value in percentage for Coordinate definition = Relative</p>
        <p>0,0</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Defines the position of the start point of the load in relative or absolute
        coordinates</td>
    </tr>
    <tr>
      <td style="text-align:left">End point [m]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">
        <p>value in meters for Coordinate definition = Absolute</p>
        <p>5,25</p>
        <p>value in percentage for Coordinate definition = Relative</p>
        <p>1,0</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Defines the position of the end point of the load in relative or absolute
        coordinates</td>
    </tr>
    <tr>
      <td style="text-align:left">Parent ID</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">67b35d84-3d04-47aa-aa4a-dc1263982320</td>
      <td style="text-align:left">no</td>
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
      <td style="text-align:left">Id</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">39f238a5-01d0-45cf-a2eb-958170fd4f39</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">Unique attribute designation</td>
    </tr>
  </tbody>
</table>

## Notes

{% hint style="info" %}
Reference to surfaces of cross-section where linear temperature can be applied. View is towards the direction of center axis \(looking from end point towards start point\).
{% endhint %}

