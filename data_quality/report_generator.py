from datetime import datetime


def generate_report(
    validation_results,
    output_path
):
    output_path.mkdir(
    parents=True,
    exist_ok=True
    )

    report_file = output_path / "data_quality_report.md"

    with open(report_file, "w", encoding="utf-8") as file:

        file.write("# RetailSphere Data Quality Report\n\n")

        file.write(
            f"Execution Date: {datetime.now()}\n\n"
        )

        file.write("---\n\n")

        for result in validation_results:

            if "Table" in result:

                file.write(f"## {result['Table']}\n")

            else:

                file.write(f"## {result['Relationship']}\n")

            for key, value in result.items():

                file.write(f"- {key}: {value}\n")

            file.write("\n")