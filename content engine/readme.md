# Content-based Recommendation Engine

## Description

It is a flask-based REST webservice designed to be deployed to Heroku and relies on Anaconda for installation of the scientific computing dependencies, and Redis to store precomputed similarities.

Read the comments in engine.py to see how it works. It's very simple!

web.py contains the two endpoints:

1. /train -- calls engine.train() which precomputes item similarities based on their descriptions in sample-data.csv using TF-IDF and cosine similarity.

2. /predict -- given an item_id, returns the precomputed 'most similar' items.

## Try it out!

Create a new virtualenv with the needed dependencies. Note this

> conda create -n crec --file conda.txt

Now, in the virtualenv (``source activate crec``):

> python web.py

Then, in a separate terminal window, train the engine:

> curl -X GET -H "X-API-TOKEN: FOOBAR1" -H "Content-Type: application/json; charset=utf-8" http://127.0.0.1:5000/train -d "{\"data-url\": \"sample-data.csv\"}"

And make a prediction!

> curl -X POST -H "X-API-TOKEN: FOOBAR1" -H "Content-Type: application/json; charset=utf-8" http://127.0.0.1:5000/predict -d "{\"item\":18,\"num\":10}"