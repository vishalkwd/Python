from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Warlord',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 26 2024'
    },
    {
        'author': 'V_Hawk',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'November 27 2024'
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title='Home')
# posts = posts will get all the variables defined in posts list in the home.html page

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(debug=True)

# Next steps - 18 mins in
# https://www.youtube.com/watch?v=QnDWIZuWYW0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=2