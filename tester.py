from Storage import Storage
import People
import discord

def main():
    
    _quit = False
    
    strge = Storage('strge.txt')
    
    while not _quit:
        print("Welcome ")
        name = input("Type name: ")
        rmte = People.People(name)
        done = False
        while not done:
            chore = input("Chore: ")
            rmte.add_chore(chore)
            is_done = input("More? Y/N: ").lower()
            if is_done == 'n':
                done = True
        strge.add_roommate(rmte)
        is_done = input('Done? Y/N: ').lower()
        if is_done == 'y':
            qui = True


if __name__ == "__main__":
    main()