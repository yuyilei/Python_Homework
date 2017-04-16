def find_lowest_cost_node(costs) :
    lowest = float("inf")
    lowest_node = None
    for cost in costs :
        cost = costs[node]
        if cost < lowest and node not  in processed :
            lowest = cost
            lowest_node = node
    return lowest_node


if __name__ == '__main__' :
    node = find_lowest_code(costs)
    while node is not None :
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys() :
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost :
                costs[n] = new_cost
                parent[n] = node

        processed.append(node)
        node =find_lowest_cost_node(costs)
