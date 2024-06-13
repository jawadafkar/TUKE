class Screening:
    def __init__(self, movie, auditorium, time):
        self.movie = movie
        self.auditorium = auditorium
        self.time = time
        self.tickets_sold = 0

    def sell_tickets(self, count):
        if self.tickets_sold + count <= self.auditorium.capacity:
            self.tickets_sold += count
            return True
        return False

    def get_occupancy(self):
        return self.tickets_sold / self.auditorium.capacity

    def get_end_time(self):
        
        hr = self.time[0] + self.movie.length // 60
        mn = self.time[1] + self.movie.length % 60

        if mn >= 60:
            mn = mn % 60
            hr += 1
        return (hr, mn)



if __name__ == '__main__':
    # you can run your tests here
    pass
