#myDicit.keys()
student = {
    "name" : "rahul",
    "subject" : {
        "chem" : 75,
        "phy" : 85,
        "bio" : 65
    }
}

print(student.keys())


#myDicit.values()
student = {
    "name" : "rahul",
    "subject" : {
        "chem" : 75,
        "phy" : 85,
        "bio" : 65
    }
}
print(student.values())



#myDicit.items()
student = {
    "name" : "rahul",
    "subject" : {
        "chem" : 75,
        "phy" : 85,
        "bio" : 65
    }
}
print(student.items())




#myDicit.get("key")
student = {
    "name" : "rahul",
    "subject" : {
        "chem" : 75,
        "phy" : 85,
        "bio" : 65
    }
}
print(student["name"])
print(student.get("name"))


#myDicit.updet()
student = {
    "name" : "rahul",
    "subject" : {
        "chem" : 75,
        "phy" : 85,
        "bio" : 65
    }
}
student.update({"city" :"bolpur"})
print(student)