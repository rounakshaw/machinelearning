from collections import deque


def input_data():
    n = int(input("n: "))
    e = int(input("e: "))

    start = list(map(int, input("from: ").split(",")))
    end = list(map(int, input("to: ").split(",")))

    value = list(map(int, input("value: ").split(",")))

    return n, e, start, end, value


def bfs(adj_list, u, v, value):
    res = value[u]
    q = deque()
    q.append(u)
    visited = set()

    while len(q) != 0:
        # print(q[0]) (used for debugging)
        vertex_idx = q.popleft()
        if vertex_idx in visited:
            continue
        visited.add(vertex_idx)

        res = res & value[vertex_idx]
        for vertex in adj_list[vertex_idx]:
            if vertex == v:
                continue
            q.append(vertex)

    return res


def main():
    # accepting input
    n, e, start, end, value = input_data()

    # adjacent list representation of the given tree
    adj_list = [[] for i in range(n)]

    for idx in range(e):
        adj_list[start[idx]].append(end[idx])
        adj_list[end[idx]].append(start[idx])

    # calculate count
    count = 0
    s = set()
    for u in range(len(adj_list)):
        for v in adj_list[u]:
            if v in s:
                continue

            s.add(v)
            # print(u, v) (used for debugging)
            res1 = bfs(adj_list, u, v, value)
            res2 = bfs(adj_list, v, u, value)
            # print("res1: ",res1) (used for debugging)
            # print("res2: ",res2) (used for debugging)
            if res1 == res2:
                count = count + 1

        s.add(u)

    # print count
    print("total no. of ways: ", count)


# program execution starts here
if __name__=="__main__":
    main()
