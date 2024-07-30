# Flask is Title-Case bc it's a class:
from flask import Flask, request

app = Flask(__name__)

# This prints __main__... why? i think it refers to the ~current file... it's supposed to distinguish the current "main" file from a module etc, even if it's not called main:
# print(__name__)

# ROUTING:


@app.route("/")
def welcome():
    # Why does this actually print to http://127.0.0.1:5000? Because it's backend, not frontend? Aamod: printing from the backend only sends things to the terminal; to print to the frontend, we must return something:
    return "Hello, welcome to testing APIs using Flask!"


# This redundant code would not get executed:
"""
@app.route("/")
def welcome_again():
    return "Hello, welcome again!"
"""


@app.route("/about")
def about():
    # Observe Internal Server Error when trying to print:
    # print("Here is some info about me.")
    return "Here is some info about me."


@app.route("/contact")
def contact_us():
    return "My contact details are ____________"


courses = [
    {
        "code": 101,
        "name": "Diploma of IT",
        "duration": "1.5 years",
    },
    {
        "code": 102,
        "name": "Diploma of Web Dev",
        "duration": "1.5 years",
    },
    {
        "code": 103,
        "name": "Diploma of Data Science",
        "duration": "2 years",
    },
    {
        "code": 104,
        "name": "Bachelor of IT",
        "duration": "3 years",
    },
    {
        "code": 105,
        "name": "Bachelor of Web Dev",
        "duration": "3 years",
    },
    {
        "code": 106,
        "name": "Bachelor of Data Science",
        # trailing commas: get used to it (although Insomnia seems not to like it?! oh because JSON doesn't allow it. JSON5 does though):
        "duration": "3 years",
    }
]

# GET request (don't need second argument [methods] inside route() bc it defaults to GET):


# @app.route("/courses", methods=["GET"])
@app.route("/courses")
def list_courses():
    limit = request.args.get("limit")
    if limit:
        return courses[0:int(limit)]
    return courses

# This can be improved with dynamic routing... next week:


@app.route("/courses/101")
def get_course_101():
    return courses[0]


@app.route("/courses/102")
def get_course_102():
    return courses[1]


@app.route("/courses/103")
def get_course_103():
    return courses[2]


# ~Error handling:
@app.route("/courses/200")
def error_route():
    return {"Error": "Course does not exist"}, 404

# POST request:
# Add a news course:


@app.route("/courses", methods=["POST"])
def add_course():
    body = request.get_json()
    courses.append(body)
    return courses

# DELETE request:
# Delet a course:


@app.route("/courses/107", methods=["DELETE"])
def delete_course_107():
    # could use 7 or -1:
    del courses[7]
    # Aamod is returning a dict because JSON format is a list of dicts (but why? does this returned value get added to the JSON file?):
    return {"message": "Duplicate course 107 successfully deleted."}

# PUT request:
# Updating an entire course:


@app.route("/courses/107", methods=["PUT"])
def update_course_107():
    body = request.get_json()
    # could use 7 or -1:
    courses[-1] = body
    return courses[-1]

# PATCH request:
# Patching a part of a course:


@app.route("/courses/101", methods=["PATCH"])
def patch_101():
    body = request.get_json()
    # use if statements to avoid producing "null" if the user doesn't enter one of the values:
    # if body.get("duration"):
    #     courses[0]["duration"] = body.get("duration")
    # if body.get("name"):
    #     courses[0]["name"] = body.get("name")
    # but a better way is using or! bc it's more efficient bc of short-circuit evaluation(?):
    courses[0]["duration"] = body.get("duration") or courses[0]["duration"]
    courses[0]["name"] = body.get("name") or courses[0]["name"]
    return courses[0]


if __name__ == "__main__":
    app.run(debug=True)
