class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        visited = set()
        supplies = set(supplies)
        # print(supplies)
        children = {}
        for i in range(len(recipes)):
            children[recipes[i]] = ingredients[i]
        # print(children)
        
        def top_sort(node):
            # print(node)
            if node in visited and node not in supplies:
                return 0
            elif node in supplies:
                return 1
            else:
                visited.add(node)
                count = 0
                if node not in children:
                    return 0
                for child in children[node]:
                    count += top_sort(child)
                # print(node, count)
                if count == len(children[node]):
                    supplies.add(node)
                    return 1
                else:
                    return 0
        res = []
        # print(supplies)
        for node in children:
            if node not in visited:
                top_sort(node)
            if node in supplies:
                res.append(node)
        return res
                    
        