import sys
 
if len(sys.argv) != 5:
        print "Arguments: userId userDataFilename movieFilename recommendationFilename"
        sys.exit(1)
 
userId, userDataFilename, movieFilename, recommendationFilename = sys.argv[1:]
 
print "Reading Movies Descriptions"
movieFile = open(movieFilename)
movieById = {}
for line in movieFile:
        tokens = line.split("|")
        movieById[tokens[0]] = tokens[1:]
movieFile.close()
 
print "Reading Rated Movies"
userDataFile = open(userDataFilename)
ratedMovieIds = []
for line in userDataFile:
        tokens = line.split("\t")
        if tokens[0] == userId:
                ratedMovieIds.append((tokens[1],tokens[2]))
userDataFile.close()
 
print "Reading Recommendations"
recommendationFile = open(recommendationFilename)
recommendations = []
for line in recommendationFile:
        tokens = line.split("\t")
        if tokens[0] == userId:
                movieIdAndScores = tokens[1].strip("[]\n").split(",")
                recommendations = [ movieIdAndScore.split(":") for movieIdAndScore in movieIdAndScores ]
                break
recommendationFile.close()
 
print "Rated Movies"
print "------------------------"
for movieId, rating in ratedMovieIds:
        print "%s, rating=%s" % (movieById[movieId][0], rating)
print "------------------------"
 
print "Recommended Movies"
print "------------------------"
for movieId, score in recommendations:
        print "%s, score=%s" % (movieById[movieId][0], score)
print "------------------------"
