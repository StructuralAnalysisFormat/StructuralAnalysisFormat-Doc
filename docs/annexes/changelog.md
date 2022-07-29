# Changelog

For release notes go to [Release Notes](release-notes.md). All the other (smaller) changes are documented here. This includes especially changes in wording and visuals. Improvements in the specification documented in changelog are not changing the functionality or compatibility of SAF. These changes only improve the understandability of SAF documentation.

## 29.7. Units page update
 * Values from [StructuralPointSupportDeformation](../loads/structuralpointsupportdeformation.md) and [ResultInteranlForce2DEdge](../results/resultinternalforce2dedge.md) were added to [Units](../annexes/units.md) table 

## 22.7. Decimal dot and small description update
* The usage of decimal separator across the documentation was unified to a point
* [StructuralSrufaceMemberOpening](../structural-analysis-elements/structuralsurfacememberopening.md)
   * Note and picture added

## 19.7.2022 Small fix in descrption
* [Load Combinations](../loads/structuralloadcombination.md) - Load factor - minor expansion of description and typos fixed

## 10.6.2022 Small tweaks and new implementation
* [Saf.guide](../index.rst) page recieved a logo at the top
* [Model specification](../getting-started/project-and-model-specifications/README.md) and [Ingored objects and groups](../annexes/ignore.md)
   * links to each other added to improve orientation in the docs
* [Ingored objects and groups](../annexes/ignore.md)
   * Typo fixed for value ResultInternalForce1D
* IDEA StatiCa added to SAF Implementation table
* AxisVM supports now also version 2.0.0
* [SAF versions](../getting-started/saf-versions.md)
   * Links to latest and stable added

## 6.6.2022 Small description update and New SAF example
* [StructuralCurveMemberRib](../structural-analysis-elements/structuralcurvememberrib.md)
   * Initial image updated, description in table clarified, note image added explaining alignment
* Steel hall - new example file was uploaded to [SAF examples](../getting-started/saf-examples.md)

## 24.5.2022 Image fixed
* In [Supported shapes of parametric cross-section](../annexes/supported-shapes-of-parametric-cross-section.md) image for Z zee fixed by filleting a corner

## 9.5.2022 New SAF implementation
* Allplan added to SAF Implementation table

## 26.4.2022 Who supports SAF table modified
* [Who Supports SAF](//docs/getting-started/who-supports-saf.md)
   * Companies' logos made smaller
   * Scroll-bar enabled when necessary

## 20.4.2022 New SAF implementation
* InfoGraph added to SAF Implementation table

## 7.4.2022 Thermal loads description and results to Who supports SAF
* [StructuralSurfaceActionThermal](../loads/structuralsurfaceactionthermal.md), [StructuralCurveActionThermal](../loads/structuralcurveactionthermal.md)
   * Thermal loads values description clarified - all values are changes of temperature
* [Who supports SAF](../getting-started/who-supports-saf.md)
   * Results - new table with companies who support results objects

## 5.4.2022 New SAF implementation
* D.I.E. added to SAF Implementation table

## 17.3.2022 SAF implementor's update
* Radimpex change to implementation table, logo update

## 7.3.2022 Small description update and fixed links
* [StructuralSurfaceAction](../loads/structuralsurfaceaction.md)
   * Location description clarified
* [StructuralCrossSesction](../structural-analysis-elements/structuralcrosssection.md)
   * Links to supported shapes of compound section and supported shapes of parametric cross section fixed

## 3.3.2022 Navigation in SAF and small description update
* [Welcome page](../index.rst)
    * Link to github discussion added
* [SAF versions](../getting-started/saf-versions.md)
    * Versions description update 
* [StructuralProxyElement](../structural-analysis-elements/structuralproxyelement.md)
   * Limitation of excel explained in a note  

## 28.2.2022 SAF implementor's update
* FEM-Design change to implementation table, logo update

## 25.2.2022 New SAF implementation
* Dlubal added to SAF Implementation table

## 21.2.2022 Description update and grooming
* [StructuralPointSupport](../supports-and-hinges/structuralpointsupport.md), [StructuralCurveConnection](../supports-and-hinges/structuralcurveconnection.md), [StructuralEdgeConnection](../supports-and-hinges/structuraledgeconnection.md)
    * Direction of compression and tension behaviour of supports described, pictures added 
* [StrucuralCurveAction](../loads/structuralcurveaction.md), [StrucuralCurveMoment](../loads/structuralcurvemoment.md)
    * LCS used for the loads explained in notes with pictures
* [StructuralPointAction](../loads/structuralpointaction.md), [StructuralPointMoment](../loads/structuralpointmoment.md)
    * LCS of node explained in notes
* Some files were overlooked when transfering from Gitbook to Read the Docs. Old pictures that were not in use are deleted from the repository.
* [StructuralCurveMember](../structural-analysis-elements/structuralcurvemember.md)
    * Small description updated 
* [StructuralCurveMemberVarying](../structural-analysis-elements/structuralcurvemembervarying.md)
   * Position of system line and alignment explained in a note

## 10.2.2022 New SAF implementation
* mbAEC StrukturEditor added to SAF Implementation table

## 31.1.2022 Small description update
* [StructuralCurveEdge](../structural-analysis-elements/structuralcurveedge.md)
    * Description updated, note added

## 25.1.2022 New SAF implementation
* ConSteel added to SAF Implementation table

## 24.1.2022 Description of enum 'Location' update
* [StrucuralCurveAction](../loads/structuralcurveaction.md). 
    * Location description clarified
* [StrucuralCurveMoment](../loads/structuralcurvemoment.md). 
    * Location description clarified

## 4.1.2022 SAF example house file update
New example file in version 2.1.0 is created and all versions of examples moved to [single page](https://examples.saf.guide/). 

## 9.12.2021 Transfer to Read the Docs and other changes
In order to move to new provider [Read the Docs](https://readthedocs.org/), it was nescesary do extensive changes in syntax. Hints and notes visuals were changed, images sizes were set and links were updated. No content was edited besides changes listed below.

* [Changelog](changelog.md)
    * New page Changelog was created under Annexes folder to separate smaller changes in documentation from [Release Notes](release-notes.md)

* [Ignored objects and groups](ignore.md)
    * Moved to Annexes

* [Units table](units.md)
    * Moved to Annexes

* [StructuralSurfaceActionDistribution](../loads/structuralsurfaceactiondistribution-1.md)
    * Object renamed to StructuralSurfaceActionDistribution to keep the same naming across the documentation. The only place where the name is shorter is in excel sheet name, where the full name doesn't fit.

* [Ignored Objects and Groups](ignore.md)
    * Updated to contain all the objects
    * StructuralProxyElement, StructuralStorey, StructuralCurveMemberVarying, StructuralCurveMemberVarying and StructuralSurfaceActionDistribution were added

## 14.9.2021 Edge indexing issue 
Discussed in this [discussion](https://github.com/StructuralAnalysisFormat/gitbookdocumentation/discussions/15).

* Clear specification provided for edge indexing ([StructuralEdgeConnection](../supports-and-hinges/structuraledgeconnection.md),  [RelConnectsSurfaceEdge](../supports-and-hinges/relconnectssurfaceedge.md),  [RelConnectsRigidMember](../supports-and-hinges/relconnectsrigidmember.md), [StructuralCurveAction](../loads/structuralcurveaction.md), [StructuralCurveMoment](../loads/structuralcurvemoment.md))

## 15.7.2021 Improving clarity of required values in loads
* [StructuralLoadGroup](../loads/structuralloadgroup.md)&#x20;
    * "Load type" string: condition moved from description (required only for "Load group >type" = Variable)

* [StructuralSurfaceActionDistribution](../loads/structuralsurfaceactiondistribution-1.md)
    * "Load applied to" string: attribute is not required (required string was in >contradiction with description) ​​​​​​​
---

## 8.8.2021 - Fixing flaws in SAF spec v1.0.9 and v2.0.0

Following changes were done based on the proposal discussed in this [discussion](https://github.com/StructuralAnalysisFormat/gitbookdocumentation/discussions/7) and changed in this [issue](https://github.com/StructuralAnalysisFormat/gitbookdocumentation/issues/11).

* [StructuralSurfaceActionDistri](../loads/structuralsurfaceactiondistribution-1.md) (SAF 1.0.9)
    * Object renamed from StructuralSurfaceActionDistribution to StructuralSurfaceActionDistri. Original name exceeds the allowed number of characters for the name of an excel sheet.

* [StructuralSurfaceAction](../loads/structuralsurfaceaction.md) (SAF 1.0.9)
    * added new column: "2D member distribution" - reference to StructuralSurfaceActionDistri
    * added new column: "Force action" - enum defining on which object is load applies (On 2D member, On 2D member region, On 2D member distribution)
    * change of a rule: "2D member column" required only if Force action = "On 2D member"

* [StructuralCurveAction](../loads/structuralcurveaction.md) (SAF 2.0.0)
    * new column added for reference: "2D member region" - reference to StructuralSurfaceMemberRegion
    * new column added for reference: "2D member opening" - reference to StructuralSurfaceMemberOpening

* [StructuralCurveMoment](../loads/structuralcurvemoment.md) (SAF 2.0.0)
    * new column added for reference: "2D member region" - reference to StructuralSurfaceMemberRegion
    * new column added for reference: "2D member opening" - reference to StructuralSurfaceMemberOpening

* [StructuralEdgeConnection](../supports-and-hinges/structuraledgeconnection.md) (SAF 2.0.0)
    * new column added for reference: "2D member region" - reference to StructuralSurfaceMemberRegion
    * new column added for reference: "2D member opening" - reference to StructuralSurfaceMemberOpening
