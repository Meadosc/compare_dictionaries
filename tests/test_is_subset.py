"""
Test the is_subset() function
"""

from comp_dict.compare_dictionaries import CompareDictionaries


def test_is_subset_true_simple(train_1, train_3):
	assert CompareDictionaries.is_subset(train_1, train_3)

def test_is_subset_true_complex(train_4, train_6, train_8, train_9):
	assert CompareDictionaries.is_subset(train_4, train_6)
	assert CompareDictionaries.is_subset(train_8, train_9)

def test_is_subset_false_complex(train_6, train_7):
	assert False == CompareDictionaries.is_subset(train_6, train_7)

def test_is_subset_order_independence(train_1, train_3, train_6, train_7, train_8, train_9):
	assert CompareDictionaries.is_subset(train_1, train_3) == CompareDictionaries.is_subset(train_3, train_1) # both true simple
	assert CompareDictionaries.is_subset(train_8, train_9) == CompareDictionaries.is_subset(train_9, train_8) # both true complex
	assert CompareDictionaries.is_subset(train_6, train_7) == CompareDictionaries.is_subset(train_7, train_6) # both false complex
