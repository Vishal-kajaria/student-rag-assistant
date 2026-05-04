import json

# Load data from JSON file
def load_students():
    with open("data.json", "r") as file:
        return json.load(file)

# Retrieve students data based on user query
def retrieve_students(query,students):
    results = []
    if "top" in query:
        top_student = students[0]
        for s in students:
            if s["marks"] > top_student["marks"]:
                top_student = s
        results.append(top_student)
    
    for student in students:
        if "above" in query and student["marks"] > 80:
            results.append(student)
        elif "below" in query and student["marks"] < 70:
            results.append(student)

    return results


#Build context for RAG 
def build_context(results):
    context = ""
    for student in results:
        context += f"Name: {student['name']} scored Marks: {student['marks']}\n"
    return context

#Generate response based on context
def generate_response(context):
    if context:
        return f"Here are the students matching your query:\n{context}"
    else:
        return "No students found matching your query."

# Main function to run the RAG assistant
def main():
    students= load_students()
    query = input("Enter your query (e.g., 'Show students above 80 marks'): ").lower()
    results = retrieve_students(query,students)
    context = build_context(results)
    response = generate_response(context)

    print("Final Response:")
    print(response)

if __name__ == "__main__":
    main()