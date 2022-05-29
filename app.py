import flask
import json
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from abcd import KNearestNeighbours
from operator import itemgetter

import requests

app = flask.Flask(__name__, template_folder='templates')

df2 = pd.read_csv('./tmdb.csv')

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df2['soup'])

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

df2 = df2.reset_index()
indices = pd.Series(df2.index, index=df2['title'])
all_titles = [df2['title'][i] for i in range(len(df2['title']))]

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


def get_recommendations(title):
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    tit = df2['title'].iloc[movie_indices]
    dat = df2['release_date'].iloc[movie_indices]
    return_df = pd.DataFrame(columns=['Title', 'Year'])
    return_df['Title'] = tit
    return_df['Year'] = dat
    return return_df


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
