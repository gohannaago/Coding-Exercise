def sExpression(nodes):
    print(nodes)
    # Write your code here
    pairs = nodes.split(' ')
    par = list(map(tuple, nodes.replace(',','').replace('(','').replace(')','').split(' ')))
    
    # create dict and organise parent child pairs
    tree = {}

    for i in range(len(par)):
        # print("".join(pairs[i]))
        parent, child = par[i]
        if parent in tree:
            tree[parent].append(child)
        else:
            tree[parent] = [child]
        
    return tree

#%%
print(sExpression("(A,B) (A,C) (B,G) (C,D) (C,E) (D,F)"))