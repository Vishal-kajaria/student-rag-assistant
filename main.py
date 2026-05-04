students=[
    {"id":1,"name":"Alice","marks": 85},
    {"id":2,"name":"Bob","marks":90},
    {"id":3,"name":"Charlie","marks":78}
]

query = "Show students with marks above 80"

context = ""

for s in students:
    if s["marks"] > 80:
        context += f"{s['name']} scored {s['marks']} marks.\n"

print("Query:", query)
print("Context:\n", context)

print("Final Answer:")
if context:
    print("Students who scored above 80 are:\n", context)
else:
    print("No students found.")