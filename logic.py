from Levenstein_distance import levenstein_dist
import numpy as np
# def func(i,j,m,n,ele,D_final):
#     mi = 18999901
#     for l in D_final[ele[m:n]]:
#         if len(l)>len(ele[i:j]):
#             if mi == 1:
#                 break
#             else:
                
#                 mi = min(mi,levenstein_dist(ele[i:j],l))
    
#     return mi

def logic_elements(ele,D_final):
    if ele in D_final[ele[0:3]]:
        return ele
    m,n=0,3
    i,j = 0,3
    first = False
    count = 0
    L = []
    while i<len(ele) and j<len(ele):
        if not D_final[ele[m:n]]:
                m += 1
                n += 1
                i = m
                j = n
                if ele[m:] in D_final[ele[m:n]]:
                    return ele[m:]
                else:
                    continue
        if ele[i:j] in D_final[ele[m:n]]:
            if ele[j:] in D_final[ele[j:j+3]]:
                L.append(ele[i:j])
                L.append(ele[j:])
                break
            
            p = ele[i:j]
            print(p)
            rec_2 = j
            print("i:",i)
            count = 0
            first = True
            #mi = func(i,j,m,n,ele,D_final)
            j += 1
            print("j:",j)
        else:
            if first:
                count += 1
                if len(ele[rec_2:])<=3:
                    if count == 1:
                        L.append(p)
                        m = i = rec_2
                        n = j = rec_2+3
                else:
                    if count == (len(ele[rec_2:])//2)-1:
                        L.append(p)
                        m = i = rec_2
                        n = j = rec_2+3
            
            mi = 18999901
            for l in D_final[ele[m:n]]:
                if len(l)>len(ele[i:j]):
                    if mi == 1:
                        break
                    else:
                        mi = min(mi,levenstein_dist(ele[i:j],l))

            j += int(mi)
            
    else:
        L.append(ele[i:j])
    return L
