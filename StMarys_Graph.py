#Goals:
#Input a map of Saint Mary's and enter a starting vertex and
#an ending vertex
#Return the fastest route from the start to the end

#Graph and Vertex Classes: https://www.bogotobogo.com/python/python_graph_data_structures.php
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 1):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()


#Graph of Saint Mary's
g = Graph()

g.add_vertex('115')
g.add_vertex('PS')
g.add_vertex('125')
g.add_vertex('129')
g.add_vertex('133')
g.add_vertex('141')
g.add_vertex('157')
g.add_vertex('124')
g.add_vertex('112')
g.add_vertex('108')
g.add_vertex('104')
g.add_vertex('132')
g.add_vertex('100A')
g.add_vertex('100B')
g.add_vertex('166')
g.add_vertex('160')
g.add_vertex('169')
g.add_vertex('172')
g.add_vertex('416')
g.add_vertex('104')
g.add_vertex('332')
g.add_vertex('401')
g.add_vertex('400')
g.add_vertex('316')
g.add_vertex('412')
g.add_vertex('312')
g.add_vertex('308')
g.add_vertex('184')
g.add_vertex('CL')
g.add_vertex('188')
g.add_vertex('176')
g.add_vertex('180')
g.add_vertex('300')
g.add_vertex('177')
g.add_vertex('201')
g.add_vertex('204')
g.add_vertex('205')
g.add_vertex('208')
g.add_vertex('213')

g.add_edge('115','PS',10)
g.add_edge('115','124',18)
g.add_edge('PS','124',8)
g.add_edge('PS','125',3)
g.add_edge('125','124',7)
g.add_edge('125','129',11)
g.add_edge('129','104',15)
g.add_edge('129','132',19)
g.add_edge('129','133',12)
g.add_edge('133','132',9)
g.add_edge('133','141',10)
g.add_edge('141','132',12)
g.add_edge('141','157',20)
g.add_edge('157','132',27)
g.add_edge('157','169',30)
g.add_edge('124','112',7)
g.add_edge('112','108',6)
g.add_edge('112','416',31)
g.add_edge('112','105',29)
g.add_edge('108','104',6)
g.add_edge('108','416',26)
g.add_edge('108','105',26)
g.add_edge('104','105',30)
g.add_edge('104','416',28)
g.add_edge('104','132',15)
g.add_edge('104','100A',12)
g.add_edge('132','100A',12)
g.add_edge('100A','100B',8)
g.add_edge('100B','166',7)
g.add_edge('100B','172',7)
g.add_edge('166','160',8)
g.add_edge('166','172',9)
g.add_edge('160','169',8)
g.add_edge('169','177',11)
g.add_edge('172','CL',12)
g.add_edge('172','184',15)
g.add_edge('172','312',36)
g.add_edge('172','412',26)
g.add_edge('172','416',10)
g.add_edge('416','312',30)
g.add_edge('416','412',15)
g.add_edge('416','105',6)
g.add_edge('105','412',11)
g.add_edge('105','312',31)
g.add_edge('412','312',19)
g.add_edge('412','400',17)
g.add_edge('400','316',8)
g.add_edge('400','401',14)
g.add_edge('400','332',29)
g.add_edge('401','332',23)
g.add_edge('316','312',8)
g.add_edge('312','184',21)
g.add_edge('312','308',8)
g.add_edge('184','308',16)
g.add_edge('184','188',7)
g.add_edge('184','CL',4)
g.add_edge('CL','176',5)
g.add_edge('188','300',11)
g.add_edge('188','180',9)
g.add_edge('176','177',12)
g.add_edge('176','180',5)
g.add_edge('180','300',14)
g.add_edge('300','201',25)
g.add_edge('177','201',24)
g.add_edge('201','205',13)
g.add_edge('201','204',10)
g.add_edge('204','205',19)
g.add_edge('205','208',10)
g.add_edge('208','213',23)


dgraph = {}
for vert in g:
    inner = {}
    for adj in vert.adjacent:
        a = adj.id
        inner[a] = vert.get_weight(g.get_vertex(a))
    dgraph[vert.id] = inner
#print(dgraph)
     
def dijkstra(graph,start,goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
 
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
                
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
 
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))
 

def main():
    print("Table of Contents:")
    print('Brother Urban Gregory Hall = 115')
    print('Public Safety = PS')
    print('Assumption Hall = 125')
    print('Power Plant = 129')
    print('St Joseph Hall = 133')
    print('Madigan Gym = 141')
    print('University Credit Union Pavilion = 157')
    print('Brother Jerome West Hall = 124')
    print('Filippi Hall = 112')
    print('Sichel Hall = 108')
    print('Galileo Hall = 104')
    print('Brother Alfred Brousseau Hall = 132')
    print('Korth Academic Hall = 100A')
    print('Chapel = 100B')
    print('Psychology = 166')
    print('Brother Cornelius Art Center = 160')
    print('Soda Activity Center = 169')
    print('Oliver Hall = 172')
    print('Dante Hall = 416')
    print('Garaventa Hall = 105')
    print('Lower Town Houses = 332')
    print('Joseph L. Altio Rec Center = 401')
    print('Filippi Academic Hall = 400')
    print('Augustine Hall = 316')
    print('St Albert Hall Library = 412')
    print('De La Salle Hall = 312')
    print('Aquinas Hall = 308')
    print('Ferroggiaro Hall = 184')
    print('Cafe Louis = CL')
    print('Mitty Hall = 188')
    print('Bookstore/Post Office = 176')
    print('Le Fevre Theater = 180')
    print('Justin Hall = 300')
    print('St Catherine of Siena Hall = 177')
    print('Claeys Hall North = 201')
    print('Claeys Hall South = 204')
    print('Ageno Hall, Michael E = 205')
    print('Ageno Hall, Jarjorie David = 208')
    print('Upper Town Houses = 213')
    print("")
    start = str(input("Please enter the code of the starting position: "))
    end = str(input("Please enter the code of the ending position: "))
    dijkstra(dgraph, start, end)

main()
