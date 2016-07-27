from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student")
def get_grade_listing_for_student():
    """Show grade listing for all projects by a student."""

    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    rows = hackbright.get_grade_listing_for_student(first_name, last_name)
    for row in rows:
        first, last, github, title, grade = row
    
    return render_template("student_info.html", rows=rows, first=first, last=last, github=github)


@app.route("/student-add", methods=['POST'])
def get_student():
    """Add a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    return render_template("student_info.html", first=first, last=last, github=github)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
