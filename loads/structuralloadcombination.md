# StructuralLoadCombination

## Load Combination

Object serves for definition a load combination. The combination is created from the existing load cases in the model, in [StructuralLoadCase](structuralloadcase.md#load-case) sheet.

Specification in the excel:

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
      <td style="text-align:left">COM1</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Human readable unique name of the object</td>
    </tr>
    <tr>
      <td style="text-align:left">Description</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">varibale_1 + dead load</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">The description of the load combination</td>
    </tr>
    <tr>
      <td style="text-align:left">Category</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>ULS (Ultimate Limit State)</p>
        <p>SLS (Serviceability Limit State)</p>
        <p>ALS (Accidental Limit State)</p>
        <p>According national standard</p>
        <p>Not defined</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">The category of the load combination</td>
    </tr>
    <tr>
      <td style="text-align:left">National standard</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>EN-ULS(STR/GEO) Set B</p>
        <p>EN-ULS (STR/GEO) Set C</p>
        <p>EN-Accidental 1</p>
        <p>EN-Accidental 2</p>
        <p>EN-Seismic</p>
        <p>EN-SLS</p>
        <p>Characteristic</p>
        <p>EN-SLS Frequent</p>
        <p>EN-SLS Quasi-permanent</p>
        <p>IBC-LRFD ultimate</p>
        <p>IBC-ASD ultimate</p>
        <p>IBC-ASD serviceability</p>
        <p>IBC-ASD seismic</p>
        <p>IBC-LRFD seismic</p>
      </td>
      <td style="text-align:left">Yes, If Category =According national standard</td>
      <td style="text-align:left">The National code application</td>
    </tr>
    <tr>
      <td style="text-align:left">Load factor #</td>
      <td style="text-align:left">double</td>
      <td style="text-align:left">1,35</td>
      <td style="text-align:left">yes, If Category in not &quot;According national standard&quot;</td>
      <td
      style="text-align:left">Load factor of the load case. # means indexing of the Load factor column,
        e.g. Load factor 1, Load factor 2, &#x2026; Load factor 99. It depends
        on how many load case is considered in combination.</td>
    </tr>
    <tr>
      <td style="text-align:left">Multiplier #</td>
      <td style="text-align:left">double</td>
      <td style="text-align:left">0,9</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">A multiplier for e.g. increase the selfweight of the structure . # means
        indexing of the Multiplier column, e.g. Multiplier 1, Multiplier 2, &#x2026;
        Multiplier 99. It depends on how many load case is considered in combination.</td>
    </tr>
    <tr>
      <td style="text-align:left">Load case name #</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">LC1</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Valid name of the load case (<a href="structuralloadcase.md#load-case">StructuralLoadCase</a>).
        # means indexing of the load case name column, e.g. Load case name 1, Load
        case name 2, &#x2026; load case name 99. It depends on how many load case
        is considered in combination.</td>
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

