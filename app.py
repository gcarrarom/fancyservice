from flask import Flask, request
from pyfiglet import Figlet


app = Flask("FancyService")

@app.route('/')
def root():
    user_agent = request.headers.get("User-Agent", "curl")
    print(user_agent)
    if "Mozilla" in user_agent:
        with open("./root.html", "r") as filereader:
            response = filereader.read()
    elif "curl" in user_agent:
        response = {"name": "FancyService", "version": "0.0.0"}
    else:
        f = Figlet()
        response = f.renderText("Welcome to the fancyService!")
    return response