"""
Testing Fixtures.
The fixtures were arbitrarily chosen to be represented with 'trains' because
it makes the them slightly easier to grok, but the choice of 'trains' has 
no inherent meaning.
"""

import pytest


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


@pytest.fixture
def train_list():
	train_list = [
		{
		'occupancy': {'car_1': 25, 'car_2': 30},
		'average_speed': 100
		},
		{
		'occupancy': {'car_1': 25, 'car_2': 35},
		'average_speed': 100
		},
		{
		'occupancy': {'car_1': 25, 'car_2':30, 'caboose':25},
		'average_speed': 100
		},
		{
		'occupancy': {
			'car_1': 25, 
			'car_2': 30, 
			'caboose': {'left_side': 10,'right_side': 15},
			},
		'average_speed': 100
		},
		{
		'occupancy': {
			'car_1': 25, 
			'car_2': 35, 
			'caboose': {'left_side': 10,'right_side': 15},
			},
		'average_speed': 100
		},
		{
		'occupancy': {
			'car_1': 25, 
			'caboose': {'left_side': 11,'right_side': 10, 'middle': 5},
			},
		'average_speed': 100
		},
		{
		'occupancy': {
			'car_1': 25, 
			'car_2': {'left_side':10,'right_side':10},
			'caboose': {'left_side': 11,'right_side': 10, 'back': 5},
			},
		'average_speed': 100
		},
		{
		'occupancy': {
			'car_1': {'left_side':10,'right_side':10},
			'caboose': {'left_side': 11,'right_side': 10},
			},
		'average_speed': 100
		},
		{
		'occupancy': {
			'car_1': {'left_side':10},
			'caboose': {'left_side': 11,'right_side': 10, 'back': 5},
			},
		'average_speed': 100
		},
	]
	return train_list

