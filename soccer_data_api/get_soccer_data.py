from bs4 import BeautifulSoup
import requests
from .config import CONF
from time import sleep


class GetData:
    def __init__(self, league):
        page = requests.get(CONF['url']+league)
        self.soup = BeautifulSoup(page.content, features="html.parser")
        self.league = ""
        self.array = []
        self.clubs = []
        self.points = []
        self.games = []
        self.wins = []
        self.draws = []
        self.losses = []
        self.goals_for = []
        self.goals_against = []
        self.goal_diff = []
        self.top_scorer = []
        self.league = league

    def get_club_name(self):
        raw_response = self.soup.find_all('td', {'class': 'left'})
        for pos in raw_response:
            self.array.append(pos.get_text()[1:])
        self.clubs += self.array
        if self.league == "comps/20/Bundesliga-Stats":

            return self.clubs[-18:]

        return self.clubs[-20:]

    def get_points(self):
        sleep(.25)
        raw_response = self.soup.find_all('td', {'data-stat': 'points'})
        for points in raw_response:
            self.array.append(points.get_text())
        self.points += self.array
        if self.league == "comps/20/Bundesliga-Stats":
            return self.points[-18:]

        return self.points[-20:]

    def get_matches_played(self):
        sleep(.5)
        raw_response = self.soup.find_all('td', {'data-stat': 'games'})
        for games in raw_response:
            self.array.append(games.get_text())
        self.games += self.array
        if self.league == "comps/20/Bundesliga-Stats":
            return self.games[-18:]

        return self.games[-20:]

    def get_wins(self):
        sleep(.75)
        raw_response = self.soup.find_all('td', {'data-stat': 'wins'})
        for wins in raw_response:
            self.array.append(wins.get_text())
        self.wins += self.array
        if self.league == "comps/20/Bundesliga-Stats":
            return self.wins[-18:]

        return self.wins[-20:]

    def get_draws(self):
        sleep(1)
        raw_response = self.soup.find_all('td', {'data-stat': 'draws'})
        for draws in raw_response:
            self.array.append(draws.get_text())
        self.draws += self.array
        if self.league == "comps/20/Bundesliga-Stats":
            return self.draws[-18:]

        return self.draws[-20:]

    def get_losses(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'losses'})
        for losses in raw_response:
            self.array.append(losses.get_text())
        self.losses += self.array
        if self.league == "comps/20/Bundesliga-Stats":
            return self.losses[-18:]

        return self.losses[-20:]

    def get_goals_for(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'goals_for'})
        for gf in raw_response:
            self.array.append(gf.get_text())
        self.goals_for += self.array
        if self.league == "comps/20/Bundesliga-Stats":
            return self.goals_for[-18:]

        return self.goals_for[-20:]

    def get_goals_against(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'goals_against'})
        for ga in raw_response:
            self.array.append(ga.get_text())
        self.goals_against += self.array
        if self.league == "comps/20/Bundesliga-Stats":
            return self.goals_against[-18:]

        return self.goals_against[-20:]

    def get_goal_diff(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'goal_diff'})
        for gd in raw_response:
            self.array.append(gd.get_text())
        self.goal_diff += self.array
        if self.league == "comps/20/Bundesliga-Stats":
            return self.goal_diff[-18:]

        return self.goal_diff[-20:]

    def get_top_scorer(self):
        raw_response = self.soup.find_all('td', {'data-stat': 'top_team_scorers'})
        for top_scorer in raw_response:
            self.array.append(top_scorer.get_text())
        self.top_scorer += self.array
        if self.league == "comps/20/Bundesliga-Stats":
            return self.top_scorer[-18:]

        return self.top_scorer[-20:]
