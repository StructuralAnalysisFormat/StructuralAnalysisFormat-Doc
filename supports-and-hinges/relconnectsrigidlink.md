# RelConnectsRigidLink

## Rigid Link

A virtual connection of two nodes from\([StructuralPointConnection](../structural-analysis-elements/structuralpointconnection.md#node)\) for directly defined nodes, \([StructuralSurfaceMember](../structural-analysis-elements/structuralsurfacemember.md#2d-member-plate-wall)\) or \([StructuralCurveMember](../structural-analysis-elements/structuralcurvemember.md#1d-member-beam-column)\)for internal nodes on 1D and 2D members, where structural behavior could be set. Master and slave node have to be defined. The rigid links are used for the connection, where you want to simulate infinite rigidity or user defined properties.

![](../.gitbook/assets/26_rigidlink.png)

![](../.gitbook/assets/26_rigidlink_2.png)

### Specification in the excel

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
      <td style="text-align:left">RL1</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Human readable unique name of the object</td>
    </tr>
    <tr>
      <td style="text-align:left">Nodes</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">N3; N4</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">
        <p>The name of the valid existing node (<a href="../structural-analysis-elements/structuralpointconnection.md#node">StructuralPoinConnection</a>),
          or (<a href="../structural-analysis-elements/structuralcurvemember.md#1d-member-beam-column">StructuralCurveMember</a>,
          <a
          href="../structural-analysis-elements/structuralsurfacemember.md#2d-member-plate-wall">StructuralSurfaceMember</a>) for internal nodes</p>
        <p>Maximum of two nodes can be connected by RelConnectsRigitLink</p>
        <p>First in node is seen as &quot;master node&quot;, second in row is &quot;slave
          node&quot;</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Hinge position</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>None</p>
        <p>Begin (master node)</p>
        <p>End (slave node)</p>
        <p>Both</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">
        <p>This attribute serves to indicate if hinges should be applied to rigid
          link and if so, than on which node.</p>
        <p>Hinge position allows user to define constrains of selected node or nodes
          of RelConnectsRigidLink for translation (ui) and rotation (fii)</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">ux</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>Free</p>
        <p>Rigid</p>
        <p>Flexible</p>
        <p>Compression only</p>
        <p>Tension only</p>
        <p>Flexible compression only</p>
        <p>Flexible tension only</p>
        <p>Non linear</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">
        <p>Displacement in the direction X</p>
        <p>Free - That is it imposes no constraint in the direction. Rigid - The
          connection in fully rigid in the specified direction. Flexible - The connection
          is flexible (elastic) in the specified direction. Non linear - resistance
          in specified direction could be defined</p>
        <p>(Flexible) compression/tension only - acts rigid or flexible, only for
          defined strain (compression or tension)</p>
        <p>See notes for coordinates reference.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">uy</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>Free</p>
        <p>Rigid</p>
        <p>Flexible</p>
        <p>Compression only</p>
        <p>Tension only</p>
        <p>Flexible compression only</p>
        <p>Flexible tension only</p>
        <p>Non linear</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">
        <p>Displacement in the direction Y</p>
        <p>Free - That is it imposes no constraint in the direction. Rigid - The
          connection in fully rigid in the specified direction. Flexible - The connection
          is flexible (elastic) in the specified direction. Non linear - resistance
          in specified direction could be defined</p>
        <p>(Flexible) compression/tension only - acts rigid or flexible, only for
          defined strain (compression or tension)</p>
        <p>See notes for coordinates reference.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">uz</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>Free</p>
        <p>Rigid</p>
        <p>Flexible</p>
        <p>Compression only</p>
        <p>Tension only</p>
        <p>Flexible compression only</p>
        <p>Flexible tension only</p>
        <p>Non linear</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">
        <p>Displacement in the direction Z</p>
        <p>Free - That is it imposes no constraint in the direction. Rigid - The
          connection in fully rigid in the specified direction. Flexible - The connection
          is flexible (elastic) in the specified direction. Non linear - resistance
          in specified direction could be defined</p>
        <p>(Flexible) compression/tension only - acts rigid or flexible, only for
          defined strain (compression or tension)</p>
        <p>See notes for coordinates reference.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">fix</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>Free</p>
        <p>Rigid</p>
        <p>Flexible</p>
        <p>Non linear</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">
        <p>Rotation around X axis</p>
        <p>Free - That is it imposes no constraint in the direction. Rigid - The
          connection in fully rigid in the specified direction. Flexible - The connection
          is flexible (elastic) in the specified direction. Non linear - resistance
          in specified direction could be defined</p>
        <p>See notes for coordinates reference.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">fiy</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>Free</p>
        <p>Rigid</p>
        <p>Flexible</p>
        <p>Non linear</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">
        <p>Rotation around Y axis</p>
        <p>Free - That is it imposes no constraint in the direction. Rigid - The
          connection in fully rigid in the specified direction. Flexible - The connection
          is flexible (elastic) in the specified direction. Non linear - resistance
          in specified direction could be defined</p>
        <p>See notes for coordinates reference.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">fiz</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>Free</p>
        <p>Rigid</p>
        <p>Flexible</p>
        <p>Non linear</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">
        <p>Rotation around Z axis</p>
        <p>Free - That is it imposes no constraint in the direction. Rigid - The
          connection in fully rigid in the specified direction. Flexible - The connection
          is flexible (elastic) in the specified direction. Non linear - resistance
          in specified direction could be defined</p>
        <p>See notes for coordinates reference.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Stiffness X [MN/m]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">3.00</td>
      <td style="text-align:left">yes, if ux = Flexible, Flexible compression/tension only or Non linear</td>
      <td
      style="text-align:left">
        <p>The flexibility in direction X</p>
        <p>Use this property only if the ux is set Flexible, Flexible compression/tension
          only or Non linear</p>
        <p>See notes for coordinates reference.</p>
        </td>
    </tr>
    <tr>
      <td style="text-align:left">Resistance X [MN]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">0.25</td>
      <td style="text-align:left">yes, if ux = Non linear</td>
      <td style="text-align:left">
        <p>The resistance in direction X</p>
        <p>Use this property only if the ux is set to Non linear</p>
        <p>See notes for coordinates reference.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Stiffness Y [MN/m]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">2.50</td>
      <td style="text-align:left">yes, if uy = Flexible, Flexible compression/tension only or Non linear</td>
      <td
      style="text-align:left">
        <p>The flexibility in direction Y</p>
        <p>Use this property only if the uy is set Flexible, Flexible compression/tension
          only or Non linear</p>
        <p>See notes for coordinates reference.</p>
        </td>
    </tr>
    <tr>
      <td style="text-align:left">Resistance Y [MN]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">0.30</td>
      <td style="text-align:left">yes, if uy = Non linear</td>
      <td style="text-align:left">
        <p>The resistance in direction Y</p>
        <p>Use this property only if the uy is set Non linear</p>
        <p>See notes for coordinates reference.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Stiffness Z [MN/m]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">2.00</td>
      <td style="text-align:left">yes, if uz = Flexible, Flexible compression/tension only or Non linear</td>
      <td
      style="text-align:left">
        <p>The flexibility in direction Z</p>
        <p>Use this property only if the uz is set Flexible, Flexible compression/tension
          only or Non linear</p>
        <p>See notes for coordinates reference.</p>
        </td>
    </tr>
    <tr>
      <td style="text-align:left">Resistance Z [MN]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">0.75</td>
      <td style="text-align:left">yes, if uz = Non linear</td>
      <td style="text-align:left">
        <p>The resistance in direction Z</p>
        <p>Use this property only if the uz is set Non linear</p>
        <p>See notes for coordinates reference.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Stiffness Fix [MNm/rad]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">5.00</td>
      <td style="text-align:left">yes, if fix = Flexible or Non linear</td>
      <td style="text-align:left">
        <p>The flexibility in rotation around X axis</p>
        <p>Use this property only if the Rotational stiffness fix is Flexible or
          Non linear</p>
        <p>See notes for coordinates reference.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Resistance Fix [MNm]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">1.00</td>
      <td style="text-align:left">yes, if fix = Non linear</td>
      <td style="text-align:left">
        <p>The resistance in rotation around Y axis</p>
        <p>Use this property only if the Rotational stiffness fix is Non linear</p>
        <p>See notes for coordinates reference.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Stiffness Fiy [MNm/rad]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">6.25</td>
      <td style="text-align:left">yes, if fiy = Flexible or Non linear</td>
      <td style="text-align:left">
        <p>The flexibility in rotation around Y axis</p>
        <p>Use this property only if the Rotational stiffness fiy is Flexible or
          Non linear</p>
        <p>See notes for coordinates reference.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Resistance Fiy [MNm]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">0.80</td>
      <td style="text-align:left">yes, if fiy = Non linear</td>
      <td style="text-align:left">
        <p>The resistance in rotation around Y axis</p>
        <p>Use this property only if the Rotational stiffness fiy is Non linear</p>
        <p>See notes for coordinates reference.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Stiffness Fiz [MNm/rad]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">3.00</td>
      <td style="text-align:left">yes, if fiz = Flexible or Non linear</td>
      <td style="text-align:left">
        <p>The flexibility in rotation around Z axis</p>
        <p>Use this property only if the Rotational stiffness fiz is Flexible or
          Non linear</p>
        <p>See notes for coordinates reference.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Resistance Fiz [MNm]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">0.10</td>
      <td style="text-align:left">yes, if fiz = Non linear</td>
      <td style="text-align:left">
        <p>The resistance in rotation around Z axis</p>
        <p>Use this property only if the Rotational stiffness fiz is Non linear</p>
        <p>See notes for coordinates reference.</p>
      </td>
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
For constrains, the LCS of RelConnectsRigidLink is taken into account.

Local coordination system is given by master node and its parent object.

**Non linear** behavior of material is handled with "Resistance". The example is shown below.
{% endhint %}

![](../.gitbook/assets/25_rigidlink_resistance%20%281%29%20%281%29.png)

