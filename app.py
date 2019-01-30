from flask import Flask,render_template,url_for,request
import content

movies = content.content_movies()
tvs = content.content_tvs()
app = Flask(__name__)

context = {
    'movies': movies,
    'tvs': tvs,
}

@app.route('/')
def index():
    return render_template('index.html',**context)

@app.route('/list/')
def item_list():
    category = int(request.args.get('category'))
    if category == 1:
        items = movies
    else:
        items = tvs
    # print(items)
    return render_template('list.html',items = items)

if __name__ == '__main__':
    app.run(debug=True)