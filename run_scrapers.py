import scrapers

stats = scrapers.getInstagramData("deathbydust")
print stats

devKey = ""
with open('key.txt') as f:
    devKey = f.readline()
    #"Honey-Cloud-Media"
fbstats = scrapers.getFacebookData("211243276281736", devKey)
print fbstats