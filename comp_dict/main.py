"""
Iterate over dictionaries and find the unique keys
"""
import os
import json

from compare_dictionaries import comp_dict, is_subset, which_param_subset
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


def save_schemas(schemas):
	print(f"\nnumber of schemas: {len(schemas)}")
	print(f"Saving schemas...")
	for i, schema in enumerate(schemas):
		file_name = os.path.join("schemas", str(i))
		with open(file_name + '_schema.json', 'w') as fp:
			json.dump(schema.schema, fp)
		with open(file_name + '_fname.json', 'w') as fp:
			json.dump(schema.fnames, fp)
		with open(file_name + '_count.txt', 'w') as fp:
			fp.write(str(schema.count))
	print("Done.\n")


def main():
	schemas = []
	s3_gen = get_s3_data_chunk()

	for save_i, (chunk, fname) in enumerate(s3_gen):
		if save_i % 100 == 0 and save_i > 0:
			save_schemas(schemas)	
		print(f"{fname}")

		for index, d in enumerate(chunk):
			schema_exists = False 
			for obj in schemas:
				match = comp_dict(d, obj.schema)
				if match:
					obj.add(fname, index)
				schema_exists = schema_exists or match
			if not schema_exists:
				for obj in schemas:
					it_is_subset = is_subset(d, obj.schema)
					if it_is_subset:
						obj.add(fname, index)
						if which_param_subset(d, obj.schema) == 2:
							obj.schema = d # replace the old subset schema
						break # necessary otherwise 'is_subset' could be overwritten
				if not schemas or not it_is_subset:
					schemas.append(dict_schema(fname, index, d))
	save_schemas(schemas)	


if __name__ == '__main__':
	main()
