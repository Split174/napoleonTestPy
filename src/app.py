from sanic import Sanic
from sanic.response import json
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from blueprints.user import bp as bp_user
from blueprints.offer import bp as bp_offer



app = Sanic(__name__)
app.blueprint((bp_user,
               bp_offer))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, workers=os.cpu_count())


