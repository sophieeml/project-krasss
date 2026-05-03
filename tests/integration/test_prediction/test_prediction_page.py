import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parents[3] / "app"
sys.path.insert(0, str(APP_DIR))

from main import app



def test_predict_page_contains_pred_form():
    client = app.test_client()

    response = client.get("/predict")
    html = response.get_data(as_text=True)

    assert response.status_code == 200
    assert '<form action="/predict" method="POST">' in html


def test_predict_page_contains_required_form_fields():
    client = app.test_client()

    response = client.get("/predict")
    html = response.get_data(as_text=True)

    assert 'name="county_state"' in html
    assert 'name="target"' in html
    assert 'name="scenario"' in html


def test_predict_page_contains_expected_targets():
    client = app.test_client()

    response = client.get("/predict")
    html = response.get_data(as_text=True)

    assert "CASTHMA" in html
    assert "MHLTH" in html
    assert "PHLTH" in html
    assert "STROKE" in html
    assert "SLEEP" in html


def test_predict_page_contains_expected_scenarios():
    client = app.test_client()

    response = client.get("/predict")
    html = response.get_data(as_text=True)

    assert "low_warming" in html
    assert "middle_road" in html
    assert "high_warming" in html
    assert "very_high_warming" in html