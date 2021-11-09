# Ideas and proposals for next SAF versions

This chapter is a list of collected feedback, ideas and proposals how to improve SAF format.

**Please note that these ideas were collected among the whole SAF community.**

To discuss these I would encourage you to follow corresponding thread in MS teams or write an email.

If you would found any discrepancy between listed topics and your actual feedback, let us know (as misunderstandings might happen).

## Voting outcome, March 2021

| **Feature name**                               | <p><img src="../.gitbook/assets/1_scia (3).png" alt="1"></p><p>SCIA</p> | <p> <img src="../.gitbook/assets/1_grgnay6o_400x400 (3).png" alt="1">​</p><p>Graphisoft</p> | <p> <img src="../.gitbook/assets/1_radimpex (3).png" alt="1">​</p><p>Radimpex</p> | <p> <img src="../.gitbook/assets/1_logo_lira (3).png" alt="1">​</p><p>LIRA SAPR SAPHIR</p> | <p> <img src="../.gitbook/assets/1_axis (3).png" alt="1">​</p><p>AxisVM</p> | <p> <img src="../.gitbook/assets/1_fem-design-logo (3).png" alt="1">​</p><p>FEM-Design</p> | **Total number of votes** |
| ---------------------------------------------- | :---------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------: | ------------------------- |
| Alignment of tapered beam as shift vector      |                                    1                                    |                                              0                                              |                                         1                                         |                                              1                                             |                                      1                                      |                                              1                                             | **5**                     |
| Change Load case and Load group object content |                                    1                                    |                                              2                                              |                                         0                                         |                                              0                                             |                                      0                                      |                                              0                                             | **4**                     |
| Rotation of supports                           |                                    1                                    |                                              1                                              |                                         1                                         |                                              0                                             |                                      1                                      |                                              0                                             | **4**                     |
| Free geometry supports                         |                                    0                                    |                                              0                                              |                                         1                                         |                                              1                                             |                                      0                                      |                                              1                                             | **3**                     |

## Move SAF to GIT

**Proposal**: We will move SAF documentation to GIT hub using gitbook to maintain documentation.

**Reasoning**: Documentation will be open and much easier for you to propose new idea and discuss them.

MS teams: [Move to GIT](https://teams.microsoft.com/l/channel/19:f9383b54f0d74747a65e8dd15bb1a6bf@thread.skype/Move%20to%20GIT?groupId=ac7791f6-bfa2-46d2-8922-3c0acd48d2b0\&tenantId=7ae3415a-60f6-4b09-82f6-40ee16d1a1d1)\
Email to MS team thread: \<d5944aa6.scia.net@emea.teams.ms>

## Results

**Proposal**: Make transfer of basic results (internal forces and deformations) available via SAF.

**Reasoning**: We are missing this possibility at all and opens huge potential for custom check, 3rd party designers interoperability.

MS teams: [Results](https://teams.microsoft.com/l/channel/19:f8a94404bede4ff2b05533a361df8be3@thread.skype/Results?groupId=ac7791f6-bfa2-46d2-8922-3c0acd48d2b0\&tenantId=7ae3415a-60f6-4b09-82f6-40ee16d1a1d1)\
Email to MS team thread: \<e5a31eed.scia.net@emea.teams.ms>

## Change Load case and Load group object content

**Proposal**: Attribute Load group type Load type from Load group will be moved added and consolidated with enum attribute Load type in Load case.

We will keep Load Group object to group/sort load cases under specific group which says how the load cases in it will be combined (Together, Exclusive, Standard). You can see work in progress here: [LC](https://dev.saf.guide/LC/Default.htm)

**Reasoning**: Current Load case and Load group were becoming misleading and caused confusion for implementors. Also some setting in LC could contradict LG setting.

MS teams: [LC and LG data change](https://teams.microsoft.com/l/channel/19:fd0717f869b441b88bc1a8504a264f97@thread.skype/LC%20and%20LG%20data%20change?groupId=ac7791f6-bfa2-46d2-8922-3c0acd48d2b0\&tenantId=7ae3415a-60f6-4b09-82f6-40ee16d1a1d1)\
Email to MS team thread: \<db4d6432.scia.net@emea.teams.ms>

## National code based loads and combination

**Proposal**: Add info about used code and national annex to Project sheet. Extend Load type to cover EC and IBC national code with annexes. Add reduction factors (based on used code) to combinations.

**Reasoning**: Currently missing, might ease the exchange of load case and combination.

MS teams: [Code dependent LC and CO](https://teams.microsoft.com/l/channel/19:d1b47ceb0b934383ac9f4c3aa728d617@thread.skype/Code%20dependent%20LC%20and%20CO?groupId=ac7791f6-bfa2-46d2-8922-3c0acd48d2b0\&tenantId=7ae3415a-60f6-4b09-82f6-40ee16d1a1d1)\
Email to MS team thread: <4fc987b7.scia.net@emea.teams.ms>

## Free geometry supports

**Proposal**: Extend/create support objects so it is possible to add surface and line support as free geometry objects

**Reasoning**: There is a need to define internal edges or subregions if user wants to define partial support

MS teams: [Free geometry supports](https://teams.microsoft.com/l/channel/19:80052e82fd664af7b2f59736573d2dbe@thread.skype/Free%20geometry%20supports?groupId=ac7791f6-bfa2-46d2-8922-3c0acd48d2b0\&tenantId=7ae3415a-60f6-4b09-82f6-40ee16d1a1d1)\
Email to MS team thread: <4cef7642.scia.net@emea.teams.ms>

## Rotation of supports

**Proposal**: Extend support objects so it is possible to specify inclination of support, defined as vector

**Reasoning**: It would allow to exchange rotated supports

MS teams: [Rotation of support](https://teams.microsoft.com/l/channel/19:7922cd647417491e837016309faa0718@thread.skype/Rotation%20of%20support?groupId=ac7791f6-bfa2-46d2-8922-3c0acd48d2b0\&tenantId=7ae3415a-60f6-4b09-82f6-40ee16d1a1d1)\
Email to MS team thread: <46cf3f0b.scia.net@emea.teams.ms>

## Alignment of tapered beam as shift vector

**Proposal**: Extend [StructuralCurveMemberVarying](https://dev.saf.guide/Content/A\_Objects/8\_\_StructuralCurveMemberVarying.htm) alignment attribute with shift vector

**Reasoning**: Current alignment (Top / Bottom / Left / etc.) is not clear and is misleading. Adding shift is clear info about how the cross-sections should be aligned.

MS teams: [Alignment of CSS](https://teams.microsoft.com/l/channel/19:fe751197230d48ec83665ddf9355d20f@thread.skype/Alignment%20of%20CSS?groupId=ac7791f6-bfa2-46d2-8922-3c0acd48d2b0\&tenantId=7ae3415a-60f6-4b09-82f6-40ee16d1a1d1)\
Email to MS team thread: <9a0db963.scia.net@emea.teams.ms>

## Reinforcement objects

**Proposal**: Extend SAF with new category which would group various reinforcement objects

**Reasoning**:New objects extending current SAF.

MS teams: [Reinforcement objects](https://teams.microsoft.com/l/channel/19:b6ad8c17f2f84f6c83e0518e40ddd9b5@thread.skype/Reinforcement%20objects?groupId=ac7791f6-bfa2-46d2-8922-3c0acd48d2b0\&tenantId=7ae3415a-60f6-4b09-82f6-40ee16d1a1d1)\
Email to MS team thread: <1f72749d.scia.net@emea.teams.ms>
