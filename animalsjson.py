#import json file in the same directory, for animal details list
import json
with open('animals.json','r') as file:
    animals = json.load(file)


#load json data with read mode
def load_data():
    
    try:
        with open("animals.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {} 

#open json data with write mode
def save_data(data):
    with open("animals.json","w") as file:
        json.dump(data, file, indent=4)
        

#method to check if animal is in the data otherwise its added into it
def add_animal(newbie):
    animal_data = load_data()
    
    #animal_name = input ("Enter the name of the animal").lower().strip()
    
    animal_name = newbie
    
    if animal_name in animal_data:
        print(f"{animal_name.capitalize()} already exists in the dataset")
        
    else:
    
     animal_sound = input("Enter the sound of the animal: ").lower()
     animal_group = input("Enter the group of the animal: ").lower()
     animal_feature = input("Enter the feature of the animal: ").lower()
    
    animal_data[animal_name] = {
        
        "sound": animal_sound,
        "group": animal_group,
        "feature": animal_feature,
        
    }
    
    save_data(animal_data)
    
    print(f"{animal_name.capitalize()} has been added to the dataset")
    
    
            

def describe_animal(animal_input):

    animal_list = load_data()
    
    if animal_input in animal_list:
        
     animal_retrieve = animal_list[animal_input]
        
     sound = animal_retrieve["sound"]
     feature = animal_retrieve["feature"]
     group = animal_retrieve["group"]
    
     ##if sound and feature and group:
     print(f"A {animal_input} {sound}, has {feature}, and belongs to the {group} group")
    

    else:
        
      print(f"I dont know {animal_input} yet!")
      add_animal(animal_input)
        
    
    
def dialogue():
    
    user_input = input("Enter the name of the animal: ").lower().strip()
    
#    animal_data = user_input
    describe_animal(user_input)
 

if __name__ == "__main__":

   dialogue()




''''

#print(describe_animal(name))

animal_sounds = {
    
    "cat": "meows",
    "monkey": "ooo-ooo",
    "elephant": "trunks",
    "dog": "barks",
    "lion": "roars",
    "snake": "hisses",
    "eagle": "sqeauls",
    "falcon": "makes a falcon sound",
    "sparrow": "makes a sparrow sound",
    "shark": "makes a shark sound",

} 

animal_groups = {
    
    "cat": "mammal",
    "monkey": "mammal",
    "elephant": "mammal",
    "dog": "mammal",
    "eagle": "bird",
    "falcon": "bird",
    "sparrow": "bird",
    "shark": "fish",
}


animal_features = {
    
    "cat": "whiskers and cute paws",
    "monkey": "agile body and a tail",
    "elephant": "think skin and a trunk",
    "dog": "sharp teeth and a tail",
    "eagle": "white feathers and sharp eyes",
    "falcon": "golden beak and sharp legs",
    "sparrow": "small body and flexible wings",
    "shark": "heavy body and sharp teeth",
}





'''