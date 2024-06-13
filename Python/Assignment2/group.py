class FriendGroup:
    def __init__(self, members):
        self.members = members

    def order_movies(self, cinema):
        list_movies = []
        for movie in cinema.get_movies_shown():
            count = 0
            notmatch = False
            for member in self.members:
                if member.is_allowed(movie) and member.is_interested(movie):
                    count += 1
                elif not member.is_allowed(movie):
                    notmatch = True
            if notmatch:
                continue
        
            if (movie, count) not in list_movies:
                list_movies.append((movie, count))
            
            list_movies.sort(key=lambda x: x[1], reverse=True)
    
        return list_movies

    def choose_screening(self, cinema):
        def can_all_members_attend(screening):
            for person in self.members:
                if not person.is_allowed(screening.movie):
                    return False
            return True

        def count_attendance(screening):
            general_attendance = 0
            crowdedness_attendance = 0
            for person in self.members:
                if person.can_attend(screening):
                    general_attendance += 1
                    if person.will_attend(screening):
                        crowdedness_attendance += 1
            return general_attendance, crowdedness_attendance

        screenings_info = []

        for screening in cinema.screenings:
            if can_all_members_attend(screening):
                general_attendance, crowdedness_attendance = count_attendance(screening)
                days_since_release = screening.movie.get_time_passed('2023/04/12')
                screenings_info.append((screening, general_attendance, crowdedness_attendance, days_since_release))

        screenings_info.sort(key=lambda x: (-x[1], -x[2], x[3]))

        return screenings_info[0][0], screenings_info



    def buy_tickets(self, screening):
        can = 0
        end_time = screening.get_end_time()[0]
        for person in self.members:
            if person.bedtime > end_time:
                can += 1
        screening.tickets_sold += can

if __name__ == '__main__':
    # you can run your tests here
    pass
