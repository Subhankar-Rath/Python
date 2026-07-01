info={
    "name":"subhankar",
    "cgpa":7.2,
    "subject":["math","phy"],
    3.14:"PI",

}
info["subject"].append("chem")
info["sgpa"]=info["cgpa"]
del info["name"] #unique thing that is discovered
del info[3.14]
print(info)