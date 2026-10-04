from datetime import date
from typing import Literal
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="GoodStride matching API", version="0.1.0")

SPOTS = [
 {"id":"nyc-youth","charity":"Miles for Youth","cause":"Youth","race":"NYC Marathon","deadline":"2026-06-30","minimum":3500,"spots":8,"verified":True},
 {"id":"nyc-food","charity":"City Table Fund","cause":"Food access","race":"NYC Marathon","deadline":"2026-05-15","minimum":4250,"spots":3,"verified":True},
 {"id":"chicago-water","charity":"Clear Water Relay","cause":"Clean water","race":"Chicago Marathon","deadline":"2026-07-15","minimum":2200,"spots":12,"verified":True},
 {"id":"berlin-climate","charity":"Run Green Europe","cause":"Climate","race":"Berlin Marathon","deadline":"2026-04-30","minimum":2900,"spots":5,"verified":False},
 {"id":"london-health","charity":"Bright Minds UK","cause":"Mental health","race":"London Marathon","deadline":"2026-10-31","minimum":3000,"spots":10,"verified":True},
]

class MatchRequest(BaseModel):
    race: str | None = Field(default=None, max_length=80)
    cause: str | None = Field(default=None, max_length=80)
    max_minimum: int = Field(ge=500, le=25000)
    require_verified: bool = True

class PlanRequest(BaseModel):
    spot_id: str = Field(min_length=2, max_length=80)
    already_raised: int = Field(ge=0)
    weeks_remaining: int = Field(ge=1, le=52)

@app.get("/health")
def health() -> dict[str, str]: return {"status":"ok"}

@app.post("/matches")
def matches(request: MatchRequest) -> dict:
    found=[]
    for spot in SPOTS:
        if request.race and spot["race"] != request.race: continue
        if request.cause and spot["cause"] != request.cause: continue
        if spot["minimum"] > request.max_minimum: continue
        if request.require_verified and not spot["verified"]: continue
        score=100-round(spot["minimum"]/request.max_minimum*35)+(8 if request.cause else 0)
        found.append({**spot,"fit_score":max(0,min(100,score))})
    found.sort(key=lambda item:(-item["fit_score"],item["minimum"]))
    return {"count":len(found),"matches":found,"disclaimer":"Fictional demo inventory; verify directly with the charity."}

@app.post("/fundraising-plan")
def fundraising_plan(request: PlanRequest) -> dict:
    spot=next((item for item in SPOTS if item["id"]==request.spot_id),None)
    if not spot: raise HTTPException(status_code=404,detail="Charity place not found")
    if request.already_raised > spot["minimum"]: raise HTTPException(status_code=422,detail="already_raised exceeds the commitment")
    remaining=spot["minimum"]-request.already_raised
    return {"spot_id":spot["id"],"remaining":remaining,"weekly_target":round(remaining/request.weeks_remaining,2),"weeks":request.weeks_remaining}
