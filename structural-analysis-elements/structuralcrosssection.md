# StructuralCrossSection

## Cross-section

A cross-section together with material \([StructuralMaterial](structuralmaterial.md#material)\) is a basic property of a 1D member. Various kinds of shapes can be defined, including steel rolled sections, timber specific cross-sections or general geometric sections. Supported shapes of cross-sections are defined in documents Formcodes and Description ID of the profile, in chapter Annexes in this document.

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
      <td style="text-align:center">CS1</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Human readable unique name of the Cross-section</td>
    </tr>
    <tr>
      <td style="text-align:center">Material</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">MAT1</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">
        <p>Name reference to the existing StructuralMaterial object.</p>
        <p>The general type of cross-section can have more than one material.</p>
        <p>Each material name is separated by a semicolon.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Cross-section type</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>Parametric</p>
        <p>
          <br />Manufactured</p>
        <p>
          <br />Compound</p>
        <p>
          <br />General</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Define the type of profile library:
        <br />
        <br /><b>General</b>: Serves to define any general shape of the cross-section
        consisting of one or more closed polygons including openings.
        <br />Shape of the cross-section (polygons) is defined on separate sheet &quot;CompositeShapeDef&quot;
        <br
        />
        <br /><b>Parametric</b>: Cross-sections defined by shape and dimensions (parameters).
        <br
        />
        <br /><b>Manufactured</b>: This option refers to the industrially manufactured
        cross-sections.
        <br />
        <br /><b>Compound</b>: prepared for compounded section fom more manufactured
        profiles
        <br />e.g. for two I-sections. Example of compound cross-section input:
        <br />profile = IPE200 and parameters=10mm (distance between profiles).
        <br />All supported shapes of compound section can be found in Annex
        <br />
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Shape</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">T Section</td>
      <td style="text-align:center">
        <p>yes, if Cross-section type = Parametric</p>
        <p>yes, if Cross-section type = Compound</p>
      </td>
      <td style="text-align:left">
        <p>This field defines geometrical shape of the cross-section, is required
          only if Cross-section type is not manufactured.</p>
        <p>Complete list of supported shapes is attached in Supported shapes of cross-section.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Parameters [mm]</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">50; 80; 500; 450</td>
      <td style="text-align:center">
        <p>yes, if Cross-section type = Parametric
          <br />
        </p>
        <p>yes, if Cross-section type = Compound</p>
      </td>
      <td style="text-align:left">
        <p>The parameters property is required only if Cross-section type is Parametric
          and it represents dimensions of the cross-section. The format of the parameters
          depends on cross-section shape.</p>
        <p>Each parameter has to be divided by a semicolon.</p>
        <p>Complete list of supported parameters is attached in Annex.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Profile</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">HEB180</td>
      <td style="text-align:center">
        <p>yes, if Cross-section type = Manufactured</p>
        <p>yes, if Cross-section type = Compound</p>
        <p>yes, if Cross-section type = General</p>
      </td>
      <td style="text-align:left">
        <p>This field is required only if Cross-section type is Manufactured or Compound.</p>
        <p>Defines name of the industrially manufactured profile in the globally
          common format (naming).</p>
        <p>For Cross-section type = general, name reference to valid CompositeShapeDef
          object is required in the cell &quot;Profile&quot;</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Form code</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">1</td>
      <td style="text-align:center">yes, if Cross-section type = Manufactured</td>
      <td style="text-align:left">
        <p>This field is valid only if profile type is Manufactured. It helps to
          define hot rolled or cold formed profiles.</p>
        <p>The shape of the cross-section is uniquely identified by a so-called Formcode.</p>
        <p>The Formcode defines the shape and in some cases also additional parameters
          like distance between bolt holes, unit warping coordinates etc.</p>
        <p>Complete list of supported form codes is attached in Formcodes.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Description ID of the profile</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">2</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">This field is valid only if the cross-section type is Manufactured. The
        description of the hot rolled and cold formed cross-section referring to
        the source of manufacturer. Complete list is attached in Description ID
        of the profile.</td>
    </tr>
    <tr>
      <td style="text-align:center">A [m2]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">0,075484</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Section area</td>
    </tr>
    <tr>
      <td style="text-align:center">Iy [m4]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">0,000641</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Moment of inertia about y-axis</td>
    </tr>
    <tr>
      <td style="text-align:center">Iz [m4]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">0,013319</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Moment of inertia about z-axis</td>
    </tr>
    <tr>
      <td style="text-align:center">It [m4]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">0,0000591</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Torsion moment of inertia</td>
    </tr>
    <tr>
      <td style="text-align:center">Iw[m6]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">0,00015548</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Warping constant</td>
    </tr>
    <tr>
      <td style="text-align:center">Wply [m3]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">0,029497</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Plastic modulus about the y-axis</td>
    </tr>
    <tr>
      <td style="text-align:center">Wplz [m3]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">0,029497</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Plastic modulus about the z-axis</td>
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
The general cross-section shape definition and is represented as a separate sheet CompositeShapeDef in Excel. It is required when the cross-section type is "General".
{% endhint %}

