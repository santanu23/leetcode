"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        graph = {}

        for employee in employees:
            graph[employee.id] = employee

        return self.dfs(graph[id], graph)
        
    
    def dfs(self, employee, graph):
        return employee.importance + sum([self.dfs(graph[s_id], graph) for s_id in employee.subordinates])
