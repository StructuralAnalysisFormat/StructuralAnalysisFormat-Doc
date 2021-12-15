# Other Notes


```{warning}
name under devlopment:\
    Change Log\
    Other Notes\
    Tweak Notes\
    Improvement Changes\
    Specification improvements\
```

For release notes go to [Release Notes](release-notes.md). All the other (smaller) changes are documented here. This includes especially changes in wording and visuals. Improvements in the specification are not changing the functionality or compatibility of SAF. These changes only improve the understandability of SAF documentation.


## 9.12.2021 Transfer to Read the Docs and other changes
In order to move to new provider [Read the Docs](https://readthedocs.org/), it was nescesary do extensive changes in syntax. Hints and notes visuals were changed, images sizes were set and links were updated. No content was edited.

[Changelog](changelog.md)
* New page Changelog was created to separate smaller changes in documentation from [Release Notes](release-notes.md)

[StructuralSurfaceActionDistribution](../loads/structuralsurfaceactiondistribution-1.md)
* Object renamed to StructuralSurfaceActionDistribution to keep the same naming across the documentation. The only place where the name is shorter is in excel sheet name, where the full name doesn't fit.

[Ignored Objects and Groups](project-and-model-specifications/ignore.md)
* Updated to contain all the objects
* StructuralProxyElement, StructuralStorey, StructuralCurveMemberVarying, StructuralCurveMemberVarying and StructuralSurfaceActionDistribution were added

## 14.9.2021 Edge indexing issue 
[GitHub](https://github.com/StructuralAnalysisFormat/gitbookdocumentation/discussions/15) - discussion&#x20;

* Clear specification provided for edge indexing ([StructuralEdgeConnection](../supports-and-hinges/structuraledgeconnection.md),  [RelConnectsSurfaceEdge](../supports-and-hinges/relconnectssurfaceedge.md),  [RelConnectsRigidMember](../supports-and-hinges/relconnectsrigidmember.md), [StructuralCurveAction](../loads/structuralcurveaction.md), [StructuralCurveMoment](../loads/structuralcurvemoment.md))

## 15.7.2021 
[StructuralLoadGroup](../loads/structuralloadgroup.md)&#x20;

* "Load type" string: condition moved from description (required only for "Load group >type" = Variable)

 [StructuralSurfaceActionDistribution](../loads/structuralsurfaceactiondistribution-1.md)

* "Load applied to" string: attribute is not required (required string was in >contradiction with description) ​​​​​​​
---

## 8.8.2021 - Fixing flaws in SAF spec v1.0.9 and v2.0.0

Following changes were done based on the proposal discussed on [GitHub](https://github.com/StructuralAnalysisFormat/gitbookdocumentation/discussions/7) - discussion, [GitHub](https://github.com/StructuralAnalysisFormat/gitbookdocumentation/issues/11) - issue.&#x20;

[StructuralSurfaceActionDistri](../loads/structuralsurfaceactiondistribution-1.md) (SAF 1.0.9)

* Object renamed from StructuralSurfaceActionDistribution to StructuralSurfaceActionDistri. Original name exceeds the allowed number of characters for the name of an excel sheet.

[StructuralSurfaceAction](../loads/structuralsurfaceaction.md) (SAF 1.0.9)

* added new column: "2D member distribution" - reference to StructuralSurfaceActionDistri
* added new column: "Force action" - enum defining on which object is load applies (On 2D member, On 2D member region, On 2D member distribution)
* change of a rule: "2D member column" required only if Force action = "On 2D member"

\
[StructuralCurveAction](../loads/structuralcurveaction.md) (SAF 2.0.0)

* new column added for reference: "2D member region" - reference to StructuralSurfaceMemberRegion
* new column added for reference: "2D member opening" - reference to StructuralSurfaceMemberOpening

[StructuralCurveMoment](../loads/structuralcurvemoment.md) (SAF 2.0.0)

* new column added for reference: "2D member region" - reference to StructuralSurfaceMemberRegion
* new column added for reference: "2D member opening" - reference to StructuralSurfaceMemberOpening

[StructuralEdgeConnection](../supports-and-hinges/structuraledgeconnection.md) (SAF 2.0.0)

* new column added for reference: "2D member region" - reference to StructuralSurfaceMemberRegion
* new column added for reference: "2D member opening" - reference to StructuralSurfaceMemberOpening