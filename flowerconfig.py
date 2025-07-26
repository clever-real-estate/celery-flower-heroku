import os

auth_provider="flower.views.auth.GoogleAuth2LoginHandler"
auth="allowed-emails.*@movewithclever.com"
oauth2_key=os.getenv('GOOGLE_CLIENT_ID')
oauth2_secret=os.getenv('GOOGLE_CLIENT_SECRET')
oauth2_redirect_uri=os.getenv('GOOGLE_REDIRECT_URL')
