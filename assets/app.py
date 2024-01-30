from pathlib import Path
from nbconvert.nbconvertapp import NbConvertApp
from nbconvert.exporters import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.writers import FilesWriter

def lambda_handler (event, context):

    exporter = HTMLExporter()
    exporter.register_preprocessor(ExecutePreprocessor(), True)

    writer = FilesWriter()
    writer.build_directory = "/tmp"
    writer.relpath = "hello.html"

    app = NbConvertApp()
    app.exporter = exporter
    app.writer = writer
    app.convert_single_notebook("./hello.ipynb")

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": Path("/tmp/hello.html").read_text()
    }