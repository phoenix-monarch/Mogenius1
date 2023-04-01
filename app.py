import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'GreyMatters_Bot'

#Ex https://Greymattersbot:ghp_147bkkabcdefgh@github.com/Greymattersbot/Mogenius
os.system("git clone https://phoenix-monarch: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@github.com/phoenix-monarch/AUTO-FILTER-XYZ okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
