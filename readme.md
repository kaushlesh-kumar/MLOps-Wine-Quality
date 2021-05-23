# Steps Followed in creating the mlops project

### create a virtual environment

```bash
conda create --prefix=wineq python=3.7 -y
```

### activate the environment
```bash
conda activate wineq
```

### create a requirements.txt file & install them
```bash
pip install -r requirements.txt
```

### create a project structure
```bash
python template.py
```

### Download the dataset from -
https://drive.google.com/file/d/1A4Xw5xoHCLY4vo0E93EbjcbSdwrIby5T/view?usp=sharing

### Keep the raw dataset in /source_data/

### Initialize git repo
```bash
git init
```

### Initialize DVC repo
```bash
dvc init
```

### Add dataset to DVC for tracking
```bash
dvc add data/raw/winequality.csv
```

### Add project & model configurations in params.yaml

### Add pipeline for fetching data from Data source- /src/get_data.py

### Add pipeline for loading the raw data locally- /src/load_data.py

### Add load_data stage in dvc.yaml & then run
```bash
dvc repro
```
to run the pipeline

### Add pipeline for spliting dataset into train and test data- /src/split_data.py

### Add split_data stage in dvc.yaml file & then run
```bash
dvc repro
```
to run the pipeline

### Add pipeline for training and evaluation- /src/train_and_evaluate.py

### Add train_and_evaluate stage in dvc.yaml file & then run
```bash
dvc repro
```
to run the pipeline

### To see current parameters ans scores, run
```bash
dvc metrics show
```

### Change model paramerters and run
```bash
dvc repro
```
to run the pipeline again

### To compare previous and current parameters and scores, run
```bash
dvc metrics diff
```

### Create and configure tox.ini file and add test cases for different environments
To run tests on the environments, ensure test cases are added to /tests/test_config.py, & run-
```bash
tox
```

### Create setup.py file & add packaging info to it
Then run-
```bash
pip install -e .
```
We would see a folder in root dir named src.egg-info, where we find Packaging info and contents to be packaged.

Note: To package as a tar, run-
```bash
python setup.py sdist bdist_wheel
```
It would create a distribution for us in /dist, which we can share with others for installing the library.
