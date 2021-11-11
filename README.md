# Kue-Web

Web Component of [Kue](https://github.com/YingjieQiao/kue).

Built with Vue for frontend and Flask for backend, hosted on an AWS EC2 server instance.

![landingpage](https://user-images.githubusercontent.com/49013092/101913724-53e23e00-3bfe-11eb-9fec-5c641bc536e5.png)


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
pip install -r requirements.txt

# serve back-end at localhost:5000
FLASK_APP=run.py flask run
```

