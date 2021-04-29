# Project and model specifications

{% hint style="warning" %}
Structure of sheets "Project" and "Model" is different from all the other sheets. Properties are oriented in columns not in rows as usual.
{% endhint %}

## Project

In the list called “Project”, you can specify basic information about your project.

The specification in excel:

| Name of the row | Type of data | Value example or enum definition | Required value | Description |
| :---: | :---: | :---: | :---: | :---: |
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

<table>
  <thead>
    <tr>
      <th style="text-align:centre">
        <p>Name of the row
          <br />
        </p>
        <p>
          <br />
        </p>
      </th>
      <th style="text-align:centre">
        <p>Type of data
          <br />
        </p>
        <p>
          <br />
        </p>
      </th>
      <th style="text-align:centre">
        <p>Value example or enum definition
          <br />
        </p>
        <p>
          <br />
        </p>
      </th>
      <th style="text-align:centre">
        <p>Required value
          <br />
        </p>
        <p>
          <br />
        </p>
      </th>
      <th style="text-align:centre">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:centre">Name</td>
      <td style="text-align:centre">String</td>
      <td style="text-align:centre">Park Office - object A</td>
      <td style="text-align:centre">no</td>
      <td style="text-align:centre">The name of the model
        <br />
      </td>
    </tr>
    <tr>
      <td style="text-align:centre">Description</td>
      <td style="text-align:centre">String</td>
      <td style="text-align:centre">Highrise</td>
      <td style="text-align:centre">no</td>
      <td style="text-align:centre">The name of the model
        <br />
      </td>
    </tr>
    <tr>
      <td style="text-align:centre">Discipline</td>
      <td style="text-align:centre">String</td>
      <td style="text-align:centre">Load-bearing structure</td>
      <td style="text-align:centre">no</td>
      <td style="text-align:centre">Discipline can be set as Undefined, Architecture, HVAC, Load-bearing structure,
        Terrain, Facility etc.
        <br />
      </td>
    </tr>
  </tbody>
</table>

