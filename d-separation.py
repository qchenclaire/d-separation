from argparse import ArgumentParser
import pdb
import copy
class Node(object):
    def __init__(self):
        self.parent_ids = set()
        self.child_ids = set()
    def add_parent(self, id):
        self.parent_ids.add(id)
    def add_child(self, id):
        self.child_ids.add(id)
    def get_parents(self):
        return self.parent_ids
    def get_children(self):
        return self.child_ids

def construct_BN(file):
    f = open(file)
    lines = f.readlines()
    n_nodes = len(lines[0].split(' '))
    bn = [Node() for i in range(n_nodes)]
    for i, line in enumerate(lines[1:]):
        edges = line.split(' ')[1:]
        for j in range(len(edges)):
            if '1' in edges[j]:
                bn[i].add_child(j)
                bn[j].add_parent(i)

    # for node in bn:
    #     print node.get_parents(), node.get_children()
    return bn

def reachable(bn, n1, n2, ob):
    #phase I: insert all ancestors of ob into A
    L = set(ob)
    A = set()
    while L:
        Y = L.pop()
        if not Y in A:
            L = L | bn[Y].get_parents()
        A.add(Y)
    #phase II: traverse active trails starting from n1
    L = set([(n1, 'up')])
    V = set()
    R = set()
    while L:
        (Y, d) = L.pop()
        if not (Y, d) in V:
            if not Y in set(ob):
                if Y == n2: return False
                R.add(Y)
            V.add((Y, d))
            if d == 'up' and not Y in ob:
                for Z in bn[Y].get_parents():
                    L.add((Z, 'up'))
                for Z in bn[Y].get_children():
                    L.add((Z, 'down'))
            elif d == 'down':
                if not Y in set(ob):
                    for Z in bn[Y].get_children():
                        L.add((Z, 'down'))
                if Y in A:
                    for Z in bn[Y].get_parents():
                        L.add((Z, 'up'))
    return True



#parse args
parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="file",
                    help="input bn file", metavar="FILE")
parser.add_argument("-n1", "--node1", dest="n1", help="first node",
                    type=int)
parser.add_argument("-n2", "--node2", dest="n2", help="second node",
                    type=int)
parser.add_argument("-ob", "--observations", dest="ob",help="observations, should be in the format of X1,X2, ...(no space)",
                    type=str)
args = parser.parse_args()
n1 = args.n1 - 1
n2 = args.n2 - 1
ob = map(int, args.ob.split(','))
ob = [i - 1 for i in ob]

assert (not n1 in ob), "node 1 should not appear in observations"
assert (not n2 in ob), "node 2 should not appear in observations"

bn = construct_BN(args.file)
print reachable(bn, n1, n2, ob)
