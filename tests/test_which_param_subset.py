"""
Test the which_param_subset() function
"""

from comp_dict.compare_dictionaries import which_param_subset


def test_which_param_subset_simple_first(train_1, train_3):
	assert which_param_subset(train_1, train_3) == 1

def test_which_param_subset_simple_second(train_1, train_3):
	assert which_param_subset(train_3, train_1) == 2

def test_which_param_subset_complex_first(train_4, train_7):
	assert which_param_subset(train_4, train_7) == 1

def test_which_param_subset_complex_second(train_4, train_6):
	assert which_param_subset(train_4, train_6) == 2
