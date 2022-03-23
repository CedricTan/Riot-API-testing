# Ideation document and initial trials

import keys # Needed for API keys safe-storage, placed in .gitignore

import cassiopeia as cass

cass.set_riot_api_key(keys.Riot_API_key)
cass.set_default_region("EUW")

from cass import Summoner

pewprew = Summoner(name="PewPrew", region="EUW")
pewprew.match_history


# Test code
