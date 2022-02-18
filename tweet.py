import tweepy
import config
auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth, 
                 wait_on_rate_limit=True)
status = "Check de seguir funcionando"
api.update_status(status)