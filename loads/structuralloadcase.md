# StructuralLoadCase

## Load case

Individual loads are not defined "freely". They must be included in load cases. A load case is a group, commonly used to group loads from the same action source. The load cases correspond with the professional terminology specified in national technical standards dealing with loads of civil engineering structures. The application of load cases follows the load management procedures that are usual and also obligatory in civil engineering practice.

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
      <td style="text-align:center">LC1</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Human readable unique name of the object</td>
    </tr>
    <tr>
      <td style="text-align:center">Description</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">Offices &#x2013; Cat.B</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Description of the load case</td>
    </tr>
    <tr>
      <td style="text-align:center">Action type</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>Permanent</p>
        <p></p>
        <p>Variable</p>
        <p></p>
        <p>Accidental</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Type of load in general. Other parameters depend on the adjustment of
        the load case type</td>
    </tr>
    <tr>
      <td style="text-align:center">Load group</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">LG 1</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Name reference to existing <a href="structuralloadgroup.md#load-group">StructuralLoadGroup</a> object
        with appropriate settings of Load group type</td>
    </tr>
    <tr>
      <td style="text-align:center">Load type</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>Self weight</p>
        <p></p>
        <p>Others</p>
        <p></p>
        <p>Prestress</p>
        <p></p>
        <p>Dynamic</p>
        <p></p>
        <p>Static</p>
        <p></p>
        <p>Temperature</p>
        <p></p>
        <p>Wind</p>
        <p></p>
        <p>Snow</p>
        <p></p>
        <p>Maintenance</p>
        <p></p>
        <p>Fire</p>
        <p></p>
        <p>Moving</p>
        <p></p>
        <p>Seismic</p>
        <p></p>
        <p>Standard</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">
        <p>Define subtype of load. Depends on Action type property.</p>
        <p></p>
        <p>Subtypes for <b>Permanent</b>:</p>
        <p>Self weight; Others ;Prestress; Standard</p>
        <p>Use value &quot;Self weight&quot; only for cases of automatically generated
          load.</p>
        <p>If your app is exporting self weight load as load objects, use type &quot;Standard&quot;
          and use field &quot;Description&quot; to carry the information it is Self
          weight (example: &quot;Self weight load impulses&quot;)</p>
        <p></p>
        <p>Subtypes for <b>Variable</b>:</p>
        <p>Others; Dynamic; Static; Temperature; Wind; Snow; Maintenance; Fire; Moving;
          Seismic; Standard</p>
        <p></p>
        <p>Subtypes for <b>Accidental</b>:</p>
        <p>Others; Dynamic; Static; Temperature; Wind; Snow; Maintenance; Fire; Moving;
          Seismic; Standard</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Duration</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>Long</p>
        <p></p>
        <p>Medium</p>
        <p></p>
        <p>Short</p>
        <p></p>
        <p>Instantaneous</p>
      </td>
      <td style="text-align:center">yes, if Action type = Variable</td>
      <td style="text-align:left">For static standard loads, the duration of the load impact can be specified</td>
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

