from sanic import Sanic
from sanic.response import json
import os
from config import Config
from blueprints.user import bp as bp_user
from blueprints.offer import bp as bp_offer
from blueprints.auth import bp as bp_auth


app = Sanic("test")
app.blueprint((bp_user,
               bp_offer,
               bp_auth))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, workers=os.cpu_count())


