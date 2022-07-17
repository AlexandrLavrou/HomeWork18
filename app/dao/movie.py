from app.dao.model.director import Director
from app.dao.model.genre import Genre
from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def get_by_genre(self, gid):
        return self.session.query(Movie).filter(Genre.id == gid).join(Genre).all()

    def get_by_director(self, did):
        return self.session.query(Movie).filter(Director.id == did).join(Director).all()

    def get_all(self):
        return self.session.query(Movie).all()

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()
