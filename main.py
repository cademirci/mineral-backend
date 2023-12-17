import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

def openai_question_answer(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ],
        temperature=0.7,
        max_tokens=30,
        n=1
    )
    return response['choices'][0]['message']['content'].strip()

if __name__ == "__main__":
    mineral_name = input("Enter Mineral Name: ")

    while True:
        type_selection = input(f"Please choose what you want to write for {mineral_name} (0 for poetry, 1 for story): ")

        if type_selection == "0":
            type = "poem"
            length = input(f"{type.capitalize()} Determine the number of quatrains: ")
            type1 = input(f"{type.capitalize()} Determine the genre: ")
            lang = input(f"{type.capitalize()} Determine your language: ")
            question = f"Can you write a {length} stanza {type} in {lang} about the {mineral_name} mineral, the subject of which is {type1}?"
            answer = openai_question_answer(question)
            break
        elif type_selection == "1":
            type = "story"
            length = input(f"{type.capitalize()} Specify the number of paragraphs:")
            type1 = input(f"{type.capitalize()} State the subject:")
            lang = input(f"{type.capitalize()} Please specify your language:")
            question = f"Can you write a {type} about the {mineral_name} mineral,{length} paragraph long, with a {type1} subject, in {lang}?"
            answer = openai_question_answer(question)
            break
        else:
            print("Invalid selection, Select again.")
            continue

    print("\nOpenAI API's Answer:")
    print(answer)
