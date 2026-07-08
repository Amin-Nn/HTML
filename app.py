from flask import Flask

app = Flask(__name__)

students = {
                1: "Murad", 
                2: "Leyla", 
                3: "Aysel", 
                4: "Aysu", 
                5: "Elcan"
            } 


@app.route('/')
def home():
    return """
    <h1>Welcome to my Portfolio</h1>
    <a href="portfolio">Click here to visit my Portfolio</a>
    """

@app.route("/portfolio")
def portfolio():
    with open("website_.html", "r", encoding="utf-8") as file:
        return file.read()

@app.route("/style_.css")
def serve_css():
    with open("style_.css", "r", encoding="utf-8") as file:
        return file.read(), 200, {'Content-Type': 'text/css'}

@app.route("/about")
def about():
    return """
    <h1>Welcome to the About Page</h1>
    <ul style="font-size: 20px" align="left">
                <li>2008 təvəllüdlü</li> 
                <li>UNEC-də Rəqəmsal İqtisadiyyat fakültəsinin Kompüter Mühəndisliyi ixtisası üzrə təhsil alıram.</li>
                <li>FutureDev Camp-da Web Programming üzrə təhsil alıram.</li>
    </ul>
    """

@app.route('/skills')
def skills():
    return """
    <h1>Bacarıqlarım</h1> 
        <ol style="font-size: 20px" align="left">
            <li>Java, HTML, Python kimi proqramlaşdırma dillərində orta səviyyəli təcrübə.</li> 
            <li>Kompüterin hardware quruluşunda və  təcrübə.</li>
            <li>hardwarein bir yerə gətirilməsində təcrübə.</li>
            <li>Microsoft Office proqramlarında təcrübə.</li>
            <li>Microsoft Windows əməliyyat sistemində təcrübə.</li>
        </ol>
    """

@app.route('/students')
def get_all_students():
    student_list = "<br>".join([f"Student ID: {id}, Name: {name}" for id, name in students.items()])
    return f"<h1>All Students</h1><br>{student_list}"

@app.route('/profile/<username>')
def profile(username):
    return f"<h1>Salam, {username}!</h1>"

@app.route('/student/<int:id>')
def student_id(id):
    if id in students:
        return f"<h1>Student ID: {id}, Name: {students[id]}</h1>"
    else:
        return f"<h1>Student with ID {id} not found!</h1>"
    
@app.route('/sum/<int:a>/<int:b>')
def sum_numbers(a, b):
    return f"<h1>Cəm: {a + b}</h1>"

# @app.route('/')
# def home():
#     return """
#     <h1>Welcome to the Home Page</h1>
#     """

# @app.route("/about")
# def about():
#     return """
#     <h1>Welcome to the About Page</h1>
#     """

# @app.route('/student/<int:id>')
# def student_id(id):
#     return f"<h1>Student ID: {id}</h1>"

# @app.route('/students')
# def get_all_students():
#     student_list = "<br>".join([f"Student ID: {id}, Name: {name}" for id, name in students.items()])
#     return f"<h1>All Students</h1><br>{student_list}"

# @app.route('/profile/<username>')
# def profile(username):
#     if username in students.values():
#         return f"<h1>Salam, {username}!</h1>"
#     else:
#         return f"<h1>Student {username} not found!</h1>"




if __name__ == '__main__':
    app.run(debug=True)