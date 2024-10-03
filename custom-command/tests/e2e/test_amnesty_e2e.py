import pytest
from datasets import load_dataset

from ragas import evaluate
from ragas.metrics import (
    answer_relevancy,
    faithfulness,
    context_recall,
    context_precision,
)

def assert_in_range(score: float, value: float, plus_or_minus: float):
    """
    Check if computed score is within the range of value +/- max_range
    """
    assert value - plus_or_minus <= score <= value + plus_or_minus


@pytest.mark.ragas_ci
def test_amnesty_e2e():
    # loading the V2 dataset
    amnesty_qa = load_dataset("explodinggradients/amnesty_qa", "english_v2")["eval"]


    result = evaluate(
        amnesty_qa,
        metrics=[answer_relevancy, faithfulness, context_recall, context_precision],
        in_ci=True,
    )
    assert result["answer_relevancy"] >= 0.5
    assert result["context_recall"] >= 0.55
    assert result["context_precision"] >= 0.55
    # assert_in_range(result["faithfulness"], value=0.4, plus_or_minus=0.1)
