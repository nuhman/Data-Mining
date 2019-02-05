## Collaborative Filtering  
  
> Colloborative filtering is used to make recommendations based on other people— in effect, people collaborate to come up with recommendations 
> – [Ron Zacharski](http://guidetodatamining.com/assets/guideChapters/DataMining-ch2.pdf)  
  
Algorithms covered:  
* minkowski distance algorithm (manhattan distance, euclidean distance)  
* pearson coefficient  
* k-nearest neighbor  
* cosine similarity  
  
`recommender.py` can be used to  recommend movies for a specific person.  
Example usage:  
  
```python
r = recommender()  
r.loadMovieDB() # load movie to 'self.data' as '{'aaron': {'Braveheart': 4, 'Gladiator': 4,...}, 'Patrick C': {'Braveheart': 4, 'Dodgeball': 5..}, ...}'  

```  
Then to get recommendations:  
```python
r.recommend('Patrick C')
Out: [('Pulp Fiction', 4.0), ('Jaws', 3.0)]
```
