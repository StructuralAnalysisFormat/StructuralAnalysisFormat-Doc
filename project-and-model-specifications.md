# Project and model specifications

{% hint style="warning" %}
Structure of sheets "Project" and "Model" is different from all the other sheets. Properties are oriented in columns not in rows as usual.
{% endhint %}

## Project

In the list called “Project”, you can specify basic information about your project.

The specification in excel:

| Name of the row | Type of data | Value example or enum definition | Required value | Description |
| :--- | :---: | :---: | :---: | :--- |
| Name | String | Park Office | no | The name of the project |
| Description | String | Administrative complex | no | The description of the project |
| Project nr | String | 23/2019 | no | Project numerical designation |
| Created | Date Time | 16.12.2018 15:48 | no | Creation time, in UTC, in format yyyy-mm-dd hh:mm |
| Last update | Date Time | 23.12.2018 23:58 | no | Last update time, in UTC, in format yyyy-mm-dd hh:mm |
| Project type | String | Building construction | no | The type of the project. The project type can be assigned to e.g. "Building construction" or "Infrastructure construction" |
| Project kind | String | New building | no | The kind of the project. The project kind can be assigned to e.g. "Extension", "Finish", "New building", "Reconstruction" |
| Building type | String | Business | no | Kind of use of the building such as Administrative, Residential, etc… |
| Status | String | Planning stage | no | Status of the project |
| Location | String | South Bohemia | no | Location of the designed project |
| Id | String | bba1ede8-4106-47fd-b5e1-48637ab87f47 | no | ID of project. |

## Model

In the list called “model” you can specify basic info about your project.

The specification in excel:

<table style="mc-table-style: url('Resources/TableStyles/NewStyle.css');" class="TableStyle-NewStyle" cellspacing="6">
            <col style="width: 155px;" class="TableStyle-NewStyle-Column-Column1" />
            <col style="width: 181px;" class="TableStyle-NewStyle-Column-Column1" />
            <col style="width: 254px;" class="TableStyle-NewStyle-Column-Column1" />
            <col style="width: 254px;" class="TableStyle-NewStyle-Column-Column1" />
            <col style="width: 557px;" class="TableStyle-NewStyle-Column-Column1" />
            <tbody>
                <tr class="TableStyle-NewStyle-Body-Body1">
                    <td style="background-color: #0f486e;color: #ffffff;font-size: 11pt;vertical-align: middle;" class="TableStyle-NewStyle-BodyE-Column1-Body1">
                        <p style="color: #ffffff;text-align: center;padding-left: 4px;padding-right: 4px;">Name
						of the row</p>
                    </td>
                    <td style="background-color: #0f486e;color: #ffffff;font-size: 11pt;vertical-align: middle;" class="TableStyle-NewStyle-BodyE-Column1-Body1">
                        <p style="text-align: center;padding-left: 4px;padding-right: 4px;color: #ffffff;">Type
						of data</p>
                    </td>
                    <td style="background-color: #0f486e;color: #ffffff;font-size: 11pt;vertical-align: middle;" class="TableStyle-NewStyle-BodyE-Column1-Body1">
                        <p style="text-align: center;padding-left: 4px;padding-right: 4px;color: #ffffff;">Value
						example or enum definition</p>
                    </td>
                    <td style="background-color: #0f486e;color: #ffffff;font-size: 11pt;vertical-align: middle;" class="TableStyle-NewStyle-BodyE-Column1-Body1">
                        <p style="color: #ffffff;padding-left: 4px;padding-right: 4px;text-align: center;">Required value</p>
                    </td>
                    <td style="background-color: #0f486e;color: #ffffff;font-size: 11pt;vertical-align: middle;" class="TableStyle-NewStyle-BodyD-Column1-Body1">
                        <p style="color: #ffffff;padding-left: 4px;padding-right: 4px;text-align: left;">Description</p>
                    </td>
                </tr>
                <tr class="TableStyle-NewStyle-Body-Body2">
                    <td style="text-align: center;font-size: 9pt;" class="TableStyle-NewStyle-BodyE-Column1-Body2">Name</td>
                    <td style="font-size: 9pt;text-align: center;" class="TableStyle-NewStyle-BodyE-Column1-Body2">String</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body2" style="font-size: 9pt;">Park Office - object A</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body2" style="font-size: 9pt;">no</td>
                    <td class="TableStyle-NewStyle-BodyD-Column1-Body2" style="font-size: 9pt;text-align: left;">The name of the model</td>
                </tr>
                <tr class="TableStyle-NewStyle-Body-Body1">
                    <td style="text-align: center;font-size: 9pt;" class="TableStyle-NewStyle-BodyE-Column1-Body1">Description</td>
                    <td style="font-size: 9pt;text-align: center;" class="TableStyle-NewStyle-BodyE-Column1-Body1">String</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body1" style="font-size: 9pt;">Highrise</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body1" style="font-size: 9pt;">no</td>
                    <td class="TableStyle-NewStyle-BodyD-Column1-Body1" style="font-size: 9pt;text-align: left;">The description of the model</td>
                </tr>
                <tr class="TableStyle-NewStyle-Body-Body2">
                    <td style="text-align: center;font-size: 9pt;" class="TableStyle-NewStyle-BodyE-Column1-Body2">Discipline</td>
                    <td style="font-size: 9pt;text-align: center;" class="TableStyle-NewStyle-BodyE-Column1-Body2">String</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body2" style="font-size: 9pt;">Load-bearing structure</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body2" style="font-size: 9pt;">no</td>
                    <td class="TableStyle-NewStyle-BodyD-Column1-Body2" style="font-size: 9pt;text-align: left;">Discipline can be set as Undefined, Architecture, HVAC, Load-bearing structure, Terrain, Facility etc.</td>
                </tr>
                <tr class="TableStyle-NewStyle-Body-Body1" style="height: 9px;">
                    <td style="text-align: center;font-size: 9pt;" class="TableStyle-NewStyle-BodyE-Column1-Body1">Level of detail</td>
                    <td style="font-size: 9pt;text-align: center;" class="TableStyle-NewStyle-BodyE-Column1-Body1">String</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body1" style="font-size: 9pt;">Draft</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body1" style="font-size: 9pt;">no</td>
                    <td class="TableStyle-NewStyle-BodyD-Column1-Body1" style="font-size: 9pt;text-align: left;">Describe level of detail of the model</td>
                </tr>
                <tr class="TableStyle-NewStyle-Body-Body2">
                    <td style="text-align: center;font-size: 9pt;" class="TableStyle-NewStyle-BodyE-Column1-Body2">Status</td>
                    <td style="font-size: 9pt;text-align: center;" class="TableStyle-NewStyle-BodyE-Column1-Body2">String</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body2" style="font-size: 9pt;">Planning stage</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body2" style="font-size: 9pt;">no</td>
                    <td class="TableStyle-NewStyle-BodyD-Column1-Body2" style="font-size: 9pt;text-align: left;">Description of model status</td>
                </tr>
                <tr class="TableStyle-NewStyle-Body-Body1">
                    <td style="text-align: center;font-size: 9pt;" class="TableStyle-NewStyle-BodyE-Column1-Body1">Owner</td>
                    <td style="font-size: 9pt;text-align: center;" class="TableStyle-NewStyle-BodyE-Column1-Body1">String</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body1" style="font-size: 9pt;">Person A</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body1" style="font-size: 9pt;">no</td>
                    <td class="TableStyle-NewStyle-BodyD-Column1-Body1" style="font-size: 9pt;text-align: left;">Define the owner of the model</td>
                </tr>
                <tr class="TableStyle-NewStyle-Body-Body2">
                    <td style="text-align: center;font-size: 9pt;" class="TableStyle-NewStyle-BodyE-Column1-Body2">Revision number</td>
                    <td style="font-size: 9pt;text-align: center;" class="TableStyle-NewStyle-BodyE-Column1-Body2">String</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body2" style="font-size: 9pt;">rev.02</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body2" style="font-size: 9pt;">no</td>
                    <td class="TableStyle-NewStyle-BodyD-Column1-Body2" style="font-size: 9pt;text-align: left;">Current revision number</td>
                </tr>
                <tr class="TableStyle-NewStyle-Body-Body1">
                    <td style="text-align: center;font-size: 9pt;" class="TableStyle-NewStyle-BodyE-Column1-Body1">Created</td>
                    <td style="font-size: 9pt;text-align: center;" class="TableStyle-NewStyle-BodyE-Column1-Body1">Date Time</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body1" style="font-size: 9pt;">2018-12-16</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body1" style="font-size: 9pt;">no</td>
                    <td class="TableStyle-NewStyle-BodyD-Column1-Body1" style="font-size: 9pt;text-align: left;">Creation time, in UTC, in ISO format year-month-day</td>
                </tr>
                <tr class="TableStyle-NewStyle-Body-Body2">
                    <td style="text-align: center;font-size: 9pt;" class="TableStyle-NewStyle-BodyE-Column1-Body2">Last update</td>
                    <td style="font-size: 9pt;text-align: center;" class="TableStyle-NewStyle-BodyE-Column1-Body2">Date Time</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body2" style="font-size: 9pt;">2018-12-19</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body2" style="font-size: 9pt;">no</td>
                    <td class="TableStyle-NewStyle-BodyD-Column1-Body2" style="font-size: 9pt;text-align: left;">Last update time, in UTC, in ISO format year-month-day</td>
                </tr>
                <tr class="TableStyle-NewStyle-Body-Body1">
                    <td style="text-align: center;font-size: 9pt;" class="TableStyle-NewStyle-BodyE-Column1-Body1">Source type</td>
                    <td style="font-size: 9pt;text-align: center;" class="TableStyle-NewStyle-BodyE-Column1-Body1">String</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body1" style="font-size: 9pt;">Structural analysis model</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body1" style="font-size: 9pt;">no</td>
                    <td class="TableStyle-NewStyle-BodyD-Column1-Body1" style="font-size: 9pt;text-align: left;">Definition of the source data</td>
                </tr>
                <tr class="TableStyle-NewStyle-Body-Body2">
                    <td style="text-align: center;font-size: 9pt;" class="TableStyle-NewStyle-BodyE-Column1-Body2">Source application</td>
                    <td style="font-size: 9pt;text-align: center;" class="TableStyle-NewStyle-BodyE-Column1-Body2">String</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body2" style="font-size: 9pt;">Scia Engineer</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body2" style="font-size: 9pt;">no</td>
                    <td class="TableStyle-NewStyle-BodyD-Column1-Body2" style="font-size: 9pt;text-align: left;">Definition of the source application </td>
                </tr>
                <tr class="TableStyle-NewStyle-Body-Body1">
                    <td style="text-align: center;font-size: 9pt;" class="TableStyle-NewStyle-BodyE-Column1-Body1">SAF Version</td>
                    <td style="font-size: 9pt;text-align: center;" class="TableStyle-NewStyle-BodyE-Column1-Body1">String</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body1" style="font-size: 9pt;">1.0.3</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body1" style="font-size: 9pt;">yes</td>
                    <td class="TableStyle-NewStyle-BodyD-Column1-Body1" style="font-size: 9pt;text-align: left;">Definition of used version of the Structural Analysis Format</td>
                </tr>
                <tr class="TableStyle-NewStyle-Body-Body2">
                    <td style="text-align: center;font-size: 9pt;" class="TableStyle-NewStyle-BodyE-Column1-Body2">Source company</td>
                    <td style="font-size: 9pt;text-align: center;" class="TableStyle-NewStyle-BodyE-Column1-Body2">String</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body2" style="font-size: 9pt;">Statical company</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body2" style="font-size: 9pt;">no</td>
                    <td class="TableStyle-NewStyle-BodyD-Column1-Body2" style="font-size: 9pt;text-align: left;">Define the author company of source data</td>
                </tr>
                <tr class="TableStyle-NewStyle-Body-Body1">
                    <td style="text-align: center;font-size: 9pt;" class="TableStyle-NewStyle-BodyE-Column1-Body1">Global coordinate system</td>
                    <td style="font-size: 9pt;text-align: center;" class="TableStyle-NewStyle-BodyE-Column1-Body1">Enum</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body1" style="font-size: 9pt;">
                        <p>X vertical</p>
                        <p>Y vertical</p>
                        <p>Z vertical</p>
                        <p>minus X vertical </p>
                        <p>minus Y vertical</p>
                        <p>minus Z vertical</p>
                    </td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body1" style="font-size: 9pt;">yes</td>
                    <td class="TableStyle-NewStyle-BodyD-Column1-Body1" style="font-size: 9pt;text-align: left;">
                        <p>Define the space orientation of the coordinates system for model</p>
                        <p>Right hand rule applies all the time.</p>
                        <p>X vertical - X axis goes against gravity</p>
                        <p>Y vertical - Y axis goes against gravity</p>
                        <p>Z vertical - Z axis goes against gravity</p>
                        <p>minus X vertical - X axis goes in direction of gravity</p>
                        <p>minus Y vertical - Y axis goes in direction of  gravity</p>
                        <p>minus Z vertical - Z axis goes in direction of  gravity</p>
                        <p>* For further explanation see notes below<br /></p>
                    </td>
                </tr>
                <tr class="TableStyle-NewStyle-Body-Body2">
                    <td style="text-align: center;font-size: 9pt;" class="TableStyle-NewStyle-BodyE-Column1-Body2">LCS&#160;of cross-section</td>
                    <td style="font-size: 9pt;text-align: center;" class="TableStyle-NewStyle-BodyE-Column1-Body2">Enum</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body2" style="font-size: 9pt;">
                        <p>ZYX</p>
                        <p>MinusYZX</p>
                        <p>MinusZMinusYX</p>
                        <p>YMinusZX</p>
                        <p>YZMinusX</p>
                        <p>MinusZYMinusX</p>
                        <p>MinusYMinusZMinusX</p>
                        <p>ZMinusYMinusX</p>
                    </td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body2" style="font-size: 9pt;">yes</td>
                    <td class="TableStyle-NewStyle-BodyD-Column1-Body2" style="font-size: 9pt;text-align: left;">
                        <p>Define the LCS orientation of used cross-section. </p>
                        <p>With row "LCS of cross-section" the user is able to define, how the LCS of cross section is defined in his software. This will give opportunity to receiving application of SAF file to correctly interpret LCS of cross section with different standard. The x-axis is always in the centre line and all possible cases are described by this enum.</p>
                        <p>For further explanation see notes below</p>
                    </td>
                </tr>
                <tr class="TableStyle-NewStyle-Body-Body1">
                    <td style="text-align: center;font-size: 9pt;" class="TableStyle-NewStyle-BodyE-Column1-Body1">System of units</td>
                    <td style="font-size: 9pt;text-align: center;" class="TableStyle-NewStyle-BodyE-Column1-Body1">Enum</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body1" style="font-size: 9pt;">
                        <p>Metric</p>
                        <p>Imperial</p>
                    </td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body1" style="font-size: 9pt;">yes</td>
                    <td class="TableStyle-NewStyle-BodyD-Column1-Body1" style="font-size: 9pt;text-align: left;">Define the type of units system used in model</td>
                </tr>
                <tr class="TableStyle-NewStyle-Body-Body2">
                    <td style="text-align: center;font-size: 9pt;" class="TableStyle-NewStyle-BodyE-Column1-Body2">National code</td>
                    <td style="font-size: 9pt;text-align: center;" class="TableStyle-NewStyle-BodyE-Column1-Body2">Enum</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body2" style="font-size: 9pt;">
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
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body2" style="font-size: 9pt;">yes</td>
                    <td class="TableStyle-NewStyle-BodyD-Column1-Body2" style="font-size: 9pt;text-align: left;">Sets national code used for structural analysis</td>
                </tr>
                <tr class="TableStyle-NewStyle-Body-Body1">
                    <td style="text-align: center;font-size: 9pt;" class="TableStyle-NewStyle-BodyE-Column1-Body1">Ignored objects</td>
                    <td style="font-size: 9pt;text-align: center;" class="TableStyle-NewStyle-BodyE-Column1-Body1">String</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body1" style="font-size: 9pt;"> StructuralCrossSection;StructuralPointAction</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body1" style="font-size: 9pt;">no</td>
                    <td class="TableStyle-NewStyle-BodyD-Column1-Body1" style="font-size: 9pt;text-align: left;">
                        <p style="font-size: 9pt;">Field used for update work-flow</p>
                        <p style="font-size: 9pt;">Specify the object(s) that should be excluded from update</p>
                        <p style="font-size: 9pt;">Multiple objects are divided by a semicolon</p>
                        <p style="font-size: 9pt;">See notes for all SAF objects<br /></p>
                    </td>
                </tr>
                <tr class="TableStyle-NewStyle-Body-Body2">
                    <td style="text-align: center;font-size: 9pt;" class="TableStyle-NewStyle-BodyE-Column1-Body2">Ignored groups</td>
                    <td style="font-size: 9pt;text-align: center;" class="TableStyle-NewStyle-BodyE-Column1-Body2">String</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body2" style="font-size: 9pt;">SupportsAndHinges;StructuralLoad</td>
                    <td class="TableStyle-NewStyle-BodyE-Column1-Body2" style="font-size: 9pt;">no</td>
                    <td class="TableStyle-NewStyle-BodyD-Column1-Body2" style="font-size: 9pt;text-align: left;">
                        <p style="font-size: 9pt;">Field used for update work-flow</p>
                        <p style="font-size: 9pt;">Specify the groups(s) that should be excluded from update</p>
                        <p style="font-size: 9pt;">Groups are parent to objects - each group consists of multiple objects</p>
                        <p style="font-size: 9pt;">Multiple groups are divided by a semicolon</p>
                        <p style="font-size: 9pt;">See notes for all SAF groups</p>
                    </td>
                </tr>
                <tr class="TableStyle-NewStyle-Body-Body1">
                    <td style="text-align: center;font-size: 9pt;" class="TableStyle-NewStyle-BodyB-Column1-Body1">Id</td>
                    <td style="font-size: 9pt;text-align: center;" class="TableStyle-NewStyle-BodyB-Column1-Body1">String</td>
                    <td class="TableStyle-NewStyle-BodyB-Column1-Body1" style="font-size: 9pt;">bba1ede8-4106-47fd-b5e1-48637ab87f47</td>
                    <td class="TableStyle-NewStyle-BodyB-Column1-Body1" style="font-size: 9pt;">no</td>
                    <td class="TableStyle-NewStyle-BodyA-Column1-Body1" style="font-size: 9pt;text-align: left;">
                        <p>ID of model.</p>
                    </td>
                </tr>
            </tbody>
        </table>
