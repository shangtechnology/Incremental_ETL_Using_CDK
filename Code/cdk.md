# This is a short run sheet on CDK


Cloud9 Create environment giveit project name

Dev here because it's linux and we will run on
linux

install cdk by 
```commandline
python -m pip inmstall aws-cdk-lib
```
```commandline
mkdir project-name
cd project-name
cdk init app --language python
```
```commandline
source .venv/bin/activiate
```
python decouple is to get environmenrt variables
```commandline
pip install -r requirements.txt
pip install boto3
pip install python_decouple
```
In project folder IDE look for generic folder that can be deleted

Create a folder and python file for each stack
Create new file called .env

Layers for packaging libraries
create a directory layers
create a directory for layer in layers
and a create a python folder in there

```commandline
mkdir layers
mkdir layers/alpha_vantage_layer
mkdir layers/alpha_vantage_layer/python
cd mkdir layers/alpha_vantage_layer/python
pip install -t . alpha_vantage

```
Create app.py

Care you made need to activate env before 
you may also need to bootstrap 

cd to directory with cdk.json
do one ata time from app.py
```commandline
cdk synth KinesisStreamStack
cdk deploy KinesisStreamStack --verbose
```

```commandline

```
