'''
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, 
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).

Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
'''
from sys import exit


def generate_graph(edge_count):
    graph = {}

    for i in range(edge_count):
        graph[i] = []
        for j in range(edge_count):
            if i != j:
                graph[i].append(j)

    return graph


def DFS_graph_traversal(start, visited):
    visited.add(start)
    print(start, end=' ')

    for neighbour in graph[start]:
        if neighbour not in visited:
            DFS_graph_traversal(neighbour, visited)


edge_count = int(input('Введите количество вершин графа: '))
graph = generate_graph(edge_count)
print(f'Список смежности графа: {graph}')
start = int(input('Укажите начальную вершину: '))

if start > edge_count:
    print('Старт должен быть меньше либо равен количеству вершин графа.')
    exit()

visited = set()
print(f'Обход графа от вершины {start}: ', end='')
DFS_graph_traversal(start, visited)
