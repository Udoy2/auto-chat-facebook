from .lib.autochat import Autochat


def app(username, passs, name, msg, year, month, day, hour, minn):

    chat = Autochat(username, passs, name, msg, year, month, day,  hour, minn)
    chat.send_message()
