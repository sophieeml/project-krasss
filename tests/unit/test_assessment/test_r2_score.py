import sys
from pathlib import Path

import numpy as np

APP_FUNCTIONS = Path(__file__).resolve().parents[3] / "app" / "functions"
sys.path.insert(0, str(APP_FUNCTIONS))

from assessment import Assessment



def test_r2_score_perfect_predictions():
    assessment = Assessment()

    y_true = np.array([1, 2, 3])
    y_pred = np.array([1, 2, 3])

    result = assessment.r2_score(y_true, y_pred)

    assert result == 1.0