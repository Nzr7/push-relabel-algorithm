from collections import deque

class PushRelabel:
    def __init__(self, G, source, sink):
        self.G = G
        self.source = source
        self.sink = sink
        self.height = {node: 0 for node in G.nodes}
        self.excess = {node: 0 for node in G.nodes}
        self.flow = {}

    def initialize_preflow(self):
        self.height[self.source] = len(self.G)
        for neighbor in self.G.successors(self.source):
            cap = self.G[self.source][neighbor]['capacity']
            self.flow[(self.source, neighbor)] = cap
            self.flow[(neighbor, self.source)] = -cap
            self.excess[neighbor] += cap
            self.excess[self.source] -= cap

    def push(self, u, v):
        residual_capacity = self.G[u][v]['capacity'] - self.flow.get((u, v), 0)
        send = min(self.excess[u], residual_capacity)
        if send > 0 and self.height[u] == self.height[v] + 1:
            self.flow[(u, v)] = self.flow.get((u, v), 0) + send
            self.flow[(v, u)] = self.flow.get((v, u), 0) - send
            self.excess[u] -= send
            self.excess[v] += send
            return True
        return False

    def relabel(self, u):
        min_height = float('inf')
        for v in self.G.successors(u):
            residual_capacity = self.G[u][v]['capacity'] - self.flow.get((u, v), 0)
            if residual_capacity > 0:
                min_height = min(min_height, self.height[v])
        if min_height < float('inf'):
            self.height[u] = min_height + 1

    def run(self):
        self.initialize_preflow()
        active = deque([u for u in self.G.nodes if u != self.source and u != self.sink and self.excess[u] > 0])
        while active:
            u = active.popleft()
            pushed = False
            for v in self.G.successors(u):
                if self.push(u, v):
                    pushed = True
                    if v != self.source and v != self.sink and self.excess[v] == self.flow[(u, v)]:
                        active.append(v)
                    if self.excess[u] == 0:
                        break
            if not pushed:
                self.relabel(u)
                active.append(u)
        return sum(self.flow.get((self.source, v), 0) for v in self.G.successors(self.source))
