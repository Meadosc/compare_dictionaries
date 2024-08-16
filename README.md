# Compare_Dictionaries
Compare_Dictionaries compares two nested dictionaries to see if they have unique schemas and/or if one is a subset of the other. 

Granted, that last sentence is gibberish unless you're using my very special definitions of "schema" and "subset". 

These are defined below, but first note that Compare_Dictionaries will by default process an entire dataset in an s3 Bucket, find every unique schema, and save the schema, filename, and count of schemas in the comp_dict/schema/ directory. Schemas that are subsets of another schema are counted under the previously found schema.

### Schema
Here "schema" is defined as the key structure of a dictonary. A simple dictionary may have three keys ('name', 'number', 'weight') which create its schema. All dictionaries with the same three keys and nothing else are considered to have the same schema. The actual values of the dictionary don't matter to it's schema, only the key names.

For example, here are two dictionaries that have the same schema:
```
cat = {
    'name': 'Mittens', 
    'age': 5, 
    'color': 'orange'
    }

dog = {
    'name': 'Rover', 
    'age': 7, 
    'color': 'brown'
    }
```

And two with different schemas:
```
cat = {
    'name': 'Mittens', 
    'age': 5, 
    'color': 'orange'
    }

dog = {
    'name': 'Rover', 
    'age': 7, 
    'breed': 'Lab'
    }
```

You may ask "But this is so simple, why would I need an entire tool set to figure this out? Just take dict.keys() and use Python's built in set logic." And to that I would respond: "rude". Also, Compare_Dictionaries is specifically designed to handle nested dictionaries. Consider:

```
train = {
    'occupancy': {'car_1': 25, 'car_2': 30},
    'average_speed': 100,
}

minivan = {
    'occupancy': {'front': 2, 'middle': 2, 'back': 3},
    'average_speed': 60,
}
```

They have the same top level keys, but are clearly different structures! The solution is of course to compare the keys of the nested dictionaries. But how deep do they go? And how many times are you willing to do this manually before it becomes tedious and you want to automate the process?

Congratulations, you've just walked through my thought process while exploring a large database with inconsistent data.

### Subset
Here "subset" is defined as a schema where the top level keys are a subset of another schema, and that remains true for all nested dictionaries.

For example, train_2 is a subset of train_1:
```
train_1 = {
    'occupancy': {'car_1': 25, 'car_2': 30},
    'average_speed': 100,
}

train_2 = {
    'occupancy': {'car_1': 25},
    'average_speed': 100,
}
```

But train_3 is not a subset of train_1:
```
train_1 = {
    'occupancy': {'car_1': 25, 'car_2': 30},
    'average_speed': 100,
}

train_3 = {
    'occupancy': {'car_1': 25, 'caboose':20},
    'average_speed': 100,
}
```

What about these two dictionaries?
```
train_8 = {
    'occupancy': {
        'car_1': {'left_side':10,'right_side':10},
        'caboose': {'left_side': 11,'right_side': 10},
    },
    'average_speed': 100
}

train_9 = {
    'occupancy': {
        'car_1': {'left_side':10},
        'caboose': {'left_side': 11,'right_side': 10, 'back': 5},
    },
    'average_speed': 100
}
```
Here train_8 contains a dictionary that is a subset of train_9, but train_9 contains a dicitonary that is a subset of train_8! This is where the definition of a dictionary subset becomes ambiguous.

Compare_Dictionaries will consider either of these dictionaries as subsets of the other. For the purposes of parsing similar data structures out of a large dataset, this is ideal, however other use cases may lead to different desired behavior.


## Requirements

[Poetry](https://github.com/python-poetry/poetry)
* Poetry replaces older dependency management systems like requirements.txt, and it helps package your application
* Documentation is available at the website [here](https://python-poetry.org/)

Python Packages:
* boto3
* pyyaml

## Instructions

1. Edit constants.yaml to point to your s3 bucket. You'll need to supply the AWS key to access it as well, but the 'prefix' value is optional.
2. Either run poetry shell or set up the envoronment in your preferred way
```
poetry shell
```
3. From compare_dictionaries/comp_dict/ run main.py. And yes, that should be better, but this is v0.01
```
python main.py
```

## Testing

This repo uses [pytest](https://github.com/pytest-dev/pytest/) for testing. For details, review the source documentation.
```
poetry shell
python -m pytest
```
Pytest is installed as a development dependency within the poetry shell, but it can be used from outside the shell as well, assuming it is installed in the environment.
