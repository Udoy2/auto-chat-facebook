from app.app import app
from app.lib import generate
import argparse

parser = argparse.ArgumentParser(description="Auto chat in facebook options")
parser.add_argument('-g', '--generate', action='store_true',
                    help="-g will generate session")
parser.add_argument('-c', '--chat', action='store_true',
                    help="-c/--chat will send message")
args = parser.parse_args()

############################################## variables that needs to change according to users wish #############################################################

username = "humansuper534@gmail.com"  # email or phone no of id

passs = "humansuper534@"  # password of id
name = "Udoy Rahman"    # id name to send message
msg = ['hello', 'hi i am working',
       'Its midnight I 😂😂😂😂😂😂😂 was thinking that I will wish you a happy birthday that"s why I made this bot to do it instead of me..:P']  # list of messages to send
year = 2021  # the year of message to send
month = 2    # the month of message to send
day = 1     # the day of message to send
hour = 17    # the hour of message to send, its in 24 hour formate
minn = 47    # the min to send message

######################################################x-------variables that needs to change according to users wish----------x#######################################


if __name__ == "__main__":
    if args.generate:
        generate(username, passs)
    elif args.chat:
        app(username, passs, name, msg, year, month, day, hour, minn)
    else:
        print("no argument given")
