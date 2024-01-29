import os
from nbconvert.nbconvertapp import NbConvertApp

def lambda_handler (event, context):
    app = NbConvertApp()
    return app