from bardapi import Bard
import os

os.environ["_BARD_API_KEY"] ="dwgdqmk_nqZKrSOThDpnvwNeaCSbFU5AToVBJpVv8KOqzaSwgrUM7vFgORWH5MpW_0SwQw."

def bard_question_answer(question):
    bard = Bard()
    answer = bard.get_answer(question)
    return answer["content"]

if __name__ == "__main__":
    mineral_name = input("Enter Mineral Name:")
    
    while True:
        type_selection = input(f"Please choose what you want to write for {mineral_name} (0 for poetry, 1 for story): ")  

        if type_selection == "0":
            type= "poem"
            length = input(f"{type.capitalize()} Determine the number of quatrains: ")
            type1 = input(f"{type.capitalize()} Determine the genre: ")
            lang = input(f"{type.capitalize()} Determine your language: ") 
            question =f"Can you write a {length} stanza {type} in {lang}   about the {mineral_name} mineral,the subject of which is {type1}?"
            answer = bard_question_answer(question)
            break
        elif type_selection == "1":
            type = "story"            
            length = input(f"{type.capitalize()} Specify the number of paragraphs:")
            type1 = input(f"{type.capitalize()} State the subject:")
            lang = input(f"{type.capitalize()} Please specify your language:") 
            question = f"Can you write a {type} about the {mineral_name} mineral,{length} paragraph long, with a {type1} subject, in {lang}?"
            answer = bard_question_answer(question)
            break
        else:
         print("Invalid selection,Select again.")
         continue


    print("\nBard API's Answer:")
    print(answer)

