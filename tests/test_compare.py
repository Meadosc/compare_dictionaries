"""
Test compare functions
"""


import pytest

from comp_dict.compare_dictionaries import comp_dict, is_subset, which_param_subset


@pytest.fixture
def train_1():
	train_1 = {
		'occupancy': {'car_1': 25, 'car_2': 30},
		'average_speed': 100
	}
	return train_1


@pytest.fixture
def train_2():
	train_2 = {
		'occupancy': {'car_1': 25, 'car_2': 35},
		'average_speed': 100
	}
	return train_2


@pytest.fixture
def train_3():
	train_3 = {
		'occupancy': {'car_1': 25, 'car_2':30, 'caboose':25},
		'average_speed': 100
	}
	return train_3


@pytest.fixture
def train_4():
	train_4 = {
		'occupancy': {
			'car_1': 25, 
			'car_2': 30, 
			'caboose': {'left_side': 10,'right_side': 15},
		},
		'average_speed': 100
	}
	return train_4


@pytest.fixture
def train_5():
	train_5 = {
		'occupancy': {
			'car_1': 25, 
			'car_2': 35, 
			'caboose': {'left_side': 10,'right_side': 15},
		},
		'average_speed': 100
	}
	return train_5


@pytest.fixture
def train_6():
	train_6 = {
		'occupancy': {
			'car_1': 25, 
			'caboose': {'left_side': 11,'right_side': 10, 'middle': 5},
		},
		'average_speed': 100
	}
	return train_6


@pytest.fixture
def train_7():
	train_7 = {
		'occupancy': {
			'car_1': 25, 
			'car_2': {'left_side':10,'right_side':10},
			'caboose': {'left_side': 11,'right_side': 10, 'back': 5},
		},
		'average_speed': 100
	}
	return train_7


@pytest.fixture
def train_8():
	train_8 = {
		'occupancy': {
			'car_1': {'left_side':10,'right_side':10},
			'caboose': {'left_side': 11,'right_side': 10},
		},
		'average_speed': 100
	}
	return train_8


@pytest.fixture
def train_9():
	train_9 = {
		'occupancy': {
			'car_1': {'left_side':10},
			'caboose': {'left_side': 11,'right_side': 10, 'back': 5},
		},
		'average_speed': 100
	}
	return train_9


def test_comp_dict_equal_simple(train_1, train_2):
	assert comp_dict(train_1, train_2)


def test_comp_dict_equal_complex(train_4, train_5):
	assert comp_dict(train_4, train_5)


def test_comp_dict_not_equal_simple(train_1, train_3):
	assert False == comp_dict(train_1, train_3)


def test_comp_dict_not_equal_complex(train_4, train_6):
	assert False == comp_dict(train_4, train_6)


def test_is_subset_true_simple(train_1, train_3):
	assert is_subset(train_1, train_3)


def test_is_subset_true_complex(train_4, train_6):
	assert is_subset(train_4, train_6)


def test_is_subset_false_complex(train_6, train_7):
	assert False == is_subset(train_6, train_7)


def test_which_param_subset_simple_first(train_1, train_3):
	assert which_param_subset(train_1, train_3) == 1


def test_which_param_subset_simple_second(train_1, train_3):
	assert which_param_subset(train_3, train_1) == 2


def test_which_param_subset_complex_first(train_4, train_7):
	assert which_param_subset(train_4, train_7) == 1


def test_which_param_subset_complex_second(train_4, train_6):
	assert which_param_subset(train_4, train_6) == 2


def test_is_subset_complication(train_8, train_9):
	assert is_subset(train_8, train_9) and is_subset(train_9, train_8)

