import os
from pathlib import Path
from nbconvert.nbconvertapp import NbConvertApp
from nbconvert.exporters import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.writers import FilesWriter

def lambda_handler (event, context):

    name = event["rawPath"].lstrip("/")
    if name == "favicon.ico":
        return {
            "statusCode": 200,
            "body": "",
        }

    executor = ExecutePreprocessor()

    exporter = HTMLExporter()
    exporter.register_preprocessor(executor, True)
    exporter.mathjax_url = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS_CHTML-full,Safe"
    exporter.require_js_url = "https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"

    writer = FilesWriter()
    writer.build_directory = "/tmp"
    writer.relpath = f"{name}.html"

    app = NbConvertApp()
    app.exporter = exporter
    app.writer = writer

    os.environ["var1"] = str(123)
    os.environ["var2"] = str(456)
    app.convert_single_notebook(f"./notebooks/{name}.ipynb")

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": Path(f"{writer.build_directory}/{writer.relpath}").read_text()
    }