import sqlite3
def init_db():
    conn = sqlite3.connect('incidents.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS incidents (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, affected_service TEXT, ai_category TEXT, ai_severity TEXT)')
    conn.commit()
    conn.close()
    
if __name__ == '__main__':
    init_db()