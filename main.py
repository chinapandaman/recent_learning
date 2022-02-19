# -*- coding: utf-8 -*-

from bottle import route, run, template, static_file


@route("/")
def index():
    return template("index.html")


@route("/like_button.js")
def like_button():
    return static_file("like_button.js", root=".")


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
