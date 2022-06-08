from flask import Flask, render_template, request, jsonify
import os
import pandas
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/getDataCast/<actor>", methods=["POST", "GET"])
def getDataCast(actor):
    filePath = os.getcwd()
    # Read in csv's
    castFile = pandas.read_csv(filePath +"\\static\\archive\\cast2.csv")
    moviesFile = pandas.read_csv(filePath +"\\static\\archive\\movies_ratings.csv")
    crewFile = pandas.read_csv(filePath + "\\static\\archive\\crew.csv")
    # Use loc on castFile for actor
    castList = castFile.loc[castFile.name==actor]
    # use merge to find movies
    moviesFound = moviesFile.merge(castList, left_on = 'id', right_on = 'movie_id')
    print(moviesFound)
    # replace null values
    moviesFound = moviesFound.fillna(0)
    return jsonify(moviesFound.to_dict("records"))
@app.route("/getDataDirector/<actor>", methods=["POST", "GET"])
def getDataDirector(actor):
    filePath = os.getcwd()
    # Read in csv's
    moviesFile = pandas.read_csv(filePath +"\\static\\archive\\movies_ratings.csv")
    crewFile = pandas.read_csv(filePath + "\\static\\archive\\crew.csv")
    # Use loc on crewfile for /director
    directorList = crewFile.loc[(crewFile.job=="Director")&(crewFile.name==actor)] 
    # use merge to find movies
    directorsFound = moviesFile.merge(directorList, left_on = 'id', right_on = 'movie_id')
    # replace null values
    directorsFound = directorsFound.fillna(0)
    return jsonify(directorsFound.to_dict("records"))
@app.route("/getDataComposer/<actor>", methods=["POST", "GET"])
def getDataComposer(actor):
    filePath = os.getcwd()
    # Read in csv's
    moviesFile = pandas.read_csv(filePath +"\\static\\archive\\movies_ratings.csv")
    crewFile = pandas.read_csv(filePath + "\\static\\archive\\crew.csv")
    # Use loc on crewFile for composer
    composerList = crewFile.loc[((crewFile.job=="Music")|(crewFile.job=="Original Music Composer"))&(crewFile.name==actor)]
    # use merge to find movies
    composersFound = moviesFile.merge(composerList, left_on = 'id', right_on = 'movie_id')
    # replace null values
    composersFound = composersFound.fillna(0)
    return jsonify(composersFound.to_dict("records"))
@app.route("/getDataGenre/<actor>", methods=["POST", "GET"])
def getDataGenre(actor):
    filePath = os.getcwd()
    # Read in csv's
    moviesFile = pandas.read_csv(filePath +"\\static\\archive\\movies_ratings.csv")
    genreFile = pandas.read_csv(filePath + "\\static\\archive\\genre_counts3.csv")
    return jsonify(genreFile.to_dict("records"))
@app.route("/getDataRatings/<actor>", methods=["POST", "GET"])
def getDataRatings(actor):
    filePath = os.getcwd()
    # Read in csv's
    voteFile = pandas.read_csv(filePath + "\\static\\archive\\avg_rev_vote.csv")
    return jsonify(voteFile.to_dict("records"))
if __name__ == "__main__":
    app.run(debug=True)