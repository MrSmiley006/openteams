import libteams

tokens = libteams.login()
teams_list = libteams.get_teams(tokens["access_token"])
print("Moje týmy: ")
for i in teams_list:
    print(i["displayName"])
