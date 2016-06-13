import twitter
import json

with open('apiPass.json') as data_file:
    apiData = json.load(data_file)

api = twitter.Api(consumer_key = apiData['passes']['consumer_key'].encode('ascii', 'ignore'),
                  consumer_secret = apiData['passes']['consumer_secret'].encode('ascii', 'ignore'),
                  access_token_key = apiData['passes']['access_token_key'].encode('ascii', 'ignore'),
                  access_token_secret = apiData['passes']['access_token_secret'].encode('ascii', 'ignore'))

with open('/usr/local/bin/pythonpic/curr.txt', 'r') as myfile:
    data = myfile.read().replace('\n', '')

newdata = int(data) + 1
if(newdata >= 24):
    newdata = 0

with open('/usr/local/bin/pythonpic/curr.txt', 'w') as myfile:
    myfile.write('{}'.format(newdata))


api.UpdateImage('/usr/local/bin/pythonpic/pics/' + data + '.jpg')
