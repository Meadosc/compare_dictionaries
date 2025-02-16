class DictSchema:
	def __init__(self, fname, fname_index, schema):
		self.fnames = {fname: [fname_index]}
		self.schema = schema
		self.count = 1

	def add(self, fname, fname_index):
		"""
		try:
			self.fnames[fname].append(fname_index)
		except KeyError:
			self.fnames[fname] = [fname_index]
		"""
		self.fnames.get(fname, [fname_index]).append(fname_index)
		self.count += 1
