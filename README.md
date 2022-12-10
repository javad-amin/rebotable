# roboTable
The project simulates a robot moving around on a square table.

## How to run the project
- Install [poetry](https://python-poetry.org/docs/) 
- Activate your virtual environment `$ poetry shell`
- Install the dependencies  `$ poetry install`
- Set your python path `export PYTHONPATH=src`
- Run the app script  `python src/app.py` 
- There is a default command file under `src/examples/commands.txt` in order to try new commands simply replace this file or give the path of your file as input when running the app.

## Commands
### Place 
#### Parameters
* X,Y,D
  
| Parameter | Description | Allowed Values | 
|--|--|--|
| X | coordinate one table | 0 - 4 |
| Y | coordinate one table | 0 - 4 |
| D | direction that robot is facing | "NORTH", "EAST", "SOUTH", "WEST" |
#### Example
* `PLACE 0,0,NORTH` Places the robot on the south west most corner facing north

### MOVE 
#### Example
* `Move` <= moves the robot one square ahead towards the facing direction

### LEFT 
#### Example
* `LEFT` <= rotates the robot to the left by 90 degrees

### RIGHT 
#### Example
* `RIGHT` <= rotates the robot to the right by 90 degrees

### REPORT 
#### Example
* `REPORT` <= reports the position and the direction the robot is facing
#### Outout Example
* `1,2,SOUTH` <= placed on position `(1,2)` facing `SOUTH`


## Linting, Typing & Tests:
`flake8` and `mypy` are used for linting and type checking.
Use `pytest tests` to run the existing unit tests.
