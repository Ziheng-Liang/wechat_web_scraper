from flask.ext.api import FlaskAPI
from flask import request, current_app, abort
from functools import wraps
import csv

app = FlaskAPI(__name__)
app.config.from_object('settings')


def token_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.headers.get('X-API-TOKEN', None) != current_app.config['API_TOKEN']:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


@app.route('/predict', methods=['POST'])
@token_auth
def predict():
    from engines import content_engine
    item = request.data.get('item')
    realID = item
    # if item == -1, means prediction for the last row.
    if item == '-1':
        with open('backup.csv') as source:
            reader = csv.DictReader(source.read().splitlines())
            realID = str(len(list(reader)) - 1)

    num_predictions = request.data.get('num', 10)
    data_url = request.data.get('data-url', None)
    if not realID:
        return []
    
    # For now, only returns a nested list of the top num of post and their scores, need more detailed loggin info!
    return content_engine.predict(str(realID), int(num_predictions), data_url)


@app.route('/train')
@token_auth
def train():
    from engines import content_engine
    data_url = request.data.get('data-url', None)
    content_engine.train(data_url)
    return {"message": "Success!", "success": 1}

# note that backup.csv has fields: [id,title,author,date,content].
@app.route('/update')
@token_auth
def update():
    title = request.data.get('title')
    author = request.data.get('author')
    date = request.data.get('date')
    content = request.data.get('content')
    if content and len(content) > 100:
        with open('backup.csv') as source:
            reader = csv.DictReader(source.read().splitlines())
            # return "number of row: " + str(len(list(reader))) # return the number of rows inside backup.csv, used as next index.
            rowid = str(len(list(reader)))
            newrow = [rowid, title, author, date, content]
            with open('backup.csv', 'a') as target:
                writer = csv.writer(target)
                writer.writerow(newrow)
                return newrow
    else:
        return "Just a reminder that it's successfully updated, while it won't modify the database for now."



if __name__ == '__main__':
    app.debug = True
    app.run()





















