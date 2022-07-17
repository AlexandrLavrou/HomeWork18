from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self, year, gid, did):
        if year:
            return self.dao.get_by_year(year)
        if gid:
            return self.dao.get_by_genre(gid)
        if did:
            return self.dao.get_by_director(did)
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data.get("id")

        movie = self.get_one(mid)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.rating = data.get("rating")
        movie.year = data.get("year")
        movie.trailer = data.get("trailer")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        self.dao.update(movie)

    def update_partial(self, data):
        mid = data.get("id")

        movie = self.get_one(mid)

        if 'title' in data:
            movie.title = data.get("title")
        if 'description' in data:
            movie.description = data.get("description")
        if 'rating' in data:
            movie.rating = data.get("rating")
        if 'year' in data:
            movie.year = data.get("year")
        if 'trailer' in data:
            movie.trailer = data.get("trailer")
        if 'genre_id' in data:
            movie.genre_id = data.get("genre_id")
        if 'director_id' in data:
            movie.director_id = data.get("director_id")
        self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)
