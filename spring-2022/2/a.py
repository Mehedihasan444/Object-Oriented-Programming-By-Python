country_list=["India","Thailand","Bhutan","China","Nepal","Myanmar"]
# country_list.remove("Myanmar")
# print(country_list)
for country in country_list:
    if country=="Myanmar":
        continue
    print(country,",",end=" ")