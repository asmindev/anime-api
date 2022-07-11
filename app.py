import os
from flask import Flask
from flask_restful import Api, Resource
from src import views, errors

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
api = Api(app, errors=errors.errors)
settings = app.config.get("RESTFUL_JSON", {})
settings.setdefault("indent", 2)
settings.setdefault("sort_keys", True)
app.config["RESTFUL_JSON"] = settings


class HelloWorld(Resource):
    def get(self):
        host = os.getenv("OTAKUDESU")
        owner = "https://github.com/asmindev"
        maintenance = "asmindev"
        message = "API from {} build with love by {}".format(host, maintenance)
        return {"message": message, "owner": owner, "maintenance": maintenance}


api.add_resource(HelloWorld, "/")
api.add_resource(views.Home, "/home")
api.add_resource(views.Search, "/search")
api.add_resource(views.Detail, "/detail")
api.add_resource(views.Ongoing, "/ongoing")
api.add_resource(views.AnimeList, "/animelist")
api.add_resource(views.MovieList, "/movielist")
api.add_resource(views.GetVideo, "/getvideo")
if __name__ == "__main__":

    # app.run(debug=True, load_dotenv=True)
    # bind port heroku
    app.run(
        host="0.0.0.0",
        load_dotenv=True,
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )
