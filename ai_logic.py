def ai_classify_incident(incident: dict) -> dict:
    # Perform AI classification based on incident data
    title = incident['title'].lower()
    description = incident['description'].lower()
    
    if "server" in description or "down" in title:
        category = "Infrastructure"
        severity = "High"
    elif "login" in title or "authentication" in description:
        category = "Access Management"
        severity = "Medium"
    else:
        category = "General"
        severity = "Low"
    
    incident['ai_category'] = category
    incident['ai_severity'] = severity
    return incident