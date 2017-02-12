import requests
import re

def moviedetails(film):
            film=film.lower()
            url = 'https://www.google.co.in/search?q='+film+'+imdb'
            
            r = requests.get(url)
            k = r.text
            m = re.search('www.imdb.com/title/(.+?)/', k)
            if m:
                    found = m.group(1)
                    #print found
                    m = re.search('www.imdb.com/title/(.+?)/', k)
                    movie = 'http://www.omdbapi.com/?i='+found+'&plot=longt&r=json'
                    r = requests.get(movie)
                    k = r.text
                    m = re.search('Title":"(.+?)",', k)
                    Title = m.group(1)
                    #print Title
                    m = re.search('imdbRating":"(.+?)",', k)
                    Rating = m.group(1)
                    m = re.search('Genre":"(.+?)",', k)
                    Genre = m.group(1)
                    m = re.search('Director":"(.+?)",', k)
                    Director = m.group(1)
                    m = re.search('Writer":"(.+?)",', k)
                    Writer = m.group(1)
                    m = re.search('Plot":"(.+?)",', k)
                    Plot = m.group(1)
                    m = re.search('Actors":"(.+?)",', k)
                    Actors = m.group(1)
                    m = re.search('Released":"(.+?)",', k)
                    Rls = m.group(1)
                        #tkMessageBox.showinfo( "Input", m,)
                    if(Title!=film):
                        print("Showing Result for "+Title+"\n\n")
                    print("Title         : "+Title+"\n")
                    print("Rating        : "+Rating+"\n")
                    print("Released Date : "+Rls+"\n")
                    print("Genre         : "+Genre+"\n")
                    print("Director      : "+Director+"\n")
                    print("Writer        : "+Writer+"\n")
                    print("Cast          : "+Actors+"\n\n")
                    print("Synopsis:\n")
                    print(Plot+"\n\n")
                    req="done"
film=raw_input("\n(improve search accuarcy by using keywords such as \n'Toy Story-Animated, Kireedam-Mohanlal, Kismath-Malayalam'\n Enter the name of the movie : ") 
moviedetails(film)
