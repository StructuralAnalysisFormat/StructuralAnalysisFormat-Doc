# StructuralMaterial

## Material

Material is the basic entity affecting the behaviour of the structure. It is subsequently applied to a chosen profile \([StructuralCrossSection](structuralcrosssection.md)\). The user can use a pre-defined material or change the properties to get a custom one. The predefined materials correspond to materials defined in particular technical codes.The specification in excel:

### Specification in excel:

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
      <td style="text-align:center">S235</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Human readable unique name of the material *see notes</td>
    </tr>
    <tr>
      <td style="text-align:center">Type</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>Concrete</p>
        <p></p>
        <p>Steel</p>
        <p></p>
        <p>Timber</p>
        <p></p>
        <p>Aluminium</p>
        <p></p>
        <p>Masonry</p>
        <p></p>
        <p>Other</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">The type of material</td>
    </tr>
    <tr>
      <td style="text-align:center">Subtype</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">Hot rolled</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">The subtype of the material, e.g. hot rolled, cold formed, stainless steel,
        prestressed concrete, fiber-reinforced concrete, UHPC etc.</td>
    </tr>
    <tr>
      <td style="text-align:center">Quality</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">S235</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">
        <p>The quality grade of the material. Use a commonly known naming of grades
          of specific structural material. Example:</p>
        <p>Steel - S235, S275, S355...</p>
        <p>Concrete - C16/20, C25/30, C30/35...</p>
        <p>Timber - C18, C22, D18...</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Unit mass [kg/m3]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">7850</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Self-weight of the material</td>
    </tr>
    <tr>
      <td style="text-align:center">E modulus [MPa]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">210000</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Young&apos;s modulus of elasticity</td>
    </tr>
    <tr>
      <td style="text-align:center">G modulus [MPa]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">12500</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Shear modulus</td>
    </tr>
    <tr>
      <td style="text-align:center">Poisson Coefficient</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">0,2</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Poisson coefficient</td>
    </tr>
    <tr>
      <td style="text-align:center">Thermal expansion [1/K]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">0,000012</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">The coefficient of thermal expansion of the material</td>
    </tr>
    <tr>
      <td style="text-align:center">Design properties</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">1|1.1; 2|4.8; 9|1100</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Custom design characteristics of the material. The format of the data
        has to follow this convention: &quot;label of the design property&quot;
        &quot;|&quot; &quot;value of the design property&quot; The list of available
        properties with indexes can be found in Annex.</td>
    </tr>
    <tr>
      <td style="text-align:center">Id</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">6bbd256e-0225-4ee5-91e5-c7ef791a33cb</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Unique attribute designation</td>
    </tr>
    <tr>
      <td style="text-align:center">Poisson Coefficient</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">0,2</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Poisson coefficient</td>
    </tr>
    <tr>
      <td style="text-align:center">Thermal expansion [1/K]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">0,000012</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">The coefficient of thermal expansion of the material</td>
    </tr>
    <tr>
      <td style="text-align:center">Design properties</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">1|1.1; 2|4.8; 9|1100</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Custom design characteristics of the material. The format of the data
        has to follow this convention: &quot;label of the design property&quot;
        &quot;|&quot; &quot;value of the design property&quot; The list of available
        properties with indexes can be found in Annex.</td>
    </tr>
    <tr>
      <td style="text-align:center">Id</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">6bbd256e-0225-4ee5-91e5-c7ef791a33cb</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Unique attribute designation</td>
    </tr>
  </tbody>
</table>

## Notes

{% hint style="info" %}
"**Name**" is recommended to set the same as the "**Quality**" of the defined material.
{% endhint %}

