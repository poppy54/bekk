# bekk
import random

# Quiz questions and options with correct answers
quiz = {
    "Mathematics": [
        {"question": "Solve for x: ?", "options": ["A) 4", "B) 6", "C) 7", "D) 8"], "answer": "C"},
        {"question": "Find the perimeter of a rectangle with length 12 cm and width 8 cm.", "options": ["A) 40 cm", "B) 24 cm", "C) 20 cm", "D) 16 cm"], "answer": "A"},
        {"question": "What is the derivative of ?", "options": ["A", "B", "C", "D"], "answer": "B"},
        {"question": "A die is rolled once. What is the probability of getting an even number?", "options": ["A) 1/2", "B) 1/3", "C) 2/3", "D) 1/6"], "answer": "A"},
        {"question": "Simplify: ?", "options": ["A) 11/12", "B) 1 1/8", "C) 7/8", "D) 9/8"], "answer": "C"}
    ],
    "Physics": [
        {"question": "Newton’s third law of motion states:", "options": ["A) Force = mass × acceleration", "B) Every action has an equal and opposite reaction", "C) Objects remain at rest unless acted upon", "D) Energy cannot be created or destroyed"], "answer": "B"},
        {"question": "A car accelerates from rest to 20 m/s in 10 seconds. What is its acceleration?", "options": ["A) 5 m/s²", "B) 2 m/s²", "C) 4 m/s²", "D) 10 m/s²"], "answer": "B"},
        {"question": "Kinetic energy is:", "options": ["A) Energy stored in an object", "B) Energy due to motion", "C) Energy from the sun", "D) Energy in chemical bonds"], "answer": "B"},
        {"question": "The SI unit of electric current is:", "options": ["A) Volt", "B) Ohm", "C) Ampere", "D) Watt"], "answer": "C"},
        {"question": "A ball is thrown upwards with a speed of 15 m/s. Time to reach maximum height is (g = 10 m/s²):", "options": ["A) 2.5 s", "B) 1.5 s", "C) 3 s", "D) 5 s"], "answer": "A"}
    ],
    "English": [
        {"question": "Synonym of 'generous' is:", "options": ["A) Mean", "B) Kind", "C) Angry", "D) Silent"], "answer": "B"},
        {"question": "Identify the verb: 'She quickly finished her homework.'", "options": ["A) She", "B) Quickly", "C) Finished", "D) Homework"], "answer": "C"},
        {"question": "Which sentence correctly uses 'although'?", "options": ["A) Although it rained, we played football.", "B) Although we went to market.", "C) I although like pizza.", "D) Although was hungry."], "answer": "A"},
        {"question": "Passive voice of 'The teacher explained the lesson':", "options": ["A) The lesson explained the teacher.", "B) The lesson was explained by the teacher.", "C) The teacher was explained by the lesson.", "D) The lesson is the teacher."], "answer": "B"},
        {"question": "'The stars danced in the sky' is an example of:", "options": ["A) Simile", "B) Metaphor", "C) Personification", "D) Hyperbole"], "answer": "C"}
    ],
    "Biology": [
        {"question": "The basic unit of life is:", "options": ["A) Atom", "B) Cell", "C) Tissue", "D) Organ"], "answer": "B"},
        {"question": "The process by which plants prepare food is called:", "options": ["A) Respiration", "B) Photosynthesis", "C) Transpiration", "D) Digestion"], "answer": "B"},
        {"question": "Osmosis is the movement of water molecules from:", "options": ["A) High to low concentration through a membrane", "B) Low to high concentration without a membrane", "C) High to low pressure in gases", "D) One cell to another without control"], "answer": "A"},
        {"question": "Which organ pumps blood throughout the body?", "options": ["A) Brain", "B) Heart", "C) Lungs", "D) Kidney"], "answer": "B"},
        {"question": "Plant cells differ from animal cells because they have:", "options": ["A) Nucleus", "B) Cell wall", "C) Cytoplasm", "D) Mitochondria"], "answer": "B"}
    ],
    "Chemistry": [
        {"question": "Chemical formula of water is:", "options": ["A) CO₂", "B) H₂O", "C) O₂", "D) H₂SO₄"], "answer": "B"},

{"question": "An acid is defined as a substance that:", "options": ["A) Releases hydroxide ions", "B) Releases hydrogen ions", "C) Accepts electrons", "D) Neutralizes bases only"], "answer": "B"},
        {"question": "Hydrochloric acid + Zinc → ? gas released:", "options": ["A) Oxygen", "B) Hydrogen", "C) Nitrogen", "D) Carbon dioxide"], "answer": "B"},
        {"question": "A property of noble gases is:", "options": ["A) Highly reactive", "B) Colorful flames", "C) Chemically inert", "D) Easily combined with metals"], "answer": "C"},
        {"question": "pH of a neutral solution is:", "options": ["A) 0", "B) 7", "C) 14", "D) 1"], "answer": "B"}
    ]
}

score = 0

print("Welcome to the 25-question Quiz!\n")

# Loop through subjects
for subject, questions in quiz.items():
    print(f"--- {subject} ---\n")
    random.shuffle(questions)  # Shuffle questions in each subject
    
    for q in questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        answer = input("Your answer (A/B/C/D): ").upper()
        if answer == q["answer"]:
            print("Correct! ✅\n")
            score += 1
        else:
            print(f"Wrong ❌. Correct answer: {q['answer']}\n")

print(f"Quiz Completed! Your final score: {score}/25")
