"""
Iterate over dictionaries and find the unique keys
"""
from compare_dictionaries import CompareDictionaries
from dict_schema import DictSchema
from data_fetcher.data_fetcher import FetcherFactory
from helper import save_schemas


def main():
	# get data
	fetcher = FetcherFactory.get_fetcher("test")
	generator = fetcher.return_generator()

	# process data
	schemas = get_schemas_from_data(generator)
	save_schemas(schemas)	


def get_schemas_from_data(data_generator):
	schemas = []
	for i, (chunk, fname) in enumerate(data_generator):
		if i % 100 == 0 and i > 0: # simple checkpoint
			save_schemas(schemas)	
		
		print(f"{fname}")
		for index, d in enumerate(chunk):
			schema_exists = False 
			
			# check if current schema is identical to a previously found schema
			for obj in schemas:
				match = CompareDictionaries.comp_dict(d, obj.schema)
				if match:
					obj.add(fname, index)
				schema_exists = schema_exists or match

			# if schema is not identical to any previously found schema, check if it's a subset of an existing schema
			if not schema_exists:
				for obj in schemas:
					issubset = CompareDictionaries.is_subset(d, obj.schema)
					if issubset:
						obj.add(fname, index)
						if CompareDictionaries.which_param_subset(d, obj.schema) == 2: # Check if old schema is subset of new schema 
							obj.schema = d # replace the old subset schema
						break # necessary otherwise 'issubset' could be overwritten

				# New schema found! Create a new DictSchema object and append to the list
				if not schemas or not issubset:
					schemas.append(DictSchema(fname, index, d))
	return schemas


if __name__ == '__main__':
	main()
