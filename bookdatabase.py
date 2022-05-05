'''
Database using SQL to store book information. Such as what you plan to read, what you have read, and overall book score /10.
'''

from pickle import NONE
import sqlite3

#Connect to the database
connection = sqlite3.connect('Books.db')
cursor = connection.cursor()

#Create the table (if it doesn't exist)
cursor.execute("CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, status TEXT, SCORE TINYINT)")

def get_title(cursor):
  cursor.execute("SELECT title FROM books")
  index = 1
  results = cursor.fetchall()
  for titles in results:
    print(f"{index}. {titles[0]}")
    index += 1
  choice = int(input("Select >"))
  print(results)
  print(results[choice-1])
  return results[choice-1]

#Simple choice dashboard 
choice = NONE
while choice != "0":
    print("0) Quit Program")
    print("1) Display Books")
    print("2) Add Books")
    print("3) Delete Books")
    print("4) Update Books")
    choice = input("> ")
    if choice == "1":
        #Display a list of all books
        cursor.execute("SELECT * FROM books ORDER BY title DESC")
        print("{:>10}  {:>15}  {:>10}  {:>8}".format("Title", "Author", "Status", "Score"))
        for record in cursor.fetchall():
            print("{:>10}  {:>15}  {:>10}  ".format(record[0], record[1], record[2]), record[3])
    elif choice == "2":
        #Add a new book
        title = input("Title: ")
        author = input("Author: ")
        status = input("Status: ")
        score = input("Score: ")
        values = (title, author, status, score)
        cursor.execute("INSERT INTO books VALUES (?, ?, ?, ?)", values)
        connection.commit()
    elif choice == "3":
        title = get_title(cursor)
        values = (title)
        cursor.execute("DELETE FROM books WHERE title = (?)", values)
        pass
    elif choice == "4":
        #Update a books status or score
        print("1) Update Status")
        print("2) Update Score")
        update_choice = input("> ")
        if update_choice == "1":
            title = input("Title: ")
            status = input("Status: ")
            update_values = (status, title)
            cursor.execute("UPDATE books SET status = (?) WHERE title = (?) ", update_values)
            if cursor.rowcount == 0:
                print("ERROR INVALID TITLE")
        elif update_choice == "2":
            title = input("Title: ")
            score = input("Score: ")
            update_values = (score, title)
            cursor.execute("UPDATE books SET score = (?) WHERE title = (?) ", update_values)
            if cursor.rowcount == 0:
                print("ERROR INVALID TITLE")

#Close the database connection   
connection.close()