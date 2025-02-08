# ASP alternative version
The project consists of an interpreter
## Set up

### Create and activate virtual environment
- `python -m venv venv`
- `venv\Scripts\activate`

### Install requirements
- `pip install -r requirements.txt`

### How to run
- Run the following command in the terminal: `python user_input.py`

### Tests
- To run the tests type the following command in the terminal: `python -m unittest discover -s tst`

# Project Overview
The idea is that we have four components: Facts, Rules, More Rules and Constraints
The 'main' fact is only one and we can connect many entities to it. For example:
- penguin is a bird --> goes to file as: bird(penguin).
- tweety is a bird --> goes to file as: bird(tweety). and so on..

Then we can add more facts:
- penguin cannot_fly --> goes to file as: cannot_fly(penguin).
- tweety sing --> goes to file as: sing(tweety).

Now we establish the rules:
- fly if bird and not cannot_fly and sing --> goes to file as: fly(X) :- bird(X), not cannot_fly(X), sing(X).
- scream if bird and sing --> goes to file as: scream(X) :- bird(X), sing(X).

***after "if" you should enter the 'main' fact***
And finally (optionally) constraints:
- if bird should fly --> bird(X), not fly(X).
- if bird should scream -->  bird(X), not scream(X). (which means that if it a bird it is NOT allowed NOT to fly\sing.)

***after "should" you should enter a rule (it can also be "should not")***
***it is important to mention that this works like implicantion meaning that if the fact 'bird' is False then it doesn't matter if the rest of the facts are True or False, the model is trivially True***
