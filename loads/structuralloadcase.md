# StructuralLoadCase

## Load case

Individual loads are not defined "freely". They must be included in load cases. A load case is a group, commonly used to group loads from the same action source. The load cases correspond with the professional terminology specified in national technical standards dealing with loads of civil engineering structures. The application of load cases follows the load management procedures that are usual and also obligatory in civil engineering practice.

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
      <td style="text-align:left">LC1</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Human readable unique name of the object</td>
    </tr>
    <tr>
      <td style="text-align:left">Description</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">Offices &#x2013; Cat.B</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">Description of the load case</td>
    </tr>
    <tr>
      <td style="text-align:left">Action type</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>Permanent</p>
        <p>Variable</p>
        <p>Accidental</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Type of load in general. Other parameters depend on the adjustment of
        the load case type</td>
    </tr>
    <tr>
      <td style="text-align:left">Load group</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">LG 1</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Name reference to existing <a href="structuralloadgroup.md#load-group">StructuralLoadGroup</a> object
        with appropriate settings of Load group type</td>
    </tr>
    <tr>
      <td style="text-align:left">Load type</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>Self weight</p>
        <p>Others</p>
        <p>Prestress</p>
        <p>Dynamic</p>
        <p>Static</p>
        <p>Temperature</p>
        <p>Wind</p>
        <p>Snow</p>
        <p>Maintenance</p>
        <p>Fire</p>
        <p>Moving</p>
        <p>Seismic</p>
        <p>Standard</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">
        <p>Define subtype of load. Depends on Action type property.</p>
        <p>Subtypes for <b>Permanent</b>:</p>
        <p>Self weight; Others ;Prestress; Standard</p>
        <p>Use value &quot;Self weight&quot; only for cases of automatically generated
          load.</p>
        <p>If your app is exporting self weight load as load objects, use type &quot;Standard&quot;
          and use field &quot;Description&quot; to carry the information it is Self
          weight (example: &quot;Self weight load impulses&quot;)</p>
        <p>Subtypes for <b>Variable</b>:</p>
        <p>Others; Dynamic; Static; Temperature; Wind; Snow; Maintenance; Fire; Moving;
          Seismic; Standard</p>
        <p>Subtypes for <b>Accidental</b>:</p>
        <p>Others; Dynamic; Static; Temperature; Wind; Snow; Maintenance; Fire; Moving;
          Seismic; Standard</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Duration</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>Long</p>
        <p>Medium</p>
        <p>Short</p>
        <p>Instantaneous</p>
      </td>
      <td style="text-align:left">yes, if Action type = Variable</td>
      <td style="text-align:left">For static standard loads, the duration of the load impact can be specified</td>
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

