import pytest
from code_challenges.mergesort import merge_sort, merge


def test_exist():
    input_list = [5, 3, 2, 8, 1, 9, 4, 6, 7]
    assert merge_sort(input_list)
    print("pass")


def test_one():
    input_list = [5, 3, 2, 8, 1, 9, 4, 6, 7]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert merge_sort(input_list) == expected
    print('pass')


def test_reverse_sorted():
    input_list = [20, 18, 12, 8, 5, -2]
    expected = [-2, 5, 8, 12, 18, 20]
    assert merge_sort(input_list) == expected
    print('pass reverse_sorted')


def test_few_uniques():
    input_list = [5, 12, 7, 5, 5, 7]
    expected = [5, 5, 5, 7, 7, 12]
    assert merge_sort(input_list) == expected
    print('pass few_uniques')


def test_nearly_sorted():
    input_list = [2, 3, 5, 7, 13, 11]
    expected = [2, 3, 5, 7, 11, 13]
    assert merge_sort(input_list) == expected


def test_small_list():
    input_list = [6, 9, 3]
    expected = [3, 6, 9]
    assert merge_sort(input_list) == expected


def test_empty_list():
    assert merge_sort([]) == []
