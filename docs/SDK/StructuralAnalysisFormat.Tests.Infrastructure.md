# Tests Infrastructure

**StructuralAnalysisFormat.Tests.Infrastructure**

This package adds some functionality that may come in handy for testing purposes.

[Download the package at nuget.org](https://www.nuget.org/packages/StructuralAnalysisFormat.Tests.Infrastructure)

## Data builders
One of the features are what we call **data builders**
These are fluent-api classes that allow you to quickly construct data objects that by default pass validation.
They also have the benefit that if a property would be renamed on an object, the data builder will be adjusted but the API of the builder remains the same.
Which means you won't have to make any changes to your test code!

```{admonition} Metric & Imperial
Any values unit wise that are set using doubles, will always be metric as this is how the data builders are set up.
If the builder accepts actual units, you are free to provide it with units defined in the imperial system for example.
```

```{admonition} Sane values
While we do our best to make sure that the model actually makes sense in the context of structural engineering, this may sometimes not be the case.  
So it may happen that some objects constructed by either the data builders or from the house model have weird values that do not make sense to a structural engineer.
```

### Usage
The API is the same for each builder available.  
In general _(replace &lt;NameOfDataObject&gt; with the name of object)_:

- The builders all end with *Builder in their name
- `<NameOfDataObject>Builder.Create();` will quickly create an object using either pre-defined or random values that are considered valid in terms of validation
- `<NameOfDataObject>Builder.Setup();` allows you to enter "configuration" mode for the builder
- `<NameOfDataObject>Builder.Setup() ... .Build();` will construct the object for you using the configured settings you have defined in the `...` part

```csharp
using SAF.Infrastructure.Tests.DataBuilders.StructuralElements;
using SAF.DataAccess.Models.StructuralElements;

// Create a node with zero value coordinates (X,Y,Z)
ExcelStructuralPointConnection node = ExcelStructuralPointConnectionBuilder.Create(); 

// Create a node with coordinate values, X = 2 meters, Y = 5.5 meters and Z = 7 meters
ExcelStructuralPointConnection node2 = ExcelStructuralPointConnectionBuilder
    .Setup()
    .WithCoordinates(2D, 5.5D, 7D)
    .Build();
```

## Example models
Another feature is that we have included a full-blown house model.  
The goal of this model is to include every supported object from the SDK.  


You can get this model by executing the following lines of code:
```csharp
using SAF.Infrastructure.Tests.Models;
using SAF.DataAccess.Models;

House house = new House();
ExcelModel houseAsModel = house.Construct();
```