import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] : %(message)s")
'''
This line of code sets up the basic configuration for logging in Python. It configures the root logger to log messages of level INFO and above, and specifies the format in which the log messages should be displayed.

logging.basicConfig: This function sets up the default logging configuration for the root logger.
level=logging.INFO: This sets the logging level to INFO, which means that all messages at INFO level and above (such as WARNING, ERROR, and CRITICAL) will be logged.
format="[%(asctime)s] : %(message)s": This specifies the format of the log messages. %(asctime)s is replaced with the current time in a human-readable format, and %(message)s is replaced with the actual log message.
'''

project_name = 'wine_quality_prediction'

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py', 
    #why do we need __init__.py file? answer: to make it importable and useable.example: from wine_quality_prediction import __init__, here __init__ is the name of the file and wine_quality_prediction is the name of the project in the project folder, so this file is used to import the project. that is why we need this file.
    
    f'src/{project_name}/components/__init__.py', # to make the file inside the components folder importable, not just file but it's function example: from wine_quality_prediction.components import data_ingestion, data_validation, data_transformation, model_trainer, model_evaluation, model_pusher etc.

    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/entity/config_entity.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'param.yaml',
    'schema.yaml',
    'main.py',
    'app.py',
    'setup.py',
    'requirements.txt',
    'research/trial.ipynb',
    'templates/index.html',
]

for filename in list_of_files:
    filepath = Path(filename)
    filedir, filename = os.path.split(filepath)
    # this is to create a directory if the directory doesn't exist.

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")
        # this is to create a directory if the directory doesn't exist.

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    # if the file doesn't exist or is empty, we create it again.

    else:
        logging.info(f"{filename} already exists!")
# tha above means that if the file doesn't exist or is empty, we create it.
