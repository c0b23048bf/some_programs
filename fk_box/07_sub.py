import heapq

def dijkstra(graph, start):
    # 各頂点の最短距離を無限大に初期化
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # 開始点の距離は0
    # 各頂点の前の頂点を記録する辞書
    previous_vertices = {vertex: None for vertex in graph}
    # 優先度付きキューを初期化
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # 既に見た距離よりも長い場合はスキップ
        if current_distance > distances[current_vertex]:
            continue

        # 現在の頂点に隣接する頂点を見て、距離を更新
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # 新しい距離が現在の距離よりも短い場合、距離を更新
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_vertices

def shortest_path(graph, start, end):
    distances, previous_vertices = dijkstra(graph, start)
    path = []
    current_vertex = end

    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    
    path = path[::-1]  # 経路を逆にする

    if distances[end] == float('infinity'):
        return "経路が見つかりません"
    else:
        return path, distances[end]

def print_all_distances(distances):
    print("各頂点の始点からの最短距離:")
    for vertex, distance in distances.items():
        print(f"頂点 {vertex}: {distance}")

# グラフの例 (隣接リスト)
graph = {
    'v1': {'v2': 25, 'v3': 15},
    'v2': {'v1': 25, 'v3': 30, 'v4': 10, 'v6': 30},
    'v3': {'v1': 15, 'v2': 30, 'v6': 35},
    'v4': {'v2': 10, 'v5': 20, 'v7': 40},
    'v5': {'v4': 20, 'v7': 25},
    'v6': {'v2': 30, 'v3': 35, 'v7': 10},
    'v7': {'v4': 40, 'v5': 25, 'v6': 10}
}

start = 'v5'
distances, previous_vertices = dijkstra(graph, start)

# 各頂点の始点からの最短距離の出力
print_all_distances(distances)

# 'v5' から 'v1' への最短経路と距離の出力
end = 'v1'
path, distance = shortest_path(graph, start, end)
print(f"最短経路: {path}")
print(f"最短距離: {distance}")
