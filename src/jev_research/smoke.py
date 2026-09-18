from __future__ import annotations

import json

from jev_research.config import JevConfig
from jev_research.jev.client import JevClient
from jev_research.jev.normalize import normalize_system_one_response
from jev_research.jev.questions import choice_question


def main() -> None:
    questions = {
        "study_design": choice_question(
            "What study design is described?",
            {
                "randomized_trial": "Participants are randomly assigned to intervention groups.",
                "observational": "Exposure or treatment is observed without random assignment.",
                "insufficient_information": "The description does not establish the design.",
            },
        )
    }
    state = (
        "Synthetic smoke-test text: 120 adults were randomly assigned 1:1 "
        "to an intervention or usual-care group and followed for 30 days."
    )

    with JevClient(JevConfig.from_env()) as client:
        raw = client.evaluate(state=state, questions=questions)

    output = {
        "status": "ok",
        **normalize_system_one_response(raw),
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
