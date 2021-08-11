from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import json
from pythonizedData import *

app = FastAPI()

f = open('OrientationData.json', 'r')
data = json.load(f)

@app.get("/")
def home():
    return "welcome"


@app.get("/calendar/{input_calendar}/date/{input_date}/")
def info(input_calendar: str, input_date: str):
    if input_calendar == "oteam":

        if input_date == "82421":
            return oteam824Events

        if input_date == "82521":
            return oteam825Events

        if input_date == "82621":
            return oteam826Events

        if input_date == "82721":
            return oteam827Events

        if input_date == "82821":
            return oteam828Events

    if input_calendar == "FY":
        if input_date == "82421":
            return FY824Events

        if input_date == "82521":
            return FY825Events

        if input_date == "82621":
            return FY826Events

        if input_date == "82721":
            return FY827Events

        if input_date == "82821":
            return FY828Events

    if input_calendar == "S2Y":
        if input_date == "82421":
            return S2Y824Events

        if input_date == "82521":
            return S2Y825Events

        if input_date == "82621":
            return S2Y826Events

        if input_date == "82721":
            return S2Y827Events

        if input_date == "82821":
            return S2Y828Events
