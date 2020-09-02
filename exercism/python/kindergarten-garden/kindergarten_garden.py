class Garden:
    def __init__(self, diagram, students = ["Alice", "Bob", "Charlie", "David", "Eve", 
        "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.diagram = diagram.split()
        self.students = sorted(students)
    
    def plants(self, name):
        result = []
        seeds = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}
        index = self.students.index(name) * 2
        
        for i in range(2):
            for j in range (2):
                result.append(seeds[self.diagram[i][j + index]])

        return result