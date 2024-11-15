""" 
Manage comparison logic 
"""

class CompareDictionaries:

	@classmethod
	def comp_dict(cls, d1, d2):
		"""
		Compare the structure of two dictionaries to see if they are identical
		return True if same schema, False if not
		"""
		if d1.keys() != d2.keys():
			return False
		else:
			same = True
			for key in d1.keys(): # both sets of keys are the same
				if dict == type(d1[key]) == type(d2[key]):
					same = same and cls.comp_dict(d1[key], d2[key])
			return same 

	@classmethod
	def is_subset(cls, d1, d2):
		k1 = d1.keys() # dict.keys() returns a 'dict_keys' object that follows set logic
		k2 = d2.keys()

		if k1 <= k2 or k2 <= k1: # Current comparison is a subset
			issubset = True
			union = k1 & k2
			for k in union:
				if isinstance(d1[k], dict) and isinstance(d2[k], dict):
					issubset = issubset and cls.is_subset(d1[k], d2[k]) # check if nested are subsets
			return issubset
		else: # it's not a subset
			return False	
	
	@classmethod
	def which_param_subset(cls, d1, d2):
		""" 
		Between two dictionaries where one is a subset of the other,
		return ints 1, 2, or 3 depending on the result.
		1: first param is subset of 2nd
		2: second param is subset of 1st
		3: neither are subsets of each other
		"""
		k1 = d1.keys()
		k2 = d2.keys()

		if k1 == k2:
			for key in k1:
				if isinstance(d1[key], dict) and isinstance(d2[key], dict):
					value = cls.which_param_subset(d1[key], d2[key])
					if value == 1 or value == 2:
						return value
					else:
						pass
		elif k1 <= k2:
			return 1 
		elif k1 >= k2:
			return 2 
		else:
			return 3

