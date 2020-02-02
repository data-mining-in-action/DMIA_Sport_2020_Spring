# DMIA Sport Homework Checker

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Installation 
```
pip install -e "git+https://github.com/data-mining-in-action/DMIA_Sport_2020_Spring.git#egg=hwcheck&subdirectory=Homework checker"
```
or 
```
git clone https://github.com/data-mining-in-action/DMIA_Sport_2020_Spring.git
cd "DMIA_Sport_2020_Spring/Homework checker"
python setup.py install
```

## Usage
importing
```
import hwcheck
```

Get token for submission
```
hwcheck.get_token('your_email')
```

Submit homework
```
hwcheck.check(token, homework, task, answer)
```
