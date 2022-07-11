from flask_restful import Resource, reqparse
from .errors import FieldIsRequired
from . import utils


parser = reqparse.RequestParser()


class Home(Resource):
    def get(self):
        return utils.Home().get()


class Search(Resource):
    def get(self):
        # get the query from the params
        cari = utils.Search()
        parser.add_argument(
            "query",
            type=str,
            required=True,
            help="query is required",
            location="args",
        )
        data = parser.parse_args()
        data = data["query"]
        return cari.get(data)


class Detail(Resource):
    def get(self):
        parser.add_argument(
            "slug",
            type=str,
            # required=True,
            help="slug is required",
            location="args",
        )
        data = parser.parse_args()
        slug = data["slug"]
        if slug is None:
            return {"message": "slug is required"}
        detail = utils.Details().get(slug)
        return detail


class Ongoing(Resource):
    def get(self):
        parser.add_argument(
            "page",
            type=str,
            # required=True,
            location="args",
        )
        data = parser.parse_args()
        page = data["page"]

        return utils.OnGoing().get(page=page)


class AnimeList(Resource):
    def get(self):
        parser.add_argument(
            "page",
            type=str,
            # required=True,
            location="args",
        )
        data = parser.parse_args()
        page = data["page"]

        return utils.AnimeList().get(page=page)


class MovieList(Resource):
    def get(self):
        parser.add_argument(
            "page",
            type=str,
            # required=True,
            location="args",
        )
        data = parser.parse_args()
        page = data["page"]

        return utils.MovieList().get(page=page)


class GetVideo(Resource):
    def get(self):
        parser.add_argument(
            "slug",
            type=str,
            # required=True,
            location="args",
        )
        parser.add_argument(
            "id",
            type=str,
            # required=True,
            location="args",
        )
        data = parser.parse_args()
        slug = data["slug"]
        id = data["id"]
        if slug is None:
            return {"message": "slug is required"}
        if id is None:
            return {"message": "id is required"}
        detail = utils.GetVideo().get(anime_slug=slug, id=id)
        return detail
