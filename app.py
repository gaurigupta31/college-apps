import os
from flask import Flask, session, redirect, request, render_template
from h11 import CLIENT
from requests_oauthlib import OAuth2Session
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
   notion = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)
   token = notion.fetch_token(
        TOKEN_URL,
        client_secret = CLIENT_SECRET,
        authorization_response = request.url,
   )
   session['user_token'] = token
   return 'Thanks for granting us authorization.'

@app.route('/privacy-policy')
def privacy_policy():
   return 'Hello Privacy'

@app.route('/terms-of-use')
def terms_of_use():
   return 'Hello Terms'

if __name__ == '__main__':
   app.run()
