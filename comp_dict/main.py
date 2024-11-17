"""
Iterate over dictionaries and find the unique keys
"""
import os
import json

from compare_dictionaries import CompareDictionaries
from s3_fetcher import get_s3_data_chunk


class dict_schema:
	def __init__(self, fname, fname_index, schema):
		self.fnames = {fname: [fname_index]}
		self.schema = schema
		self.count = 1

	def add(self, fname, fname_index):
		try:
			self.fnames[fname].append(fname_index)
		except KeyError:
			self.fnames[fname] = [fname_index]
		self.count += 1


def main():
	s3_generator = get_s3_data_chunk()
	schemas = get_schemas_from_data(s3_generator)
	save_schemas(schemas)	


def get_schemas_from_data(s3_generator):
	schemas = []
	for i, (chunk, fname) in enumerate(s3_generator):
		if i % 100 == 0 and i > 0: # simple checkpoint
			save_schemas(schemas)	
		
		print(f"{fname}")
		for index, d in enumerate(chunk):
			schema_exists = False 
			for obj in schemas:
				match = CompareDictionaries.comp_dict(d, obj.schema)
				if match:
					obj.add(fname, index)
				schema_exists = schema_exists or match
			if not schema_exists:
				for obj in schemas:
					issubset = CompareDictionaries.is_subset(d, obj.schema)
					if issubset:
						obj.add(fname, index)
						if CompareDictionaries.which_param_subset(d, obj.schema) == 2:
							obj.schema = d # replace the old subset schema
						break # necessary otherwise 'issubset' could be overwritten
				if not schemas or not issubset:
					schemas.append(dict_schema(fname, index, d))
	return schemas


def save_schemas(schemas):
	print(f"\nnumber of schemas: {len(schemas)}")
	print(f"Saving schemas...")
	for i, schema in enumerate(schemas):
		file_name = os.path.join("comp_dict/schemas", str(i))
		with open(f"{file_name}_schema.json", 'w') as fp:
			json.dump(schema.schema, fp)
		with open(f"{file_name}_fname.json", 'w') as fp:
			json.dump(schema.fnames, fp)
		with open(f"{file_name}_count.txt", 'w') as fp:
			fp.write(str(schema.count))
	print("Done.\n")


if __name__ == '__main__':
	main()
