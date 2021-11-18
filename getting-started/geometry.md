# Geometry

## Geometry

Basic construction elements are simple geometry types, that are used for shape definition of structural members and geometrical object. With defining the further attributes to these elements from the lists Structural analysis elements, Supports and hinges and Loads the complete structural model is created. All values refer to the list [StrucutralPointConnection](https://saf.guide/Content/A\_Objects/5\_StructuralPointConnection.htm).

Following geometrical types are available:

|                                                      | Geometry type | Type definition                                              | Insertion data explanation                                                                                                                                  | SAF geometry strings                                              | Notes                                                                                                                                                                                                                                                                                            |
| ---------------------------------------------------- | ------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![1](../.gitbook/assets/4\_geometry\_line.png)       | Line          | Straight-line between two nodes                              | <p>Start point , End point</p><p>N1;N2</p>                                                                                                                  | Line                                                              | -                                                                                                                                                                                                                                                                                                |
| ![1](../.gitbook/assets/4\_geometry\_CA\_2.png)      | Circular Arc  | Arch defined with 3 nodes                                    | <p>Start point, Intermediate point, End point</p><p>N3;N4;N5</p>                                                                                            | Circular Arc                                                      | -                                                                                                                                                                                                                                                                                                |
| ![1](../.gitbook/assets/4\_geometry\_PA.png)         | Parabolic Arc | <p>Parabolic arch defined with 3 nodes<br></p>               | <p>Start point, Intermediate point, End point</p><p>N6;N7;N8</p>                                                                                            | Parabolic Arc                                                     | -                                                                                                                                                                                                                                                                                                |
| ![1](../.gitbook/assets/4\_geometry\_bezier.png)     | Bezier        | Cubic Bezier curve                                           | <p>Start point, 2nd point of control polygon (vertex), 3rd point of control polygon (vertex), End point</p><p>N9;Vertex_B1_1;</p><p>Vertex_B1_2;N10<br></p> | Bezier                                                            | <p>N9 and N10 stands for start and end node</p><p>Vertex_B1_1, Vertex_B1_2 define vertexes of bezier curve</p><p>All values refers to list StrucutralPointConnection</p><p>Bezier curve is parabolic, when 2nd and 3rd control points are the identical (values of coordinates are the same)</p> |
| ![1](../.gitbook/assets/4\_geomery\_spline.png)      | Spline        | Curved line defined by polynomial function                   | <p>Start point, Set of mid points, End point</p><p>N11;N12;N13;N14;N15;N16;N17;N18<br></p>                                                                  | Spline-8                                                          | "Spline-#" where "#" stands for number of nodes defining the spline                                                                                                                                                                                                                              |
| ![1](../.gitbook/assets/4\_geometry\_circle.png)     | Circle        | Circle                                                       | <p>Center Point, Point on the perimeter</p><p>N36;N37</p><p>Or</p><p>Three point on perimeter</p><p>N36;N37;N38<br></p>                                     | <p>Circle and Point<br></p><p>or</p><p>Circle by 3 points<br></p> | <p>Circle is not valid to define StrucutralCurveMember<br></p>                                                                                                                                                                                                                                   |
| ![1](../.gitbook/assets/4\_Geometry\_poly\_line.png) | Polyline      | <p>Combination of in nodes connected geometric types<br></p> | <p>List of nodes</p><p>N21;N22;N23;N24;N25;N26;N27;N28;N29; N30;N31;N32;N33;Vertex_B1_1;VertexB_1_2;N34;N35<br></p>                                         | Line;Line;Spline-7;Line;Circular Arc;Line;Bezier;Line             | <p>Detail explanation can be found in notes below<br></p>                                                                                                                                                                                                                                        |

## Notes

{% hint style="info" %}
**Mathematical definitions:**

* Bezier   \
  $$Q(t)=\sum_{i=0}^{3}P_iB_i(t)$$ ; $$t\epsilon<0,1>$$  $$B_{0t}=(1-t)^3,B_{1t}=3t(1-t)^2,B_{2t}=3t^2(1-t),B_{3t}=t^3$$    \
  $$Q(t)$$ is for the Bezier curve  \
  $$P_{i}$$ is for coodinates, and  \
  $$B_{it}$$is for basis function  \

* Spline\
  $$Q(t)=\sum_{i=0}^{m}P_iN_i^n(t)$$ ; $$t\epsilon<t_i,t_{i+1}>$$ \
  $$N_i^0(t)=1$$for$$t\epsilon<t_i,t_{i+1}>$$  $$N_i^0(t)=0$$otherwise  $$N{i}^{k}{(t)}=\frac{t-t_i}{t_{i+k}-t_i}N_{i}^{k-1}{(t)}+\frac{t_{i+k+1}-t}{t_{i+k+1}-t_{i+1}}N_{i+1}^{k-1}{(t)}$$  \
  $$Q(t)$$is for the Spline curve  \
  $$P_i$$is for the coordinates  \
  $$N_i^n(t)$$is for basis function  \
  $$n$$is for the degree of curve  \
  $$m$$is for points of the control polygon

**Polyline schematics:**
{% endhint %}

![1](../.gitbook/assets/4\_Geometry\_poly\_line\_2.png)
