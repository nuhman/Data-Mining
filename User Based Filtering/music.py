import codecs
from math import sqrt

''' The data set for different users and their ratings '''

music = {"Dr Dog/Fate": {"piano": 2.5, "vocals": 4, "beat": 3.5, "blues": 3, "guitar": 5, "backup vocals": 4, "rap": 1},
         "Phoenix/Lisztomania": {"piano": 2, "vocals": 5, "beat": 5, "blues": 3, "guitar": 2, "backup vocals": 1, "rap": 1},
         "Heartless Bastards/Out at Sea": {"piano": 1, "vocals": 5, "beat": 4, "blues": 2, "guitar": 4, "backup vocals": 1, "rap": 1},
         "Todd Snider/Don't Tempt Me": {"piano": 4, "vocals": 5, "beat": 4, "blues": 4, "guitar": 1, "backup vocals": 5, "rap": 1},
         "The Black Keys/Magic Potion": {"piano": 1, "vocals": 4, "beat": 5, "blues": 3.5, "guitar": 5, "backup vocals": 1, "rap": 1},
         "Glee Cast/Jessie's Girl": {"piano": 1, "vocals": 5, "beat": 3.5, "blues": 3, "guitar":4, "backup vocals": 5, "rap": 1},
         "La Roux/Bulletproof": {"piano": 5, "vocals": 5, "beat": 4, "blues": 2, "guitar": 1, "backup vocals": 1, "rap": 1},
         "Mike Posner": {"piano": 2.5, "vocals": 4, "beat": 4, "blues": 1, "guitar": 1, "backup vocals": 1, "rap": 1},
         "Black Eyed Peas/Rock That Body": {"piano": 2, "vocals": 5, "beat": 5, "blues": 1, "guitar": 2, "backup vocals": 2, "rap": 4},
         "Lady Gaga/Alejandro": {"piano": 1, "vocals": 5, "beat": 3, "blues": 2, "guitar": 1, "backup vocals": 2, "rap": 1}}


users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0,
                        "Norah Jones": 4.5, "Phoenix": 5.0,
                      "Slightly Stoopid": 1.5,
                      "The Strokes": 2.5, "Vampire Weekend": 2.0},

         "Bill":     {"Blues Traveler": 2.0, "Broken Bells": 3.5,
                      "Deadmau5": 4.0, "Phoenix": 2.0,
                      "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},

         "Chan":     {"Blues Traveler": 5.0, "Broken Bells": 1.0,
                      "Deadmau5": 1.0, "Norah Jones": 3.0,
                      "Phoenix": 5, "Slightly Stoopid": 1.0},

         "Dan":      {"Blues Traveler": 3.0, "Broken Bells": 4.0,
                      "Deadmau5": 4.5, "Phoenix": 3.0,
                      "Slightly Stoopid": 4.5, "The Strokes": 4.0,
                      "Vampire Weekend": 2.0},

         "Hailey":   {"Broken Bells": 4.0, "Deadmau5": 1.0,
                      "Norah Jones": 4.0, "The Strokes": 4.0,
                      "Vampire Weekend": 1.0},

         "Jordyn":   {"Broken Bells": 4.5, "Deadmau5": 4.0,
                      "Norah Jones": 5.0,
                      "Phoenix": 5.0, "Slightly Stoopid": 4.5,
                      "The Strokes": 4.0, "Vampire Weekend": 4.0},

         "Sam":      {"Blues Traveler": 5.0, "Broken Bells": 2.0,
                      "Norah Jones": 3.0, "Phoenix": 5.0,
                      "Slightly Stoopid": 4.0,  "The Strokes": 5.0},
         
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0,
                      "Phoenix": 4.0,  "Slightly Stoopid": 2.5,
                      "The Strokes": 3.0}}

'''
There are three methods to calculate the closeness between two users
on their likeness.
1) Manhattan or Euclidean (i.e.. minkowski in general) should be used
If your data is dense (almost all attributes have nonzero values)
and the magnitude of the attribute values is important
2) If the data is subject to grade-inﬂation (different users
may be using different scales) use Pearson.
3) If the data is sparse (i.e.. if mostly zero values)
consider using Cosine Similarity.
'''


        
def manhattan(first,second):
    '''The first and second are two dictionaries of the form
       {'The stokes':3.5,'Stoopid':4.0....}
       Computes the manhattan distance'''
    distance = 0
    for rating in first:
        if rating in second:
            distance += abs(first[rating] - second[rating])
    return distance                

def minkowski(first, second, r):
    ''' when r = 1 ,  the distance is manhattan
        when r = 2 , it's eucledian '''
    distance = 0
    
    ''' inittialize a flag so sa to check the common ratings exist between
        firsr and second , since we need to retutn pow(distance , 1/r) and
        if the distance is 0 (i.e no common rating), it raises an error '''
    flag = 0
    
    for rating in first:
        if rating in second:
            distance += pow(abs(first[rating] - second[rating]) , r)
            flag = 1
    if flag:
        return pow(distance , 1/r)
    else:
        return 0


def pearson(first,second):	    
    a,c1,Xi,Yi,d1,n=0,0,0,0,0,0
    for rating in first:
        if rating in second:
            a += first[rating]*second[rating]
            Xi += first[rating]
            Yi += first[rating]
            #b = (Xi*Yi)/n
            c1 += first[rating]**2
            #c = pow((c1 -  (Xi**2/n)) , 1/2)
            d1 += second[rating]**2
            n += 1
    if n == 0:
        return 0
    b = (Xi*Yi)/n
    c = sqrt((c1 - ((Xi**2)/n)))
    d = sqrt((d1 - ((Yi**2)/n)))
    denominator = c * d
    if c == 0:
        return 0
    return (a - b)/denominator


def cosine(first , second):
    numerator = 0
    x,y=0,0
    for rating in first:
        if rating in second:
            numerator += first[rating] * second[rating]
        x += first[rating]**2
    for rating in second:
        y += second[rating]**2
    x = sqrt(x)
    y = sqrt(y)
    print(x)
    print(y)
    print(numerator)
    return (numerator/(x*y))


def nearestNeighbour(username , users):
    '''Creates a sorted list of users based on their distance to username'''
    distances = []
    for user in users:
        if user != username:
            distance = minkowski(users[username] , users[user] , 2)
            distances.append( (distance,user) )
    #sort based on distance --> closest first
    distances.sort() 
    return distances
            
def recommend(username, users):
    ''' returns a recommended list for the given username '''
    # nearest neughbour for username
    nearest = nearestNeighbour(username , users)[0][1]
    print(nearest)
    recommendations = []
    # now finding the artists the neighbour rated but username didn't
    # we are assuming username would have similar tastes
    neighbourRatings = users[nearest]
    print(neighbourRatings)
    userRatings = users[username]
    for artist in neighbourRatings:
        if artist not in userRatings:
            recommendations.append( (artist,neighbourRatings[artist]) )
            
    ''' here key = lambda ..... means we are sorting based
     on the key that is second parameter of the recommendation tuple
     which are ratings like 4.0 , 3.5 etc... '''
    return sorted(recommendations,
                  key = lambda artistRating : artistRating[1],
                  reverse = True)


