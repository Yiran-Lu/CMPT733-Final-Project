"""
A simple Reddit crawler. 

Usage:
  reddit_crawler.py crawl <subreddit> [-o FILENAME]
  reddit_crawler.py (-h | --help)

Options:
  -h --help     Show this screen.
  -o FILENAME   Specify output file. Default will be the subreddit name.
  -l LIMIT      The total limit of posts to scrape. Default: 100
  -s SORT       Sorting method. Valid options: new, top, hot, rising. Default: new
"""
from docopt import docopt
import redditwarp.SYNC
import pandas as pd

client = redditwarp.SYNC.Client()

def escape_special_chars(s):
    return s.replace("\\", "\\\\").replace("\n", "\\n").replace("\t", "\\t").replace("\r", "\\r")

if __name__ == '__main__':
    args = docopt(__doc__)
    #print(args)

    subreddit = args['<subreddit>']
    limit = args['-l'] if args['-l'] else 100
    output_filename = args['-o'] if args['-o'] else subreddit + '.csv'

    output = pd.DataFrame()

    for post in client.p.subreddit.pull.new(subreddit, amount=limit):
        post_dict = {
            'permalink': post.permalink, 
            'subreddit': post.subreddit.name,
            'author': post.author.name,
            'score': post.score,
            'upvote_ratio': post.upvote_ratio,
            'title': post.title,
            'content': escape_special_chars(post.d['selftext'].strip())
        }
        df_dictionary = pd.DataFrame(post_dict, index=[0])
        output = pd.concat([output, df_dictionary], ignore_index=True)
    
    output.to_csv(output_filename)
    
