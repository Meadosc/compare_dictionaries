"""
Collection of minor helper functions and classes
"""
import json
import os

import yaml


class Constants:
	def __init__(self):
		with open('comp_dict/constants.yaml', 'r') as f:
			constants = yaml.safe_load(f)
		self.constants = constants
		self.prefix = constants['prefix']
		self.prefix_start = constants['prefix_start']
		self.bucket = constants['s3_bucket_name']
	

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