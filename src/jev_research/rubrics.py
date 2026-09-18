from __future__ import annotations

from typing import Any

from jev_research.jev.questions import choice_question

RUBRIC_VERSION = "0.1"


def paper_questions(focus: str = "overall") -> dict[str, dict[str, Any]]:
    prefix = f"Evaluate the supplied scientific paper or section. Focus: {focus}. "
    return {
        "methodological_validity": choice_question(
            prefix + "How strong is the methodological validity based only on the supplied text?",
            {
                "strong": "Design and analysis are appropriate with no important apparent weakness.",
                "adequate": "Mostly appropriate, with limitations unlikely to overturn the main inference.",
                "concerning": "One or more important weaknesses could materially affect the inference.",
                "critical": "A fundamental design or analysis problem threatens the main inference.",
                "insufficient_information": "The supplied text is insufficient to judge.",
            },
        ),
        "claim_evidence_alignment": choice_question(
            prefix + "How well do the stated conclusions match the evidence described?",
            {
                "well_aligned": "Claims stay within what the evidence supports.",
                "minor_overreach": "Some wording is stronger than the evidence but the main conclusion remains reasonable.",
                "material_overreach": "Important conclusions go beyond the evidence or analysis described.",
                "contradicted": "The stated conclusion conflicts with the evidence described.",
                "insufficient_information": "The supplied text is insufficient to judge.",
            },
        ),
        "reproducibility_readiness": choice_question(
            prefix + "How reproducible is the described work from the information provided?",
            {
                "high": "Key cohort, variables, preprocessing, analyses, and evaluation steps are operationally specified.",
                "moderate": "Most steps are described but some implementation details are missing.",
                "low": "Multiple important implementation details are missing or ambiguous.",
                "very_low": "The analysis cannot be reconstructed from the supplied description.",
                "not_applicable": "Reproducibility cannot reasonably be judged from this material.",
            },
        ),
        "dominant_scientific_risk": choice_question(
            prefix + "Which single domain is the most important scientific risk in the supplied text?",
            {
                "study_design": "Design, comparator, temporal structure, selection, or confounding.",
                "population": "Sampling, inclusion/exclusion, representativeness, or transportability.",
                "measurement": "Exposure, outcome, phenotype, instrument, labeling, or measurement error.",
                "analysis": "Statistical or machine-learning analysis, assumptions, leakage, multiplicity, or uncertainty.",
                "validation": "Internal or external validation, robustness, calibration, or generalization.",
                "interpretation": "Causal language, extrapolation, clinical meaning, or unsupported conclusion.",
                "reporting": "Missing operational detail, inconsistent reporting, or unclear presentation.",
                "none_apparent": "No important scientific risk is apparent from the supplied text.",
                "insufficient_information": "The supplied text is insufficient to identify a dominant risk.",
            },
        ),
    }


def proposal_questions(section: str = "overall") -> dict[str, dict[str, Any]]:
    prefix = f"Evaluate the supplied research proposal or section. Section: {section}. "
    return {
        "significance_strength": choice_question(
            prefix + "How convincingly does the text establish an important, specific scientific or clinical problem?",
            {
                "strong": "The problem, burden, gap, and consequence are concrete and well connected.",
                "adequate": "The problem is important but one part of the significance argument is underdeveloped.",
                "weak": "Importance is asserted more than demonstrated or the gap is vague.",
                "poor": "The proposal does not establish why the problem matters.",
                "insufficient_information": "The supplied section is insufficient to judge significance.",
            },
        ),
        "aim_method_alignment": choice_question(
            prefix + "How well do the proposed methods answer the stated aims or hypotheses?",
            {
                "tight": "Each aim has a direct method, outcome, and analysis capable of answering it.",
                "mostly_aligned": "Most methods map to aims but some operational or analytic gaps remain.",
                "misaligned": "At least one central aim is not adequately answered by the proposed methods.",
                "fundamentally_misaligned": "The core methods cannot answer the central scientific question.",
                "insufficient_information": "The supplied section is insufficient to judge alignment.",
            },
        ),
        "feasibility": choice_question(
            prefix + "How feasible is the proposed work as written, considering scope, data, recruitment, analysis, and timeline?",
            {
                "high": "The scope and operational plan are credible with appropriate contingencies.",
                "moderate": "Feasible overall but one or more elements need stronger operational detail.",
                "low": "Several unresolved dependencies or scope problems threaten completion.",
                "very_low": "The proposed work is not realistically executable as written.",
                "insufficient_information": "The supplied section is insufficient to judge feasibility.",
            },
        ),
        "overclaim_risk": choice_question(
            prefix + "What is the risk that the proposal overstates novelty, impact, causal inference, or expected benefit?",
            {
                "low": "Claims are appropriately bounded by the proposed design and evidence.",
                "moderate": "Some claims need qualification but do not undermine the proposal.",
                "high": "Several important claims exceed what the design or preliminary evidence can support.",
                "very_high": "The proposal's central promise depends on unsupported or implausible claims.",
                "insufficient_information": "The supplied section is insufficient to judge.",
            },
        ),
        "dominant_reviewer_concern": choice_question(
            prefix + "Which single domain is most likely to generate a substantive scientific reviewer concern?",
            {
                "premise": "Weak scientific premise, gap, or supporting evidence.",
                "innovation": "Novelty is unclear, incremental, or disconnected from impact.",
                "design": "Study design does not adequately address the question.",
                "measurement": "Key constructs, outcomes, or exposures are not operationalized credibly.",
                "analysis": "Statistical, causal, or machine-learning analysis is underspecified or inappropriate.",
                "feasibility": "Recruitment, data, resources, implementation, or timeline is not credible.",
                "safety_ethics": "Human-subjects, safety, privacy, or escalation issues are unresolved.",
                "none_apparent": "No major concern is apparent from the supplied text.",
                "insufficient_information": "The supplied text is insufficient to identify a dominant concern.",
            },
        ),
    }


def writing_questions() -> dict[str, dict[str, Any]]:
    return {
        "clarity": choice_question(
            "Judge the clarity of the supplied scientific writing for an educated reader who may not be a specialist.",
            {
                "clear": "Meaning is direct, sentences are readable, and technical terms are used appropriately.",
                "mostly_clear": "Readable overall with a few dense, ambiguous, or overloaded sentences.",
                "difficult": "Frequent density, ambiguity, jargon, or long constructions interfere with comprehension.",
                "very_difficult": "The writing is hard to follow even for a scientific reader.",
            },
        ),
        "specificity": choice_question(
            "Judge whether the scientific writing uses concrete, operationally meaningful statements instead of vague academic language.",
            {
                "specific": "Claims identify concrete subjects, actions, quantities, methods, or consequences where needed.",
                "mixed": "The text combines specific statements with some vague or generic language.",
                "vague": "Many statements use broad abstractions without enough operational meaning.",
                "very_vague": "The text relies heavily on generic academic phrasing and unclear referents.",
            },
        ),
        "formulaic_llm_style_risk": choice_question(
            "Judge the risk that the prose contains formulaic patterns commonly associated with generic LLM writing. Do not infer authorship. Consider repetitive transitions, rhetorical symmetry, canned contrasts, generic synthesis, and templated paragraph structure.",
            {
                "low": "Few or no formulaic patterns are apparent.",
                "moderate": "Some formulaic patterns are present but do not dominate the prose.",
                "high": "Repeated formulaic constructions are prominent and make the prose sound templated.",
                "very_high": "The prose is dominated by repeated generic and highly patterned constructions.",
            },
        ),
        "scientific_tone": choice_question(
            "Judge whether the prose is scientifically precise without inflated, promotional, or unnecessarily polished language.",
            {
                "appropriate": "Precise and restrained scientific language.",
                "slightly_inflated": "Some unnecessary emphasis or polished academic phrasing.",
                "inflated": "Frequent promotional, grand, vague, or overstated language.",
                "non_scientific": "Tone substantially interferes with scientific precision.",
            },
        ),
        "revision_priority": choice_question(
            "Which single writing problem should be addressed first to improve this text?",
            {
                "clarity": "Sentence structure or organization obscures meaning.",
                "specificity": "Claims or descriptions are too vague to be operationally meaningful.",
                "brevity": "Unnecessary words or repetition weaken the text.",
                "scientific_precision": "Terms, claims, or qualifiers are scientifically imprecise.",
                "formulaic_style": "Templated or repetitive rhetorical patterns weaken the author's voice.",
                "none_apparent": "No important writing problem is apparent.",
            },
        ),
    }


def claim_questions() -> dict[str, dict[str, Any]]:
    return {
        "support_strength": choice_question(
            "Given the claim, evidence, and context in the supplied state, how strongly is the claim supported?",
            {
                "directly_supported": "The evidence directly supports the claim at the stated level of certainty.",
                "partially_supported": "The evidence supports the direction of the claim but not its full scope or certainty.",
                "weakly_supported": "The evidence is indirect, incomplete, or vulnerable to major alternative explanations.",
                "unsupported": "The supplied evidence does not support the claim.",
                "contradicted": "The supplied evidence conflicts with the claim.",
                "insufficient_information": "The supplied information is insufficient to judge.",
            },
        ),
        "inference_type": choice_question(
            "What is the strongest inference type justified by the supplied evidence?",
            {
                "descriptive": "The evidence supports description only.",
                "association": "The evidence supports association but not a causal conclusion.",
                "prediction": "The evidence supports predictive performance for the evaluated setting.",
                "causal": "The design and analysis support a causal inference under stated assumptions.",
                "mechanistic": "The evidence supports a mechanism rather than only an association.",
                "insufficient_information": "The supplied information is insufficient to classify the inference.",
            },
        ),
        "alternative_explanation_risk": choice_question(
            "How vulnerable is the claim to plausible alternative explanations, bias, confounding, measurement error, or chance?",
            {
                "low": "Important alternatives are addressed or unlikely to change the inference.",
                "moderate": "Some alternatives remain but the claim may still be reasonable with qualification.",
                "high": "One or more plausible alternatives could materially change the inference.",
                "very_high": "The claim is highly sensitive to unresolved alternatives.",
                "insufficient_information": "The supplied information is insufficient to judge.",
            },
        ),
        "recommended_claim_action": choice_question(
            "What should be done to the claim before scientific submission?",
            {
                "keep": "The claim can remain as written.",
                "qualify": "Keep the claim but add an important limitation or uncertainty qualifier.",
                "narrow": "Reduce the scope, population, endpoint, or inference strength of the claim.",
                "reframe": "Change the claim to a different inference type, such as association instead of causation.",
                "remove": "The claim should not be made from the supplied evidence.",
                "need_more_information": "More evidence or methodological detail is needed before deciding.",
            },
        ),
    }
