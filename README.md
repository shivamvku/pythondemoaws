# Code Standards
Simple python code standards using pylint and pipenv

To make `good.py` pass run `pipenv run pylint --reports=n --disable=useless-else-on-loop --const-rgx='[a-z_][a-z0-9_]{2,30}$' good.py`

To make `bad.py` fail run `pipenv run pylint --reports=n --const-rgx='[a-z_][a-z0-9_]{2,30}$'  bad.py `