# info = {
#     "name":"anil",
#     "course":"csit",
#     "sub" : ["NM","CG","DSA"]
# }
# print(info)
# print(info["course"]) #displaying course only
# info["name"]="gyanu" #assigning new name
# print(info)

info1 = {
    "name":"anil",
    "course":"csit",
    "sub" : {
        "Numerical methods": 55,
        "Computer grapjics": 56,
        "DSA": 57
    }
}
print(info1)
print(info1["sub"])
print(info1["sub"]["DSA"])