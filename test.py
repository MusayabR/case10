import pandas as pd
from app import compute_risk_category

def test_risk_category():
    r = compute_risk_category(20000, 4, 15000, 7)
    assert r in ["Low", "Medium", "High", "No data"]


def test_csv_loads():
    df = pd.read_csv("assets/medicalmalpractice.csv")
    assert "Amount" in df.columns
    assert "Severity" in df.columns
    assert len(df) > 0
