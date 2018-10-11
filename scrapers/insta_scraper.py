import re
import urllib2
import json

accountName = "deathbydust";

def getInstagramData(username):
  r = re.compile('<script type="text\/javascript">' + 
                   '([^{]+?({.*profile_pic_url.*})[^}]+?)' +
                   '<\/script>')
  url = "https://www.instagram.com/" + username
  totalComments = 0
  totalLikes = 0
  source = urllib2.urlopen(url).read()
  jsonStr = r.search(source).group(2)
  data = json.loads(jsonStr)
  oldVariantOfData = data['entry_data']['ProfilePage'][0]
 
  for i in range (0, 12):
    totalComments += int(oldVariantOfData['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_media_to_comment']['count'])

  for i in range (0, 12):
    totalLikes += int(oldVariantOfData['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_liked_by']['count'])
    #print oldVariantOfData['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']
  return {
    'follower_count' : oldVariantOfData['graphql']['user']['edge_followed_by']['count'],
    'follow_count' : oldVariantOfData['graphql']['user']['edge_followed_by']['count'], 
    'media_count' : oldVariantOfData['graphql']['user']['edge_owner_to_timeline_media']['count'],
    'total_comments' : totalComments,
    'total_likes' : totalLikes,
    'engagement_ratio' : (((totalLikes+totalComments))/float(oldVariantOfData['graphql']['user']['edge_followed_by']['count']))/12
  }
