# Step 1: Get user inputs
adj1 = input("Enter an adjective: ")
adj2 = input("Enter another adjective: ")
adj3 = input("Enter a third adjective: ")
adj4 = input("Enter one last adjective: ")
animal = input("Name an animal: ")
feeling = input("How did it make you feel (e.g., amazed, scared)? ")

# Step 2: Conditional variation
if animal.lower() == "elephant":
    extra_sentence = "It sprayed water all over the crowd!"
elif animal.lower() == "lion":
    extra_sentence = "It roared so loud that everyone jumped!"
else:
    extra_sentence = f"It looked very {adj4} and unique."

# Step 3: Build and print the story
print("\n--- Your Mad Libs Story ---\n")
print(f"On a beautiful {adj1} day, I went to the zoo.")
print(f"I saw a funny {adj2} monkey swinging from the trees.")
print(f"Then, I spotted a majestic {adj3} {animal} lounging in the sun.")
print(extra_sentence)
print(f"What a wild and {adj4} experience! I felt so {feeling} afterward.")
