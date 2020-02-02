# DMIA Sport Homework Checker

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Installation 
```
pip install git+https://github.com/gleberof/DMIA_sport_homework.git
```
or 
```
git clone https://github.com/gleberof/DMIA_sport_homework.git
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