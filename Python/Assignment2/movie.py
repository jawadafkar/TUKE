from constants import GENRES
from datetime import datetime
class Movie:
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    def __init__(self, title, length, genre, age_limit, release_date):
        
        if isinstance(title, str):
            self.title = title
        else:
            raise TypeError("Movie title must be string")

        if isinstance(length, int) and length >= 1:
            self.length = length
        elif not isinstance(length, int):
            raise TypeError("Movie length must be integer")
        elif length < 1:
            raise ValueError("Movie length must be at least 1")
        
        if genre in GENRES:
            self.genre = genre
        else:
            raise ValueError(f'Unknown genre "{genre}"')

        if isinstance(age_limit, int) and age_limit >= 1:
            self.age_limit = age_limit
        elif not isinstance(age_limit, int):
            raise TypeError("Age limit must be integer")
        elif age_limit < 1:
            raise ValueError("Age limit must be at least 1")
        
        if self.validate_date(release_date):
            self.release_date = release_date

    
    
    def validate_date(self, date):
        if not isinstance(date, str):
            raise TypeError("Release date must be string")

        if date.count("/") != 2 or date[4] != "/" or date[7] != "/":
            raise ValueError("Release date must meet format YYYY/MM/DD")
        
        if date[:4].startswith("-"):
            if not date[1:4].isdigit():
                raise ValueError(f'Could not load date from string: "{date}"')
        else:
            if not date[:4].isdigit():
                raise ValueError(f'Could not load date from string: "{date}"')
        
        if date[5:7].startswith("-"):
            if not date[6:7].isdigit():
                raise ValueError(f'Could not load date from string: "{date}"')
        else:
            if not date[5:7].isdigit():
                raise ValueError(f'Could not load date from string: "{date}"')
        
        if date[8:].startswith("-"):
            if not date[9:].isdigit():
                raise ValueError(f'Could not load date from string: "{date}"')
        else:
            if not date[8:].isdigit():
                raise ValueError(f'Could not load date from string: "{date}"')
        
        if int(date[5:7]) < 1 or int(date[5:7]) > 12:
            raise ValueError(f'Invalid month {int(date[5:7])}')
        
        if date[5:7] in ("01", "03", "05", "07", "08", "10", "12"):
            if int(date[8:]) < 1 or int(date[8:]) > 31:
                raise ValueError(f"Invalid day for {Movie.months[int ( date[5:7] ) - 1 ] }: {int(date[8:])}")
        elif date[5:7] in ("04", "06", "09", "11"):
            if int(date[8:]) < 1 or int(date[8:]) > 30:
                raise ValueError(f"Invalid day for {Movie.months[int ( date[5:7] ) - 1 ] }: {int(date[8:])}")
        elif date[5:7] == "02":
            if int(date[8:]) < 1 or int(date[8:]) > 29:
                raise ValueError(f"Invalid day for {Movie.months[int ( date[5:7] ) - 1 ] }: {int(date[8:])}")

        return True

    def get_time_passed(self, date):

        if self.validate_date(date):
           r_date = datetime.strptime(self.release_date, "%Y/%m/%d")
           new = datetime.strptime(date, "%Y/%m/%d")
           time_passed = new - r_date
        
        return int(time_passed.days)



if __name__ == '__main__':
    # you can run your tests here)
    pass
