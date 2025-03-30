import requests, requests_oauthlib as oauthlib
import webbrowser

from oauthlib.oauth2 import WebApplicationClient
from urllib.parse import urlparse, parse_qs

url = "https://graph.microsoft.com/v1.0/"

def login():
    oauth = oauthlib.OAuth2Session(client=WebApplicationClient(client_id="5fce29ed-a3ae-4ea1-9f36-0326c9f7988c"),
                                   redirect_uri="https://login.microsoftonline.com/common/oauth2/nativeclient",
                                   scope=["openid", "user.read", "offline_access", "Team.ReadBasic.All"])
    auth_url, state = oauth.authorization_url("https://login.microsoftonline.com/common/oauth2/v2.0/authorize")
    input("Přihlaš se ke svému účtu a poté sem vlož obsah adresního řádku.\nPro pokračování k přihlášení stiskni jakoukoli klávesu.")
    webbrowser.open(auth_url)
    redirect_url = urlparse(input())
    code = parse_qs(redirect_url.query)["code"][0]
    token_data = {
        'grant_type': 'authorization_code',
        'client_id': "5fce29ed-a3ae-4ea1-9f36-0326c9f7988c",
        'code': code,
        'redirect_uri': "https://login.microsoftonline.com/common/oauth2/nativeclient",
    }
    
    r = requests.post("https://login.microsoftonline.com/common/oauth2/v2.0/token", data=token_data)
    return r.json()

def get_teams(access_token):
    r = requests.get(url + "me/teamwork/associatedTeams", headers={"Authorization": "Bearer " + access_token})
    return r.json()["value"]
