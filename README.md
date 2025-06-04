# Incident-Classification

## Overview

This project is a simple incident classification system that uses a SQLite database to store and manage incident reports. The system allows users to submit incident reports with a title, description, affected service, and AI-generated category and severity.

## Features

* Incident report submission with title, description, affected service, and AI-generated category and severity
* Storage of incident reports in a SQLite database
* Creation of a table to store incident reports

## Requirements

* Python 3.x
* SQLite3 library
* DB Browser for SQLite (optional)

## Setup

1. Clone this repository to your local machine.
2. Install the required libraries by running `pip install -r requirements.txt`.
3. Create a new SQLite database file named `incidents.db` in the root directory of the project.
4. Run the `init_db.py` script to create the `incidents` table in the database.

## Usage

1. Run the `main.py` script to start the incident classification system.
2. Submit an incident report by providing the required fields (title, description, affected service, and AI-generated category and severity).
3. The system will store the incident report in the SQLite database.

## Notes

* This project is a simple example of an incident classification system and is not intended for production use.
* The AI-generated category and severity fields are currently placeholders and do not actually generate values.
* The database schema and table structure can be modified as needed to support additional features or requirements.
* The `init_db.py` script creates a table with the following columns:
	+ `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
	+ `title` (TEXT)
	+ `description` (TEXT)
	+ `affected_service` (TEXT)
	+ `ai_category` (TEXT)
	+ `ai_severity` (TEXT)

## Software Design choices

1. Backend: FastAPI
2. AI Logic: Python(Simulated Rule-based)
3. DB: SQLite

### Reason: 

* FastAPI  provides clean structure and also speed.
* SQLite is Lightweight and suitable for quick setup.
* Simulated logic allows future ML model upgrades.

## Database Schema

The database schema for this project consists of a single table, `incidents`, with the following columns:

| Column Name | Data Type | Description |
| --- | --- | --- |
| `id` | INTEGER PRIMARY KEY AUTOINCREMENT | Unique identifier for each incident report |
| `title` | TEXT | Title of the incident report |
| `description` | TEXT | Description of the incident report |
| `affected_service` | TEXT | Affected service or system |
| `ai_category` | TEXT | AI-generated category for the incident report |
| `ai_severity` | TEXT | AI-generated severity level for the incident report |

## API Design

The API for this project is designed to allow users to submit incident reports and retrieve existing reports. The API consists of the following endpoints:

### POST /incidents

* Create a new incident report
* Request Body:
	+ `title` (string)
	+ `description` (string)
	+ `affected_service` (string)
	+ `ai_category` (string)
	+ `ai_severity` (string)
* Response:
	+ `id` (integer)
	+ `title` (string)
	+ `description` (string)
	+ `affected_service` (string)
	+ `ai_category` (string)
	+ `ai_severity` (string)

### GET /incidents

* Retrieve a list of all incident reports
* Response:
	+ `id` (integer)
	+ `title` (string)
	+ `description` (string)
	+ `affected_service` (string)
	+ `ai_category` (string)
	+ `ai_severity` (string)

## Error Handling

* If you encounter an error message indicating that the `incidents` table does not exist, run the `init_db.py` script to create the table.
* If you encounter an error message indicating that the `description` field is missing, ensure that you are providing a value for this field when submitting an incident report.

## Troubleshooting

* If you encounter an error message indicating that the `conn` variable is not defined, ensure that you have created the `incidents.db` database file and run the `init_db.py` script to create the `incidents` table.
* If you encounter an error message indicating that the `incidents` table already exists, delete the `incidents.db` database file and re-run the `init_db.py` script.

## Assumptions made:

* Rule-based AI is used instead of ML to save time.
* No frontend is implemented, but the architecture supports the React, Next frontend.
* No security is required for this assignment.
* No filtering in GET endpoint for simplicity.

## Potential Improvement and Enhancements:
* Replace ai_calssify_incident() with an actual ML model(e.g. BERT).
* Add PUT and DELETE endpoints for full CRUD.
* Implement a dashboard using React.js or Next.js.
* Add Authentication forsecure APIs

## AI Usage

I used windsurf AI for code completion and error solving.

## AI Code Assistant  Usage Log:

# Codeium Chat Conversation

Note: _This is purely the output of the chat conversation and does not contain any raw data, codebase snippets, etc. used to generate the output._

**User** _at 12:24 pm, Jun 4, 2025_

Explain problem: `"conn" is not defined`

---

**Windsurf** _at 12:25 pm, Jun 4, 2025_



The issue is that the variable `conn` is not defined before it's being used.

In the line `cursor = conn.cursor()`, you're trying to call the `cursor()` method on `conn`, but `conn` hasn't been assigned a value yet.

Looking at the previous line, you have `sqlite3.connect('incidents.db')`, which returns a connection object, but you're not assigning it to a variable.

To fix this, you should assign the result of `sqlite3.connect()` to the `conn` variable, like this:
```python
conn = sqlite3.connect('incidents.db')
```
Then, the rest of your code should work as expected.

So, the corrected code would be:
```python
import sqlite3

def init_db():
    conn = sqlite3.connect('incidents.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, affected_service TEXT, ai_category TEXT, ai_severity TEXT)')
    conn.commit()
    conn.close()
```

---

**User** _at 12:44 pm, Jun 4, 2025_

error: {
    "detail": [
        {
            "type": "missing",
            "loc": [
                "body",
                "description"
            ],
            "msg": "Field required",
            "input": {
                "title": "Server Down",
                "descriptiom": "server is down",
                "affected_service": "Web hosting"
            }
        }
    ]
}

---

**Windsurf** _at 12:45 pm, Jun 4, 2025_



It looks like you're getting a validation error from an API.

The error message is indicating that the `description` field is missing from the request body. However, you're passing a field called `descriptiom` (note the typo) instead of `description`.

To fix this, simply correct the typo in your request body:
```json
{
    "title": "Server Down",
    "description": "server is down",
    "affected_service": "Web hosting"
}
```
Make sure to double-check the spelling of your field names to avoid this kind of error.

---

**User** _at 12:45 pm, Jun 4, 2025_

errrpr:   File "D:\Full Stack Developement\AI Assignment\main.py", line 18, in classify_incident
    cursor.execute('INSERT INTO incidents (title, description, affected_service, ai_category, ai_severity) VALUES (?, ?, ?, ?, ?)', (data['title'],data['description'], data['affected_service'], data['ai_category'], data['ai_severity']))
sqlite3.OperationalError: no such table: incidents

---

**Windsurf** _at 12:46 pm, Jun 4, 2025_



It looks like you're trying to insert data into a table called `incidents`, but that table doesn't exist in your database.

Looking at the code you provided earlier, I see that you have a function `init_db()` that creates a table called `users`, but not `incidents`.

You need to create the `incidents` table before you can insert data into it. You can do this by modifying your `init_db()` function to create the `incidents` table instead of the `users` table.

Here's an updated version of the `init_db()` function that creates the `incidents` table:
```python
def init_db():
    conn = sqlite3.connect('incidents.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS incidents (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, affected_service TEXT, ai_category TEXT, ai_severity TEXT)')
    conn.commit()
    conn.close()
```
Make sure to call this function before trying to insert data into the `incidents` table.

Alternatively, you can also create the `incidents` table manually using a tool like DB Browser for SQLite or by running a SQL query directly in the SQLite database.

Once you've created the `incidents` table, you should be able to insert data into it without getting this error.

_Context Items Read (8):_

- db.py `init_db`
- main.py `classify_incident`
- db.py `(0-0)`
- db.py `(7-9)`
- ai_logic.py `ai_classify_incident`
- main.py `(0-6)`
- main.py `Incident`
- requirements.txt `(0-1)`


---

**User** _at 12:59 pm, Jun 4, 2025_

Create an readme file to explain this project 

---

**Windsurf** _at 12:59 pm, Jun 4, 2025_



Here's a sample README file for your project:

**Incident Classification Project**

**Overview**

This project is a simple incident classification system that uses a SQLite database to store and manage incident reports. The system allows users to submit incident reports with a title, description, affected service, and AI-generated category and severity.

**Features**

* Incident report submission with title, description, affected service, and AI-generated category and severity
* Storage of incident reports in a SQLite database
* Creation of a table to store incident reports

**Requirements**

* Python 3.x
* SQLite3 library
* DB Browser for SQLite (optional)

**Setup**

1. Clone this repository to your local machine.
2. Install the required libraries by running `pip install -r requirements.txt`.
3. Create a new SQLite database file named `incidents.db` in the root directory of the project.
4. Run the `init_db.py` script to create the `incidents` table in the database.
5. To test the API go to `http://127.0.0.1:8000/docs` to test the API.

**Usage**

1. Run the `main.py` script to start the incident classification system.
2. Submit an incident report by providing the required fields (title, description, affected service, and AI-generated category and severity).
3. The system will store the incident report in the SQLite database.

**Notes**

* This project is a simple example of an incident classification system and is not intended for production use.
* The AI-generated category and severity fields are currently placeholders and do not actually generate values.
* The database schema and table structure can be modified as needed to support additional features or requirements.

