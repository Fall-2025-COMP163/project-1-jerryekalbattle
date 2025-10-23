"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Jerryeka Battle
Date: 10/21/2025

AI Usage: Use ai to see how to format def calculate_stats i changed most of what ai gave me to add more stats to fit my added points
"""

def create_character(name, character_class, heritage=" ")):
    level = 1
    gold = 100
    if heritage.strip() != '':
        gold += 100
    strength, magic, health = calculate_stats(character_class, level)
    new_character = {
        "name": name,
        "class": character_class.capitalize(),
        "heritage": heritage,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }
    return new_character

    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    pass

def calculate_stats(character_class, level):
    strength = 10
    dexterity = 17
    magic = 4
    health = 10
    intelligence = 16
    wisdom = 14
    charisma = 18
    if character_class.lower() == "warrior":
        strength += 6
        magic += 0
        health += 2
    elif character_class.lower() == "mage":
        strength += 2
        magic += 10
        health += 4
    elif character_class.lower() == "rogue":
        strength += 2
        magic += 3
        health += 1
    elif character_class.lower() == "cleric":
        strength += 1
        magic += 4
        health += 1
    elif character_class.lower() == "Alchemist":
        strength += 1
        magic += 5
        health += 1
    else:
        print("Invalid class! Defaulting to Warrior.")
        character_class = 'warrior'
        strength += 6
        magic += 0
        health += 2
    return (strength, magic, health)

    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    pass

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    pass

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    pass

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    name = input("Enter your character's name: ")
    heritage = input("Enter your character's heritage (any or ' '):")
    character_class = input("Choose your class (Warrior, Mage, Rogue, Cleric, Alchemist): ")
    new_character = create_character(name, character_class)
    print("=== CHARACTER CREATOR ===")
    for key, value in new_character.items():
        print(f"{key.capitalize()}: {value}")
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
