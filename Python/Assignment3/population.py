from random import choice, randint, sample, random
from news import CATEGORIES
from person import Person


class Population:
    def __init__(self, n, friends_count, patience_limit):
        self.people = list()
        self.active_news = list()

        self.generate_population(n, friends_count, patience_limit)

    def generate_population(self, n, friends_count, patience_limit):

        for i in range(n):
            
            thr = round(random(), 2)
            patience_n = randint(patience_limit[0], patience_limit[1])
            categ = sample(CATEGORIES, 4)
            p = Person(thr, categ, patience_n)
            self.people.append(p)
        for person in self.people:
            person.make_friends(self.people, friends_count)

    
    def introduce_news(self, news):
        self.active_news.append(news)
        list = []
        for person in self.people:
            if person.is_interested_in(news.category):
                if person not in list:
                    list.append(person)

        return list[:5]


    def update_news(self, time_step):
        for news in self.active_news:
            if news.get_excitement(time_step) == 0:
                self.active_news.remove(news)
            

    def count_readers(self, news):
        count = 0
        for person in self.people:
            if person.has_read_news(news):
                count += 1
        return count

    def get_number_of_interested(self, category):
        count = 0
        for person in self.people:
            if person.is_interested_in(category):
                count += 1

        return count


class HomogeneousPopulation(Population):
    def __init__(self, n, friends_count, patience_limit, category):
        self.category = category
        super().__init__(n, friends_count, patience_limit)

    def generate_population(self, n, friends_count, patience_limit):
        
        for j in range(n):
            t = random()
            p = randint(patience_limit[0], patience_limit[1])
            i = [self.category]
            self.people.append(Person(t, i, p))
        for person in self.people:
            person.make_friends(self.people, friends_count)