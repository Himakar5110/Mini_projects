print("Answers asuming that you went to vist Zoo\n")

adjective1 = input("enter an adjective: ")
noun1 = input("enter a Name of an animal: ")
verb1 = input("enter a verb in past tense: ")
adverb1 = input("enter adverb: ")
adjective2 = input("enter second adjective: ")
noun2 = input("enter second noun: ")
noun3 = input("enter a name of second animal: ")
adjective3 = input("enter third adjective: ")
verb2 = input("enter a verb: ")
adverb2 = input("enter a adverb: ")
verb3 = input("enter a verb in past tense: ")
adjective4 = input("enter fourth adjective: ")

print("\nHere is your story\n")


line1  = "Today I went to the zoo. I saw an " + adjective1 + ' ' +noun1 + " jumping up and down in its tree.\n"
line2 = "He " + verb1 + ' ' + adverb1 + " through the large tunnel that led to its " + adjective2 + ' ' + noun2 + ".\n"
line3 = "I got some peanuts and passed them through the cage to a gigantic gray " + noun3 + " towering above my head.\n"
line4 = "Feeding that animal made me hungry. I went to get a " + adjective3 + " scoop of ice cream. It filled my stomach.\n"
line5 = "Afterwards I had to " + verb2 + ' ' + adverb2 + " to catch our bus.\n"
line6 = "when I got home I " + verb3 + " my mom for a " + adjective4 + " day at zoo"

story = line1+line2+line3+line4+line5+line6

print(story)
