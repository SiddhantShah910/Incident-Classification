from fastapi import FastAPI
from pydantic import BaseModel
from ai_logic import ai_classify_incident
import sqlite3

app = FastAPI()

class Incident(BaseModel):
    title: str
    description: str
    affected_service: str

@app.get("/incidents")
def get_all_incidents():
    conn = sqlite3.connect('incidents.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM incidents')
    rows = cursor.fetchall()
    conn.close()
    incidents = []
    for row in rows:
        incidents.append({
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "affected_service": row[3],
            "ai_category": row[4],
            "ai_severity": row[5]
        })
    
    return {"incidents": incidents}



@app.post("/incidents")
async def classify_incident(incident: Incident):
    data = ai_classify_incident(incident.dict())
    conn = sqlite3.connect('incidents.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO incidents (title, description, affected_service, ai_category, ai_severity) VALUES (?, ?, ?, ?, ?)', (data['title'],data['description'], data['affected_service'], data['ai_category'], data['ai_severity']))
    conn.commit()
    conn.close()
    

    return {"status": "success", incident: data}