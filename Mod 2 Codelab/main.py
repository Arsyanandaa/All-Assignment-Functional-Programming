import copy

user = {"name" : "putri", "scores" : [90,85]}
user_shallow = copy.copy(user)
user_deep = copy.deepcopy(user)

user_shallow["scores"][0] = 75
user_deep["scores"][0] = 75

print("Yang Menggunakan Shallow copy : ", user_shallow)
print("yang Menggunakan Deep copy : ", user_deep)

print("\nUser asli :", user)

print("\nID user['scores'][0]         :", id(user["scores"][0]))
print("ID user_shallow['scores'][0] :", id(user_shallow["scores"][0]))
print("ID user_deep['scores'][0]    :", id(user_deep["scores"][0]))
