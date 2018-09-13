from .context import value_with_mask


def test_1():
    assert value_with_mask('111', 'XXX') == '111'


def test_2():
    assert value_with_mask('111', '(XXX)') == '(111)'


def test_3():
    assert value_with_mask('123456789', '(XX) XXXXXXX') == '(12) 3456789'


def test_4():
    assert value_with_mask('111', '(XXXX)') is None


def test_5():
    assert value_with_mask('11111', '(XXX)') is None
