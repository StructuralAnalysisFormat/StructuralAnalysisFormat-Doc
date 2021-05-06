# Release Notes

{% hint style="success" %}
Current version 2.0.0
{% endhint %}

## Release notes

### 21.12.2020 - Version 2.0.0

In version 2.0.0:

New attribute added:

Project and model specification - Model sheet, National code added

StructuralPointAction - Possible to input angled point force, Extended Direction enum, Added Vector attribute

StructuralPointActionFree - Possible to input angled point force, Extended Direction enum, Added Vector attribute

StructuralCurveAction

* Possible to input angled line force, Extended Direction enum, Added Vector 1 and Vector 2 attribute
* Extended Force action enum by "On subregion edge" and "On opening edge"

StructuralEdgeConnection

* Added enum attribute "Boundary condition" to allow input on different types of edges \(2D member, 2D opening, 2D subregion\)

StructuralCurveMoment - Extended Force action enum by "On subregion edge" and "On opening edge"

StructuralCurveFree - Possible to input angled line force, Extended Direction enum, Added Vector 1 and Vector 2 attribute

We removed default column value.

We included more attributes as required to ensure all important and structural engineering relevant data will be exchanged

### 11.12.2020 - Version 1.1.0

In version 1.1.0:

New object added:

Structural Proxy Element - object which allows to describe general solids

### 4.12.2020 - Version 1.0.9

In version 1.0.9:

* LCS type is required value for StructuralCurveMember
* Added ID for Model and Project sheet in

Project and model specifications

StructuralStorey

StructuralCurveMemberVarying

* New object StructuralSurfaceActionDistribution to describe load panels
* Added detailed description for Global coordinate system property in Project and model specifications

### 26.11.2020 - Version 1.0.8

In version 1.0.8, few small formal changes was made

* Thermal load for 2D members - removed delta T attribute, to specify single value for constant temperature change, use attribute "TempT "
* Added Id attribute for Project and Model information
* "Project nr." changed to "Project nr" \(removed dot\) in Project information
* removed "V" in front of SAF version attribute at Model information

### 13.11.2020 - Version 1.0.7

In version 1.0.7, three major additions were added

* Thermal load for 1D members

StructuralCurveActionThermal

* Thermal load for 2D members

StructuralSurfaceActionThermal

* New types of eccentricities \(structural and analysis\) for

StructuralCurveMember and StructuralSurfaceMember

### 23.10.2020 - Version 1.0.6

In version 1.0.6, four major additions were added

* "Parent ID" added for

StructuralSurfaceMemberRegion

StructuralSurfaceConnection

StructuralEdgeConnection

RelConnectsStructuralMember

RelConnectsSurfaceEdge

StructuralCurveAction

StructuralSurfaceActionFree

StructuralCurveMemberRib

StructuralCurveConnection

StructuralCurveMoment

StructuralSurfaceActionThermal

RelConnectsRigidCross

StructuralCurveEdge

StructuralCurveMember

StructuralSurfaceMember

StructuralSurfaceMemberOpening

* "Area" attribute added for

StructuralSurfaceMemberRegion

StructuralSurfaceMember

StructuralSurfaceMemberOpening

* Formcodes description was updated

Formcodes

* Structural and Analysis eccentricity was introduced for:

StructuralCurveMember

StructuralSurfaceMember

Changed objects:

StructuralCrossSection

* Form code is required value for CSS type "compound"

StructuralCurveMember

* Simplified System line alignment description

### 14.04.2020 - Version 1.0.5

In version 1.0.5, four major additions were added

* "Parent ID" for StructuralCurveMember and StructuralSurfaceMember
* new object StructuralCurveMemberVarying to define tapered, arbitrary, haunch beams
* new object StructuralStorey to define storey levels
* new enum describing cross section LCS type in StructuralCrossSection

New objects:

StructuralCurveMemberVarying

* New object for description tapered, arbitrary, haunch beams

StructuralStorey

* New object for description structural storey, floor levels

Changed objects:

CompositeShapeDef

* Added LCS explanation

Geometry

* Added SAF geometry strings column
* Edited values for bezier, added further explanation

Introduction

* Added general LCS vector description
* Updated pictures \(LCS is now self explaining\)

Project and model specifications

* Added description column
* Added enum LCS of cross section
* Added RigidCross in the list of objects
* New feature for ignored groups and objects and add list of groups and objects

RelConnectsStructuralMember

* Added definition of fully rigid connection

StructuralCrossSection

* Formcode is now required for manufactured cross sections
* Removed LCS of cross section enum
* Added new enum "LCS of cross section"

StructuralCurveAction

* Specified rel vs abs

StructuralCurveMember

* Added Parent ID
* LCS type "Standard" not used anymore
* Added column "Arbitrary definition" to link to StructuralCurveMemberVarying
* Fixed typos

StructuralCurveMemberRib

* Updated description column
* New picture explaining LCS of the rib
* Fixed typos

StructuralCurveMoment

* Specified rel vs abs

StructuralMaterial

* Quality and Name is recommended to set the same value

StructuralPointAction

* Specified rel vs abs

StructuralPointMoment

* Specified rel vs abs

StructuralSurfaceActionThermal

* Specified meaning of temperatures

StructuralSurfaceMember

* Added Parent ID column
* Fixed typos

StructuralSurfaceMemberOpening

* Added all supported geometries

StructuralSurfaceMemberRegion

* Fixed typos

Supported shapes of parametric cross section

* Added missing parameter "s" for I Section with haunch Asymmetric

### 10.10.2019 - Version 1.0.4

In version 1.0.4, "Id" row was added to all supported objects.

Changed objects:

Project and model specifications

* Attribute "ADM version" was deleted
* Improved description in a manner that is clear that model and project sheets are defined in rows and not in columns like other objects
* "Created" and "Last update" attributes have changed the format of the date and time
* Added excel examples

StructuralSurfaceActionThermal

* added attribute "2D Member Region"

StructuralSurfaceActionFree

* C vertexes explained in detail, added images

Introduction

* Minor changes in formatting

StructuralSurfaceMember

* Description extended for the edges numbering of surface members

RelConnectsRigidMember

* Added link to StrucutralSurfacesMember for explanation of edges numbering
* Enums for constrains sorted

RelConnectsRigidLink

* Added description about coordinate system of RigidLink
* "Type" column deleted
* Enums for constrains sorted
* Added description to hinge position

StructuralCurveMember

* Bezier, Spline and Parabolic arc are supported

StructuralCurveActionFree

* Bezier, Spline and Parabolic arc are supported

StructuralCurveMemberRib

* Bezier, Spline and Parabolic arc are supported

### 19.8.2019 - Version 1.0.3

New objects:

RelConnectsRigidCross

RelConnectsRigidMember

Changed objects:

Introduction

* Local Coordinate System of 1D and 2D members described in detail

RelConnectsRigidLink

* General update of all attributes: Functionality reduced on Nodes only \(due to implementation of internal nodes\), new enums for displacements
* Added new properties

Geometry

* Edited size of pictures
* Pictures updated

StructuralSurfaceMember

* Edited size of pictures

StructuralEdgeConnection

* Updated notes

StructuralPointAction

* Minor changes pages set up
* Updated pictures

StructuralCurveAction

* Minor changes pages set up
* Updated pictures

StructuralSurfaceMemberRegion

* Updated picture

StructuralCurveMoment

* Updated pictures

### 13.6.2019 - Version 1.0.2

New objects:

Geometry

### 23.5.2019 - Version 1.0.1

New objects:

CompositeShapeDef

Changed objects:

Supported shapes of parametric cross-section

* Updated images of parametric cross-sections

StructuralPointActionFree

* Excel sheet link fixed

StructuralPointMoment

* Excel sheet link fixed

Formcodes

* Updated "Corresponding Description ID of the profile" for L section

Supported shapes of compound section

* Unification of terminology

Supported shapes of parametric cross-section

* Shape Enum correction: "I Section with haunch Asymmetric"

StructuralEdgeConnection

* Excel sheet link fixed

RelConnectsStructuralMember

* Excel sheet link fixed

RelConnectsSurfaceEdge

* Excel sheet link fixed

StructuralLoadGroup

* Excel sheet link fixed

StructuralLoadCase

* Added values for "Load type": Temperature, Wind, Snow, Maintenance, Fire, Moving, Seismic and Standard
* Removed values for "Load type": Primary effect
* "Specification" Enum replaced by "Duration" with following possible values: Short, Medium, Long and Instantaneous
* Excel sheet link fixed

StructuralPointAction

* Excel sheet link fixed

StructuralCurveAction

* Excel sheet link fixed

StructuralCurveActionFree

* Excel sheet link fixed

StructuralSurfaceActionFree

* Notes updated
* Excel sheet link fixed

StructuralCurveMemberRib

* Alignment description updated
* Defined new value: "Eccentricity ez"
* Extended description for "Type of connection" and "Layer"
* Minor changes in table style

StructuralCurveConnection

* Defined new value as Enum: "Type"

RelConnectsRigidLink

* Redefined default value for "Hinges"

StructuralLoadCombination

* Added excel example sheet

Project and model specifications

* New value defined "SAF version"
* Extended definition of the Values: Type of data, Value example or enum definition, Required value, Default value
* Minor text changes

StructuralMaterial

* Excel sheet link fixed

StructuralCrossSection

* Defined new Enum for Cross-section type: "General"
* For Cross-section type "General" is further specification moved to CompositeShapeDef
* Excel sheet link fixed

StructuralCurveEdge

* Excel sheet link fixed

StructuralCurveMember

* Excel sheet link fixed

StructuralSurfaceMember

* Updated description for: "Edges"
* Excel sheet link fixed

Startup page

* Major update of changes in Version 1.0.0 \(Release Notes\)

StructuralPointConnection

* Excel sheet link fixed

StructuralSurfaceMemberOpening

* Excel sheet link fixed

StructuralSurfaceMemberRegion

* Excel sheet link fixed

StructuralPointSupport

* Excel sheet link fixed

StructuralSurfaceConnection

* Excel sheet link fixed

StructuralSurfaceAction

* Excel sheet link fixed

### 19.3.2019 - Version 1.0.0

New objects:

StructuralCurveConnection

RelConnectsRigidLink

StructuralLoadCombination

StructuralCurveMoment

StructuralCurveActionThermal

StructuralSurfaceActionThermal

Changed objects:

StructuralCrossSection

* Added new types to parametric shapes of Cross-section \(I Section with haunch Asymetric, T Section with haunch, Trapezoid\) - in annex
* Added definition of general cross-section
* Added support for compound cross-sections
* Added attributes for analysis properties of the cross-section

StructuralMaterial

* Quality is required value
* Added new design properties for timber material \(in Annex\)

StructuralEdgeConnection

* Coordinate system: added "Global" option

StructuralPointSupport

* Added parameters "Compression only", "Tension only" for three translation constraints \(X, Y, Z\)

StructuralCurveConnection

* Added parameters "Compression only", "Tension only" for three translation constraints \(X, Y, Z\)

StructuralEdgeConnection

* Added parameters "Compression only", "Tension only" for three translation constraints \(X, Y, Z\)

StructuralCurveMemberRib

* Alignment: add user defined value

StructuralCurveMember

* Behaviour in analysis: add new options for tension only and compression only

StructuralSurfaceMember

* Added support for variable thickness
* LCS definition by vector
* Support for circle slab \(Circle by point, Circle by 3 points\)

StructuralPointAction

Deleted attribute "extend"

StructuralLoadGroup

* Enum of "Load group type" attribute changed

StructuralLoadCase

* Deleted attribute "Specification"

StructuralSurfaceActionFree

* Added names of the vertexes of the polygon

Model specification

* Added attribute for SAF version

