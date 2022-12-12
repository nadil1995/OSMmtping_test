import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt #installs with osmnx

# download/model a street network for some city then visualize it
G = ox.graph_from_place("Adelaide, Adelaide City Council, South Australia, Australia ", 
network_type="drive")
fig, ax = ox.plot_graph(G,figsize=(20,20),bgcolor='#FFFFFF',
    node_color='black', node_size=0)