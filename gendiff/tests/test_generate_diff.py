from gendiff import generate_diff
import pytest
import os


@pytest.fixture
def json_positive():
    file1, file2 = "gendiff/tests/fixtures/file1.json", \
                   "gendiff/tests/fixtures/file2.json"
    return file1, file2


@pytest.fixture
def json_equal():
    file1 = "gendiff/tests/fixtures/file1.json"
    return file1, file1


@pytest.fixture
def json_different():
    file1, file2 = "gendiff/tests/fixtures/file1.json", \
                   "gendiff/tests/fixtures/file3.json"
    return file1, file2


@pytest.fixture
def yaml_positive():
    file1, file2 = "gendiff/tests/fixtures/file1.yml", \
                   "gendiff/tests/fixtures/file2.yml"
    return file1, file2


@pytest.fixture
def yaml_equal():
    file1 = "gendiff/tests/fixtures/file1.yml"
    return file1, file1


@pytest.fixture
def yaml_different():
    file1, file2 = "gendiff/tests/fixtures/file1.yml", \
                   "gendiff/tests/fixtures/file3.yml"
    return file1, file2


def test_json_positive(json_positive):
    result_path = os.path.abspath("gendiff/tests/fixtures/result_positive.txt")
    result = open(result_path)
    file1, file2 = json_positive
    assert generate_diff(file1, file2) == result.read()


def test_json_equal(json_equal):
    result_path = os.path.abspath("gendiff/tests/fixtures/result_equal.txt")
    result = open(result_path)
    file1, file2 = json_equal
    assert generate_diff(file1, file2) == result.read()


def test_json_different(json_different):
    result_path = os.path.abspath("gendiff/tests/fixtures/result_different.txt")
    result = open(result_path)
    file1, file2 = json_different
    assert generate_diff(file1, file2) == result.read()


def test_yaml_positive(yaml_positive):
    result_path = os.path.abspath("gendiff/tests/fixtures/result_positive.txt")
    result = open(result_path)
    file1, file2 = yaml_positive
    assert generate_diff(file1, file2) == result.read()


def test_yaml_equal(yaml_equal):
    result_path = os.path.abspath("gendiff/tests/fixtures/result_equal.txt")
    result = open(result_path)
    file1, file2 = yaml_equal
    assert generate_diff(file1, file2) == result.read()


def test_yaml_different(yaml_different):
    result_path = os.path.abspath("gendiff/tests/fixtures/result_different.txt")
    result = open(result_path)
    file1, file2 = yaml_different
    assert generate_diff(file1, file2) == result.read()


def test_file_extension_error():
    file_path = os.path.abspath("gendiff/tests/fixtures/result_positive.txt")
    file1, file2 = file_path, file_path
    with pytest.raises(ValueError) as exc_info:
        assert generate_diff(file1, file2) == exc_info
