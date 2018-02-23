<<<<<<< HEAD
# PluralSight_coding_challenge
## Flask RESTful API for User Similarity
This is a Flask application to choose appropriate features and do calculations to identiy similar users. Result can be accessible via a structured, RESTful API. The endpoint can take as an input a user handle and return a summary of the most similar users. Also, I use SQLite as back-end store in this project.

## Dependencies
. scikit-learn

. Flask

. pandas

. numpy

    pip3 install -r requirements.txt

## Usage
. Step1: open the terminal, get the repository, then go to main directory

. Step2:  convert all *.csv files in the data foler to  *.db(SimilarUsr.db)

          python3 csvToSqlite.py SimilarUsr.db /data

. Step3: step-by-step to run the notebook   Similar_User_SQLite.ipynb  after  $jupyter notebook in the terminal

.Step4:  run the RESTful API.

          python3 ap.py <port> 

=======
# PluralSight_coding_challenge
>>>>>>> a60cf507a3b2511e86230a2502a8aa4335a201bf

