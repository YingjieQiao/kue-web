# flask-vue-spa

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

