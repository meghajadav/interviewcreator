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

## Command to deploy on EC2 instance

sudo apt update

sudo apt-get update

sudo apt upgrade -y

sudo apt install git curl unzip tar make sudo vim wget -y

git clone 'repository'

ls - to see if repository is available

cd interviewcreator

ls

touch .env

ls -al

vim .env

## command for save .env after updating 
shift+: wq and enter

## install python
sudo apt install python3-pip

python3 -m venv .venv

source .venv/bin/activate

pip3 install -r requirements.txt

python3 app.py
