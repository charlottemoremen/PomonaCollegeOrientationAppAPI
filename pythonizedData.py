import json
with open('OrientationData.json', 'r') as f:
    data = json.load(f)


class Event:
    def __init__(self, Calendar, eventName, Date, Time, Location):
        self.Calendar = Calendar
        self.eventName = eventName
        self.Date = Date
        self.Time = Time
        self.Location = Location


pythonizedEvents = []
for event in data:
    pythonizedEvents.append(Event(event['Calendar '], event['eventName'], event['Date'], event['Time'], event['Location']))

oteam824Events = []
oteam825Events = []
oteam826Events = []
oteam827Events = []
oteam828Events = []

FY824Events = []
FY825Events = []
FY826Events = []
FY827Events = []
FY828Events = []

S2Y824Events = []
S2Y825Events = []
S2Y826Events = []
S2Y827Events = []
S2Y828Events = []

for x in range(len(pythonizedEvents)):
    if (pythonizedEvents[x].Date == "8/24/21") & (pythonizedEvents[x].Calendar == "OTeam"):
        oteam824Events.append(pythonizedEvents[x])
    if (pythonizedEvents[x].Date == "8/25/21") & (pythonizedEvents[x].Calendar == "OTeam"):
        oteam825Events.append(pythonizedEvents[x])
    if (pythonizedEvents[x].Date == "8/26/21") & (pythonizedEvents[x].Calendar == "OTeam"):
        oteam826Events.append(pythonizedEvents[x])
    if (pythonizedEvents[x].Date == "8/27/21") & (pythonizedEvents[x].Calendar == "OTeam"):
        oteam827Events.append(pythonizedEvents[x])
    if (pythonizedEvents[x].Date == "8/28/21") & (pythonizedEvents[x].Calendar == "OTeam"):
        oteam828Events.append(pythonizedEvents[x])

    if (pythonizedEvents[x].Date == "8/24/21") & (pythonizedEvents[x].Calendar == "FY"):
        FY824Events.append(pythonizedEvents[x])
    if (pythonizedEvents[x].Date == "8/25/21") & (pythonizedEvents[x].Calendar == "FY"):
        FY825Events.append(pythonizedEvents[x])
    if (pythonizedEvents[x].Date == "8/26/21") & (pythonizedEvents[x].Calendar == "FY"):
        FY826Events.append(pythonizedEvents[x])
    if (pythonizedEvents[x].Date == "8/27/21") & (pythonizedEvents[x].Calendar == "FY"):
        FY827Events.append(pythonizedEvents[x])
    if (pythonizedEvents[x].Date == "8/28/21") & (pythonizedEvents[x].Calendar == "FY"):
        FY828Events.append(pythonizedEvents[x])

    if (pythonizedEvents[x].Date == "8/24/21") & (pythonizedEvents[x].Calendar == "2Y"):
        S2Y824Events.append(pythonizedEvents[x])
    if (pythonizedEvents[x].Date == "8/25/21") & (pythonizedEvents[x].Calendar == "2Y"):
        S2Y825Events.append(pythonizedEvents[x])
    if (pythonizedEvents[x].Date == "8/26/21") & (pythonizedEvents[x].Calendar == "2Y"):
        S2Y826Events.append(pythonizedEvents[x])
    if (pythonizedEvents[x].Date == "8/27/21") & (pythonizedEvents[x].Calendar == "2Y"):
        S2Y827Events.append(pythonizedEvents[x])
    if (pythonizedEvents[x].Date == "8/28/21") & (pythonizedEvents[x].Calendar == "2Y"):
        S2Y828Events.append(pythonizedEvents[x])


#for y in range(len(oteam824Events)):
    #print(vars(oteam824Events[y]))




