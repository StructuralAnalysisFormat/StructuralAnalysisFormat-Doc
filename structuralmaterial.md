# StructuralMaterial

## Material

Material is the basic entity affecting the behaviour of the structure. It is subsequently applied to a chosen profile \([StructuralCrossSection](structuralcrosssection.md)\). The user can use a pre-defined material or change the properties to get a custom one. The predefined materials correspond to materials defined in particular technical codes.The specification in excel:

Specification in excel:

| Name of the row | Type of data | Value example or enum definition | Required value | Description |
| :--- | :--- | :--- | :--- | :--- |
| Name | String | Park Office | no | The name of the project |
| Description | String | Administrative complex | no | The description of the project |
| Project nr | String | 23/2019 | no | Project numerical designation |
| Created | Date Time | 2018-12-16 15:48:50 | no | Creation time, in UTC, in format yyyy-mm-dd hh:mm |
| Last update | Date Time | 2018-12-23 23:58:59 | no | Last update time, in UTC, in format yyyy-mm-dd hh:mm |
| Project type | String | Building construction | no | The type of the project. The project type can be assigned to e.g. "Building construction" or "Infrastructure construction" |
| Project kind | String | New building | no | The kind of the project. The project kind can be assigned to e.g. "Extension", "Finish", "New building", "Reconstruction" |
| Building type | String | Business | no | Kind of use of the building such as Administrative, Residential, etc… |
| Status | String | Planning stage | no | Status of the project |
| Location | String | South Bohemia | no | Location of the designed project |
| Id | String | bba1ede8-4106-47fd-b5e1-48637ab87f50 | no | ID of project. |

## Notes

{% hint style="info" %}
 "**Name**" is recommended to set the same as the "**Quality**" of the defined material.  
{% endhint %}

