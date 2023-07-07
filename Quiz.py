class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.answers = []
        self.score = 0
        self.current_question = 0
        self.max_marks = 10

    def display_question(self):
        question = self.questions[self.current_question]
        print(f"Question {self.current_question + 1}: {question['question']}")
        print("Options:")
        for i, option in enumerate(question['options']):
            print(f"{chr(97 + i)}) {option}")
        print()

    def get_answer(self):
        while True:
            answer = input("Enter your answer (a, b, c, d): ").lower()
            if answer in ['a', 'b', 'c', 'd']:
                return answer
            else:
                print("Invalid answer. Please try again.")

    def check_answer(self, answer):
        question = self.questions[self.current_question]
        correct_answer = question['answer']
        self.answers.append(answer)
        if answer == correct_answer:
            self.score += 1

    def next_question(self):
        self.current_question += 1

    def display_results(self):
        print("Quiz Results:")
        print("-------------")
        for i, question in enumerate(self.questions):
            print(f"Question {i + 1}: {question['question']}")
            print(f"Your answer: {self.answers[i]}")
            print(f"Correct answer: {question['answer']}")
            print()
        print(f"Total Score: {self.score}/{self.max_marks}")
        print(f"Result: {self.get_result()}")

    def get_result(self):
        percentage = (self.score / self.max_marks) * 100
        if percentage >= 90:
            return "Excellent"
        elif percentage >= 70:
            return "Above Average"
        elif percentage >= 50:
            return "Average"
        elif percentage >= 30:
            return "Below Average"
        else:
            return "Poor"


questions = [
    {
        'question': "Which component of JMeter is responsible for sending requests to the server and receiving responses?",
        'options': ["Sampler", "Listener", "Timer", "Controller"],
        'answer': "a"
    },
    {
        'question': "What is the purpose of the Thread Group in JMeter?",
        'options': ["It defines the number of threads/users for the test.", "It generates random test data for parameterization.", "It generates HTML reports for test results.", "It defines the duration of the test."],
        'answer': "a"
    },
    {
        'question': "Which option is used to run JMeter scripts in non-GUI mode?",
        'options': ["-g", "-n", "-t", "-r"],
        'answer': "b"
    },
    {
        'question': "Which JMeter component is used to extract data from server responses for correlation?",
        'options': ["Controller", "Timer", "Post-Processor", "Pre-Processor"],
        'answer': "c"
    },
    {
        'question': "What is the purpose of the Constant Timer in JMeter?",
        'options': ["It adds a constant delay between requests.", "It defines the maximum response time allowed for a request.", "It measures the average response time for a request.", "It pauses the test execution for a fixed duration."],
        'answer': "a"
    },
    {
        'question': "Which assertion in JMeter is used to validate the presence of a specific text in the server response?",
        'options': ["Response Assertion", "Duration Assertion", "Size Assertion", "XPath Assertion"],
        'answer': "a"
    },
    {
        'question': "What does the 'ramp-up' period in JMeter signify?",
        'options': ["The time taken to start all the threads in the test.", "The time taken to increase the load gradually during the test.", "The time taken to shut down the JMeter server.", "The time taken to collect and analyze test results."],
        'answer': "b"
    },
    {
        'question': "Which listener in JMeter is used to generate HTML reports for test results?",
        'options': ["Aggregate Report", "Summary Report", "View Results Tree", "HTML Report Dashboard"],
        'answer': "d"
    },
    {
        'question': "Which JMeter component is used to parameterize a test plan with different data values?",
        'options': ["User Defined Variables", "CSV Data Set Config", "JDBC Request", "BeanShell Processor"],
        'answer': "b"
    },
    {
        'question': "Which JMeter component is used to distribute the load across multiple servers for performance testing?",
        'options': ["Throughput Controller", "Distributed Test", "Remote Testing", "Concurrency Thread Group"],
        'answer': "c"
    },
]

quiz = Quiz(questions)

print("Welcome to the JMeter Quiz!")
print("---------------------------")
print("Answer the following questions:")
print()

while quiz.current_question < len(quiz.questions):
    quiz.display_question()
    answer = quiz.get_answer()
    quiz.check_answer(answer)
    quiz.next_question()

quiz.display_results()
