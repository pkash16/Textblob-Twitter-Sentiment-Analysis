from textblob import TextBlob 
import tweetpony
import json
import jsonpickle


text = raw_input("Give me text to analyze sentiment\n")

wiki = TextBlob(text);

print(wiki.sentiment)



api = tweetpony.API(consumer_key = "5XTZQYKqXirfeKprCQIlLGv0K", consumer_secret = "sgInLsaDTKYmsrNsiBfW7VqDXOv56bHssndhtWrwdx2U9nlOes", access_token = "1737850004-sl6kr0L2yrUDFmqgJvzSlJmfYBtjK4XCcYLDAqY", access_token_secret = "ETZN5I6B7n9Y2Svy6qV0ZkAkboN48AyqPFFmVBrfKu3YZ")
user = api.user

input_query = raw_input("Type in an a query\n")

json_data = api.search_tweets(q=input_query, lang='en', count=1)
data = json.loads(jsonpickle.encode(json_data))

print(data)

'''

print "Hello, @%s!" % user.screen_name
text = raw_input("What would you like to tweet? ")
try:
    api.update_status(status = text)
except tweetpony.APIError as err:
    print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
else:
    print "Yay! Your tweet has been sent!"
'''