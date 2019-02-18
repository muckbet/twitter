import urllib.request
import urllib.parse
import urllib.error

from documents import oauth
from documents import hidden

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py


def augment(url, parameters):
    secrets = hidden.oauth()
    consumer = oauth.OAuthConsumer(secrets['consumer_key'],
                                   secrets['consumer_secret'])
    token = oauth.OAuthToken(secrets['token_key'], secrets['token_secret'])

    oauth_request = oauth.OAuthRequest.from_consumer_and_token(
        consumer,
        token=token,
        http_method='GET',
        http_url=url,
        parameters=parameters)
    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(),
                               consumer, token)
    return oauth_request.to_url()