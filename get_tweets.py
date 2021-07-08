## Extração de dados do twitter
import json
from tweepy import OAuthHandler , Stream , StreamListener

# Cadastra as chaves de acesso de acesso
consumer_key = ***
consumer_secret = ***

access_token = ***
access_token_secret = ***
# Arquivo de saída para armazenar tweets coletados
out = open('tweets_coletados.txt' , 'w')

# Implementa classe para conexão com Twitter

class MyStreamListener(StreamListener):

  def on_data(self, data):
    iString = json.dumps(data)
    out.write(iString + "\n")
    return True

  def on_error(self,status):
    print(status)

# Implementa MAIN function
if __name__ == '__main__':
  m = MyStreamListener()
  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  stream = Stream(auth, m)
  stream.filter(track = ["cpi da covid"])
