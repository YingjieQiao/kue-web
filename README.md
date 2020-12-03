# Kue-Web

Web Component of [Kue](https://github.com/YingjieQiao/kue)


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

# serve back-end at localhost:5000
FLASK_APP=run.py flask run
```


