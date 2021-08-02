from basketball_reference_scraper.players import get_stats
import json


def getPlayerStats(player1, player2):
    player1stats = get_stats(
        player1, stat_type='PER_GAME', playoffs=False, career=False, ask_matches=False)

    player2stats = get_stats(
        player2, stat_type='PER_GAME', playoffs=False, career=False, ask_matches=False)

    return[player1stats.to_json(orient='records'), player2stats.to_json(orient='records')]


print(getPlayerStats('Stephen Curry', 'Kobe Bryant'))
