from flask import Flask, jsonify, render_template, request
import random

app = Flask(__name__)

# Your questions data (replace with your actual data)
questions_data = [
    {
        "question": "Marta Coll and colleagues’ 2010 Mediterranean Sea biodiversity census reported approximately 17,000 species, nearly double the number reported in Carlo Bianchi and Carla Morri’s 2000 census—a difference only partly attributable to the description of new invertebrate species in the interim. Another factor is that the morphological variability of microorganisms is poorly understood compared to that of vertebrates, invertebrates, plants, and algae, creating uncertainty about how to evaluate microorganisms as species. Researchers’ decisions on such matters therefore can be highly consequential. Indeed, the two censuses reported similar counts of vertebrate, plant, and algal species, suggesting that ______",
        "options": ["Coll and colleagues reported a much higher number of species than Bianchi and Morri did largely due to the inclusion of invertebrate species that had not been described at the time of Bianchi and Morri’s census.", "some differences observed in microorganisms may have been treated as variations within species by Bianchi and Morri but treated as indicative of distinct species by Coll and colleagues.", "Bianchi and Morri may have been less sensitive to the degree of morphological variation displayed within a typical species of microorganism than Coll and colleagues were.", "the absence of clarity regarding how to differentiate among species of microorganisms may have resulted in Coll and colleagues underestimating the number of microorganism species."],
        "correctAnswer": "some differences observed in microorganisms may have been treated as variations within species by Bianchi and Morri but treated as indicative of distinct species by Coll and colleagues.",
        "difficulty" : 3,
        "test" : "Reading and Writing",
        "questionAsk" : "Which choice most logically completes the text?"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correctAnswer": "Mars"
    },
    {
        "question": "Another question...",
        "options": ["Option1", "Option2", "Option3", "Option4"],
        "correctAnswer": "Option1"
    },
    # Add more questions here...
]

# Initialize the index to -1 to start with the first question
current_question_index = -1
user_score = 0  # Initialize the user's score

@app.route("/<name>")
def home(name):
    global current_question_index, user_score  # Declare global variables

    # Check if there are more questions, and if not, reset the index
    if current_question_index >= len(questions_data) - 1:
        current_question_index = -1  # Reset the index to start over

    # Increment the index to get the next question
    current_question_index += 1

    # Get the current question and its options
    current_question = questions_data[current_question_index]
    options = current_question["options"]

    # Shuffle the options randomly
    random.shuffle(options)

    return render_template('SATTEST.html', question=current_question["question"], options=options, user_score=user_score)

@app.route('/button_clicked', methods=['POST'])
def handle_button_click():
    global current_question_index, user_score  # Declare global variables
    data = request.get_json()
    current_question = questions_data[current_question_index]
    selected_option = data.get('selectedOption')
    print(current_question_index)
    print(f"Selected {selected_option}")
    correct_answer = current_question["correctAnswer"]# Replace with the actual correct answer value you're looking for
    print(f"Correct txt{correct_answer}")

    INDEX = 0
    finalINDEX = 0
    for i in current_question["options"]:
        INDEX = INDEX+1
        if str(i) == str(correct_answer):
            print("FOUND")
            finalINDEX = INDEX

    
    
    print(f"Correct {finalINDEX}")
    


    # Check if the selected option is correct
    if int(selected_option) == int(finalINDEX):
        user_score += 1
    print(user_score)
    # In this example, we'll simply return a new question and options
    current_question_index += 1
    if current_question_index == len(questions_data):
        current_question_index = 0
    current_question = questions_data[current_question_index]
    options = current_question["options"]
    question = current_question["question"]

    # Shuffle the options randomly
    random.shuffle(options)

    return jsonify({"question": question, "options": options, "user_score": user_score})

if __name__ == '__main__':
    app.run(debug=True)
