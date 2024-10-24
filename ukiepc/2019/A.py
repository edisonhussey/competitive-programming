class KDNode:
    def __init__(self, point, value, axis, left=None, right=None):
        self.point = point  # The point defining the region (x, y)
        self.value = value  # Value associated with the region
        self.axis = axis    # Splitting axis (0 = x-axis, 1 = y-axis)
        self.left = left    # Left subtree
        self.right = right  # Right subtree


class KDTree:
    def __init__(self):
        self.root = None

    def insert(self, point, value):
        """ Insert a point and its associated value into the KD-Tree. """
        self.root = self._insert(self.root, point, value, depth=0)

    def _insert(self, node, point, value, depth):
        if node is None:
            # Insert a new node at the correct location
            return KDNode(point, value, depth % 2)

        # Determine the axis to split (alternating between x and y)
        axis = depth % 2

        # Compare point on the current axis to decide the subtree
        if point[axis] < node.point[axis]:
            node.left = self._insert(node.left, point, value, depth + 1)
        else:
            node.right = self._insert(node.right, point, value, depth + 1)

        return node

    def query(self, point):
        """ Query the tree for the value associated with the point's region. """
        return self._query(self.root, point, depth=0)

    def _query(self, node, point, depth):
        if node is None:
            return None  # No value found for this region

        # If the point matches exactly, return its value
        if node.point == point:
            return node.value

        # Determine the axis
        axis = depth % 2

        # Compare point's coordinate with the current node's point along the axis
        if point[axis] < node.point[axis]:
            return self._query(node.left, point, depth + 1)
        else:
            return self._query(node.right, point, depth + 1)

    def update(self, point, value):
        """ Update the value in the region defined by point if it’s a new point between existing regions. """
        self.root = self._update(self.root, point, value, depth=0)

    def _update(self, node, point, value, depth):
        if node is None:
            # Insert a new region with the value if the point is not yet covered
            return KDNode(point, value, depth % 2)

        # If the point already defines a region, don't change its value
        if node.point == point:
            return node

        # Determine the axis to compare and update the region accordingly
        axis = depth % 2

        if point[axis] < node.point[axis]:
            node.left = self._update(node.left, point, value, depth + 1)
        else:
            node.right = self._update(node.right, point, value, depth + 1)

        return node

    def print_tree(self):
        """ Print the KD-Tree structure. """
        self._print_tree(self.root, depth=0)

    def _print_tree(self, node, depth):
        if node is not None:
            print("  " * depth + f"Point: {node.point}, Value: {node.value}, Axis: {node.axis}")
            self._print_tree(node.left, depth + 1)
            self._print_tree(node.right, depth + 1)


# Example usage:
kd_tree = KDTree()

s=int(input())
sum=0
# inserts=[]
for i in range(s):
    l0=list(int(x) for x in input().split())
    kd_tree.insert([l0[0],l0[1]], i+1)
    

coins=int(input())
for _ in range(coins):
    l0=list(int(x) for x in input().split())
    sum+=kd_tree.query([l0[0],l0[1]])
    
print(f"THe sum is {sum}\n")

# Insert points and their associated region values
# kd_tree.insert([3, 6], 10)
# kd_tree.insert([17, 15], 20)
# kd_tree.insert([13, 15], 25)
# kd_tree.insert([6, 12], 30)
# kd_tree.insert([9, 1], 35)
# kd_tree.insert([2, 7], 40)

print("KD-Tree structure after insertions:")
kd_tree.print_tree()

# Query the value of a specific point
# print("\nQuery value at point [3, 6]:", kd_tree.query([3, 6]))
# print("Query value at point [6, 12]:", kd_tree.query([6, 12]))

# Update value of a point between regions
kd_tree.update([4, 5], 50)

print("\nKD-Tree structure after update:")
kd_tree.print_tree()
