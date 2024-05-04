from scripts import generate_diff
import pytest


@pytest.fixture
def data_positive():
    file1, file2 = "fixtures/file1.json", "fixtures/file2.json"
    return file1, file2


@pytest.fixture
def data_equal_files():
    file1 = "fixtures/file1.json"
    return file1, file1


@pytest.fixture
def data_different_files():
    file1, file2 = "fixtures/file1.json", "fixtures/file3.json"
    return file1, file2


def test_positive(data_positive):
    result = open("fixtures/result_positive.txt")
    file1, file2 = data_positive
    assert generate_diff(file1, file2) == result.read()


def test_equal_files(data_equal_files):
    result = open("fixtures/result_equal.txt")
    file1, file2 = data_equal_files
    assert generate_diff(file1, file2) == result.read()


def test_completely_different_files(data_different_files):
    result = open("fixtures/result_different.txt")
    file1, file2 = data_different_files
    assert generate_diff(file1, file2) == result.read()
