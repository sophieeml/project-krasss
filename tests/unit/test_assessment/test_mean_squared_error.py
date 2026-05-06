import sys
from pathlib import Path

import numpy as np

APP_FUNCTIONS = Path(__file__).resolve().parents[3] / "app" / "functions"
sys.path.insert(0, str(APP_FUNCTIONS))

from assessment import Assessment



def test_mean_squared_error_expected_value():
    assessment = Assessment()

    y_true = np.array([1, 2, 3])
    y_pred = np.array([1, 2, 5])

    result = assessment.mean_squared_error(y_true, y_pred)

    assert result == 4 / 3