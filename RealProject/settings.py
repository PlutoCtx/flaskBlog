from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

SECRET_KEY = '1%3ya7fn3moipdpcltj(tdfcv5^@lj=t5d&72levvls+y*@4^'

SQLALCHEMY_DATABASE_URI = 'mysql://root:Yuhuangtao111@127.0.0.1:3306/flaskdb'

SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
