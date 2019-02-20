import networkx as nx
from hac import GreedyAgglomerativeClusterer
clusterer = GreedyAgglomerativeClusterer()
# This cluster call is where most of the heavy lifting happens
karate_dendrogram = clusterer.cluster(nx.karate_club_graph())
karate_dendrogram.clusters(1)
karate_dendrogram.plot(karate_dendrogram.clusters(3),karate_dendrogram.labels())