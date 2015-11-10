import os
import oauth2
import json
import urllib
import urllib2

# gather oauth2 information
KEY = os.getenv('YELP_KEY')
KEY_SECRET = os.getenv('YELP_KEY_SECRET')
TOKEN = os.getenv('YELP_TOKEN')
TOKEN_SECRET = os.getenv('YELP_TOKEN_SECRET')

url = 'https://api.yelp.com/v2'


def _get_oauth(url, key, key_secret, token, token_secret):
    app = oauth2.Consumer(key, key_secret)
    
    oa_req = oauth2.Request(method='GET', url=url)
    oa_req.update({'oauth_nonce': oauth2.generate_nonce(), 
                   'oauth_timestamp': oauth2.generate_timestamp(), 
                   'oauth_token': token, 'oauth_consumer_key': key})
    
    oa_token = oauth2.Token(token, token_secret)
    
    oa_req.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), 
                        app, oa_token)
    signed_url = oa_req.to_url()
    
    response = json.loads(urllib2.urlopen(signed_url, None).read())

    return response


def api_request(url, search_type, term, location, limit=20, offset=0):
    url = '{}/{}?term={}&location={}&limit={}&offset={}'.format(url, 
        search_type, term, location, limit, offset)
    return _get_oauth(url, KEY, KEY_SECRET, TOKEN, TOKEN_SECRET)
