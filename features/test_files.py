from nose.tools import *

from custom_asserts import *
from files import *


def test_adding_two_files():
    f = Files('file_path')
    assert f.add('id1', 'file1') != None
    assert f.add('id2', 'file2') != None


def test_getting_valid_id_files():
    f = Files('file_path')
    f.add('id1', 'file1')
    f.add('id2', 'file2')
    assert f.get('id1') != None
    assert f.get('id2') != None


def test_getting_filenames():
    f = Files('file_path')
    f.add('id1', 'file1')
    f.add('id2', 'file2')
    assert f.get('id1').filename == 'file1'
    assert f.get('id2').filename == 'file2'


def test_getting_full_filenames():
    f = Files('file_path')
    f.add('id1', 'file1')
    f.add('id2', 'file2')
    assert f.get_filename('id1') == 'file_path/file1'
    assert f.get_filename('id2') == 'file_path/file2'


@raises(DuplicatedFileException)
def test_duplicating_files():
    f = Files('file_path')
    f.add('id1', 'file1')
    f.add('id1', 'file2')


def test_invalid_file_id():
    f = Files('file_path')
    f.add('id1', 'file1')
    f.add('id2', 'file2')
    assert_exception_and_message(
            NotFoundFileException,
            lambda: f.get('id3'),
            'File id id3 not found. Possible values: id1,id2',
    )
