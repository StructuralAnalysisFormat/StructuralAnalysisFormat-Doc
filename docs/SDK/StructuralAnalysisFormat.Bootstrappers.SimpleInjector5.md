# StructuralAnalysisFormat.Bootstrappers.SimpleInjector4
This package will bootstrap the internal components for you, using SimpleInjector v5

## Usage
```csharp
using System;
using System.Linq;
using SAF.Infrastructure.Bootstrapping;
using SAF.Bootstrappers.SimpleInjector5;
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