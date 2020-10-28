import os

class Config():
    TEMPLATE_FOLDER = os.getcwd() + "/dist"
    STATIC_FOLDER = os.getcwd() + "/dist/static/"
    # AWS_ACCESS_KEY = os.environ.get("AWS_EDUCATE_ACCESS_KEY")
    # AWS_SECRET_KEY = os.environ.get("AWS_EDUCATE_SECRET_KEY")
    FIREBASE_CRED_PY = os.environ.get("FIREBASE_CRED_PY")