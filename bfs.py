
class Vertex(object):
    
    def __init__(self):
        self.color = 0
        self.distance = 'Inf'
        self.predecessor = None
        self.key = None
        self.adj_v = {}

    def 


class DAG(object):
    
    def __init__(self):
        self.vertex_dict = {};
        self.edge_dict = {};
        sefl.vertex_num = 0
    
    def reVertex(self,key):
        return vertex_dict{key}

    def addEdgeFromVertex(self,vertex):
        for k in vertex.adj_v:
            edge = str(vertex.key) + "_" + str(k)
            self.edge_dict{edge} = 1
        
    def addVertex(self,vertex):
        self.vertex_dict[vertex.key] = vertex
        if vertex.predecessor.key in vertex_dict:
            self.addVertexAdj(vertex.predecessor.key,vertex)
        self.addEdgeFromVertex(vertex)
        edge = str(vertex.predecessor.key) + "_" + str(vertex.key)
        self.edge_dict{edge} = 1
        self.vertex_num += 1


    def reEdge(self,edge):
        if edge in edge_dict:
            return edge
        else:
            return 0

    def reVertexAdj(self,key):
        if key in vertex_dict:
            return vertex_dict[key].adj_v
        else:
            return 0

    def addVertexAdj(self,key,adj_vertex):
        if key in vertex_dict:
            vertex_dict[key].adj_v[adj_vertex.key] = adj_vertex
            return 1
        else:
            return 0

    def removeEdgeByStr(self,edge):
    def removeVertexByKey(self,key):
    def removeVertexByVer(self,vertex):
    def removeEdgebyVertices(self, vertex_p, vertex)

#dag: DAG, root: the key of the Vertex
def BFS(dag,root_key):
    for vertex in dag.vertex_dict:
        if vertex.key != root_key:
            vertex.color
    
    
    

