def except_block():

    from twitter_keys import Access_Token, Access_Token_Secret, Consumer_Key, Consumer_API_Secret, api_key
    import tweepy
    import json
    import requests as r

    auth = tweepy.OAuthHandler(Consumer_Key, Consumer_API_Secret)
    auth.set_access_token(Access_Token, Access_Token_Secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    public_tweets = api.search('@enveraai', count = 1, result_type = 'recent')

    tweet_id = public_tweets['statuses'][0]['id']
    tweet_screen_name = public_tweets['statuses'][0]['user']['screen_name']

    reply_text = 'Sorry' + '@' + tweet_screen_name + 'I can\'t find that city.  Please try again.' + 'ID: ' + str(tweet_id)

    response_tweet = api.update_status(reply_text, in_reply_to_status_id = tweet_id)

    return response_tweet
