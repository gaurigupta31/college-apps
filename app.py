from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/notion-auth')
def notion_auth():
   return 'Hello Notion'

@app.route('/privacy-policy')
def privacy_policy():
   return 'Hello Privacy'

@app.route('/terms-of-use')
def terms_of_use():
   return 'Hello Terms'

if __name__ == '__main__':
   app.run()
