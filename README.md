# soccer-data-api

An easy to use python web-scrap package that gets json soccer data/stats. All data belongs to https://www.sports-reference.com/

## Installation

python3 -m pip install soccer-data-api

### or

pip3 install soccer-data-api

### Usage

```
>>>from soccer_data_api import SoccerDataAPI

>>>soccer_data = SoccerDataAPI()

>>>soccer_data.english_premier()
>>>soccer_data.la_liga()
>>>soccer_data.ligue_1()
>>>soccer_data.bundesliga()
>>>soccer_data.serie_a()
>>>soccer_data.eredivisie()
```

Leagues available: English Premier League, Spanish La Liga, French Ligue 1, German Bundesliga, Italian Serie A
