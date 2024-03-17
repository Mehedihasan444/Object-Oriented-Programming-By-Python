# k=[1001,1002,1003,1004,1005]
# v=["USA","Canada","China","Japan","UK"]
# dis=dict()
# for i in range(len(k)):
#     dis[v[i]]=k[i]

# print(dis)

def lists_to_dict(keys,values):
    return dict(zip(keys,values))

k=[1001,1002,1003,1004,1005]
v=["USA","Canada","China","Japan","UK"]

print(lists_to_dict(v,k))


