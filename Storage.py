import People

class Storage:
    
    def __init__(self, file):
        self.file = file

    def add_roommate(self, roommate):
        fil = open(self.file, 'a')
        name = roommate.get_name()
        chores = roommate.get_chores()
        fil.write('*' + name + '$')
        for chore in chores:
            fil.write("&" + chore + "@'\n")
        fil.close()
    
    def get_roommates(self):
        roomates = []
        fil = open(self.file, 'r')
        for line in fil:
            name = ''
            for char in line:
                if char == '*':
                    for char in line:
                        if char == '$':
                            break
                        name += char
                roomates.append(name)
        fil.close()
        return roomates

            
