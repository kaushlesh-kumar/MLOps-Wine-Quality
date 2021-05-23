# Steps Followed in creating the mlops project

create a virtual environment

'''bash
conda create --prefix=wineq python=3.7 -y
'''

activate the environment
'''bash
conda activate wineq
'''

create a requirements.txt file & install them
'''bash
pip install -r requirements.txt
'''

create a project structure
'''bash
python template.py
'''

download the dataset from -
[https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/]

Keep the raw dataset in /data/raw

Initialize git repo
'''bash
git init
'''

Initialize DVC repo
'''bash
dvc init
'''

Add dataset to DVC for tracking
'''bash
dvc add data/raw/winequality.csv
'''

Add project & model configurations in params.yaml

Add pipeline for fetching data from Data source- /src/get_data.py

Add pipeline for loading the raw data locally- /src/load_data.py

Add load_data stage in dvc.yaml & then run
'''bash
dvc repro
'''
to run the pipeline

Add pipeline for spliting dataset into train and test data- /src/split_data.py

Add split_data stage in dvc.yaml file & then run
'''bash
dvc repro
'''
to run the pipeline

Add pipeline for training and evaluation- /src/train_and_evaluate.py

Add train_and_evaluate stage in dvc.yaml file & then run
'''bash
dvc repro
'''
to run the pipeline

To see current parameters ans scores, run
'''bash
dvc metrics show
'''

Change model paramerters and run
'''bash
dvc repro
'''
to run the pipeline again

To compare previous and current parameters and scores, run
'''bash
dvc metrics diff
'''
