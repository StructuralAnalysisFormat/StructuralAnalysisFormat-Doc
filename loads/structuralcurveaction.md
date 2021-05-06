# StructuralCurveAction

## Line force on the beam

The Line force load models load distributed over a 1D member or on a slab edge. It may be action along the whole 1D member or only on its part. It can be constant or trapezoidal, acting in three main directions X, Y, Z \(global or local coordinate system\).

![](../.gitbook/assets/33_structuralcurveaction.png)

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
      <td style="text-align:center">F3</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Human readable unique name of the force</td>
    </tr>
    <tr>
      <td style="text-align:center">Type</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">Standard</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">This property defines what the load is caused by, E.g. Standard, Wind,
        Snow, Self weight, Hoar Frost, Predefined, Plane Load, Water Pond, Water
        Pressure, Soil Pressure, Generated Water, Generated Soil</td>
    </tr>
    <tr>
      <td style="text-align:center">Force action</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>On beam</p>
        <p></p>
        <p>On edge</p>
        <p></p>
        <p>On subregion edge</p>
        <p></p>
        <p>On opening edge</p>
        <p></p>
        <p>On rib</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Specifies on which type of object the force acts</td>
    </tr>
    <tr>
      <td style="text-align:center">Distribution</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>Uniform</p>
        <p></p>
        <p>Trapez</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">The load may be either constant along the 1D member or linearly variable
        (trapezoidal).</td>
    </tr>
    <tr>
      <td style="text-align:center">Direction</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>X</p>
        <p></p>
        <p>Y</p>
        <p></p>
        <p>Z</p>
        <p></p>
        <p>Vector</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">
        <p>Specifies the base direction of the load</p>
        <p>X, Y, Z - action will be applied in one of these directions</p>
        <p>Vector - size and direction calculated from vector</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Value 1 [kN/m]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">-150</td>
      <td style="text-align:center">yes, if Direction = X,Y or Z</td>
      <td style="text-align:left">
        <p>Specifies the first size of the load in, acts in one direction</p>
        <p>Value1 is always closer to origin (see notes)
          <br />
        </p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Value 2 [kN/m]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">-180</td>
      <td style="text-align:center">
        <p>yes, if Direction = X,Y or Z</p>
        <p>yes, if Distribution = Trapez</p>
      </td>
      <td style="text-align:left">
        <p>Specifies the second size of the load in, acts in one direction</p>
        <p>Value2 is always further from origin (see notes)</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Vector 1(X;Y;Z) [kN/m]</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">(10;10;0)</td>
      <td style="text-align:center">yes, if Direction = Vector</td>
      <td style="text-align:left">
        <p>Specifies the first size of the load in, direction by vector</p>
        <p>Note: Vector1 and Vector2 needs to be in same direction</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Vector 2(X;Y;Z) [kN/m]</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">(20;20;0)</td>
      <td style="text-align:center">
        <p>yes, if Direction = Vector</p>
        <p>yes, if Dsitribution = Trapez</p>
      </td>
      <td style="text-align:left">
        <p>Specifies the second size of the load in, direction by vector</p>
        <p>Note: Vector1 and Vector2 needs to be in same direction</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Member</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">B11</td>
      <td style="text-align:center">yes, if Force action = On beam</td>
      <td style="text-align:left">The name of the <a href="https://saf.guide/Content/A_Objects/7_StructuralCurveMember.htm">StructuralCurveMember</a> on
        which the load is applied</td>
    </tr>
    <tr>
      <td style="text-align:center">Member Rib</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">B11</td>
      <td style="text-align:center">yes, if Force action = On rib</td>
      <td style="text-align:left">The name of the <a href="https://saf.guide/Content/A_Objects/25_StructuralCurveMemberRib.htm">StructuralCurveMemberRib</a> on
        which the load is applied</td>
    </tr>
    <tr>
      <td style="text-align:center">2D Member</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">S1</td>
      <td style="text-align:center">yes, if Force action = On edge
        <br />or On subregion edge
        <br />or On opening edge</td>
      <td style="text-align:left">The name of the <a href="https://saf.guide/Content/A_Objects/8_StructuralSurfaceMember.htm">StructuralSurfaceMember</a> or
        <a
        href="https://saf.guide/Content/A_Objects/10_StructuralSurfaceMemberRegion.htm">StructuralSurfaceMemberRegion</a>or <a href="https://saf.guide/Content/A_Objects/9_StructuralSurfaceMemberOpening.htm">StructuralSurfaceMemberOpening</a> on
          which the load is applied. <a href="https://saf.guide/Content/A_Objects/19_StructuralCurveAction.htm#">StructuralCurveAction</a> can
          act either on a 2D member edge or on internal edge.</td>
    </tr>
    <tr>
      <td style="text-align:center">Edge</td>
      <td style="text-align:center">Integer</td>
      <td style="text-align:center">1</td>
      <td style="text-align:center">yes, if Force action acts on 2D Member edge</td>
      <td style="text-align:left">Index of the edge of the the <a href="https://saf.guide/Content/A_Objects/8_StructuralSurfaceMember.htm">StructuralSurfaceMember</a> on
        which the load is applied</td>
    </tr>
    <tr>
      <td style="text-align:center">Internal edge</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">ES2</td>
      <td style="text-align:center">yes, if Force action = On edge</td>
      <td style="text-align:left">The name of the <a href="https://saf.guide/Content/A_Objects/6_StructuralCurveEdge.htm">StructuralCurveEdge</a> on
        which is the load applied. <a href="https://saf.guide/Content/A_Objects/19_StructuralCurveAction.htm#">StructuralCurveAction</a> can
        act either on a 2D member edge or on internal edge.</td>
    </tr>
    <tr>
      <td style="text-align:center">Load case</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">LC1</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">The name of the load case to which the force belongs</td>
    </tr>
    <tr>
      <td style="text-align:center">Coordinate system</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>Global</p>
        <p></p>
        <p>Local</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">
        <p>Defines the co-ordinate system of the member in which the load is applied</p>
        <p>For &quot; Local&quot;, coordinate system is defined by the member where
          is load applied</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">Location</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>Length</p>
        <p></p>
        <p>Projection</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Specifies whether the load is &quot;put directly on an inclined 1D member&quot;
        or whether the &quot;projection on plan&quot; is defined.</td>
    </tr>
    <tr>
      <td style="text-align:center">Coordinate definition</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>Absolute</p>
        <p></p>
        <p>Relative</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Selects the coordinate system that is used to define the length of the
        line load. Relative means without units. To define length of the load in
        meters input absolute</td>
    </tr>
    <tr>
      <td style="text-align:center">Origin</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>From start</p>
        <p></p>
        <p>From end</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Specifies the origin of the coordinate system used for the definition
        of the length of the force</td>
    </tr>
    <tr>
      <td style="text-align:center">Extent</td>
      <td style="text-align:center">Enum</td>
      <td style="text-align:center">
        <p>Full</p>
        <p></p>
        <p>Span</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Defines if a load is extended just over a span instead of the whole 1D
        member, it is used if a 1D member consists of more than one span. This
        feature is not fully supported, only two spans are supported in the moment.</td>
    </tr>
    <tr>
      <td style="text-align:center">Start point [m]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">
        <p>value in meters for Coordinate definition = Absolute</p>
        <p>0,0</p>
        <p>value in percentage for Coordinate definition = Relative</p>
        <p>0,0</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Defines the position of the start point of the force in relative or absolute
        coordinates [m]</td>
    </tr>
    <tr>
      <td style="text-align:center">End point [m]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">
        <p>value in meters for Coordinate definition = Absolute</p>
        <p>5,25</p>
        <p>value in percentage for Coordinate definition = Relative</p>
        <p>1,0</p>
      </td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Defines the position of the end point of the force in relative or absolute
        coordinates [m]</td>
    </tr>
    <tr>
      <td style="text-align:center">Eccentricity ey [mm]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">-150</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Eccentricity of the force system line in Y direction of the local coordinate
        system</td>
    </tr>
    <tr>
      <td style="text-align:center">Eccentricity ez [mm]</td>
      <td style="text-align:center">Double</td>
      <td style="text-align:center">75</td>
      <td style="text-align:center">yes</td>
      <td style="text-align:left">Eccentricity of the force system line in Z direction of the local coordinate
        system</td>
    </tr>
    <tr>
      <td style="text-align:center">Parent ID</td>
      <td style="text-align:center">String</td>
      <td style="text-align:center">67b35d84-3d04-47aa-aa4a-dc1263982320</td>
      <td style="text-align:center">no</td>
      <td style="text-align:left">
        <p>Is filled for objects created be dividing curved geometry to series of
          straight line objects.
          <br />
          <br />Parent ID will ensure that curved edge is imported as straight parts to
          nonsupporting application, and back to original supporting application
          as curved geometry.</p>
        <p>To ensure successful round trip of segmented objects and their related
          objects, Parent ID needs to be present in both directions.</p>
      </td>
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
Difference between Location type Length and Projection can be seen in the picture. Location is used only if Coordinate system is Global.
{% endhint %}

![](../.gitbook/assets/34_structuralcurvemoment2.png)

{% hint style="info" %}
An example of use of parameter Extent is in the in the picture below. In case of Span the load acts only on the span which is defined by internal nodes
{% endhint %}

![](../.gitbook/assets/34_structuralcurvemoment4.png)

{% hint style="info" %}
An example with Distribution type Trapez and with different values 1 and 2 can be seen in the following picture. Coordinate definition is relative, start point 0 and end point 0,3. StructuralCurveAction 1 has origin "From start" and StructuralCurveAction 2 has origin "From end". In this case the parameter extent doesn’t make any difference, only in case of beams consisting of more parts.
{% endhint %}

![](../.gitbook/assets/34_structuralcurvemoment3.png)

