from flask import Flask #create websites
from flask import render_template #process HTML
import requests #download stuff
import json #JASON!
import random

app = Flask(__name__)

def get_meme():
    subreddit_list = ["Catmemes", "Kitten", "CatsBeingCats", "cutecats", "funnycats"]
    current_subreddit_item = random.randint(0, len(subreddit_list))
    current_subreddit_string = subreddit_list[current_subreddit_item]
    url = "https://meme-api.herokuapp.com/gimme/" + current_subreddit_string
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit


@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("meme_index.html", meme_pic = meme_pic, subreddit = subreddit)

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port = 5050)
