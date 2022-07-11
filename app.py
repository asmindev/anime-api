import os
from flask import Flask
from flask_restful import Api, Resource
from src import views, errors

app = Flask(__name__)
api = Api(app, errors=errors.errors)


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
    )
