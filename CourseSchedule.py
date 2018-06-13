class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        course_graph = [[] for _ in range(numCourses)]
        visited = [0]*numCourses
        
        for course, prereq in prerequisites:
                course_graph[course].append(prereq)
        
        def dfs(course):
            if visited[course] == -1:
                return False
            if visited[course] == 1:
                return True
            
            visited[course] = -1
            
            for prereq in course_graph[course]:
                if dfs(prereq) == False:
                    return False
            visited[course] = 1
            return True
        
        for course_index in range(len(course_graph)):
            if dfs(course_index) == False:
                return False
            
        return True
