# StructuralLoadGroup

## Load group

Load groups define "how the individual load cases may be combined together" if inserted into a load case combination. Thanks to the load groups, the user can easily specify which load cases MUST, MUST NOT, or CAN act together. Each load group may be used either for permanent loads or for variable loads. Permanent and variable loads cannot appear in the same group.

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
      <td style="text-align:center">LG1</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Human readable unique name of the object</td>
    </tr>
    <tr>
      <td style="text-align:center">Load group type</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>Permanent</p>
        <p></p>
        <p>Variable</p>
        <p></p>
        <p>Accidental</p>
        <p></p>
        <p>Seismic</p>
        <p></p>
        <p>Moving</p>
        <p></p>
        <p>Tensioning</p>
        <p></p>
        <p>Fire</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">
        <p>This parameters tell whether the load group is used for permanent or variable
          loads.</p>
        <p>Applicable Load group types for:</p>
        <p></p>
        <p><b>Permanent load case: </b>Permanent</p>
        <p></p>
        <p><b>Variable load case: </b>Variable, Seismic, Moving, Tensioning, Fire</p>
        <p></p>
        <p><b>Accidental load case: </b>Accidental</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Relation</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>Exclusive</p>
        <p></p>
        <p>Standard</p>
        <p></p>
        <p>Together</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">
        <p>The relation tells what the relation of load cases in the particular load
          group is.</p>
        <p><b>Exclusive</b>: Two load cases from the same load group of this type
          will never appear in the same combination.
          <br />Applicable for Load group types: Variable, Accidental, Seismic, Moving,
          Tensioning, Fire</p>
        <p><b>Standard</b>: It allows the user to sort load cases but it does not
          affect the process of generation of load case combinations.</p>
        <p>Applicable for Load group types: All</p>
        <p><b>Together</b>: All load cases in the same load group of this type are
          always inserted into every new load case combination</p>
        <p>Applicable for Load group types: Permanent</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Load type</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">Domestic</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">
        <p>Define type of variable load, E.g. Domestic,</p>
        <p>Offices,</p>
        <p>Congregation,</p>
        <p>Shopping,</p>
        <p>Storage,</p>
        <p>Vehicle &lt; 30kN,</p>
        <p>Vehicle &gt; 30kN,</p>
        <p>Roofs,</p>
        <p>Snow,</p>
        <p>Wind,</p>
        <p>Temperature</p>
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

