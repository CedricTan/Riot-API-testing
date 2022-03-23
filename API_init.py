# Ideation document and initial trials
# Needed for API keys safe-storage, placed in .gitignore
import keys
import cassiopeia as cass

cass.set_riot_api_key(keys.Riot_API_key)

summoner = cass.get_summoner(name="PewPrew", region="EUW")
print("{name} is a level {level} summoner on the {region} server.".format(name=summoner.name,
                                                                          level=summoner.level,
                                                                          region=summoner.region)) # Test code

match_history = cass.get_summoner(name="PewPrew", region="EUW").match_history