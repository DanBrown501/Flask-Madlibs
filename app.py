from flask import Flask, request, render_template
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "coolfirstkey"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Create Home Page"""
    html = """
    <html>
        <body>
            <h1>Home Page!</h1>
            <p>Welcome to my simple app!</p>
            <a href='/hello'> Go to hello page</a>
        </body>
    </html>
    """
    return render_template('home.html')

@app.route('/form')
def show_form():
    return render_template("form.html")

@app.route('/form-2')
def show_form_2():
    return render_template("form_2.html")

COMPLIMENTS = ["cool", "clever", "tenacions", "awesome", "Pythonic"]


@app.route('/greet')
def get_greeting():
    username = request.args["username"]
    nice_thing = choice(COMPLIMENTS)
    return render_template("greet.html", username=username, compliment=nice_thing)

@app.route('/greet-2')
def get_greeting_2():
    username = request.args["username"]
    wants = request.args.get("wants_compliments")
    nice_things = sample(COMPLIMENTS, 3)
    return render_template("greet_2.html", username=username, wants_compliments=wants, compliments=nice_things)



@app.route('/lucky')
def lucky_number():
    num = randint(1,10)
    return render_template('lucky.html', lucky_num=num, msg="You are so lucky!")

@app.route('/spell/<word>')
def spell_word(word):
    caps_word = word.upper()
    return render_template('spell_word.html', word=caps_word)


@app.route('/hello')
def say_hello():
    """Create Hello Page"""
    return render_template("hello.html")


@app.route('/search')
def search():
    """Searches Terms after Sorting Them"""
    term = request.args["term"]
    sort = request.args["sort"]
    print(request.args)
    return f"<h1>Search Results For: {term}</h1> <p>Sorting by:{sort}</p>"

# @app.route("/post", methods=["POST"])
# def post_demo():
#     return "You made a post request! "

# @app.route("/post", methods=["GET"])
# def get_demo():
#     return "You made a get request! "


@app.route('/add-comment')
def add_comment_form():
    """Handles adding comment"""
    return"""
    <h1>Add Comment </h1>
    <form method='POST'>
        <input type+'text' placeholder='comment' name='comment'/>
        <input type+'text' placeholder='username' name='username'/>
        <button>Submit</button>
    </form>
    """

@app.route('/add-comment', methods=["POST"])
def save_comment():
    """Handles Saving Comments"""
    comment= request.form["comment"]
    username = request.form["username"]
    return f"""
    <h1>SAVED YOUR COMMENT</h1>
    <ul>
        <li>Username: {username}
        <li>Comment: {comment}
    </ul>
    """

@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f"<h1>Browsing The {subreddit} Subreddit</h1>"

@app.route("/r/<subreddit>/comments/<int:post_id>")
def show_comments(subreddit, post_id):
    return f"<h1>Viewing comments for post with id: {post_id} from the {subreddit} Subreddit</h1>"

POSTS = {
    1: "I like python",
    2: "I hate mayo",
    3: "Double rainbow all the way",
    4: "YOLO OMG"
}

@app.route('/posts/<int:id>')
def find_post(id):
    post = POSTS.get(id, "Post not found")
    return f"<p>{post}</p>"