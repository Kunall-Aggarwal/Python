a = {
    "Kunal": "Smart",
    "class":  10,
    "age": 20,
    "college": "Chitkara"
}

a["Kunal"] = ["Smart", "studious"]

print(a["harry"])
print(a.get("harry"))


print(a.keys())
print(a.values())
print(a.items())

b = {"ahfjajef": "afhje"}

a.update(b)
print(a.items())
