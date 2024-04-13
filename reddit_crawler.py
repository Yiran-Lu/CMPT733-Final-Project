"""
A simple Reddit crawler. 

Usage:
  reddit_crawler.py crawl <subreddit> [-o FILENAME | -l LIMIT | -i INTERVAL | -d DELAY]
  reddit_crawler.py (-h | --help)

Options:
  -h --help     Show this screen.
  -o FILENAME   Specify output file. Default will be the subreddit name.
  -l LIMIT      The total limit of posts to scrape. Default: 100
  -i INTERVAL   Interval between saving to file. Default is saving for every 100 posts.
  -d DELAY      Delay between scraping. Default is 600ms 
"""
from docopt import docopt
import redditwarp.SYNC
import pandas as pd
import numpy as np
from time import sleep

client = redditwarp.SYNC.Client()

def escape_special_chars(s):
    return s.replace("\\", "\\\\").replace("\n", "\\n").replace("\t", "\\t").replace("\r", "\\r")

if __name__ == '__main__':
    args = docopt(__doc__)

    subreddit = args['<subreddit>']
    limit = int(args['-l']) if args['-l'] else 100
    output_filename = args['-o'] if args['-o'] else subreddit + '.csv'
    save_interval = int(args['-i']) if args['-i'] else 100
    delay = int(args['-d']) if args['-d'] else 600

    output = pd.DataFrame()

    posts_scraped = 0
    current_posts_scraped = 0

    for post in client.p.subreddit.pull.new(subreddit, amount=limit):
        post_dict = {
            'permalink': post.permalink if post.permalink else None, 
            'subreddit': post.subreddit.name if post.subreddit else None,
            'time': post.created_at if post else None,
            'author': post.author.name if post.author else None,
            'score': post.score if post else None,
            'upvote_ratio': post.upvote_ratio if post else None,
            'title': post.title if post else None,
            'selftext': escape_special_chars(post.d['selftext'].strip()) if post.d['selftext'] else None
        }
        df_dictionary = pd.DataFrame(post_dict, index=[0])
        output = pd.concat([output, df_dictionary], ignore_index=True)

        posts_scraped += 1
        current_posts_scraped += 1
        
        if current_posts_scraped >= save_interval:
            output.to_csv(output_filename)
            current_posts_scraped = 0

            print("Saving.. Total Scraped: "  + str(posts_scraped))
            sleep(delay / 1000)
        
    output['created'] = output.time.values.astype(np.int64) / 1000000
    output.to_csv(output_filename)
    print("Done!")
