from random import choice
class Person:
    def __init__(self, threshold, interested_in, patience):
        self.threshold = threshold
        self.interested_in = interested_in
        self.friends_list = list()
        self.has_read = list()
        self.patience = patience

    def is_interested_in(self, category):
        if category in self.interested_in:
            return True
        return False

    def has_read_news(self, news):
        if news in self.has_read:
            return True
        return False

    def make_friends(self, population, n):
        i = 0
        while True:
            selected = choice(population)
            if selected not in self.friends_list and selected != self:
                self.friends_list.append(selected)
                i += 1
            if i == n:
                break
        

    def process_news(self, news, time_step):  # 1b
        friend_list = []
        read = True
        if len(self.has_read) == self.patience:
            read = False
        if self.has_read_news(news):
            read = False
        if news.get_excitement(time_step) < self.threshold:
            read = False
        if read:
            self.has_read.append(news)
            for friend in self.friends_list:
                if friend.is_interested_in(news.category):
                    friend_list.append(friend)
        return friend_list
