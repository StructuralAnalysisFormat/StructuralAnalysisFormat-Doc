# StructuralAnalysisFormat
This package implements the Structural Analysis Format in C#

The aim of this SDK is to allow anyone to rapidly get started implementing the SAF specification in their own software.

## Features
- Straight forward API (One import and one export service)
- Validation
- Compatibility support between versions
- Effortlessly switch between metric & imperial values

## Dependencies
- Uses [EPPlus](https://github.com/JanKallman/EPPlus) (4.5.3.3) for handling excel files
- Uses [FluentValidation](https://docs.fluentvalidation.net/en/latest/) for validation
- Uses [UnitsNet](https://github.com/angularsen/UnitsNet) for unit operations

## What do you need to do?
In order to use this SDK, it is sufficient for you to provide a mapping between the data objects in your software and the data objects defined in the SDK
Once you have that, you only need to call the import or export service and the rest is taken care of by the SDK.

## Remarks
Due to how this SDK is defined, with most of the actual implementation details being internal, you should also use one of our bootstrapping packages:
- **[StructuralAnalysisFormat.Bootstrappers.SimpleInjector4](./StructuralAnalysisFormat.Bootstrappers.SimpleInjector4.md)**  
  _If you wish to use SimpleInjector v4_
- **[StructuralAnalysisFormat.Bootstrappers.SimpleInjector5](./StructuralAnalysisFormat.Bootstrappers.SimpleInjector5.md)**  
  _If you wish to use SimpleInjector v5_

**If you are only required to work with the data model of the SDK, then this package is sufficient.**

## Usage
```csharp
using System;
using System.Linq;
using SAF.Infrastructure.Bootstrapping;
using SAF.Bootstrappers.SimpleInjector4;
using SAF.Infrastructure.Events;
using SAF.Infrastructure.Extensions;
using SAF.DataAccess.Contracts;
using SAF.DataAccess.Models;
using SAF.DataAccess.Models.Enums;
using SAF.DataAccess.Models.Infrastructure;

class Program
{
    static void Main(string[] args)
    {
        IBootstrapper bootstrapper = new SimpleInjectorBootstrapper();

        IServiceProvider scope = bootstrapper.CreateScope();
        IEventService eventService = scope.GetService<IEventService>();

        using (IEventSubscription subscription = eventService.Subscribe<LogEvent>(OnLog))
        {
            ExcelModel result = Read("some_saf_file.xlsx", scope);

            if (result == null)
            {
                Console.WriteLine("Failed to read excel");
                return;
            }

            Console.WriteLine("Successfully read excel, it contains the following objects:");

            var grouped = result.Objects.GroupBy(x => x.GetType());

            foreach (var group in grouped)
            {
                Console.WriteLine($"{group.Key.Name}: {group.Count()}");
            }

            Console.WriteLine();
            Console.WriteLine("Press any key to continue.");
            Console.Read();
            Console.Clear();

            Write("export.xlsx", result, scope);
        }
    }

    private static void OnLog(LogEvent obj)
    {
        Console.WriteLine($"[{obj.Severity.ToString().ToUpper()}] {obj.Message}");
    }

    private static ExcelModel Read(string file, IServiceProvider scope)
    {
        IExcelImportService reader = scope.GetService<IExcelImportService>();
        ExcelModel result = null;

        using (var stream = File.OpenRead(file))
        {
            result = reader.Import(stream);
        }

        return result;
    }

    private static void Write(string file, ExcelModel source, IServiceProvider scope)
    {
        var writer = scope.GetService<IExcelExportService>();

        using (var stream = File.Create(file))
        {
            writer.Export(stream, source);
        }
    }
}
```