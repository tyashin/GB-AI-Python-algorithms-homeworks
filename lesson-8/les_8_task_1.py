'''
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?

Примечание. Решите задачу при помощи построения графа.
'''

n = int(input('Укажите число друзей: '))
graph = []
h_shakes = 0

for i in range(n):
    graph.append([])

    for j in range(n):
        if j > i:
            val = 1
            h_shakes = h_shakes + 1
        else:
            val = 0

        graph[i].append(val)

print(
    f'Количество рукопожатий = {h_shakes}')

print(
    f'Проверка по формуле "N(N-1)/2": {int(n*(n-1)/2)}')
