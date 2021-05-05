# StructuralLoadCombination

## Load Combination

Object serves for definition a load combination. The combination is created from the existing load cases in the model, in [StructuralLoadCase](structuralloadcase.md#load-case) sheet.

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
      <td style="text-align:center">COM1</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Human readable unique name of the object</td>
    </tr>
    <tr>
      <td style="text-align:center">Description</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">varibale_1 + dead load</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">The description of the load combination</td>
    </tr>
    <tr>
      <td style="text-align:center">Category</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>ULS (Ultimate Limit State)</p>
        <p></p>
        <p>SLS (Serviceability Limit State)</p>
        <p></p>
        <p>ALS (Accidental Limit State)</p>
        <p></p>
        <p>According national standard</p>
        <p></p>
        <p>Not defined</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">The category of the load combination</td>
    </tr>
    <tr>
      <td style="text-align:center">National standard</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>EN-ULS(STR/GEO) Set B</p>
        <p></p>
        <p>EN-ULS (STR/GEO) Set C</p>
        <p></p>
        <p>EN-Accidental 1</p>
        <p></p>
        <p>EN-Accidental 2</p>
        <p></p>
        <p>EN-Seismic</p>
        <p></p>
        <p>EN-SLS</p>
        <p></p>
        <p>Characteristic</p>
        <p></p>
        <p>EN-SLS Frequent</p>
        <p></p>
        <p>EN-SLS Quasi-permanent</p>
        <p></p>
        <p>IBC-LRFD ultimate</p>
        <p></p>
        <p>IBC-ASD ultimate</p>
        <p></p>
        <p>IBC-ASD serviceability</p>
        <p></p>
        <p>IBC-ASD seismic</p>
        <p></p>
        <p>IBC-LRFD seismic</p>
      </td>
      <td style="text-align:center">Yes, If Category =According national standard</td>
      <td style="text-align:left">The National code application</td>
    </tr>
    <tr>
      <td style="text-align:center">Load factor #</td>
      <td style="text-align:center">double</td>
      <td style="text-align:center">1,35</td>
      <td style="text-align:center">yes, If Category in not &quot;According national standard&quot;</td>
      <td
      style="text-align:left">Load factor of the load case. # means indexing of the Load factor column,
        e.g. Load factor 1, Load factor 2, &#x2026; Load factor 99. It depends
        on how many load case is considered in combination.</td>
    </tr>
    <tr>
      <td style="text-align:center">Multiplier #</td>
      <td style="text-align:center">double</td>
      <td style="text-align:center">0,9</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">A multiplier for e.g. increase the selfweight of the structure . # means
        indexing of the Multiplier column, e.g. Multiplier 1, Multiplier 2, &#x2026;
        Multiplier 99. It depends on how many load case is considered in combination.</td>
    </tr>
    <tr>
      <td style="text-align:center">Load case name #</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">LC1</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Valid name of the load case (<a href="structuralloadcase.md#load-case">StructuralLoadCase</a>).
        # means indexing of the load case name column, e.g. Load case name 1, Load
        case name 2, &#x2026; load case name 99. It depends on how many load case
        is considered in combination.</td>
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

