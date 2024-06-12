# interviewcreator

# create the virtual env 

conda create -n interviewcreator python=3.9 -y

# conda activate interviewcreator

conda activate interviewcreator

### clone the github repository

git clone https://github.com/meghajadav/interviewcreator.git

## Folder Structure
Create the template.py which will create folder structure and files for the project as follows:
folder src - __init__.py,  helper.py, prompt.py
another files outside src is setup.py, requirements.txt, .env, app.py
another folder research.py which contains trials.ipynb for experiments.

### install requirements.txt
pip install -r requirements.txt

### -e . in requirements.txt tells the python to see for setup.py and install the .py as a local package