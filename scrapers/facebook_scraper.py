import urllib2

def getFacebookData(page, devKey):
    url = "https://graph.facebook.com/v2.6/" + page +"/posts/?fields=message,link,permalink_url,created_time,type,name,id,comments.limit(0).summary(true),shares,likes.limit(0).summary(true),reactions.limit(0).summary(true)&limit=100&access_token=" + devKey
    source = urllib2.urlopen(url).read()
    print source
    return {"fbstats" : "stats"}