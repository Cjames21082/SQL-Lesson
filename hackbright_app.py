import sqlite3

DB = None
CONN = None

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])

def grade_by_project(first_name, last_name, project_title):
    query = """SELECT grade, project_title FROM Students INNER JOIN Grades ON github = student_github 
        WHERE first_name = ? AND last_name = ? AND project_title = ?"""
    DB.execute(query, (first_name, last_name, project_title))
    row = DB.fetchone()
    print """\
    Title: %s
    Grade: %s""" % (row[1], row[0])

def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values (?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github))
    CONN.commit()
    print "Successfully added student: %s %s" % (first_name, last_name)

# def make_new_project(title,description, max_grade):
#     query= """INSERT into Projects values (?,?,?)"""
#     DB.execute(query, (title, description, max_grade))
#     CONN.commit()
#     print "Successfully added project: %s" %(title)

def project_by_title(project_title):
    query = """SELECT title, description, max_grade FROM Projects WHERE title = ?"""
    DB.execute(query, (project_title,))
    row = DB.fetchone()
    print """\
Title: %s
Description: %s
Max Grade: %d"""%(row[0], row[1], row[2])

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "project":
            project_by_title(*args)
        # elif command == "new_project":
        #     make_new_project()
        elif command == "grade":
            grade_by_project(*args)

    CONN.close()

if __name__ == "__main__":
    main()
