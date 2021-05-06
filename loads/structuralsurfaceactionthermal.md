# StructuralSurfaceActionThermal

## Thermal load on surface elements

The thermal load on the surface elements \([StructuralSurfaceMember](../structural-analysis-elements/structuralsurfacemember.md#2d-member-plate-wall)\). The variation of the thermal load can be constant or linear over the cross-section of the beam.

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
        <p>Constant: The load is defined by means of a single value T1. The value
          specifies the change in temperature of the 2D member (straight &#x394;T).
          Temperature change is constant along the cross-section.</p>
        <p>Linear: The load is defined by means of a set of two values T1 and T2.
          The individual values specify the temperature at individual surfaces -
          top, bottom of the 2D member.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">TempT [&#xB0;C]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">18</td>
      <td style="text-align:center">yes
        <br />
      </td>
      <td style="text-align:left">
        <p>Specifies the first size of the load in Celsius/Fahrenheit.</p>
        <p>For constant: Delta temperature on the center plane</p>
        <p>For linear: Temperature of top surface (LCS direction +z) of 2D member</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">TempB [&#xB0;C]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">18</td>
      <td style="text-align:center">yes, if Variation = Linear</td>
      <td style="text-align:left">
        <p>Specifies the second size of the load in Celsius/Fahrenheit.</p>
        <p>For linear: Temperature of bottom surface (LCS direction -z) of 2D member</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">2D Member</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">S15</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">The name of the <a href="../structural-analysis-elements/structuralcurvemember.md#1d-member-beam-column">StructuralSurfaceMember </a>or
        <a
        href>StructuralSurfaceActionDistribution</a>which is the surface load related
          to.</td>
    </tr>
    <tr>
      <td style="text-align:center">2D Member Region</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">R1</td>
      <td style="text-align:center">yes, if on region</td>
      <td style="text-align:left">The name of the <a href="../structural-analysis-elements/structuralsurfacememberregion.md#region-of-different-plate-thickness">StructuralSurfaceMemberRegion </a>to
        which is the surface action related if it is available on 2D member.</td>
    </tr>
    <tr>
      <td style="text-align:center">Load case</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">LC1</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">The name of the load case to which the load belongs</td>
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

