import json


def json_response(team, pos, points, matches_played, wins, draws, losses, goals_for, goals_against, goal_diff, top_scorer):
    raw_response = []
    for i in range(0, len(team)):
        raw_response.append({
            "team": team[i],
            "pos": pos[i],
            "points": points[i],
            "matches_played": matches_played[i],
            "wins": wins[i],
            "draws": draws[i],
            "losses": losses[i],
            "goals_for": goals_for[i],
            "goals_against": goals_against[i],
            "goal_diff": goal_diff[i],
            "top_scorer": top_scorer[i]
        })

    json_str = json.dumps(raw_response, ensure_ascii=False).encode('utf-8')
    json_list = json.loads(json_str.decode())

    return json_list
