from comp_dict.compare_dictionaries import comp_dict, is_subset, which_param_subset


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

