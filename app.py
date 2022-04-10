import os
from flask import Flask, session, redirect, request, render_template
from h11 import CLIENT
from requests_oauthlib import OAuth2Session
from selenium import webdriver
from urllib.parse import urlparse
from urllib.parse import parse_qs
app = Flask(__name__)

CLIENT_ID = os.getenv('NOTION_CLENT_ID')
CLIENT_SECRET =  os.getenv('NOTION_API_KEY')
BASE_NOTION_API_URL = "https://api.notion.com"
NOTION_AUTHORIZE_URL = "https://api.notion.com/v1/oauth/authorize"
REDIRECT_URI = "https://chief-fortune-judo.glitch.me/notion-auth"
TOKEN_URL = "https://api.notion.com/v1/oauth/token"


@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/notion-auth')
def notion_auth():
   driver = webdriver.Chrome()
   return driver.current_url


@app.route('/privacy-policy')
def privacy_policy():
   return 'Hello Privacy'

@app.route('/terms-of-use')
def terms_of_use():
   return 'Hello Terms'

if __name__ == '__main__':
   app.run()