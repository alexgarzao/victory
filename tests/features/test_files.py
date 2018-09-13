from nose.tools import raises

from .context import assert_exception_and_message
from .context import Files, DuplicatedFileException, NotFoundFileException


def test_adding_two_files():
    f = Files('file_path')
    assert f.add('id1', 'file1') is not None
    assert f.add('id2', 'file2') is not None


def test_getting_valid_id_files():
    f = Files('file_path')
    f.add('id1', 'file1')
    f.add('id2', 'file2')
    assert f.get('id1') is not None
    assert f.get('id2') is not None


def test_getting_valid_id_files_case_insensitive():
    f = Files('file_path')
    f.add('Id1', 'file1')
    f.add('iD2', 'file2')
    assert f.get('ID1') is not None
    assert f.get('ID2') is not None


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


def test_getting_full_filenames_case_insensitive():
    f = Files('file_path')
    f.add('iD1', 'File1')
    f.add('ID2', 'filE2')
    assert f.get_filename('ID1') == 'file_path/File1'
    assert f.get_filename('id2') == 'file_path/filE2'


@raises(DuplicatedFileException)
def test_duplicating_files():
    f = Files('file_path')
    f.add('id1', 'file1')
    f.add('id1', 'file2')


@raises(DuplicatedFileException)
def test_duplicating_files_case_insensitive():
    f = Files('file_path')
    f.add('id1', 'file1')
    f.add('ID1', 'file2')


def test_invalid_file_id():
    f = Files('file_path')
    f.add('id1', 'file1')
    f.add('id2', 'file2')
    assert_exception_and_message(
            NotFoundFileException,
            lambda: f.get('id3'),
            'File id id3 not found. Possible values: id1,id2',
    )
