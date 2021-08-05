class People:
    
    def __init__(self, name):
        self.name = name
        self.chores = []

    
    def add_chore(self, chore):
        self.chores.append(chore)

    def del_chore(self, chore):
        self.chores.remove(chore)

    def get_chores(self):
        return self.chores

    def get_name(self):
        return self.name