import osmnx as ox
import networkx as nx
import datetime
from colorama import Fore, Style

def loadingGraph(neighborhood, city, country, road_type):
    if (neighborhood):
        G = ox.graph_from_place(neighborhood + ", " + city + ", " + country, network_type=road_type, simplify=True).to_undirected()
    else:
        G = ox.graph_from_place(city + ", " + country, network_type=road_type, simplify=True).to_undirected()
    G = nx.convert_node_labels_to_integers(G) 
    return G

def eulerized(G):
    H = nx.eulerize(G)
    return H

def get_GPS(H):
    tmp = nx.eulerian_circuit(H)
    list_ = []
    GPS = []
    for elem in tmp:
        list_.append(elem[0])
        name = ""
        try:
            name = H.edges[(elem[0], elem[1], 0)]['name']
            if (type(name) == list):
                for road in name:
                    GPS.append(road)
            else:
                GPS.append(name)
        except KeyError:
            continue
    return GPS,list_

def pretty_printGPS(GPS):
    print(Fore.RED + Style.BRIGHT + "Start the drone" + Style.RESET_ALL)
    i = 0
    for i in range (0 , len(GPS)):
        if i == 0:
            print("Start by taking the " + Fore.GREEN + Style.DIM + GPS[i] + Style.RESET_ALL)
        else:
            if GPS[i] == GPS[i - 1]:
                continue
            else:
                print("Continue with " + Fore.GREEN + Style.DIM + str(GPS[i]) + Style.RESET_ALL)
    print(Fore.RED + Style.BRIGHT + "Land the drone")

def main_drone(neighborhood, city, country, road_type, print_gps, print_map, print_drone):
    
    #Graph Loading
    begin_load = datetime.datetime.now()
    print(Fore.GREEN + Style.BRIGHT + "Loading graph..." + Style.RESET_ALL)
    G = loadingGraph(neighborhood, city, country, road_type)
    print(Fore.BLUE + Style.BRIGHT + "Loading graph time: " + str(datetime.datetime.now() - begin_load))
    if (print_map):
        fig, ax = ox.plot_graph(ox.project_graph(G))


    #Eulerize Graph
    begin_euler = datetime.datetime.now()
    print(Fore.GREEN + Style.BRIGHT + "Beginning eulerization...")
    H = nx.eulerize(G)
    print(Fore.BLUE + Style.BRIGHT + "Eulerize time: " + str(datetime.datetime.now() - begin_euler))
    
    #Option : print the GPS path
    liste = []
    gps,liste = get_GPS(H)
    if (print_gps):
        pretty_printGPS(gps)   
    
    #Print the figures
    if (print_drone):
        fig, ax = ox.plot_graph_route(G, liste, route_linewidth=4, node_size=1, bgcolor='k')

    print(Fore.RED + Style.BRIGHT + "Total time: " + str(datetime.datetime.now() - begin_load))

def main_snowplow(neighborhood, city, country, road_type, required_len_pull, required_len, min_accuracy, completion, maps):
    if (neighborhood):
        G = ox.graph_from_place(neighborhood + ", " + city + ", " + country, network_type=road_type, simplify=True)
    else:
        G = ox.graph_from_place(city + ", " + country, network_type=road_type, simplify=True)
    G = nx.convert_node_labels_to_integers(G)
    list_ = []
    path = dict(nx.all_pairs_shortest_path(G))
    all_path = create_path_pull(path, required_len)
    res_path = find_critical_road(G, path, all_path, min_accuracy, required_len, completion, maps)


def create_path_pull(path, required_len):
    all_path = []
    for elem in path.values():
        for var in elem.values():
            if len(var) > required_len:
                all_path.append(var)
    return all_path

def rentability(checked_mat, need_to_happend):
    res = 0
    for elem in need_to_happend:
        if checked_mat[elem] != 1:
            res+=1
    return res/len(need_to_happend)

def update(checked_mat, res_path):
    for elem in res_path:
        if checked_mat[elem] != True:
            checked_mat[elem] = True
    return checked_mat

def find_critical_road(G, path, all_path, min_accuracy, required_len, completion, maps):
    checked_mat = [False] * len(path.values())
    
    #niveau de précision demandé à la première itération
    critical_floor = min_accuracy
    #longueur minimale de chaque chemin à la première itération
    acceptable_len = required_len
    
    critical_road = []
    length = len(all_path) - 1
    i = 0
    final = []
    while False in checked_mat:
        if i > length:
            i = 0
            #Ici la précision et la longueur acceptable des chemins est modifié de manière a ne pas
            #tomber dans un creu et que nous puissions trouver les sommets que nous n'avons pas encore traverser
            #quitte à repasser sur des sommets que nous avons déjàn visité 
            critical_floor -= 0.05
            acceptable_len -= 1
            if completion:
                formatted_float = "{:.2f}".format(checked_mat.count(True)*100/len(checked_mat))
                print("The complete cover is at : " + Fore.BLUE + Style.BRIGHT + formatted_float + Style.RESET_ALL + "% of its completion")
        if len(all_path[i]) > acceptable_len:
            if rentability(checked_mat, all_path[i]) > critical_floor:
                critical_road.append(all_path[i])
                if maps:
                    final.append(all_path[i])
                checked_mat = update(checked_mat, all_path[i])
        i+=1
    colors = ['r', 'b', 'g', 'c', 'y', "m", "w"]
    used_colors = []
    j = 0
    for i in range(len(final)):
        if (j == len(colors)):
            j = 0
        used_colors.append(colors[j])
        j += 1
    fig, ax = ox.plot_graph_routes(G, final, used_colors, route_linewidth=8, node_size=1, bgcolor='k')
    return critical_road

print(Fore.RED + Style.BRIGHT + "Beginning drone path calculation for roads" + Style.RESET_ALL)
main_drone("Outremont", "Montreal", "Canada", "drive", True, True, True)
print(Fore.RED + Style.BRIGHT + "Beginning snowplow path calculation for roads" + Style.RESET_ALL)
main_snowplow("Outremont","Montreal", "Canada", "drive" , 4, 15, 0.9, True, True)
print(Fore.RED + Style.BRIGHT + "Beginning drone path calculation for sidewalks" + Style.RESET_ALL)
main_drone("Outremont", "Montreal", "Canada", "walk", True, True, True)
print(Fore.RED + Style.BRIGHT + "Beginning snowplow path calculation for sidewalks" + Style.RESET_ALL)
main_snowplow("Outremont","Montreal", "Canada", "walk" , 4, 15, 0.9, True, True)

print(Fore.BLUE + Style.BRIGHT + "All calculation done" + Style.RESET_ALL)