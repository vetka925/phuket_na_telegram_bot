import sqlite3

class NABotDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def create_messages_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                text TEXT
            )
        ''')
        self.conn.commit()
    
    def create_admins_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS admins (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT UNIQUE
            )
        ''')
        self.conn.commit()

    def insert_row(self, name, text):
        try:
            self.cursor.execute('INSERT INTO messages (name, text) VALUES (?, ?)', (name, text))
            self.conn.commit()
            print(f"Row with name '{name}' inserted successfully.")
        except sqlite3.IntegrityError:
            print(f"Row with name '{name}' already exists. Use 'edit_row' to update it.")

    def get_text_by_name(self, name):
        self.cursor.execute('SELECT text FROM messages WHERE name = ?', (name,))
        row = self.cursor.fetchone()
        return row[0]

    def remove_row_by_name(self, name):
        self.cursor.execute('DELETE FROM messages WHERE name = ?', (name,))
        if self.cursor.rowcount > 0:
            self.conn.commit()
            print(f"Row with name '{name}' removed successfully.")
        else:
            print(f"No row found with name '{name}'.")

    def edit_row(self, name, new_text):
        self.cursor.execute('UPDATE messages SET text = ? WHERE name = ?', (new_text, name))
        if self.cursor.rowcount > 0:
            self.conn.commit()
            print(f"Row with name '{name}' updated successfully.")
        else:
            print(f"No row found with name '{name}'.")

    def add_admin(self, user_id):
        try:
            self.cursor.execute('INSERT INTO admins (user_id) VALUES (?)', (user_id, ))
            self.conn.commit()
            print(f"Admin '{user_id}' added successfully.")
        except sqlite3.IntegrityError:
            print(f"Admin '{user_id}' added successfully.")
    
    def get_admins(self):
        rows = self.cursor.execute('SELECT user_id FROM admins').fetchall()
        return set([e[0] for e in rows])
    
    def get_text_by_name(self, name):
        self.cursor.execute('SELECT text FROM messages WHERE name = ?', (name,))
        row = self.cursor.fetchone()
        return row[0]

    def remove_admin(self, user_id):
        self.cursor.execute('DELETE FROM admins WHERE user_id = ?', (user_id,))
        if self.cursor.rowcount > 0:
            self.conn.commit()
            print(f"Admin '{user_id}' removed successfully.")
        else:
            print(f"No admin with '{user_id}' found.")

    def close_connection(self):
        self.cursor.close()
        self.conn.close()