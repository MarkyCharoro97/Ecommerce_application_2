import tweepy
from django.conf import settings

auth = tweepy.OAuth1UserHandler(
    settings.TWITTER_API_KEY,
    settings.TWITTER_API_SECRET_KEY,
    settings.TWITTER_ACCESS_TOKEN,
    settings.TWITTER_ACCESS_TOKEN_SECRET,
)

twitter_api = tweepy.API(auth)


def tweet_store(store):
    text = f"New Store Added!\n {store.name}\n{store.description}"
    if store.logo:
        twitter_api.update_with_media(store.logo.path, status=text)
    else:
        twitter_api.update_status(status=text)


def tweet_product(product):
    text = f"New Product in {product.store.name}!\n {product.name}\n{product.description}"
    if product.image:
        twitter_api.update_with_media(product.image.path, status=text)
    else:
        twitter_api.update_status(status=text)
