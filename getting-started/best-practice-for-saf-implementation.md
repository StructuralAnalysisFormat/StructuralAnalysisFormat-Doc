# Best practice for SAF implementation

Best practice for SAF implementation

This chapter is a list of collected proved and functional approaches for SAF implementation to your application.

{% hint style="warning" %}
**They are not obligatory but following these rules ensures smooth export/import of SAF file and you might avoid any un-foreseen issues.**
{% endhint %}

Please in case you want to:

* explain any of the best practice
* share best practice with us
* challenge anything in this chapter

Contact us via email:

a.vyskocil@scia.net

or send message directly to our MS team channel at - 99ef7709.scia.net@emea.teams.ms

## Header strings

As everybody should follow specified header names in documentation per version, We would also recommend to:

* strip all headers from blank space, dot, comma, dash etc. when importing and base your import on stripped strings
* make import case non-sensitive
* ignore units information in header for import purposes, SAF should be possible to import without this information in header
* when exporting, include units \(for better readability of end user\) according to unit setting and table of units provided in Project and model specifications

## Format of cells

All numerical values \(doubles, integers\) should be exported as "Number" format in Excel

* This rule should apply also for cells which could contain more values, in a case it will have only on.
  * Example: Thickness for StructuralSurfaceMember can contain single value in case of constant thickness type. In this case cell format should be number. In case of variable thickness type, string will be used

## Values in cells

Empty and blank cells

* On export side - do not export blank cells as empty strings, use null value instead
* On import side - null should be standard indicator of blank cell, but make your solution prepared also to empty strings or blank space

Numerical values \(integer, double\)

* You should always read raw data from XML structure of XLS file
* Rounding is not recommended

Numerical chain values \(string\)

* standard separator for more values in a cell is semicolon 

## Culture invariant decimal separator

On import and export side you should always use culture invariant decimal symbol - **dot** and **no thousands separator**

## Units in headers

Import or export should be based on header without unit specification. Missing unit should not block import, either its presence. It is recommended though to include unit information to header for better user read-ability of SAF file.

