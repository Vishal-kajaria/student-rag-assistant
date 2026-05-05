import json

# Load data from JSON file
def load_students():
    with open("data.json", "r") as file:
        return json.load(file)

# Retrieve students data based on user query
def retrieve_students(query,students):
    results = []
    query = query.lower()

    #extract number from query
    num = None
    for word in query.split():
        if word.isdigit():
            num = int(word)
        
    #above case
    if "above" in query and num is not None:
        for student in students:
            if student["marks"] > num:
                results.append(student)
    #below case
    elif "below" in query and num is not None:
        for student in students:
            if student["marks"] < num:
                results.append(student)
    #top case
    elif "top" in query:
        top_student = students[0]
        for student in students:
            if student["marks"] > top_student["marks"]:
                top_student = student
        results.append(top_student)
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