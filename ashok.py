import mysql.connector

def insert_data(id, name, email):
    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="roottoor",
        database="nandini_cse"
    )
    mycursor = mydb.cursor()

    # Check if the email already exists
    check_email = "SELECT * FROM user WHERE email = %s"
    mycursor.execute(check_email, (email,))
    result = mycursor.fetchone()

    if result:
        print("Email already exists.")
    else:
        # Insert new data
        sql = "INSERT INTO user (id, name, email) VALUES (%s, %s, %s)"
        val = (id, name, email)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    mycursor.close()
    mydb.close()

# Input from user
id = input("Enter the ID: ")
name = input("Enter the name: ")
email = input("Enter the email: ")
password = input("Enter the password (not yet used in query): ")

insert_data(id, name, email)
