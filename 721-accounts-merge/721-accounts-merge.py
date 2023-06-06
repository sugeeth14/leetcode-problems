class Node:
    def __init__(self, email):
        self.email = email
        self.rank = 0
        self.name = ""
        self.parent = None
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        
        def find(node):
            if node.parent == node:
                return node
            else:
                parent = find(node.parent)
                node.parent = parent
                return node.parent
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            
            if parent1 == parent2:
                return
            if parent1.rank == parent2.rank:
                parent1.rank += 1
                parent2.parent = parent1
            elif parent1.rank > parent2.rank:
                parent2.parent = parent1
            else:
                parent1.parent = parent2
        
        node_map = {}
        for account in accounts:
            name, first_email = account[0], account[1]
            if first_email not in node_map:
                node = Node(first_email)
                node.name = name
                node.parent = node
                node_map[first_email] = node
        
            for email in account[2:]:
                if email not in node_map:
                    # create a node for it
                    node = Node(email)
                    node.name = name
                    node.parent = node
                    node_map[email] = node
                union(node_map[first_email], node_map[email])
        
        # print(node_map)
        # for node in node_map:
        #     print(node, node_map[node].parent.email)
        for node in node_map:
            parent = find(node_map[node].parent)
            node_map[node].parent = parent
        email_lists = {}
        for email in node_map:
            name, parent_email = node_map[email].name, node_map[email].parent.email
            if (name, parent_email) in email_lists:
                email_lists[(name, parent_email)].append(email)
            else:
                email_lists[(name, parent_email)] = [email]
        
        for key in email_lists:
            email_lists[key].sort()
        # print(email_lists)
        res = []
        for key in email_lists:
            temp = [key[0]] + email_lists[key]
            res.append(temp)
        return res
        
        
        