from jev_research.rubrics import (
    claim_questions,
    paper_questions,
    proposal_questions,
    writing_questions,
)


def _assert_choice_only(questions: dict) -> None:
    assert questions
    for question in questions.values():
        assert question["type"] == "choice"
        assert len(question["criteria"]) >= 2


def test_v01_rubrics_use_choice_questions() -> None:
    _assert_choice_only(paper_questions())
    _assert_choice_only(proposal_questions())
    _assert_choice_only(writing_questions())
    _assert_choice_only(claim_questions())
