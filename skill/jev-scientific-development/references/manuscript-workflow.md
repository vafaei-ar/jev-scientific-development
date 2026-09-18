# Manuscript workflow

## Section development

Draft or revise the section using normal scientific reasoning first. Then call `evaluate_paper` on the smallest section that contains enough context for the question.

For Methods, focus on design, variables, preprocessing, analysis, validation, missingness, uncertainty, and reproducibility.

For Results, focus on whether reported conclusions match analyses and whether uncertainty is represented correctly.

For Discussion, focus on claim-evidence alignment, causal language, generalization, limitations, and unsupported extrapolation.

## Full-paper checkpoint

Near submission, run `evaluate_paper` on the abstract and key conclusion-bearing sections separately rather than sending the entire manuscript as one undifferentiated state. Compare the dominant risks across sections.

Use deterministic checks for numbers, sample sizes, percentages, table/figure consistency, and cross-document contradictions. JEV should complement those checks, not replace them.
