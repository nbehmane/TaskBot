import discord
import People
import Storage


chores = []

def get_chores(file):
    """Grabs the current chore list from file"""
    chores = open(file, 'r')
    chore_list = []
    for chore in chores:
        chore_list.append(chore)
    chores.close()
    return chore_list

def add_chore(args, file):
    """Adds a chore to the end of the chore text file"""
    global chores
    chore_list = open(file, 'a+')
    chore = ''
    for word in args[2:]:
        chore += word + ' '
    chores.append(chore)
    chore_list.write(chore)
    chore_list.write('\n')
    chore_list.close()



class MyClient(discord.Client):
    async def on_ready(self):
        global chores
        print('Logged on as', self.user)
        chores = get_chores('chores.txt')
        print('Loading chores...')
        print(chores)

    async def on_message(self, message):
        global chores
        # Makes sure we don't respond to ourselves.
        if message.author == self.user:
            return
        # Splits the message content to be parsed by a function reader.
        args = message.content.split(' ')
        # Everything past this point handles commands...
        # I know it's dirty but I need this working soon

        # Simply prints out what you sent in.
        if args[0] == '$test':
            await message.channel.send(args)

        # Add branch to add roommates and chores.
        elif args[0] == '$add':
            
            # Adds a chore.
            if args[1] == 'chore':
                if len(args) < 3:
                    await message.channel.send("No chore? uhh...")
                else:

                    # Add the chore..
                    add_chore(args, 'chores.txt')
                    await message.channel.send("Success!") 

                    # update the chores
                    chores = get_chores('chores.txt')

                    # For backend reasons...
                    print(chores)

        elif args[0] == '$chores':
            await message.channel.send('Here are the chores:')
            await message.channel.send(chores)
        


client = MyClient()
client.run('Lol what key')