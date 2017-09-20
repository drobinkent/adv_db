from bottle import route, run,debug, template, request
import sqlite3

@route('/hello/<name>')
def index(name):
    print(dict(request.query))
    if (int(request.query.caps) >0 ):
        name = name.upper()
    tag1 = ""
    tag2 = ""
    if (int(request.query.italics) >0 ):
        tag1 = "<i>"
        tag2 = "</i>"
        name = name.upper()

    return template('{{tag1}}Hello {{name}}{{tag2}}!', name=name,tag1=tag1,tag2 = tag2)

@route('/new', method='GET')
def new_item():

    print("gfdksg")
    new = request.GET.task.strip()

    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new, 1))
    new_id = c.lastrowid

    conn.commit()
    c.close()
    print("Done")

    return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id

@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output

run(host='localhost', port=8080, reloader=True)