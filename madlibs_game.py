
print("Welcome to Mad Libs!")
print("-" * 40)


adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")
adjective2 = input("Enter another adjective: ")
noun2 = input("Enter another noun: ")
verb2 = input("Enter another verb (past tense): ")
adverb = input("Enter an adverb: ")
adjective3 = input("Enter one more adjective: ")

story = f"""
Once upon a time, there was a {adjective1} {noun1} that loved to {verb1}.
One day, it met a {adjective2} {noun2} who could {verb2} {adverb}.
Together, they had the most {adjective3} adventure ever!
"""

print("\n" + "-" * 40)
print("Here's your Mad Libs story:")
print("-" * 40)
print(story)