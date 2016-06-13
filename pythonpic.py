import twitter
api = twitter.Api(consumer_key='ScfUowDWDMsjpFwOnL7244ui7',
                  consumer_secret='tlXMzT9CyBwng9tVtNWfDRDiny092kCByf7KoIU6VnSw1z6WFD',
                  access_token_key='16139414-VVhO9d8zcLdcyNS3sMHx16u2yg2jVVOE3G4icauIy',
                  access_token_secret='FsVIW6BQMRb3qXvGYFgyAWBTlMsClUagzNRo2WeBK1Ahq')

with open('/usr/local/bin/pythonpic/curr.txt', 'r') as myfile:
    data = myfile.read().replace('\n', '')

newdata = int(data) + 1
if(newdata >= 24):
    newdata = 0

with open('/usr/local/bin/pythonpic/curr.txt', 'w') as myfile:
    myfile.write('{}'.format(newdata))


api.UpdateImage('/usr/local/bin/pythonpic/pics/' + data + '.jpg')
