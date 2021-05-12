# ResultInternalForce1D

## Internal force 1D

Internal forces on line, beam, member. Result in member axis \(not in principal axis\).

![](../.gitbook/assets/47_resultsinternal_force_1.gif)

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
      <td style="text-align:center">1D member</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">B1</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Reference to 1D member</td>
    </tr>
    <tr>
      <td style="text-align:center">Load case</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">LC1</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Reference to load case from where the result is comming from</td>
    </tr>
    <tr>
      <td style="text-align:center">Section at [m]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">0.100</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">X coordinate on the beam (distance from the start node) where the result
        is located</td>
    </tr>
    <tr>
      <td style="text-align:center">N [kN]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">3,00</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">
        <p>Result value of N</p>
        <p>(Normal force)</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Vy [kN]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">3,00</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">
        <p>Result value of Vy</p>
        <p>(Shear force in Y axis direction)</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Vz [kN]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">3,00</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">
        <p>Result value of Vz</p>
        <p>(Shear force in Z axis direction)</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Mx [kNm]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">0,000</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">
        <p>Result value of Mx</p>
        <p>(Moment around X axis)</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">My [kNm]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">4,500</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">
        <p>Result value of My</p>
        <p>(Moment around Y axis)</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Mz [kNm]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">4,500</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Result value of Mz (Moment around Z axis)</td>
    </tr>
  </tbody>
</table>

