# pybaht

[![CI and CD](https://github.com/jojoee/pybaht/actions/workflows/continuous-integration.yml/badge.svg?branch=main)](https://github.com/jojoee/pybaht/actions/workflows/continuous-integration.yml)
[![PyPI version fury.io](https://badge.fury.io/py/pybaht.svg)](https://pypi.python.org/pypi/pybaht/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/jojoee/pybaht/branch/main/graph/badge.svg)](https://codecov.io/gh/jojoee/pybaht)

Baht library for Python

## Installation

```
pip install pybaht
```

## Usage

```python
from pybaht import bahttext

bahttext(37) == "สามสิบเจ็ดบาทถ้วน"
bahttext(63147.89) == "หกหมื่นสามพันหนึ่งร้อยสี่สิบเจ็ดบาทแปดสิบเก้าสตางค์"
bahttext(-0.36) == "ลบสามสิบหกสตางค์"
```

## Development

```bash
# Conda env
conda create --name pybaht python=3.10.4
conda activate pybaht
 
# test case file
curl -L -o ./tests/testcases.csv https://docs.google.com/spreadsheets/d/e/2PACX-1vTb8PIKzgo07rn9UpcjqE0YrdMAmf4fyDbL2plUieLCyrn_5O3vDvece7UfkaArWQLUSsaw92jVpY_z/pub?gid=0&single=true&output=csv
csvtojson ./tests/testcases.csv | jq > ./tests/testcases.json
```

## Other languages
- JavaScript: [jojoee/bahttext](https://github.com/jojoee/bahttext)

## Reference
- [Google Sheets BAHTTEXT function](https://support.google.com/docs/answer/9982303?hl=en)
