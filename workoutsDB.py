import sqlite3
import json


conn = sqlite3.connect(':memory:', check_same_thread=False)
cursor = conn.cursor()

# Create tables
def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exercises (
        id TEXT PRIMARY KEY,
        name TEXT,
        force TEXT,
        level TEXT,
        mechanic TEXT,
        equipment TEXT,
        primaryMuscles TEXT,
        secondaryMuscles TEXT,
        instructions TEXT,
        category TEXT,
        images TEXT
    )
    """)

create_table()


# Helper method to convert objects into insert statement
def json_to_insert(json_obj, table_name="exercises"):
    # Convert array fields into comma-separated strings
    primary_muscles = ', '.join(json_obj.get("primaryMuscles", [])) or "NULL"
    secondary_muscles = ', '.join(json_obj.get("secondaryMuscles", [])) or "NULL"
    instructions = ', '.join(json_obj.get("instructions", [])) or "NULL"
    images = ', '.join(json_obj.get("images", [])) or "NULL"
    
    # Prepare the values for the INSERT statement
    columns = [
        "id", "name", "force", "level", "mechanic", "equipment",
        "primaryMuscles", "secondaryMuscles", "instructions", 
        "category", "images"
    ]
    
    values = [
        json_obj.get("id", ""),
        json_obj.get("name", ""),
        json_obj.get("force", ""),
        json_obj.get("level", ""),
        json_obj.get("mechanic", ""),
        json_obj.get("equipment", ""),
        primary_muscles,
        secondary_muscles,
        instructions,
        json_obj.get("category", ""),
        images
    ]
    
    # Escape single quotes and prepare the SQL statement
    escaped_values = [f"'{str(value).replace('\'', '\'\'')}'" if value != "NULL" else "NULL" for value in values]
    columns_str = ', '.join(columns)
    values_str = ', '.join(escaped_values)
    
    insert_statement = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str});"
    # print(insert_statement)
    return insert_statement

# Method reads and process the JSON file
def read_and_process_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        # print(data)

        for json_obj in data:
            cursor.execute(json_to_insert(json_obj))
            # print(json_obj)
        conn.commit()

# read_and_process_json('./exercise10.json')

# Query the database
def retrieve_exercises():
    cursor.execute("""
        SELECT * FROM exercises;
    """)
    results = cursor.fetchall()
    return results, [description[0] for description in cursor.description]

print(retrieve_exercises())