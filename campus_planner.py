# Campus Navigation & Utility Planner - Python implementation
# Implements Building ADT, BST, AVL, Graph (adj list + matrix), BFS/DFS, Dijkstra, Kruskal, ExpressionTree
# Run this script to see demonstrations.

from collections import deque, defaultdict
import heapq
import math

# -------------------------
# Building ADT
# -------------------------
class Building:
    def __init__(self, bid: int, name: str, location: str):
        self.id = bid
        self.name = name
        self.location = location
        self.connections = {}  # dict target_id -> weight (distance)

    def add_connection(self, other_id: int, distance: float):
        self.connections[other_id] = distance

    def __str__(self):
        return f"[{self.id}] {self.name} ({self.location})"

# -------------------------
# Binary Search Tree (BST)
# -------------------------
class BSTNode:
    def __init__(self, building: Building):
        self.building = building
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, building: Building):
        def _insert(node, b):
            if node is None:
                return BSTNode(b)
            if b.id < node.building.id:
                node.left = _insert(node.left, b)
            elif b.id > node.building.id:
                node.right = _insert(node.right, b)
            else:
                # duplicate id - update
                node.building = b
            return node
        self.root = _insert(self.root, building)

    def search(self, bid: int):
        node = self.root
        while node:
            if bid == node.building.id:
                return node.building
            if bid < node.building.id:
                node = node.left
            else:
                node = node.right
        return None

    def inorder(self):
        res = []
        def _in(node):
            if not node: return
            _in(node.left)
            res.append(node.building)
            _in(node.right)
        _in(self.root)
        return res

    def preorder(self):
        res = []
        def _pre(node):
            if not node: return
            res.append(node.building)
            _pre(node.left)
            _pre(node.right)
        _pre(self.root)
        return res

    def postorder(self):
        res = []
        def _post(node):
            if not node: return
            _post(node.left)
            _post(node.right)
            res.append(node.building)
        _post(self.root)
        return res

    def height(self):
        def _h(node):
            if not node: return 0
            return 1 + max(_h(node.left), _h(node.right))
        return _h(self.root)

# -------------------------
# AVL Tree
# -------------------------
class AVLNode:
    def __init__(self, building: Building):
        self.building = building
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        return node.height if node else 0

    def _update_height(self, node):
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right)
