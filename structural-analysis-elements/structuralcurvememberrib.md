# StructuralCurveMemberRib

## 2D member rib

The 2D member rib is a 1D member related to slabs. The part of the slab which cooperates with the rib is called the effective width. Different values of effective widths can be considered for checks and for calculation of the internal forces.

![](../.gitbook/assets/13_structuralcurvememberrib.png)

### Specification in the excel:

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
      <td style="text-align:left">B1</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Human readable unique name of the rib</td>
    </tr>
    <tr>
      <td style="text-align:left">2D member</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">S1</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">The name of the structural surface member on which the rib is placed</td>
    </tr>
    <tr>
      <td style="text-align:left">Cross section</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">CS1</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">The name reference to the existing, valid name of the StructuralCrossSection
        object.</td>
    </tr>
    <tr>
      <td style="text-align:left">Nodes</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">N1;N2</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">All nodes that belong to the curve member and define its geometric shape.
        The names of the nodes are separated by ; (semicolon) and space. The order
        of the nodes has to be from beginning to end.</td>
    </tr>
    <tr>
      <td style="text-align:left">Segments</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">Line; Circular Arc</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Defines shape of the curve between two next nodes. Supported strings are:
        Line; Circular Arc; Parabolic arc; Bezier; Spline. The names are separated
        by ; (semicolon) and space.</td>
    </tr>
    <tr>
      <td style="text-align:left">Begin node</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">N1</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">The starting node of the 1D member. Has to be specified in the StructuralPointConnection
        sheet</td>
    </tr>
    <tr>
      <td style="text-align:left">End node</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">N2</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">The end node of the 1D member. Has to be specified in the StructuralPointConnection
        sheet</td>
    </tr>
    <tr>
      <td style="text-align:left">Internal nodes</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">N17; N18</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">Internal nodes belonging to StructuralCurveMemberRib defined in StructuralPointConnection
        Internal nodes are not geometry defining The names of the nodes are separated
        by ; (semicolon) and space</td>
    </tr>
    <tr>
      <td style="text-align:left">Length [m]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">5,37</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">Distance between begin and end node of the curve member in meters</td>
    </tr>
    <tr>
      <td style="text-align:left">Geometrical shape</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>Line</p>
        <p>Circular Arc</p>
        <p>Parabolic Arc</p>
        <p>Bezier</p>
        <p>Spline</p>
        <p>Polyline</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Description of the geometrical type of curve member in general. If the
        member consists of more than one segments, Geometrical shape is automatically
        set to Polyline.</td>
    </tr>
    <tr>
      <td style="text-align:left">Alignment</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>Bottom</p>
        <p>Centre</p>
        <p>Top</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">This property item determines the position of the system-lines on the
        cross-section of the rib. The user defined value - custom value defines
        position of the system line of the rib on local Z axis (ez).</td>
    </tr>
    <tr>
      <td style="text-align:left">Eccentricity ez [mm]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">150</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Eccentricity of the member system line in Z direction of the local coordinate
        system from the centre of the gravity of the cross-section</td>
    </tr>
    <tr>
      <td style="text-align:left">Type of connection</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>Full shear connection</p>
        <p>Partial shear connection</p>
        <p>Without Composite Action</p>
        <p>User Defined Eccentricity</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Determines the degree of shear connection between the rib and the plate
        Full shear connection - in this case, the composite beam is modelled as
        an eccentric plate rib (real eccentricity). The composite effect is taken
        into account directly through the real eccentricity of the 1D member Partial
        shear connection - In this case, the composite beam is modelled as a plate
        rib without eccentricity. In order to consider the composite action, the
        stiffness of the beam is adjusted to take into account the effect of the
        eccentricity and of the participating deck width. Without Composite Action
        - assumes that there is no longitudinal shear connection between the beam
        and the deck User Defined Eccentricity - serves for any plate rib linked
        to a non-composite deck</td>
    </tr>
    <tr>
      <td style="text-align:left">Shape of the rib</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>T Symmetric</p>
        <p>Right Left</p>
        <p>T Non-symmetric</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Determines the shape of the effective width of the rib</td>
    </tr>
    <tr>
      <td style="text-align:left">Layer</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">Layer 1</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">Custom created layer. The layer can thus comprise entities that have something
        in common (e.g. one floor, columns of one floor, columns of the same length,
        etc.)</td>
    </tr>
    <tr>
      <td style="text-align:left">Behaviour in analysis</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>Standard</p>
        <p>Axial Force Only</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">From the finite element analysis point of view, the 1D member can act
        like a standard 1D member or like a hinged (pinned) rod. The difference
        is that the standard 1D member is capable of transferring all the internal
        forces, while the latter variant only provides for transferring of the
        axial force.</td>
    </tr>
    <tr>
      <td style="text-align:left">Effective width</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>Number Of Thickness</p>
        <p>Width</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Determines the method which is considered for specifying the effective
        width. Number of thickness - the multiple thickness of the slab to which
        is rib connected. The parametric way how to specify the effective width.
        Width - Direct numerical input of the effective width of the slab</td>
    </tr>
    <tr>
      <td style="text-align:left">Width left for check [mm]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">500</td>
      <td style="text-align:left">yes, if Shape of the rib is Right, Left or T Non-symmetric</td>
      <td style="text-align:left">Effective width on the left side (depends on LCS), used for check. If
        Effective width is set to &quot;Number Of Thickness&quot;, then inputted
        value is considered as unitless multiplier</td>
    </tr>
    <tr>
      <td style="text-align:left">Width right for check [mm]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">500</td>
      <td style="text-align:left">yes, if Shape of the rib is Right, Left or T Non-symmetric</td>
      <td style="text-align:left">Effective width on the right side (depends on LCS), used for check. If
        Effective width is set to &quot;Number Of Thickness&quot;, then inputted
        value is considered as unitless multiplier</td>
    </tr>
    <tr>
      <td style="text-align:left">Width left for internal forces [mm]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">500</td>
      <td style="text-align:left">yes, if Shape of the rib is Right, Left or T Non-symmetric</td>
      <td style="text-align:left">Effective width on the left side (depends on LCS), used for calculation
        of internal forces. If Effective width is set to &quot;Number Of Thickness&quot;,
        then inputted value is considered as unitless multiplier</td>
    </tr>
    <tr>
      <td style="text-align:left">Width right for internal forces [mm]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">500</td>
      <td style="text-align:left">yes, if Shape of the rib is Right, Left or T Non-symmetric</td>
      <td style="text-align:left">Effective width on the right side (depends on LCS), used for calculation
        of internal forces. If Effective width is set to &quot;Number Of Thickness&quot;,
        then inputted value is considered as unitless multiplier</td>
    </tr>
    <tr>
      <td style="text-align:left">Color</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">#808080</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">Defines color and transparency of the object. Color is defined by Hex
        format #AARRGGBB. Transparency is controlled by the alpha channel AA. If
        no color is set then default color is used.</td>
    </tr>
    <tr>
      <td style="text-align:left">Parent ID</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">67b35d84-3d04-47aa-aa4a-dc1263982320</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">Is filled for objects created be dividing curved geometry to series of
        straight line objects. Parent ID will ensure that curved edge is imported
        as straight parts to nonsupporting application, and back to original supporting
        application as curved geometry. To ensure successful round trip of segmented
        objects and their related objects, Parent ID needs to be present in both
        directions.</td>
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

## Notes

{% hint style="info" %}
**LCS of the rib** is set due to the following rules: X is set from the start node to the end node, Z is set in parallelly to Z LCS in the slab \([StructuralSurfaceMember](https://saf.guide/Content/A_Objects/8_StructuralSurfaceMember.htm)\), Y is determined by right hand rule.
{% endhint %}

![](../.gitbook/assets/13_structuralcurvememberrib2.png)

{% hint style="info" %}
Complete enumeration of the Formcode and Description ID can be found in chapter Annexes, in this documentation.
{% endhint %}

