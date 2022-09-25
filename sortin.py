import constants
import copy


def clean_data(itera):
    newnie = []
    for i in itera.copy():
        if i['experience'] == 'YES':
            i['experience'] = True
        if i['experience'] == 'NO':
            i['experience'] = False

        i['height'] = i['height'].split()
        i['height'] = int(i['height'][0])
        i['guardians'] = i['guardians'].split(' and ')
        newnie.append(i)
    return newnie

def teamclean(itera):
    teamdick = {}
    for i in itera:
        n = {i : []}
        teamdick.update(n)
    return teamdick



def balance_teams(itera, itera2):
    exp_players = []
    newbs =[]
    teams = teamclean(itera2)
    for i in itera:
        if i['experience'] == True:
            exp_players.append(i)
        else:
            newbs.append(i)
    while exp_players:
        for key, value in teams.items():
            value.append(exp_players[0])
            exp_players.remove(exp_players[0])

    while newbs:
        for key, value in teams.items():
            value.append(newbs[0])
            newbs.remove(newbs[0])
    return teams

def guardlist(team):
    glist = []
    for i in team:
        for g in i['guardians']:
            glist.append(str(g))
    return ', '.join(glist)

def plist(team):
    plist = []
    for i in team:
        plist.append(str(i['name']))
    return ', '.join(plist)


def whipheight(team):
    height_pool = []
    for i in team:
        height_pool.append(i['height'])
    return str(round(sum(height_pool)/len(height_pool), 2)) + ' inches'

if __name__ == '__main__':
    data = copy.deepcopy(constants.PLAYERS)
    newnie = clean_data(data)
    teams = balance_teams(newnie, constants.TEAMS)
    print(teams)

    for i in teams:
        print(i)
