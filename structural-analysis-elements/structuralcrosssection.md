# StructuralCrossSection

## Cross-section

A cross-section together with material \([StructuralMaterial](structuralmaterial.md#material)\) is a basic property of a 1D member. Various kinds of shapes can be defined, including steel rolled sections, timber specific cross-sections or general geometric sections. Supported shapes of cross-sections are defined in documents Formcodes and Description ID of the profile, in chapter Annexes in this document.

Specification in excel:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Name of&nbsp;&nbsp;&nbsp;the column header</th>
    <th class="tg-0pky">Type of data</th>
    <th class="tg-0pky">Value example or enum definition</th>
    <th class="tg-0pky">Required value</th>
    <th class="tg-0pky">Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-c3ow">Name</td>
    <td class="tg-c3ow">String</td>
    <td class="tg-c3ow">CS1</td>
    <td class="tg-c3ow">yes</td>
    <td class="tg-0pky">Human readable unique name of the Cross-section</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Material</td>
    <td class="tg-c3ow">String</td>
    <td class="tg-c3ow">MAT1</td>
    <td class="tg-c3ow">yes</td>
    <td class="tg-0pky">Name reference to the existing StructuralMaterial object. The&nbsp;&nbsp;&nbsp;general type of cross-section can have more than one materials. Each material&nbsp;&nbsp;&nbsp;name is separated by a semicolon.</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Cross-section type</td>
    <td class="tg-c3ow">Enum</td>
    <td class="tg-c3ow">Parametric<br>Manufactured<br>Compound<br>General</td>
    <td class="tg-c3ow">yes</td>
    <td class="tg-0pky">Define type of profile library:<br><br>General: Serves to define any general shape of the cross-section consisting   of one or more closed polygons including openings. <br>Shape of the cross-section   (polygons) is defined on separate sheet "CompositeShapeDef"<br><br>Parametric: Cross-sections defined by shape and dimensions (parameters).<br><br>Manufactured: This option refers to the industrially manufactured cross-sections.<br><br>Compound: prepared for compounded section fom more manufactured profiles<br>e.g. for two I-sections. Example of compound cross-section input: <br>profile =   IPE200 and parameters=10mm (distance between profiles). <br>All supported shapes of compound section can be found in Annex<br></td>
  </tr>
  <tr>
    <td class="tg-c3ow">Shape</td>
    <td class="tg-c3ow">Enum</td>
    <td class="tg-c3ow">T Section</td>
    <td class="tg-c3ow">yes, if Cross-section type =   Parametricyes, <br>yes, if Cross-section type = Compound</td>
    <td class="tg-0pky">This field defines geometrical&nbsp;&nbsp;&nbsp;shape of the cross-section, is required only if Cross-section type is not&nbsp;&nbsp;&nbsp;manufactured. Complete list of supported shapes is attached in Supported&nbsp;&nbsp;&nbsp;shapes of cross-section.</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Parameters [mm]</td>
    <td class="tg-c3ow">String</td>
    <td class="tg-c3ow">50; 80; 500; 450</td>
    <td class="tg-c3ow">yes, if Cross-section type = Parametricyes, <br>yes, if Cross-section type = Compound</td>
    <td class="tg-0pky">The parameters property is required only if Cross-section type&nbsp;&nbsp;&nbsp;is Parametric and it represents dimensions of the cross-section. The format&nbsp;&nbsp;&nbsp;of the parameters depends on cross-section shape. Each parameter has to be&nbsp;&nbsp;&nbsp;divided by a semicolon. Complete list of supported parameters is attached in&nbsp;&nbsp;&nbsp;Annex.</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Profile</td>
    <td class="tg-c3ow">String</td>
    <td class="tg-c3ow">HEB180</td>
    <td class="tg-c3ow">yes, if Cross-section type = Manufacturedyes, if Cross-section&nbsp;&nbsp;&nbsp;type = Compoundyes, if Cross-section type = General</td>
    <td class="tg-0pky">This field is required only if Cross-section type is&nbsp;&nbsp;&nbsp;Manufactured or Compound. Defines name of the industrially manufactured&nbsp;&nbsp;&nbsp;profile in the globally common format (naming).For Cross-section type =&nbsp;&nbsp;&nbsp;general, name reference to valid CompositeShapeDef object is required in the&nbsp;&nbsp;&nbsp;cell "Profile"</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Form code</td>
    <td class="tg-c3ow">Enum</td>
    <td class="tg-c3ow">1</td>
    <td class="tg-c3ow">yes, if Cross-section type = Manufactured</td>
    <td class="tg-0pky">This field is valid only if profile type is Manufactured. It&nbsp;&nbsp;&nbsp;helps to define hot rolled or cold formed profiles. The shape of the&nbsp;&nbsp;&nbsp;cross-section is uniquely identified by a so-called Formcode. The&nbsp;&nbsp;&nbsp;Formcodedefines the shape and in some cases also additional parameters like&nbsp;&nbsp;&nbsp;distance between bolt holes, unit warping coordinates etc. Complete list of&nbsp;&nbsp;&nbsp;supported form codes is attached in Formcodes.</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Description ID of the profile</td>
    <td class="tg-c3ow">Enum</td>
    <td class="tg-c3ow">2</td>
    <td class="tg-c3ow">no</td>
    <td class="tg-0pky">This field is valid only if the cross-section type is&nbsp;&nbsp;&nbsp;Manufactured. The description of the hot rolled and cold formed cross-section&nbsp;&nbsp;&nbsp;referring to the source of manufacturer. Complete list  is attached in Description ID of the&nbsp;&nbsp;&nbsp;profile.</td>
  </tr>
  <tr>
    <td class="tg-c3ow">A [m2]</td>
    <td class="tg-c3ow">Double</td>
    <td class="tg-c3ow">0,075484</td>
    <td class="tg-c3ow">no</td>
    <td class="tg-0pky">Section area</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Iy [m4]</td>
    <td class="tg-c3ow">Double</td>
    <td class="tg-c3ow">0,000641</td>
    <td class="tg-c3ow">no</td>
    <td class="tg-0pky">Moment of inertia about y-axis</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Iz [m4]</td>
    <td class="tg-c3ow">Double</td>
    <td class="tg-c3ow">0,013319</td>
    <td class="tg-c3ow">no</td>
    <td class="tg-0pky">Moment of inertia about z-axis</td>
  </tr>
  <tr>
    <td class="tg-c3ow">It [m4]</td>
    <td class="tg-c3ow">Double</td>
    <td class="tg-c3ow">0,0000591</td>
    <td class="tg-c3ow">no</td>
    <td class="tg-0pky">Torsion moment of inertia</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Iw[m6]</td>
    <td class="tg-c3ow">Double</td>
    <td class="tg-c3ow">0,00015548</td>
    <td class="tg-c3ow">no</td>
    <td class="tg-0pky">Warping constant</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Wply [m3]</td>
    <td class="tg-c3ow">Double</td>
    <td class="tg-c3ow">0,029497</td>
    <td class="tg-c3ow">no</td>
    <td class="tg-0pky">Plastic modulus about the y-axis</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Wplz [m3]</td>
    <td class="tg-c3ow">Double</td>
    <td class="tg-c3ow">0,029497</td>
    <td class="tg-c3ow">no</td>
    <td class="tg-0pky">Plastic modulus about the z-axis</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Id</td>
    <td class="tg-c3ow">String</td>
    <td class="tg-c3ow">6bbd256e-0225-4ee5-91e5-c7ef791a33cb</td>
    <td class="tg-c3ow">no</td>
    <td class="tg-0pky">Unique attribute designation</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Id</td>
    <td class="tg-c3ow">String</td>
    <td class="tg-c3ow">6bbd256e-0225-4ee5-91e5-c7ef791a33cb</td>
    <td class="tg-c3ow">no</td>
    <td class="tg-0pky">Unique attribute designation</td>
  </tr>
</tbody>
</table>

## Notes

{% hint style="info" %}
"**Name**" is recommended to set the same as the "**Quality**" of the defined material.
{% endhint %}

