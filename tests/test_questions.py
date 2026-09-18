import pytest

from jev_research.jev.questions import choice_question


def test_choice_question_shape() -> None:
    question = choice_question("Choose one.", {"a": "First", "b": "Second"})
    assert question == {
        "type": "choice",
        "instructions": "Choose one.",
        "criteria": {"a": "First", "b": "Second"},
    }


def test_choice_requires_two_options() -> None:
    with pytest.raises(ValueError):
        choice_question("Choose one.", {"a": "Only"})
