#slope one algorithm for item-based filtering
#finding the deviatioins between item rating ahead of time

users2 = {"Amy": {"Taylor Swift": 4, "PSY": 3, "Whitney Houston": 4},
          "Ben": {"Taylor Swift": 5, "PSY": 2},
          "Clara": {"PSY": 3.5, "Whitney Houston": 4},
          "Daisy": {"Taylor Swift": 5, "Whitney Houston": 3}}


class SlopeOne:

    def __init__(self,data=users2):

        self.frequencies = {}
        self.deviations = {}
        #
        # if data is dictionary set recommender data to it
        #
        if type(data).__name__ == 'dict':
            self.data = data


    def computeDeviations(self):
        #get band and ratings for each person
        for ratings in self.data.values(): #make it a list
            for (band,rating) in ratings.items(): #make it a tuple
                self.frequencies.setdefault(band,{})
                self.deviations.setdefault(band,{})
                for (band2,rating2) in ratings.items():
                    if band != band2:
                        self.frequencies[band].setdefault(band2,0)
                        self.deviations[band].setdefault(band2,0.0)
                        self.frequencies[band][band2] += 1
                        self.deviations[band][band2] += rating - rating2
        
        for (band,ratings) in self.deviations.items():
            for i in ratings:
                ratings[i] /= self.frequencies[band][i]
    


    def recommend(self , username):

        recommendations = {}    
        newfrequencies = {}
        #for every item and rating in the user's recommendations
        
        for (useritem,userrating) in self.data[username].items():        
            #print(deviations.items())
            for (diffitem , diffratings) in self.deviations.items():
                #print('hello')
                if diffitem not in self.data[username] and useritem in self.deviations[diffitem]:                
                    freq = self.frequencies[diffitem][useritem]
                    recommendations.setdefault(diffitem,0.0)
                    newfrequencies.setdefault(diffitem,0)
                    #numerator
                    recommendations[diffitem] += (diffratings[useritem] + userrating) * freq
                    #denominator
                    newfrequencies[diffitem] += freq

        recommendations = [ (k,v/newfrequencies[k]) for (k,v) in recommendations.items() ]

        recommendations.sort(key=lambda artistTuple: artistTuple[1],
                                    reverse=True)
        return recommendations
