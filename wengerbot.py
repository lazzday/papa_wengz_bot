# papawengz_bot for /r/Gunners
# Responds with an Arsene Wenger qoute when prompted

import praw
import secret
import traceback
import random

reddit = praw.Reddit(client_id=secret.CLIENT_ID,
                     client_secret=secret.CLIENT_SECRET,
                     username=secret.USERNAME,
                     password=secret.PASSWORD,
                     user_agent='Created by /u/lazzday')

subreddit = reddit.subreddit('Gunners')

keyphrase = 'papa wengz'

for comment in subreddit.stream.comments():
    if keyphrase in comment.body.lower():
        with open("ids.txt", "r+") as sub_id:
            ids = sub_id.read().split()
            if comment.id not in ids:
                try:
                    quotes = open('quotes.txt').read().splitlines()
                    response = random.choice(quotes)
                    comment.reply(response)
                    print('post success:', comment.id, ":", comment.body)
                    sub_id.write(' ' + comment.id)
                except:
                    print('post failed:', comment.id, ":", comment.body)
                    traceback.print_exc()

            else:
                print("Comment", comment.id, "already responded to.")
            sub_id.close()