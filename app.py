def twitter_app():

    from twitter_keys import Access_Token, Access_Token_Secret, Consumer_Key, Consumer_API_Secret, api_key
    import tweepy
    import json
    import requests as r

    auth = tweepy.OAuthHandler(Consumer_Key, Consumer_API_Secret)
    auth.set_access_token(Access_Token, Access_Token_Secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    public_tweets = api.search('@grantaguinaldo', count = 1, result_type = 'recent')

    tweet_text = public_tweets['statuses'][0]['text']
    tweet_id = public_tweets['statuses'][0]['id']
    tweet_screen_name = public_tweets['statuses'][0]['user']['screen_name']
    tweet_hash_tag = public_tweets['statuses'][0]['entities']['hashtags'][0]['text']

    units = 'units=imperial'
    url = 'http://api.openweathermap.org/data/2.5/weather?q='
    city = tweet_hash_tag
    country = 'us'
    query_url = url + city + ',' + country + '&' + units + api_key

    response = r.get(query_url).json()
    current_temp = response['main']['temp']
    description = response['weather'][0]['description']

    reply_text = 'Thanks for the tweet' + ' @' + tweet_screen_name + ' the weather in ' + tweet_hash_tag + ' is ' + str(current_temp) + 'F' + ' and ' + description

    return api.update_status(reply_text, in_reply_to_status_id = tweet_id)

while(True):
    import time
    twitter_app()
