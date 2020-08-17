import json


def response_decorator(team, points, matches_played):
    response = f"pos | team | pts | matches played\n" \
               f"1.{team[0]} {points[0]} {matches_played[0]} \n" \
               f"2.{team[1]} {points[1]} {matches_played[1]}\n" \
               f"3.{team[2]} {points[2]} {matches_played[2]}\n" \
               f"4.{team[3]} {points[3]} {matches_played[3]}\n" \
               f"5.{team[4]} {points[4]} {matches_played[4]}\n" \
               f"6.{team[5]} {points[5]} {matches_played[5]}\n" \
               f"7.{team[6]} {points[6]} {matches_played[6]}\n" \
               f"8.{team[7]} {points[7]} {matches_played[7]}\n" \
               f"9.{team[8]} {points[8]} {matches_played[8]}\n" \
               f"10.{team[9]} {points[9]} {matches_played[9]}\n" \
               f"11.{team[10]} {points[10]} {matches_played[10]}\n" \
               f"12.{team[11]} {points[11]} {matches_played[11]}\n" \
               f"13.{team[12]} {points[12]} {matches_played[12]}\n" \
               f"14.{team[13]} {points[13]} {matches_played[13]}\n" \
               f"15.{team[14]} {points[14]} {matches_played[14]}\n" \
               f"16.{team[15]} {points[15]} {matches_played[15]}\n" \
               f"17.{team[16]} {points[16]} {matches_played[16]}\n" \
               f"18.{team[17]} {points[17]} {matches_played[17]}\n" \
               f"19.{team[18]} {points[18]} {matches_played[18]}\n" \
               f"20.{team[19]} {points[19]} {matches_played[19]}"

    return response


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

    response = json.dumps(raw_response, ensure_ascii=False).encode('utf-8')

    return response.decode()
