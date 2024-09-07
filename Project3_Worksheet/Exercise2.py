'''
2. Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a
name, return the relation of that person to Luke.

Person
Relation
Darth Vader father
Leia sister
Han brother in law
R2D2 droid

Example : relation_to_luke("Darth Vader") ➞ "Luke, I am your father."
'''



def relation_to_luke(name):
    # Dictionary containing names and their relations to Luke
    relations = {
        "Darth Vader": "father",
        "Leia": "sister",
        "Han": "brother in law",
        "R2D2": "droid"
    }
    
    # Check if the name is in the relations dictionary
    if name in relations:
        return f"Luke, I am your {relations[name]}."
    else:
        return "Relation not found."

# Example usage
print(relation_to_luke("Darth Vader")) 
print(relation_to_luke("Leia"))         
print(relation_to_luke("Han"))          
print(relation_to_luke("R2D2"))       
