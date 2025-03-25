"""Dictionary Tests"""

__author__ = "730710295"


from dictionary import invert, count, favorite_colors, bins_len


"""Tests the Invert Function"""


def test_invert_edge_case():
    """Test Invert with an Edge Case"""
    assert invert({}) == {}


def test_invert_use_case_0():
    """Tests Invert with a Use Case"""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_use_case_1():
    """Tests Invert with Another Use Case"""
    assert invert({"mom": "ur"}) == {"ur": "mom"}


"""Tests the Count Function"""


def test_count_edge_case():
    """Tests the Count Function with an Edge Case"""
    assert count([]) == {}


def test_count_use_case_0():
    """Tests the Count Function with a Use CAse"""
    assert count(["pen", "pineapple", "apple", "pen"]) == {
        "pen": 2,
        "pineapple": 1,
        "apple": 1,
    }


def test_count_use_case_1():
    """Tests the Count Function's Use Case AGAIN"""
    assert count(["meow", "meow", "meow"]) == {"meow": 3}


"""Tests the favorite_colors function"""


def test_favorite_colors_edge_0():
    """Tests the favorite_colors function's edge case"""
    assert favorite_colors({}) == None


def test_favorite_colors_use_0():
    """Tests the favorite_colors function's Use case"""
    assert (
        favorite_colors({"angie": "purple", "mari": "green", "abby": "green"})
        == "green"
    )


def test_favorite_colors_use_1():
    """Tests the favorite_colors function's Use case"""
    assert favorite_colors(
        {"angie": "purple", "emily": "blue", "elizabth": "blue", "dev": "purple"}
    )


def test_favorite_colors_edge_1():
    """Tests the favorite_colors function's edge case"""
    assert favorite_colors({"obi": "pink"})


"""Test bins_len function"""


def test_bins_len_edge():
    """Tests the edge case of the bins_len function"""
    assert bins_len([]) == {}


def test_bins_len_use_0():
    """Tests the use case of the bins_len function"""
    assert bins_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: "quick"}


def test_bins_len_use():
    """Tests the use case of the bins_len function"""
    assert bins_len(["boom", "shakalaka", "boom"]) == {4: {"boom"}, 9: "shakalaka"}
