
#FILE_NAME = 'A-sample'
#FILE_NAME = 'A-small-attempt0'
FILE_NAME = 'A-large'
#FILE_NAME = 'A-practice'

def do_case():
    num_teams = get_int()
    teams = [[int(item) if item.isdigit() else -1 for item in list(get_line())] for i in xrange(num_teams)]
    games_played = []
    wins = []
    WPs = []
    OWPs = []
    OOWPs = []
    RPIs = []
    for team in teams:
        games_played.append(sum(1 for game in team if game != -1))
        wins.append(sum(game for game in team if game != -1))
        WPs.append(1. * wins[-1] / games_played[-1])# if games_played[-1] != 0 else 0)

    for ti in xrange(num_teams):
        temp_WPs = []
        for ti2, team2 in enumerate(teams):
            if ti == ti2 or team2[ti] == -1: continue
            temp_WPs.append(1. * (wins[ti2]-team2[ti]) / (games_played[ti2]-1))#) if games_played != 0 else 0)
        OWPs.append(1. * sum(WP for i, WP in enumerate(temp_WPs)) / len(temp_WPs))
            
    for ti in xrange(num_teams):
        OOWPs.append(1. * sum(OWP for i, OWP in enumerate(OWPs) if teams[ti][i] != -1 and i != ti) / games_played[ti])
    
    for ti in xrange(num_teams):
        RPIs.append(.25*WPs[ti] + .5*OWPs[ti] + .25*OOWPs[ti])

    return RPIs
    

with open('{0}.in'.format(FILE_NAME), 'r') as inpt:
    with open('{0}.out'.format(FILE_NAME), 'w') as out:
        get_line = lambda: inpt.readline()[:-1]
        get_int = lambda: int(get_line())
        get_split = lambda: get_line().split()
        T = get_int()
        for t in xrange(1, T+1):
            result = do_case()
            #out.write('Case #{0}: {1}\n'.format(t, result))
            out.write('Case #{0}:\n'.format(t))
            for r in result:
                out.write('{0}\n'.format(r))

print 'done.'
