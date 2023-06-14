"""
EXERCITIUL 6:Creatio aplicatiefolosindconceptulde clasapentrua creaurmatorulefect(queue): [1,2,3,4,5] →[x,1,2,3,4] ... →5
"""

class Queue:
    def __init__(self, data):
        self.queue = list(data)

    def push(self, element):
        self.queue.append(element)

    def pop(self):
        return self.queue.pop(0)


q = Queue([1, 2, 3, 4, 5])
q.push('x')
q.pop()
print(q.queue)
