# Ignored objects and groups:

{% hint style="warning" %}
 **SAF TOC group name** is a term used for navigation in the table of contents of SAF documentation. Do not use it in "ignored groups" cells.

Each group consist of multiple objects, ignoring the group is taken in to account as ignoring all objects in the group \(groups are parent to objects\)
{% endhint %}



<table>
  <thead>
    <tr>
      <th style="text-align:left">Name of the row</th>
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
      <td style="text-align:left">Park Office - object A</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">The name of the model</td>
    </tr>
    <tr>
      <td style="text-align:left">Description</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">Highrise</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">The description of the model</td>
    </tr>
    <tr>
      <td style="text-align:left">Discipline</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">Load-bearing structure</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">Discipline can be set as Undefined, Architecture, HVAC, Load-bearing structure,
        Terrain, Facility etc.</td>
    </tr>
    <tr>
      <td style="text-align:left">Level of detail</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">Draft</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">Describe level of detail of the model</td>
    </tr>
    <tr>
      <td style="text-align:left">Status</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">Planning stage</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">Description of model status</td>
    </tr>
    <tr>
      <td style="text-align:left">Owner</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">Person A</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">Define the owner of the model</td>
    </tr>
    <tr>
      <td style="text-align:left">Revision number</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">rev.02</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">Current revision number</td>
    </tr>
    <tr>
      <td style="text-align:left">Created</td>
      <td style="text-align:left">Date Time</td>
      <td style="text-align:left">2018-12-16</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">Creation time, in UTC, in ISO format year-month-day</td>
    </tr>
    <tr>
      <td style="text-align:left">Last update</td>
      <td style="text-align:left">Date Time</td>
      <td style="text-align:left">2018-12-19</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">Last update time, in UTC, in ISO format year-month-day</td>
    </tr>
    <tr>
      <td style="text-align:left">Source type</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">Structural analysis model</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">Definition of the source data</td>
    </tr>
    <tr>
      <td style="text-align:left">Source application</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">Scia Engineer</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">Definition of the source application</td>
    </tr>
    <tr>
      <td style="text-align:left">SAF Version</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">1.0.3</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Definition of used version of the Structural Analysis Format</td>
    </tr>
    <tr>
      <td style="text-align:left">Source company</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">Statical company</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">Define the author company of source data</td>
    </tr>
    <tr>
      <td style="text-align:left">Global coordinate system</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>X vertical</p>
        <p>Y vertical</p>
        <p>Z vertical</p>
        <p>minus X vertical</p>
        <p>minus Y vertical</p>
        <p>minus Z vertical</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">
        <p>Define the space orientation of the coordinates system for model</p>
        <p>Right hand rule applies all the time.</p>
        <p>X vertical - X axis goes against gravity</p>
        <p>Y vertical - Y axis goes against gravity</p>
        <p>Z vertical - Z axis goes against gravity</p>
        <p>minus X vertical - X axis goes in direction of gravity</p>
        <p>minus Y vertical - Y axis goes in direction of gravity</p>
        <p>minus Z vertical - Z axis goes in direction of gravity</p>
        <p>* For further explanation see notes below
          <br />
        </p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">LCS of cross-section</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>ZYX</p>
        <p>MinusYZX</p>
        <p>MinusZMinusYX</p>
        <p>YMinusZX</p>
        <p>YZMinusX</p>
        <p>MinusZYMinusX</p>
        <p>MinusYMinusZMinusX</p>
        <p>ZMinusYMinusX</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">
        <p>Define the LCS orientation of used cross-section.</p>
        <p>With row &quot;LCS of cross-section&quot; the user is able to define,
          how the LCS of cross section is defined in his software. This will give
          opportunity to receiving application of SAF file to correctly interpret
          LCS of cross section with different standard. The x-axis is always in the
          centre line and all possible cases are described by this enum.</p>
        <p>For further explanation see notes below</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">System of units</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>Metric</p>
        <p>Imperial</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Define the type of units system used in model</td>
    </tr>
    <tr>
      <td style="text-align:left">National code</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>EC-Standard-EN</p>
        <p>EC-ONORM-EN (Austrian NA)</p>
        <p>EC-NBN-EN (Belgian NA)</p>
        <p>EC-BS-EN (British NA)</p>
        <p>EC-CYS-EN (Cypriot NA)</p>
        <p>EC-CSN-EN (Czech NA)</p>
        <p>EC-DS-EN (Danish NA)</p>
        <p>EC-NEN-EN (Dutch NA)</p>
        <p>EC-SFS-EN (Finnish NA)</p>
        <p>EC-NF-EN (French NA)</p>
        <p>EC-DIN-EN (German NA)</p>
        <p>EC-ELOT-EN (Greek NA)</p>
        <p>EC-IS-EN (Irish NA)</p>
        <p>EC-UNI-EN (Italian NA)</p>
        <p>EC-LU-EN (Luxembourgian NA)</p>
        <p>EC-MS-EN (Malaysian NA)</p>
        <p>EC-NS-EN (Norwegian NA)</p>
        <p>EC-PN-EN (Polish NA)</p>
        <p>EC-SR-EN (Romanian NA)</p>
        <p>EC-SS-EN (Singaporean NA)</p>
        <p>EC-STN-EN (Slovakian NA)</p>
        <p>EC-SIST-EN (Slovenian NA)</p>
        <p>EC-UNE-EN (Spanish NA)</p>
        <p>EC-SS-EN (Swedish NA)</p>
        <p>IBC</p>
        <p>NBR</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Sets national code used for structural analysis</td>
    </tr>
    <tr>
      <td style="text-align:left">Ignored objects</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">StructuralCrossSection;StructuralPointAction</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">
        <p>Field used for update work-flow</p>
        <p>Specify the object(s) that should be excluded from update</p>
        <p>Multiple objects are divided by a semicolon</p>
        <p>See notes for all SAF objects
          <br />
        </p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Ignored groups</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">SupportsAndHinges;StructuralLoad</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">
        <p>Field used for update work-flow</p>
        <p>Specify the groups(s) that should be excluded from update</p>
        <p>Groups are parent to objects - each group consists of multiple objects</p>
        <p>Multiple groups are divided by a semicolon</p>
        <p>See notes for all SAF groups</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Id</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">bba1ede8-4106-47fd-b5e1-48637ab87f47</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">ID of model.</td>
    </tr>
  </tbody>
</table>

