# StructuralCurveActionFree

## Free line force

The Free line load is related to slabs. The load is not defined by the entity it acts on, but by a specific load border. Free loads are defined by means of "loading entities" that may overlap or affect one or more slabs.

![](../.gitbook/assets/39_structuralcurveactionfree1.png)

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
      <td style="text-align:left">LF5</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Human readable unique name of the force</td>
    </tr>
    <tr>
      <td style="text-align:left">Type</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">Standard</td>
      <td style="text-align:left">no</td>
      <td style="text-align:left">This property defines what the load is caused by, E.g. Standard, Wind,
        Snow, Self weight, Hoar Frost, Predefined, Plane Load, Water Pond, Water
        Pressure, Soil Pressure, Generated Water, Generated Soil</td>
    </tr>
    <tr>
      <td style="text-align:left">Distribution</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>Uniform</p>
        <p>Trapez</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">The load may be either constant along its length or linearly variable
        (trapezoidal).</td>
    </tr>
    <tr>
      <td style="text-align:left">Direction</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>X</p>
        <p>Y</p>
        <p>Z</p>
        <p>Vector</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">
        <p>Specifies the base direction of the load</p>
        <p>X, Y, Z - action will be applied in one of these directions</p>
        <p>Vector - size and direction calculated from vector</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Value 1 [kN/m]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">-150</td>
      <td style="text-align:left">yes, if Direction = X,Y or Z</td>
      <td style="text-align:left">Specifies the first size of the load in kiloNewtons per meter</td>
    </tr>
    <tr>
      <td style="text-align:left">Value 2 [kN/m]</td>
      <td style="text-align:left">Double</td>
      <td style="text-align:left">-180</td>
      <td style="text-align:left">
        <p>yes, if Direction = X,Y or Z</p>
        <p>yes, if Dsitribution = Trapez</p>
      </td>
      <td style="text-align:left">Specifies the second size of the load in kiloNewtons per meter</td>
    </tr>
    <tr>
      <td style="text-align:left">Vector 1(X;Y;Z) [kN/m]</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">(10;10;0)</td>
      <td style="text-align:left">yes, if Direction = Vector</td>
      <td style="text-align:left">
        <p>Specifies the first size of the load in, direction by vector</p>
        <p>Note: Vector1 and Vector2 needs to be in same direction</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Vector 2(X;Y;Z) [kN/m]</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">(20;20;0)</td>
      <td style="text-align:left">
        <p>yes, if Direction = Vector</p>
        <p>yes, if Dsitribution = Trapez</p>
      </td>
      <td style="text-align:left">
        <p>Specifies the second size of the load in, direction by vector</p>
        <p>Note: Vector1 and Vector2 needs to be in same direction</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Load case</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">LC1</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">The name of the load case to which the force belongs</td>
    </tr>
    <tr>
      <td style="text-align:left">Coordinate X [m]</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">0.000; 2.050; 4.850; -2.000</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">The list of X coordinates of the nodes which define the geometry of the
        line free load. Each coordinate is separated by semicolon and space.</td>
    </tr>
    <tr>
      <td style="text-align:left">Coordinate Y [m]</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">0.500; 1.050; 2.650; -1.500</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">The list of Y coordinates of the nodes which define the geometry of the
        line free load. Each coordinate is separated by semicolon and space.</td>
    </tr>
    <tr>
      <td style="text-align:left">Coordinate Z [m]</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">0.000; 0.000; 0.000; 0.000</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">The list of Z coordinates of the nodes which define the geometry of the
        line free load. Each coordinate is separated by semicolon and space.</td>
    </tr>
    <tr>
      <td style="text-align:left">Segments</td>
      <td style="text-align:left">String</td>
      <td style="text-align:left">Line; Circular Arc; Bezier; Parabolic arc; Spline</td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">List of the shape of each segment which is part of the curve, separated
        by semicolon if there are multiple</td>
    </tr>
    <tr>
      <td style="text-align:left">Coordinate system</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>Global</p>
        <p>Local</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Defines co-ordinate system of the member in which the load is applied</td>
    </tr>
    <tr>
      <td style="text-align:left">Location</td>
      <td style="text-align:left">Enum</td>
      <td style="text-align:left">
        <p>Length</p>
        <p>Projection</p>
      </td>
      <td style="text-align:left">yes</td>
      <td style="text-align:left">Specifies whether the load is &quot;put directly on an inclined 1D member&quot;
        or whether the &quot;projection on plan&quot; is defined.</td>
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

