from typing import Union

from fastapi import FastAPI
from nba_api.stats.endpoints import playerfantasyprofile

from player_stats_categories import categories

app = FastAPI()


@app.get("/players/{player_id}")
async def get_player_stats(player_id: int):
    try:
        player_stats = playerfantasyprofile.PlayerFantasyProfile(player_id)
        player_stats_dict = player_stats.get_dict()

        result_set = player_stats_dict["resultSets"][0]
        headers = result_set["headers"]
        rows = result_set["rowSet"]

        if not rows:
            return {"error": "No data available for this player"}

        row = rows[0]

        result_dict = {}
        for category in categories:
            if category in headers:
                index = headers.index(category)
                result_dict[category] = row[index]

        return {"player_id": player_id, "stats": result_dict}

    except Exception as e:
        return {"error": str(e)}
