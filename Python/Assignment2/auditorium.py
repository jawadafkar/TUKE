class Auditorium:
    def __init__(self, capacity):
        self.capacity = capacity
        self.screenings = list()

    def is_available(self, new_screening):
        new_end_time = (new_screening.time[0] * 60) + new_screening.time[1] + new_screening.movie.length
        new_start_time = (new_screening.time[0] * 60) + new_screening.time[1]

        if not self.screenings:
            return True

        for i in range(len(self.screenings)):
            current_screening = self.screenings[i]
            current_start_time = (current_screening.time[0] * 60) + current_screening.time[1]
            current_end_time = current_start_time + current_screening.movie.length

            if (new_start_time < current_end_time) and (new_end_time > current_start_time):
                return False

        return True


    def add_screening(self, new_screening):
        if self.is_available(new_screening):
            self.screenings.append(new_screening)
            self.screenings.sort
            return True
        else:
            return False


if __name__ == '__main__':
    # you can run your tests here
    pass
