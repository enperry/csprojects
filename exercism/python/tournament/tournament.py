def tally(rows):
    matches = [match.split(";") for match in rows]

    teams_in_matches = [team for sublist in [teams[0:2] for teams in matches] for team in sublist]
    teams = list(set(teams_in_matches))

    winners = [match[0] for match in matches if match[2] == "win"] + [match[1] for match in matches if match[2] == "loss"]
    losers = [match[0] for match in matches if match[2] == "loss"] + [match[1] for match in matches if match[2] == "win"]
    draws = [team for sublist in [match[0:2] for match in matches if match[2] == "draw"] for team in sublist]
    points_for_win = 3
    points_for_draw = 1

    result_table = [[team, teams_in_matches.count(team), winners.count(team), draws.count(team), losers.count(team), winners.count(team) * points_for_win + draws.count(team) * points_for_draw] for team in teams]
    sorted_table = ["Team MP W D L P".split()] + sorted(sorted(result_table), key=lambda team: team[-1], reverse=True)
    tallied_table = [f"{str(team[0]):31s}| {str(team[1]):>2s} | {str(team[2]):>2s} | {str(team[3]):>2s} | {str(team[4]):>2s} | {str(team[5]):>2s}" for team in sorted_table]

    return tallied_table
