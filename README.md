fake-accounts
====

## Overview

Generate fake user accounts which are username, Email and password for test-account

## Requirement
- python3
- pip3
- git


## Usage

- basic usage
```
python fake_accounts.py -l 1000 -t random
```

- options

```
usage: fake_accounts.py [-h] -l LENGTH -t {random,increment} [-o OUTPUT]

generate fake user account for password list attack

optional arguments:
  -h, --help            show this help message and exit

  -l LENGTH, --length LENGTH
                        number of fake user account
  -t {random,increment}, --usertype {random,increment}
                        type of username random or increment such as user01,
                        user02...
  -o OUTPUT, --output OUTPUT
                        output csv file of fake accounts
```

## Install

```
git clone https://github.com/kazu0716/fake-accounts.git
cd fake-accounts/
pip3 install -r requirement.txt
python3 fake_accounts.py -l 1000 -t random
```
