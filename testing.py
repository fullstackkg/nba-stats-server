from nba_api.stats.endpoints import playerfantasyprofile

# Fetch player stats
player_stats = playerfantasyprofile.PlayerFantasyProfile(2544)
player_stats_dict = player_stats.get_dict()

# Extract headers and rows from the resultSets
result_set = player_stats_dict["resultSets"][0]
headers = result_set["headers"]
rows = result_set["rowSet"]

# Define the categories to extract
categories = [
    "GP",
    "W",
    "L",
    "W_PCT",
    "MIN",
    "FGM",
    "FGA",
    "FG_PCT",
    "FG3M",
    "FG3A",
    "FG3_PCT",
    "FTM",
    "FTA",
    "FT_PCT",
    "OREB",
    "DREB",
    "REB",
    "AST",
    "TOV",
    "STL",
    "BLK",
    "BLKA",
    "PF",
    "PFD",
    "PTS",
    "PLUS_MINUS",
]

# Create a dictionary
row = rows[0]
result_dict = {category: row[headers.index(category)] for category in categories}

print(result_dict)
