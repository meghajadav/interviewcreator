import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

file_list=[
    'src/prompt.py',
    'src/__init__.py',
    'src/helper.py',
    'setup.py',
    '.env',
    'research/trials.ipynb',
    'app.py',
    'requirements.txt',
]

for filepath in file_list:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    # print(filedir, filename)
    # if not os.path.exists(filedir):
    if filedir!='':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory {filedir} for the {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w' ) as f:
            pass
            logging.info(f"creating file {filepath}")
    else:
        logging.info(f"{filepath} already exists")