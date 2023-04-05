""" Test suite """
from school_schedule.student import Student
import pytest


def test_instantiate_valid_student():
    """ docstring """
    quinn = Student(
        "Quinn",
        "junior",
        [
            "Pre-Calc",
            "English III",
            "World History",
            "Gym",
            "Chemistry",
            "Music Composition"
        ]
    )
    assert quinn.name == "Quinn"
    assert len(quinn.classes) == 6


def test_class_list_empty_is_zero():
    """ docstring """
    quinn = Student(
        "Quinn",
        "junior",
        []
    )

    assert len(quinn.classes) == 0

def test_add_class():
    """ docstring """
    quinn = Student(
        "Quinn",
        "junior",
        []
)
    quinn.add_class('Creative Writing')
    assert len(quinn.classes) == 1

# def test_if_grade_not_string_raise_attribute_error():
#     """ docstring """
#     quinn = Student(
#     "Quinn",
#     10,
#     []
# )
#     with pytest.raises(AttributeError):
#         print('Please enter one of the following grades: freshman, sophomore, junior, or senior.')

#     assert 