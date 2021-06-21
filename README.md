




# Pizza_RestAPI



## Requirements

Python 3.6

Django 3.1

Django REST Framework

## Installation

After you cloned the repository, you want to create a virtual environment, so you have a clean python installation. You can do this by running the command

`python -m venv env`

After this, it is necessary to activate the virtual environment,

You can install all the required dependencies by running

`pip install -r requirements.txt`

## Overview of API.







| Methods		    | endpoints/urls         | Actions |
| ------------- |:-------------:| -----:|
| POST      | api/add_pizza | add new pizza |
| GET      | api/pizza      |   get all pizza |
| GET      | api/pizza/?type=xyz      |   get all pizza of **type** 'xyz' |
| GET      | api/pizza/?size=xyz      |   get all pizza of **size** 'xyz' | 
| GET | pizza_detail/id      |    get pizza by id(integer type) |
| PUT | pizza_update/id      |    update pizza by id(integer type) |
| DELETE | pizza_update/id      |    delete pizza by id(integer type) |



