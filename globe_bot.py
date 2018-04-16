import webbrowser

import googlemaps
import praw

# init praw

r = praw.Reddit(username='globe_bot',
                password='GLOBE_BOT_PASSWORD',
                client_id='CLIENT_ID',
                client_secret='CLIENT_SECRET',
                user_agent="<platform>:<app ID>:<version string> (by /u/<reddi"
                "t username>) globe comment responder v0.1")

# get dict from web-scraped ISO country codes
with open("output.txt", "r") as text_file:
    c = text_file.read()
    get_countries = eval(c)


# select where to scan for comments
# with open("comments.txt","w", encoding='utf-8') as comment_file:
# iterate over submissions
for submission in r.subreddit('test').new(limit=20):
    post = r.submission(id=submission)
    post.comment_sort = 'top'
    post.comments.replace_more(limit=0)
    # iterate over comments in submission
    for comment in post.comments.list():
        # turn comments into iterable
        # lower string for comparision later
        comment_string = comment.body.lower().split()
        # iterate through country list
        for word in comment_string:
            # if country name in country list matches...
            # a word in the comment continue
            if word in get_countries:
                # need to add island logic here
                # need to add special cases
                country_code = get_countries[word]
                print(country_code)
                # start Geocoding API
                gmaps = googlemaps.Client(key='AIzaSyBWeTlyImUJXWqtbou7pRw5BdS'
                                          'nSyvPy4A')
                # get geocode in variable
                geocode_result = gmaps.geocode(word)
                # store country ID
                country_id = geocode_result[0]['place_id']
                # store latitude
                latitude = str(
                        geocode_result[0]['geometry']['location']['lat'])
                # store longitude
                longitude = str(
                        geocode_result[0]['geometry']['location']['lng'])

                map_url = "https://www.google.com/maps/search/?api=1&query="
                +latitude+","+longitude+"&query_place_id="+country_id

                # comment.reply("[Here it is]("+map_url+")")

                webbrowser.open(map_url, new=2)
