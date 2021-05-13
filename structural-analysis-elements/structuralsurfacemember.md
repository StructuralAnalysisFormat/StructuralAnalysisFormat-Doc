# StructuralSurfaceMember

## 2D member \(Plate, Wall…\)

Instances of StructuralSurfaceMember describe face members, structural analysis idealizations of slabs, walls, shells. Surface members may be planar or curved with an arbitrary number of edges.

The geometry of a 2D member is defined by nodes \([StructuralPointConnection](structuralpointconnection.md)\)and edges. The edges define shape of the curve between two next nodes.

![](../.gitbook/assets/14_structuralsurfacemember.png)

![](../.gitbook/assets/14_structuralsurfacemember2.png)

### Specification in the excel

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
      <td style="text-align:center">B1</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Human readable unique name of the 2D member</td>
    </tr>
    <tr>
      <td style="text-align:center">Type</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">Plate</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">The type of the 2D member, used within the model E.g. Plate, Wall, Shell.
        The type reflects the geometry or classification in the structure. Plate
        and Wall are expected to be planar (flat) geometry objects. Shell is expected
        to be non planar object. The type DOES NOT describes available internal
        forces for 2D finite element.</td>
    </tr>
    <tr>
      <td style="text-align:center">Material</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">MAT_1</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">The name reference to the existing, valid name of the StructuralMaterial
        object.</td>
    </tr>
    <tr>
      <td style="text-align:center">Thickness type</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>Constant</p>
        <p></p>
        <p>Variable in global X</p>
        <p></p>
        <p>Variable in global Y</p>
        <p></p>
        <p>Variable in global Z</p>
        <p></p>
        <p>Variable in local X</p>
        <p></p>
        <p>Variable in local Y</p>
        <p></p>
        <p>Variable in direction XY</p>
        <p></p>
        <p>Variable radially</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Thickness of the slab can be defined as a constant - one thickness for
        whole 2D member or variable. Variability of the thickness can be defined
        in the global coordinate system (GCS) or in the local coordinate system
        (LCS) of the 2D member. For LCS are two more options: - Variable in two
        directions X and Y (three points have to be defined in thickness attribute
        ) - Variable radially, for circle slabs. Two points have to be defined,
        centre point and the point on the diameter.</td>
    </tr>
    <tr>
      <td style="text-align:center">Thickness [mm]</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">200 N1:200; N2:250</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">The thickness of the structural surface member - For constant thickness:
        One number in millimetres (e.g. 200) - For variable thickness - type &quot;Global
        X, Global Y, Global Z, Local X, Local Y and Radial: Two thicknesses in
        the following format N1:200; N2:250 . N1 means name of the existing StructuralPointConnection
        of the StructuralSurfaceMember and number is a thickness in this point.
        - For variable thickness type Direction XYThree thicknesses N1:200; N2:250;
        N3:280 have to be specified</td>
    </tr>
    <tr>
      <td style="text-align:center">System plane at</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>Bottom</p>
        <p></p>
        <p>Centre</p>
        <p></p>
        <p>Top</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Defines the position of the system plane.</td>
    </tr>
    <tr>
      <td style="text-align:center">Nodes</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">N81; N263; N659; N660</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">All nodes that belongs to surface member and defines its geometric shape.
        The names of the nodes are separated by ; (semicolon) and space.</td>
    </tr>
    <tr>
      <td style="text-align:center">Internal nodes</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">N22; N23</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Internal nodes belonging to StructuralSurfaceMember defined in StructuralPointConnection
        Internal nodes are not geometry defining The names of the nodes are separated
        by ; (semicolon) and space</td>
    </tr>
    <tr>
      <td style="text-align:center">Edges</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">
        <p>Line; Line; Circular Arc; Line</p>
        <p>or</p>
        <p>Line;Spline-5;Line;Parabolic Arc;Line</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">
        <p>Defines the shape of the curve between two next nodes (or more nodes depends
          on edge type). Supported strings are:</p>
        <p>Line</p>
        <p>Circular Arc</p>
        <p>Circle by 3 points</p>
        <p>Circle and Point</p>
        <p>Parabolic arc</p>
        <p>Bezier Spline-x</p>
        <p>Where &quot;x&quot; number of nodes defining the spline</p>
        <p>The names are separated by ; (semicolon) and space.</p>
        <p>It is possible to also define circle geometry by using &quot;Circle and
          Point&quot; or &quot;Circle by 3 points&quot;. In case of &quot;Circle
          and point&quot; two nodes have to be defined, centre of the circle and
          a point on a circle. The circle defined by two points is always horizontal.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Area [m2]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">2.359</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">The value of the surface area of the StructuralSurfaceMember</td>
    </tr>
    <tr>
      <td style="text-align:center">Layer</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">1st floor</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Custom created layer. The layer can thus comprise entities that have something
        in common (e.g. one floor, columns of one floor, columns of the same length,
        etc.)</td>
    </tr>
    <tr>
      <td style="text-align:center">LCS Type</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>x by vector</p>
        <p></p>
        <p>y by vector</p>
        <p></p>
        <p>Tilt of vector defined by point</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Defines type of the local coordinate system of the StructuralSurfaceMember.
        Option &#x201C;Tilt of vector defined by point&#x201D; allows change of
        orientation of the LCS to one point (for all mesh elements). For this,
        you have to specify coordinates of the vector. For further understanding
        see Introduction</td>
    </tr>
    <tr>
      <td style="text-align:center">Coordinate X [m]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">1</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Coordinate of the vector of the LCS in X direction</td>
    </tr>
    <tr>
      <td style="text-align:center">Coordinate Y [m]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">0</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Coordinate of the vector of the LCS in Y direction</td>
    </tr>
    <tr>
      <td style="text-align:center">Coordinate Z [m]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">1,2</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Coordinate of the vector of the LCS in Z direction</td>
    </tr>
    <tr>
      <td style="text-align:center">LCS Rotation [deg]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">45.00</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">This value defines the rotation of local axes of the 2D member</td>
    </tr>
    <tr>
      <td style="text-align:center">Structural Z Eccentricity [mm]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">-125</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Define the position difference between a physical element and its analytical
        member representation in Z direction (vertical movement of the center plane).
        Used to build up physical (structural body from analysis member). DO NOT
        affects internal forces.</td>
    </tr>
    <tr>
      <td style="text-align:center">Analysis Z Eccentricity [mm]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">-125</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Define the position difference between a physical element and its analytical
        member representation in Z direction (vertical movement of the center plane).
        Used to build up physical (structural body from analysis member). DO affects
        internal forces.</td>
    </tr>
    <tr>
      <td style="text-align:center">Shape</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>Flat</p>
        <p></p>
        <p>Curved</p>
      </td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Specify the shape of the StructuralSurfaceMember in the sense of the planarity
        of the system plane. For Flat, all nodes have to be in the same plane.</td>
    </tr>
    <tr>
      <td style="text-align:center">Behavior in analysis</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>Isotropic</p>
        <p></p>
        <p>Orthotropic</p>
        <p></p>
        <p>Membrane</p>
        <p></p>
        <p>Press only</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Isotropic: A normal isotropic slab with identical properties in all directions
        is used. Orthotropic: An orthotropic slab with different properties in
        two orthogonal directions is used Membrane: Special membrane elements are
        used for the analysis of the slab (only normal forces allowed) Press only:
        Special elements capable of resisting only compression stress are used
        for the analysis of the slab (no tension allowed)</td>
    </tr>
    <tr>
      <td style="text-align:center">Color</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">#7FFFFF00</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Defines the colour and transparency of the object. Colour is defined by
        Hex format #AARRGGBB. Transparency is controlled by the alpha channel AA.</td>
    </tr>
    <tr>
      <td style="text-align:center">Parent ID</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">67b35d84-3d04-47aa-aa4a-dc1263982320</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">Is filled for objects created be dividing curved geometry to series of
        straight line objects. Parent ID will ensure that curved edge is imported
        as straight parts to nonsupporting application, and back to original supporting
        application as curved geometry. To ensure successful round trip of segmented
        objects and their related objects, Parent ID needs to be present in both
        directions.</td>
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

## Notes

{% hint style="info" %}
Rotation of LCS is measured from origin position of local x and y-axis and orientation follows positive rotation according to right-handed rule.

An example of a definition of a curved wall defined in the StructuralSurfaceMember sheet can be seen below, nodes N1, N2, N3 define the first arc and N4, N5, N6 define the second arc. Edges shown below are important for RelConnectsRigidMember:
{% endhint %}

![](../.gitbook/assets/14_structuralsurfacemember3.png)

![](../.gitbook/assets/14_structuralsurfacemember4.png)

