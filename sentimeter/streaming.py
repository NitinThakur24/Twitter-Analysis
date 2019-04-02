from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


consumer_key="KqiUO3abFVhv0iIMcBYV0BxUf"
consumer_secret="7shjEbPXs4l5mejXxZgGhaqm8XAFiWhsv1EnYplmT60hAll9yc"


access_token="1098485478909771777-2qWb39Gju80n080aDpnQunAm22MliI"
access_token_secret="m83ujY8fqxDW9hKa0MKwjJwLPCTgBxu3goc9U0JRekv5y"

class MyStreamListener(StreamListener):
    
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = MyStreamListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['IPL'])
    

    





    