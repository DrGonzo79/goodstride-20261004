from fastapi.testclient import TestClient
from main import app
client=TestClient(app)

def test_health(): assert client.get("/health").json()=={"status":"ok"}
def test_matches_filters_and_ranks():
    data=client.post("/matches",json={"race":"NYC Marathon","max_minimum":4000,"require_verified":True}).json()
    assert data["count"]==1 and data["matches"][0]["id"]=="nyc-youth"
def test_empty_match_is_explicit():
    response=client.post("/matches",json={"race":"London Marathon","max_minimum":1000})
    assert response.status_code==200 and response.json()["matches"]==[]
def test_invalid_budget_rejected(): assert client.post("/matches",json={"max_minimum":100}).status_code==422
def test_plan_calculates_weekly_target():
    data=client.post("/fundraising-plan",json={"spot_id":"chicago-water","already_raised":200,"weeks_remaining":10}).json()
    assert data["remaining"]==2000 and data["weekly_target"]==200
def test_missing_spot_and_overfunded_fail():
    assert client.post("/fundraising-plan",json={"spot_id":"missing","already_raised":0,"weeks_remaining":10}).status_code==404
    assert client.post("/fundraising-plan",json={"spot_id":"nyc-youth","already_raised":5000,"weeks_remaining":10}).status_code==422
