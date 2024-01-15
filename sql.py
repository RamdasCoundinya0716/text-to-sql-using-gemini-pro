import sqlite3

# Creating a database
connection = sqlite3.connect("E:\Tech\Projects\LLMs\langtosql\student.db")

#creating a cursor
cursor = connection.cursor()

#Create table
table_info = """
CREATE TABLE IF NOT EXISTS student(name varchar(25), class varchar(35), section varchar(25), marks int);
"""
cursor.execute(table_info)

# Inserting records into the table
sql_statements = """
    INSERT INTO student (name, class, section, marks) VALUES
      ('John Doe', 'DevOps', 'A', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('Jane Smith', 'Data Science', 'B', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('Alice Johnson', 'Web Development', 'C', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('Bob Wilson', 'Game Development', 'D', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('Emma Brown', 'DevOps', 'A', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('Frank Miller', 'Data Science', 'B', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('Grace Taylor', 'Web Development', 'C', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('Henry White', 'Game Development', 'D', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('Sophia Adams', 'DevOps', 'A', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('William Turner', 'Data Science', 'B', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('Ella Davis', 'Web Development', 'C', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('James Brown', 'Game Development', 'D', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('Olivia Moore', 'DevOps', 'A', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('Liam Johnson', 'Data Science', 'B', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('Ava Davis', 'Web Development', 'C', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('Noah Smith', 'Game Development', 'D', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('Isabella Wilson', 'DevOps', 'A', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('Mia Brown', 'Data Science', 'B', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('Logan Taylor', 'Web Development', 'C', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('Sophie White', 'Game Development', 'D', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('Ethan Adams', 'DevOps', 'A', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('Amelia Turner', 'Data Science', 'B', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('Jackson Davis', 'Web Development', 'C', CAST(ABS(RANDOM()) % 100 AS INT)),
      ('Avery Moore', 'Game Development', 'D', CAST(ABS(RANDOM()) % 100 AS INT));
"""
cursor.execute(sql_statements)

# Displaying records
print("The inserted Records are: ")

data = cursor.execute("select * from student")

for row in data:
    print(row)

# Closing the Connection
connection.commit()
connection.close()