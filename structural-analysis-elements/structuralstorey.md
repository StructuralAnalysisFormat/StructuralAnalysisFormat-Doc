# StructuralStorey

## Storey, Floor levels...

StructuralStorey object describes definition of floor levels/storeys in structural model.

![](../.gitbook/assets/17_structuralstorey_1.png)

![](../.gitbook/assets/17_structuralstorey_2.png)

### Specification in the excel

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
      <td style="text-align:center">FL1</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Human readable unique name of the Arbitrary definition</td>
    </tr>
    <tr>
      <td style="text-align:center">Height level [m]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">
        <p>-2.000</p>
        <p>2.500</p>
        <p>5.500</p>
        <p>8.500</p>
        <p>10.500</p>
        <p>15.500
          <br />
        </p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Height level [m] or [m] of the floor.
        <br />Zero height level refers to horizontal plane of GCS (mostly XY plane).</td>
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

