""" 
Follow up of an interview question

given integer pair (a,b), check if (c,d) can be made up of adding up both sides
"""
# #%%
# def adduper(a,b,dir = 'b'): #direction either left for right
#     assert dir == 'b' or dir == 'a', "Insert valid direction either 'b' or 'a' "

#     if dir == 'b':
#         b = a+b

#     if dir == 'a':
#         a = a+b
    
#     return a,b


# def isPossible(a,b,c,d): 
#     if a == c:
#         if b == d:
#             return 'Yes'
#     elif b == d:
#         A = a
#         while A < c:
#            A,b  = adduper(a,b,dir='a')
#         if A == C:
# #             return 'Yes'

    

#     return 'No'


#%%
        


#test cases 
# (1,1), (5,2) yes
# (1,4) (5,9) yes        

#%%
def isPossible(a,b,c,d):
    A = c
    B = d

    while A > a or B > b:
        if A > B:
            A -= B
        elif A < B:
            B -= A
        else:
            return 'No'
        
        print("(", A, ",", B, ")")

    if A == a and B == b:
        return 'Yes'
    else:
        return 'No'
#%%