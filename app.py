from flask import Flask, request  
from flask_mysqldb import MySQL  

app = Flask(__name__)  


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'roottoor'
app.config['MYSQL_DB'] = 'aug_cse'

mysql = MySQL(app)

@app.route('/')
def home():
    return "Hello from Flask!"

@app.route('/save_blog', methods=['POST'])
def save_blog():
    #title = request.form["title"]
    #content = request.form["content"]
    json =request.get_json()
    title=json.get("title")
    content=json.get("content")
    cur = mysql.connection.cursor()
    sql = "insert into blog (title, content) values (%s, %s)"
    val = [title, content]
    cur.execute(sql, val)
    mysql.connection.commit()
    cur.close()
    return "Register success"





@app.route('/update_blog', methods=['POST'])
def update_blog():
    #title = request.form["title"]
    #content = request.form["content"]
    json =request.get_json()
    id=json.get("id")
    title=json.get("title")
    content=json.get("content")
    cur = mysql.connection.cursor()
    sql = "update blog set title=%s,content=%s where id=%s"
    val = [title, content,id]
    cur.execute(sql, val)
    mysql.connection.commit()
    cur.close()
    return "Register success"


if __name__ == '__main__':
    app.run()




@app.route('/delete_blog', methods=['POST'])
def delete_blog():
    #title = request.form["title"]
    #content = request.form["content"]
    json =request.get_json()
    id=json.get("id")
    cur = mysql.connection.cursor()
    sql = "delete from blog where id=%s"
    val = [id]
    cur.execute(sql, val)
    mysql.connection.commit()
    cur.close()
    return "Register success"


if __name__ == '__main__':
    app.run()




@app.route('/select_blog', methods=['POST'])
def select_blog():
    #title = request.form["title"]
    #content = request.form["content"]
    json =request.get_json()
    id=json.get("id")
    cur = mysql.connection.cursor()
    sql = "select * from blog where id=%s"
    val = [id]
    cur.execute(sql, val)
    mysql.connection.commit()
    cur.close()
    return "Register success"


if __name__ == '__main__':
    app.run()


