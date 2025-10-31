import numpy as np
import csv

class Actor: 
    def __init__(self, nmid, name): #movie set must be a set
        self._nmid = nmid
        self._name = name 
        self._movie_set = set() #Starred movies

    def return_id(self):
        return self._nmid
    
    def add_movie_set(self, movie_set):
        self._movie_set = movie_set

    def get_name(self):
        return self._name

    def __str__(self):
        string = f"{self._name} | {self._nmid} | "
        for item in self._movie_set:
            string += f"{str(item)} |" 
        return string

    def __eq__(self, value):
        if not isinstance(value, Actor):
            return 
        return self._nmid == value._nmid
    
    def __hash__(self):
        return hash(self._nmid)
    
class Movie: 
    def __init__(self, ttid, title, rating, amount_votes):
        self._ttid = ttid
        self._title = title
        self._rating = rating
        self._amount_votes = amount_votes
        self._actor_set = set()
    
    def add_actor(self, actor_node):
        self._actor_set.add(actor_node)

    def return_id(self):
        return self._ttid

    def get_title(self):
        return self._title

    def get_rating(self):
        return self._rating

    def __eq__(self, value):
        if not isinstance(value, Movie):
            return 
        return self._ttid == value._ttid

    def __hash__(self):
        return hash(self._ttid)
    
    def __str__(self):
        return f"{self._ttid} | {self._title}"

def tsv_reader(filename, list):
            
    with open(filename, 'r', encoding='utf8') as tsv_file:
        tsv_reader = csv.reader(tsv_file, delimiter='\t')

        for row in tsv_reader:
            list.append(row)

actors = [] #nm-id Navn tt-id_1 tt-id_2 .... tt-id_k
movies = [] #tt-id Tittel Rating Antall Stemmer 

tsv_reader("actors.tsv", actors)
tsv_reader("movies.tsv", movies)
#Vi gjør adjacency list for å representere grafene

def adjacency_list(actors, movies):
    output_dict = {}
    movie_dict = {}
    for movie in movies:
        movie_dict[movie[0]] = Movie(movie[0], movie[1], movie[2], movie[3]) #tt-id to movie node

    #Connect all actor nodes to movie nodes and movies nodes to actors nodes
    for actor in actors:
        movie_set = set()
        actor_node = Actor(actor[0], actor[1]) #nm-id and name
        for i in range(2, len(actor)):
            if actor[i] not in movie_dict:
                continue
            movie_node = movie_dict[actor[i]] #It is the tt-id
            movie_node.add_actor(actor_node)
            movie_set.add(movie_node)
        
        actor_node.add_movie_set(movie_set)
        output_dict[actor_node] = actor_node._movie_set

    
    for val in movie_dict.values():
        output_dict[val] = val._actor_set

    return output_dict

def count(adjacency_list):
    nodes = len(adjacency_list)
    edges = 0

    for key, item in adjacency_list.items():
        if isinstance(key, Actor):
            continue
        edges += len(item)
    return f"Nodes: {nodes} | Edges: {edges}"

adjacency_list_test = adjacency_list(actors, movies)



