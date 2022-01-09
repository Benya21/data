class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
    
    def find_set(self, parent, i):
        if i != parent[i]:
            parent[i] = self.find_set(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        x = self.find_set(parent, x)
        y = self.find_set(parent, y)
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] = rank[x] + 1

    def kruskal(self):
        A = []
        self.graph = sorted(self.graph, key = lambda item: item[2])
        parent = []
        rank = []
        for vertex in range(self.V):
            parent.append(vertex)
            rank.append(0)
        
        i = 0
        e = 0
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find_set(parent, u)
            y = self.find_set(parent, v)
            if x != y:
                e = e + 1
                A.append([u, v, w])
                self.union(parent, rank, x, y)
        sum1 = 0
        for u, v, weight in A:
            sum1 += weight
            print("เส้นเชื่อมระหว่างจุด %d กับจุด %d มีค่าน้ำหนัก = %d" % (u, v, weight))
        print(f"Weight รวมของ Minimun spanning tree คือ  {sum1}")


n = int(input("โปรดระบุค่าตัวแปร n (จำนวนจุดในกราฟแบบไม่มีทิศทาง(Undirectd graph)): "))
g = Graph(n)
i = int(input("โปรดระบุเส้นเชื่อม(Edge)ในกราฟแบบไม่มีทิศทาง: "))

while i > 0:
    source = int(input("Surce = "))
    destination = int(input("Destination = "))
    weight = int(input("Weight = "))
    g.addEdge(source, destination, weight)
    i -= 1

g.kruskal()