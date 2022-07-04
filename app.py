import flask
import json
from abcd import KNearestNeighbours
from operator import itemgetter

app = flask.Flask(__name__, template_folder='templates')

with open(r'data.json', 'r+', encoding='utf-8') as f:
    data = json.load(f)
with open(r'titles.json', 'r+', encoding='utf-8') as f:
    print("hi")
    movie_titles = json.load(f)

movies = [title[0] for title in movie_titles]
def knn(test_point, k):
    goal = [0 for item in movie_titles]

    model = KNearestNeighbours(data, goal, test_point, k=k)
    model.fit()
    max_dist = sorted(model.distances, key=itemgetter(0))[-1]
    table = list()
    for i in model.indices:
        table.append([movie_titles[i][0], movie_titles[i][2]])
    return table

# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return flask.render_template('index.html')

    if flask.request.method == 'POST':
        m_name = flask.request.form['movie_name']
        m_name = m_name.title()
        if m_name not in movies:
            print("not found")
            return flask.render_template('negative.html', name=m_name)
        else:
            test_point = data[movies.index(m_name)]
            table = knn(test_point,11)
            names = []
            dates = []
            table.pop(0)
            for movie, link in table:
                names.append(movie)
                dates.append(link)
                

            return flask.render_template('positive.html', movie_names=names, movie_date=dates, search_name=m_name)


if __name__ == '__main__':
    app.run(debug=True)
