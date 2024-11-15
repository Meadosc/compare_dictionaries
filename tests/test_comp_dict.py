"""
Test the comp_dict() function
"""

from comp_dict.compare_dictionaries import comp_dict


def test_comp_dict_equal_simple(train_1, train_2):
	assert comp_dict(train_1, train_2)

def test_comp_dict_equal_complex(train_4, train_5):
	assert comp_dict(train_4, train_5)

def test_comp_dict_not_equal_simple(train_1, train_3):
	assert False == comp_dict(train_1, train_3)

def test_comp_dict_not_equal_complex(train_4, train_6):
	assert False == comp_dict(train_4, train_6)
