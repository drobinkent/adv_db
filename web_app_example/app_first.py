from bottle import route, run, template, request

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

run(host='localhost', port=8080)