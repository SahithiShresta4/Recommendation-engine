<center><h1>MOVIE RECOMMENDATION ENGINE</h1><center>

Recommendatio Engines are used in variety of areas such as movies,music,books,clothes. Recommendation Engines recommend things to the users based on users choices.
  
Movie Recommendation Engine suggests top 10 movies based on the movie which user has searched for.Uses KNN Algorithm to find the movies which are close to the particular movie.<br />
<img src="/Readme_images/homepage.jpeg" />
<img src="/Readme_images/Recommendations.jpeg" />
 <br />
  
### Installation and Running

1. Clone this Repository
  
```bash
  git clone https://github.com/SahithiShresta4/Recommendation-engine.git
```
  
2. Go to the project directory

```bash
  cd Recommendation-engine
```
  
3. Install dependencies

```bash
  pip install -r requirements.txt
```
4. Run app.py

5. The application will start running at the link displayed on the terminal. (http://127.0.0.1:5000)

  <br />

### Tech Stack

**WEB TECHNOLOGIES**

```bash
Backend -- Python , Flask, Numpy , Pandas 

FrontEnd -- HTML,CSS
```
<br />
**DATA SET**

```bash
https://www.kaggle.com/datasets/carolzhangdc/imdb-5000-movie-dataset
```
 <br />
###Algorithms and Learnings

**KNN Algorithm**

1. Calculate the euclidean distances between the given movie and all other movies from the dataset.
2. Store the distances and indexes in a collection.
3. Sort the collection from smallest to largest based on distances.
4. Take the first K=10 elements from the collection.
5. Collect data and links of those items and display it to the user.
  

**CONTENT BASED FILTERING**

Content based filtering is a Machine Learning technique used in Recommendation engines which gives suggestions to user based on his/her history and likings or explicit search.


