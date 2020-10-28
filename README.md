# Kue-Web

## Colab

1. You can fork a copy of this repo and clone to your computer.

2. Create a new branch using git checkout -b BRANCHNAME

3. Commit the code and push to a new branch, and open a pull request.

The rule of thumb is that don't push code to master branch directly.

## Build Setup

``` bash
# install front-end
cd frontend
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production/Flask with minification
npm run build


# install back-end
cd ../backend
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
cd ..

# serve back-end at localhost:5000
FLASK_APP=run.py flask run
```

Take note that you should run both Vue app and Flask app (meaning running 2 commands in 2 terminals) at the same time,

and observe the webpage in the Vue app, of which the url ends with 8000, when developing locally.

TODO:

1. UI realtime update from firebase

2. Java API push data in. Finalize data format.
