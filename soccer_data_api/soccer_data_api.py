from .config import CONF
from .response_types import json_response
from .get_soccer_data import GetData


class SoccerDataAPI:
    def __init__(self):
        self.get_data = None

    def english_premier(self):
        self.get_data = GetData(CONF['leagues']['english_premier_league'])
        response = json_response(self.get_data.get_club_name(), self.get_data.get_points(),
                                 self.get_data.get_matches_played(), self.get_data.get_wins(),
                                 self.get_data.get_draws(), self.get_data.get_losses(),
                                 self.get_data.get_goals_for(), self.get_data.get_goals_against(),
                                 self.get_data.get_goal_diff(), self.get_data.get_top_scorer())

        return response

    def la_liga(self):
        self.get_data = GetData(CONF['leagues']['la_liga'])
        response = json_response(self.get_data.get_club_name(), self.get_data.get_points(),
                                 self.get_data.get_matches_played(), self.get_data.get_wins(),
                                 self.get_data.get_draws(), self.get_data.get_losses(),
                                 self.get_data.get_goals_for(), self.get_data.get_goals_against(),
                                 self.get_data.get_goal_diff(), self.get_data.get_top_scorer())

    def bundesliga(self):
        self.get_data = GetData(CONF['leagues']['bundesliga'])
        response = json_response(self.get_data.get_club_name(), self.get_data.get_points(),
                                 self.get_data.get_matches_played(), self.get_data.get_wins(),
                                 self.get_data.get_draws(), self.get_data.get_losses(),
                                 self.get_data.get_goals_for(), self.get_data.get_goals_against(),
                                 self.get_data.get_goal_diff(), self.get_data.get_top_scorer())

        return response

    def serie_a(self):
        self.get_data = GetData(CONF['leagues']['serie_a'])
        response = json_response(self.get_data.get_club_name(), self.get_data.get_points(),
                                 self.get_data.get_matches_played(), self.get_data.get_wins(),
                                 self.get_data.get_draws(), self.get_data.get_losses(),
                                 self.get_data.get_goals_for(), self.get_data.get_goals_against(),
                                 self.get_data.get_goal_diff(), self.get_data.get_top_scorer())
        return response

    def ligue_1(self):
        self.get_data = GetData(CONF['leagues']['ligue_1'])
        response = json_response(self.get_data.get_club_name(), self.get_data.get_points(),
                                 self.get_data.get_matches_played(), self.get_data.get_wins(),
                                 self.get_data.get_draws(), self.get_data.get_losses(),
                                 self.get_data.get_goals_for(), self.get_data.get_goals_against(),
                                 self.get_data.get_goal_diff(), self.get_data.get_top_scorer())

        return response
