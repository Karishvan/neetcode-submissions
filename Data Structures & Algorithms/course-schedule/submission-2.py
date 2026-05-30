class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Course i to list of prereqs
        adj_list = {i:[] for i in range(numCourses)}
        visited = set()
        #print(edges)
        
        for (course, prereq) in prerequisites:
            #print(course, prereq)
            adj_list[course].append(prereq)
            #edges[course] += 1
            #print(adj_list[course])
        print(adj_list)
        #print(edges)
        print("")
        def dfs(course):
            
            if course in visited:
                return False
            
            if adj_list[course] == []:
                return True
            visited.add(course)
            
            for c in adj_list[course]:
                if not dfs(c): return False
            visited.remove(course)

            adj_list[course] = [] #remove repeated work
            return True

            
        for course in range (numCourses):
            if not dfs(course):
                return False
        return True
        