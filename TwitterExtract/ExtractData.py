import datetime
from email.utils import mktime_tz, parsedate_tz
from TwitterSearch import *


def format_date(value):
    time_tuple = parsedate_tz(value)
    timestamp = mktime_tz(time_tuple)
    return str(datetime.datetime.fromtimestamp(timestamp))


TwitterConnect = TwitterSearch(
    consumer_key='q24QyO9K264d3hbHSbfzSGoaq',
    consumer_secret='o8QT6TvTV7XjD6WY2QGVI44izit5CjpJNKr6kI3GjcmlOdiWvD',
    access_token='52308602-tLE9aO2hSTFdlK5aIn0Wb7TRcijpSDLw9e7Wcxuob',
    access_token_secret='g1wqoMUvBFhhhR36DG9k4NID2O66LTLAD3It4rchq5wQV',
 )


Search = TwitterSearchOrder()
Search.set_keywords(['bolsonaro'])
Search.set_language('pt')
# Search.set_negative_attitude_filter()
# Search.set_positive_attitude_filter()

for tweet in TwitterConnect.search_tweets_iterable(Search):
    if tweet['truncated'] == 0:
        print((format_date(tweet['created_at']) + ' @' + tweet['user']['screen_name'] + ' tweeted: ' + tweet['text']))
        # print(tweet)

