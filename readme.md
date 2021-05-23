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