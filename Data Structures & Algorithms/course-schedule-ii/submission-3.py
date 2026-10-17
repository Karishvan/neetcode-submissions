class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = { c: set() for c in range(numCourses)} #maps courses to its prereqs
        res = []
        taken = set()
        for course, prereq in prerequisites:
            adj_list[course].add(prereq)
        
        def dfs(course, visited):
            if course in taken:
                return True
            if course in visited:
                return False
            visited.add(course)
            
            for prereq in adj_list[course]:
                if not dfs(prereq, visited):
                    return False
            
           
            taken.add(course)
            res.append(course)
            return True


        for course in range(numCourses):
            if not dfs(course, set()):
                return []
        return res