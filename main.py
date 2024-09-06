import GetOldTweets3 as got

tweetCriteria = got.manager.TweetCriteria().setQuerySearch('Philippine education')\
                                           .setSince("2023-01-01")\
                                           .setUntil("2023-12-31")\
                                           .setMaxTweets(100)

# Scrape the tweets
tweets = got.manager.TweetManager.getTweets(tweetCriteria)

# Print the tweets
for tweet in tweets:
    print(f"{tweet.date} - {tweet.username}: {tweet.text}\n")