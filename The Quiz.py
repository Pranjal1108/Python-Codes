class people():
    def __init__(self, name, id):
        self.name = name
        self.id= id
        self.score = 0

person1 = people(
    str(input("Enter your Name: ")),
    input("Enter your ID: ")
)

print(" ")

to_enter = (str(input("Enter the Quiz? (yes/no): ")))
if to_enter == "yes":

    choose_subject = input("Choose the Topic for the Quiz from Space, OOPS, Environmental Impact Analysis(write eia for this), ( write in small letters) : ")
    if choose_subject == "space":


        print(" ")
        Question_1 = "Question: what is the name of the our moon?"
        choices_1 = ["a. callisto", "b. luna" , "c. beetlejuice", "d. andromeda"]
        print(Question_1)
        for i in choices_1:
            print(i)

        your_choice_1 = input("Chose The option: ")
 
        if your_choice_1 == "b":
            print("Correct!")
            person1.score += 1
        else:
            print("wrong!")

        print(" ")

        Question_2 = "Question: what is the name of the our nearest galaxy?"
        choices_2 = ["a. callisto", "b. luna" , "c. beetlejuice", "d. andromeda"]
        print(Question_2)
        for i in choices_2:
            print(i)

        your_choice_2 = input("Chose The option: ")


        if your_choice_2 == "d":
            print("Correct!")
            person1.score += 1
        else:
            print("wrong!")

        print(" ")

        Question_3 = "Question: which of these option is a star?"
        choices_3 = ["a. callisto", "b. luna" , "c. beetlejuice", "d. andromeda"]
        print(Question_3)
        for i in choices_3:
            print(i)

        your_choice_3 = input("Chose The option: ")


        if your_choice_3 == "c":
            print("Correct!")
            person1.score += 1
        else:
            print("wrong!")

        print(" ")

        Question_4 = "Question: which of these option is a moon of planet saturn?"
        choices_4 = ["a. callisto", "b. luna" , "c. beetlejuice", "d. andromeda"]
        print(Question_4)
        for i in choices_4:
            print(i)

        your_choice_4 = input("Chose The option: ")


        if your_choice_4 == "a":
            print("Correct!")
            person1.score += 1    
        else:
            print("wrong!")

        print(" ")

    elif choose_subject == "oops":

        print(" ")    
        oops_question1 = "Question: What is the main principle of object-oriented programming?"
        oops_choices1 = ["a. Inheritance", "b. Encapsulation", "c. Abstraction", "f.Polymorphism"]

        print(oops_question1)
        for i in oops_choices1:
            print(i)
        
        your_oops1 = input("Choose your Option: ")

        
        if your_oops1 == "b":
            print("Correct")
            person1.score += 1 
        else:
            print("Wrong!")

        print(" ")

        oops_question2 = "Question: In Python, which keyword is used to create a class?"
        oops_choices2 = ["a. class", "b. def", "c. Class", "d. cls"]

        print(oops_question2)
        for i in oops_choices2:
            print(i)

        your_oops2 = input("Choose your Option: ")


        if your_oops2 == "a":
            print("Correct")
            person1.score += 1
        else:
            print("Wrong!")

        print(" ")

        oops_question3 = "Question: Which of the following is a correct way to create an instance of a class in Python?"
        oops_choices3 = ["a. obj = MyClass()", "b. obj = new MyClass()", "c. obj = create MyClass()", "d. obj = instance MyClass()"]
        
        print(oops_question3)
        for i in oops_choices3:
            print(i)

        your_oops3 = input("Choose your Option: ")

        if your_oops3 == "a":
            print("Correct")
            person1.score += 1
        else:
            print("Wrong!")

        print(" ")
        
        oops_question4 = "Question: What is the first parameter that instance methods in Python should take by convention?"
        oops_choices4  = ["a. self", "b. this", "c. obj", "d. instance"]

        print(oops_question4)
        for i in oops_choices4:
            print(i)

        your_oops4 = input("Choose your Option: ")
            
        if your_oops4 == "a":
            print("Correct")
            person1.score += 1
        else:
            print("Wrong!")

    elif choose_subject == "eia":
        print(" ")

        eia_question1 = "Question: What is the primary goal of conducting an environmental impact analysis?"
        eia_choices1 = ["a. Identifying potential environmental effects", "b. Maximizing profits", "c. Minimizing regulatory compliance", "d. Ignoring ecological concerns"]

        print(eia_question1)
        for i in eia_choices1:
            print(i)
        
        your_eia1 = input("Choose your Option: ")

        if your_eia1 == "a":
            print("Correct")
            person1.score += 1
        else:
            print("Wrong!")
        
        eia_question2 = "Which of the following is a common method used in environmental impact analysis?"
        eia_choices2 = ["a. Life Cycle Assessment (LCA)", "b. Economic forecasting", "c. Political lobbying", "d. Social media analysis"]

        print(eia_question2)
        for i in eia_choices2:
            print(i)

        your_eia2 = input("Choose your Option: ")
        if your_eia2 == "a":
            print("Correct")
            person1.score += 1
        else:
            print("Wrong!")


        eia_question3 = "What is one of the key considerations in assessing the environmental impact of a project?"
        eia_choices3 = ["a. Carbon emissions", "b. Employee satisfaction", "c. Marketing strategies", "d. Executive bonuses"]

        print(eia_question3)
        for i in eia_choices3:
            print(i)

        your_eia3 = input("Choose your Option: ")
        if your_eia3 == "a":
            print("Correct")
            person1.score += 1
        else:
            print("Wrong!")
        
        eia_question4 = "What role do stakeholders play in environmental impact analysis?"
        eia_choices4 = ["a. Providing financial incentives", "b. Ignoring environmental concerns", "c. Identifying potential impacts", "d. Avoiding public engagement"]

        print(eia_question4)
        for i in eia_choices4:
            print(i)

        your_eia4 = input("Choose your Option: ")
        if your_eia4 == "c":
            print("Correct")
            person1.score += 1
        else:
            print("Wrong!")

else:
    pass

show_result = input("Do you want to check your result? (yes/no): ") 
print(" ")
if show_result == "yes":
    print(f"{person1.name} got a score {person1.score} out of 4")

    if person1.score < 3:
        print("You Fail")
    else:
        print("You pass")

else:
    pass