# Comp_Dict
Comp_Dict compares two dictionaries with nested dictionaries to see if they have unique schemas and/or if one is a subset of the other. Granted, that last sentence is gibberish unless you're using my very special definitions of "schema" and "subset".

### Schema
Here "schema" is defined as the key structure of a dictonary. So a simple dictionary may have three keys ('name', 'number', 'weight') which consist of it's schema. All dictionaries with the same three keys and nothing else are considered to have the same schema. The actual values of the dictionary don't matter to it's schema, only the key names.

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

You may ask "But this is so simple? Why would I need an entire tool set to figure this out? Just take dict.keys() and use built in set logic." First off: rude. Second off, Comp_Dict is specifically designed to handle dictionaries with nested dictionaries inside.