# https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial
import sqlite3

con = sqlite3.connect("tutorial.db") # Creates database connection
cur = con.cursor() # Creates cursor

# The database table is called "movie"
cur.execute("CREATE TABLE movie(title, year, score)")


# This adds 2 rows that give a value for "title", "year" and "score"
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

con.commit() # Commits the transaction

# Now we are adding 3 more rows to the table
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()  # Remember to commit the transaction after executing INSERT.