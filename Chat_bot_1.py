import json
from difflib import get_close_matches
import typing

# Load the knowledge base from a JSON file
def load_knowledge_base(file_path: str):
    #This function specifically is going to read the data in the given json file and return the already fed data in a dictionary form
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

# Save the updated knowledge base to the JSON file
def save_knowledge_base(file_path: str, data: dict):
    #This function saves the updated knowledge base (provided as a dictionary) to the JSON file specified by file_path.
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


# Find the closest matching question
def find_best_match(user_question: str, questions: list[str]) -> typing.Optional[str]:
    #This function finds the closest matching question in the knowledge base for the user's input question.
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.7)
    return matches[0] if matches else None


def get_answer_for_question(question: str, knowledge_base: dict) -> typing.Optional[str]:
    #Search for the answer in the knowledge base and get the answer.
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None


def chatbot():
    
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    while True:
        user_input: str = input("You: ")

        if user_input.lower() == 'quit':
            break

        # Finds the best match, if there is a match it stores it in itself , otherwise returns None
        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            # If there is a best match, return the answer from the knowledge base
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f"Bro: {answer}")
        else:
            print("Bro: I don't know the answer. Can you enlighten me?")
            new_answer: str = input("Type the answer or type 'skip' to skip: ")

            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print("Bro: Thank you! I know what to do next time now .")


if __name__ == "__main__":
    chatbot()