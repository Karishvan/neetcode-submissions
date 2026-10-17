class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(set) #maps courses to its prereqs
        res = []
        taken = set()
        visited = set()
        for course, prereq in prerequisites:
            adj_list[course].add(prereq)
        
        def dfs(course):
            if course in taken:
                return True
            if course in visited:
                return False
            visited.add(course)
            if course not in adj_list or len(adj_list[course]) == 0:
                res.append(course)
                taken.add(course)
                return True
            can_take = True
            for prereq in adj_list[course]:
                if not dfs(prereq):
                    can_take = False
            
            if can_take:
                taken.add(course)
                res.append(course)
            return can_take


        for course in range(numCourses):
            if not dfs(course):
                return []
        return res