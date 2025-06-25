from database.DAO import DAO
import networkx as nx
import geopy.distance

class Model:
    def __init__(self):
        self._nodes = list()
        self._idNodes = dict()
        self._edges = list()
        self._graph = None

    def buildGraph(self):
        # self._graph = nx.Graph()
        self._nodes = DAO.getNodes()
        for nodo in self._nodes:
            self._idNodes[nodo.id] = nodo
        self._edges = DAO.getEdges()
        self._graph.add_nodes_from(self._nodes)
        for edge in self._edges:
            self._graph.add_edge(edge.n1, edge.n2, weight=edge.weight)

    def getInfoGraph(self):
        if self._graph is None:
            return None
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getShortestPath(self, u, v):
        return nx.single_source_dijkstra(self._graph, u, v)

    def getBFSNodesFromTree(self, source):
        tree = nx.bfs_tree(self._graph, source)
        archi = list(tree.edges())
        nodi = list(tree.nodes())
        return nodi[1:]

    def getDFSNodesFromTree(self, source):
        tree = nx.dfs_tree(self._graph, source)
        nodi = list(tree.nodes())
        return nodi[1:]

    def getBFSNodesFromEdges(self, source):
        archi = nx.bfs_edges(self._graph, source)
        res = []
        for u, v in archi:
            res.append(v)
        return res

    def getDFSNodesFromEdges(self, source):
        archi = nx.dfs_edges(self._graph, source)
        res = []
        for u, v in archi:
            res.append(v)
        return res

    @property
    def nodes(self):
        return self._nodes

    def ricorsione(self, parziale):
        if self.condizione_finale():
            pass
        else:
            for el in lista:
                if self.condizione():
                    parziale.append()
                    self.ricorsione(parziale)
                    parziale.pop()

    def condizione(self):
        pass

    def condizione_finale(self):
        pass


def getTraversalTime(u,v):
    dist = geopy.distance.distance((u.coordX, u.coordY), (v.coordX, v.coordY)).km
    # geopy permette di manipolare informazioni di distanza
    return dist

def sort_list(lista):
    return lista.sort(key=lambda x:x[1], reverse=True)