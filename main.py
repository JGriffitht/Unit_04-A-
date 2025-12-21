from flask import Flask,render_template,request,redirect,url_for, flash,abort
from flask_login import LoginManager, login_user, login_required, UserMixin, logout_user, current_user


import pymysql


from dynaconf import Dynaconf


app = Flask(__name__)
