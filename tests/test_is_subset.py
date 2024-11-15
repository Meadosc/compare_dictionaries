"""
Test the is_subset() function
"""

from comp_dict.compare_dictionaries import is_subset


def test_is_subset_true_simple(train_1, train_3):
	assert is_subset(train_1, train_3)

def test_is_subset_true_complex(train_4, train_6):
	assert is_subset(train_4, train_6)

def test_is_subset_false_complex(train_6, train_7):
	assert False == is_subset(train_6, train_7)

def test_is_subset_complication(train_8, train_9):
	assert is_subset(train_8, train_9) and is_subset(train_9, train_8)
