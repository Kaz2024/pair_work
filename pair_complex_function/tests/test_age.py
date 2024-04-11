from lib.age import *
import pytest

def test_age_over_requirement():
    assert age_check_over_18("1960-10-21")

def test_age_over_requirement():
    assert age_check_over_18("2020-10-21")

def test_invalid_format():
    with pytest.raises(Exception) as err:
        age_check_over_18("21-02-1996")
        assert str(err.value) == "The date of birth isn't the right type or format."