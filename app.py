from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'roottoor'
app.config['MYSQL_DB'] = 'lion_ece'
mysql = MySQL(app)

# --- Static Routes ---
@app.route('/')
def printMyname():
    return "If you have dare come to Halasur, meet Halasur Don Karan."

@app.route('/myweb', methods=['GET'])
def myweb():
    return render_template("index.html")

@app.route('/home')
def loadHomeHtml():
    return render_template("home.html")

@app.route('/about')
def loadAboutHtml():
    return render_template("about.html")

@app.route('/contact')
def loadContactHtml():
    return render_template("contact.html")

@app.route('/user_detail')
def userDetail():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM people")
    results = cur.fetchall()
    cur.close()
    return jsonify(results)

# --- Registration Form ---
@app.route('/add_form', methods=['GET'])
def register_form():
    return render_template("register.html")

# --- Add New User ---
@app.route("/add", methods=["POST"])
def addUser():
    id = request.form.get("id")
    email = request.form.get("email")

    cur = mysql.connection.cursor()
    sql = "INSERT INTO people (id, email) VALUES (%s, %s)"
    val = (id, email)
    cur.execute(sql, val)
    mysql.connection.commit()
    cur.close()
    return "Registration successful"

# --- Update Form ---
@app.route("/update_form", methods=["GET"])
def update_form():
    return render_template("update.html")

# --- Update Existing User ---
@app.route("/update", methods=["POST"])
def update():
    id = request.form.get("id")
    email = request.form.get("name")

    cur = mysql.connection.cursor()
    sql = "UPDATE people SET name = %s WHERE id = %s"
    val = (email, id)
    cur.execute(sql, val)
    mysql.connection.commit()
    cur.close()
    return "Update successful"


@app.route("/delete",methods=["POST"])
def deleteuser():
    id= request.form['id']
    
    cur=mysql.connection.cursor()
    sql= "delete from people where id=%s"
    val=[id] 
    # follow same order
    cur.execute(sql,val)
    mysql.connection.commit()
    cur.close()
    return " Delete successful"


@app.route("/delete_form" ,methods=["GET"])
def deleteform():
    return render_template("delete.html")


# --- Run App ---
if __name__ == '__main__':
    app.run()
