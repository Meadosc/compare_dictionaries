class DictSchema:
	def __init__(self, fname, fname_index, schema):
		self.fnames = {fname: [fname_index]}
		self.schema = schema
		self.count = 1

	def add(self, fname, fname_index):
		self.fnames.setdefault(fname, []).append(fname_index)
		self.count += 1
