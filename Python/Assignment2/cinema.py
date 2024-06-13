from screening import Screening
class Cinema:
    def __init__(self, auditoriums):
        self.auditoriums = auditoriums
        self.screenings = list()

    def add_movie(self, movie, screening_times):
        for time in screening_times:
            done = False
            for auditorium in self.auditoriums:
                if auditorium.add_screening(Screening(movie, auditorium, time)):
                    self.screenings.append(Screening(movie, auditorium, time))
                    done = True
                    break
            if not done:
                    raise RuntimeError(f"Could not add movie {movie.title} at {time[0]:02d}:{time[1]:02d}")
                    


    def get_movies_shown(self):
        movies = []
        for screening in self.screenings:
            movies.append(screening.movie)
        return movies
        
    
    def get_screenings_for_movie(self, movie):
        scr = []
        for screening in self.screenings:
            if movie.title == screening.movie.title:
                scr.append(screening)
        return scr


if __name__ == '__main__':
    # you can run your tests here
    pass
