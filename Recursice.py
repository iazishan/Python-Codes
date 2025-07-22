import random
import re

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# -------------------------- Pattern Matching Engine ----------------------------

def is_variable(pattern):
    return (type(pattern) is str
            and pattern[0] == '?'
            and len(pattern) > 1
            and pattern[1] != '*'
            and pattern[1] in letters
            and ' ' not in pattern)

def is_segment(pattern):
    return (type(pattern) is list
            and pattern
            and len(pattern[0]) > 2
            and pattern[0][0] == '?'
            and pattern[0][1] == '*'
            and pattern[0][2] in letters
            and ' ' not in pattern[0])

def contains_tokens(pattern):
    return type(pattern) is list and len(pattern) > 0

def match_variable(var, replacement, bindings):
    binding = bindings.get(var)
    if not binding:
        bindings[var] = replacement
        return bindings
    if replacement == binding:
        return bindings
    return False

def match_segment(var, pattern, input, bindings):
    if not pattern:
        return match_variable(var, input, bindings)
    word = pattern[0]
    for i in range(len(input)):
        if input[i] == word:
            var_match = match_variable(var, input[:i], dict(bindings))
            match = match_pattern(pattern, input[i:], var_match)
            if match:
                return match
    return False

def match_pattern(pattern, input, bindings=None):
    if bindings is False:
        return False
    if pattern == input:
        return bindings
    bindings = bindings or {}

    if is_segment(pattern):
        token = pattern[0]
        var = token[2:]
        return match_segment(var, pattern[1:], input, bindings)
    elif is_variable(pattern):
        var = pattern[1:]
        return match_variable(var, [input], bindings)
    elif contains_tokens(pattern) and contains_tokens(input):
        first_match = match_pattern(pattern[0], input[0], bindings)
        return match_pattern(pattern[1:], input[1:], first_match)
    else:
        return False

def replace(word, replacements):
    for old, new in replacements:
        if word == old:
            return new
    return word

def switch_viewpoint(words):
    replacements = [
        ('I', 'YOU'), ('YOU', 'I'),
        ('ME', 'YOU'), ('MY', 'YOUR'),
        ('AM', 'ARE'), ('ARE', 'AM')
    ]
    return [replace(word, replacements) for word in words]

def respond(rules, input, default_responses):
    input = re.sub(r'[^\w\s]', '', input).upper().split()
    matching_rules = []
    for pattern, responses in rules:
        pattern = pattern.upper().split()
        bindings = match_pattern(pattern, input)
        if bindings:
            matching_rules.append((responses, bindings))

    if matching_rules:
        responses, bindings = random.choice(matching_rules)
        response = random.choice(responses)
    else:
        bindings = {}
        response = random.choice(default_responses)

    for variable, value in bindings.items():
        value = ' '.join(switch_viewpoint(value))
        if value:
            response = response.replace('?' + variable, value)
    return response

# --------------------------- ELIZA Runner (Generic) ----------------------------

def Eliza(prompt, rules, default_responses):
    print("Type 'exit' to quit.")
    while True:
        try:
            userinput = input(prompt)
            if userinput.strip().lower() == "exit":
                break
        except KeyboardInterrupt:
            break
        print(respond(rules, userinput, default_responses))

# ---------------------------- Scenario 1: Career Counseling ---------------------------

career_rules = [
    ("?*X I DON'T KNOW WHAT CAREER TO CHOOSE ?*Y", ["It's okay to be unsure. What are your interests?"]),
    ("?*X I NEED CAREER ADVICE ?*Y", ["Sure! What kind of jobs are you thinking about?"]),
    ("?*X I WANT TO CHANGE MY CAREER ?*Y", ["Why do you want to change your career?"]),
    ("?*X I LIKE SCIENCE ?*Y", ["There are many science careers. Do you like working in a lab or outside?"]),
    ("?*X I LIKE ART ?*Y", ["Art careers can be fun! Have you thought about design or painting?"]),
    ("?*X I WANT TO BE A DOCTOR ?*Y", ["That's a great goal. Are you ready for many years of study?"]),
    ("?*X I WANT TO BE AN ENGINEER ?*Y", ["Engineering is a good choice. What type of engineering interests you?"]),
    ("?*X I WANT TO BE A TEACHER ?*Y", ["Teaching is rewarding. What subject would you like to teach?"]),
    ("?*X I WANT TO WORK WITH COMPUTERS ?*Y", ["There are many computer jobs. Do you like coding or fixing computers?"]),
    ("?*X I AM CONFUSED ABOUT MY FUTURE ?*Y", ["It's normal to feel confused. What do you enjoy doing?"]),
    ("?*X I WANT TO HELP PEOPLE ?*Y", ["Helping people is great! Have you thought about healthcare or social work?"]),
    ("?*X I WANT TO EARN MORE MONEY ?*Y", ["Many jobs can help you earn well. What skills do you have?"]),
    ("?*X I WANT TO STUDY ABROAD ?*Y", ["Studying abroad is exciting. Which country interests you?"]),
    ("?*X I NEED MOTIVATION ?*Y", ["Think about your dreams and what makes you happy."]),
    ("?*X I FAILED AN EXAM ?*Y", ["Don't worry, everyone fails sometimes. What will you do differently next time?"]),
    ("?*X I WANT TO START A BUSINESS ?*Y", ["Starting a business is brave! What kind of business do you want?"]),
    ("?*X I LIKE HELPING OTHERS ?*Y", ["You could look into jobs like nursing, teaching, or counseling."]),
    ("?*X I WANT TO WORK FROM HOME ?*Y", ["Many jobs let you work from home, like writing or programming."]),
    ("?*X I WANT TO BE SUCCESSFUL ?*Y", ["Success comes with hard work. What does success mean to you?"]),
    ("?*X I AM GOOD AT MATH ?*Y", ["Great! You could look into jobs in finance, engineering, or data analysis."]),
]

career_default_responses = [
    "Can you tell me more about your career interests?",
    "What kind of work do you enjoy?",
    "Is there a job you have in mind?",
]

def run_career_counselor():
    Eliza("Career> ", career_rules, career_default_responses)

# ---------------------------- Scenario 2: Game Support ----------------------------

game_rules = [
    ("?*X I CAN'T PLAY ?*Y", ["Have you checked if the game is installed correctly?"]),
    ("?*X GAME ?Y CRASHING ?*Z", ["Update your graphics drivers."]),
    ("?*X GAME IS LAGGING ?*Y", ["Have you checked for updates?"]),
    ("?*X SYSTEM REQUIREMENTS ?*Y", ["You can check requirements on checkgamerrequirements.com"]),
    ("?*X GAME WON'T START ?*Y", ["Restart your PC or try running the game as administrator."]),
    ("?*X WHERE TO UPDATE ?*Y", ["You can update your game through the launcher or platforms like Steam, Epic Games, etc."]),
    ("?*X HOW TO INSTALL MODS ?*Y", ["You can usually install mods by downloading them and placing them in the game's mod folder."]),
    ("?*X HOW TO FIX GAME BUGS ?*Y", ["Check the game's official forums or support page for patches or fixes."]),
    ("?*X HOW TO REPORT A BUG ?*Y", ["You can report bugs through the game's official support page or forums."]),
    ("?*X GAME IS FREE ?*Y", ["Many games have free versions or demos available."]),
    ("?*X HOW TO UNINSTALL ?*Y", ["You can uninstall the game through your system's control panel or the game launcher."]),
    ("?*X GAME IS TOO HARD ?*Y", ["Have you tried looking for guides or walkthroughs online?"]),
    ("?*X HOW TO CHANGE SETTINGS ?*Y", ["You can usually change settings in the game's options menu."]),
    ("?*X GAME IS NOT LOADING ?*Y", ["Try verifying the game files through the game launcher."]),
    ("?*X HOW TO JOIN MULTIPLAYER ?*Y", ["You can join multiplayer by selecting the multiplayer option in the main menu."]),
    ("?*X HOW TO SAVE PROGRESS ?*Y", ["Most games save progress automatically, but you can also check the save options in the menu."]),
]

tech_default_responses = [
    "Can you describe your technical issue in more detail?",
    "I'm here to help with your computer problems.",
    "Please provide more information about the issue.",
]

def run_game_support():
    Eliza("TechSupport> ", game_rules, tech_default_responses)

# ------------------------- Choose scenario to run -------------------------

# Uncomment ONE of the following to test:
# run_career_counselor()
# run_game_support()
