from typing import List
class Solution:

    def criticalConnections(self, n: int, connections: List[List[int]]):
        graph = self.createGraph(connections)

        discoverTime = [0]*n
        lowDiscoverTime =[0]*n
        visited = [False]*n
        parent = -1
        time=-1
        output=[]
        self.dfs(graph,discoverTime,lowDiscoverTime,visited,0,parent,time, output)
        return output

    def dfs(self,graph,discoverTime,lowDiscoverTime,visited,currentNode,parentNode,time, output):
        visited[currentNode]=True
        time += 1
        discoverTime[currentNode], lowDiscoverTime[currentNode] = time, time
        #print("discover time: ", discoverTime)
        #print("lowDiscoverTime", lowDiscoverTime)
        for nextNode in graph[currentNode]:
            if parentNode != nextNode:
                if visited[nextNode]:
                    lowDiscoverTime[currentNode] = min(lowDiscoverTime[currentNode], discoverTime[nextNode])
                else:
                    self.dfs(graph,discoverTime,lowDiscoverTime,visited,nextNode,currentNode,time, output)
                    lowDiscoverTime[currentNode]=min(lowDiscoverTime[currentNode], lowDiscoverTime[nextNode])

                    if lowDiscoverTime[nextNode] > discoverTime[currentNode]:
                        #print("it's in")
                        output.append([currentNode, nextNode])
        return output

    def createGraph(self, connections:List[List[int]]):
        graph={}
        for at,to in connections:
            if at not in graph:
                graph[at]=set()
            if to not in graph:
                graph[to]=set()
            graph[at].add(to)
            graph[to].add(at)
        return graph

solution= Solution()
print(solution.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))
print(solution.criticalConnections(2, [[0,1]]))

 