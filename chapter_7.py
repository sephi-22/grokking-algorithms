# This is the implementation of Djikstra's Algorithm
# We need three hash tables, one for graph, one for costs, and one for parents

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}  # It has no neighbors

# Now we need to store costs in another hash table. The costs of a node is how long it takes to get to that node from the start.

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# We need another hash table for the parents
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# We need an array to keep track of nodes we've already processed.
# We do not process a node more than once

processed = []
print("Before running the algorithm the costs are: " + str(costs))

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # Go through each node
        cost = costs[node]
        if (
            cost < lowest_cost and node not in processed
        ):  # It's the lowest cost so far and hasn't been processed yet
            lowest_cost = cost  # Set it as the new lowest-cost node.
            lowest_cost_node = node
    return lowest_cost_node


# Algorithm code
node = find_lowest_cost_node(
    costs
)  # Find the lowest-cost node that you haven't processed yet.
while node is not None:  # If you've processed all the nodes, the while loop is done
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  # Go through all the neighbors of this node
        new_cost = cost + neighbors[n]  # If its cheaper to get to this neigghbor
        if costs[n] > new_cost:  # by going through this node
            costs[n] = new_cost  # Update the cost for this node
            parents[n] = node  # This node becomes the new parent for this neighbor
    processed.append(node)  # Mark the node as processed
    node = find_lowest_cost_node(costs)  # Find the next node to process, and loop.

print("After running the algorithm the costs are: " + str(costs))
