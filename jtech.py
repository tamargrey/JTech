import csv
import numpy as np
import matplotlib.pyplot as plt


def splitword(sentence, max_line):
    count = 0
    for word in sentence.split():
        count += len(word) + 1
        if count > max_line:
            return sentence[:count] + "\n" + sentence[count:]
    # print(count)
    return sentence


def format_week(filename):
    responses = []
    multiple_choice = {}

    with open('{}.csv'.format(filename), newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            person_responses = []
            name_key = "Name, please!"
            name = row.pop(name_key)
            person_responses = ["\\headline{%s} \n"%name]

            for key, entry in row.items():
                for literal in '&#{}':
                    if literal in entry:
                        loc = entry.find(literal)
                        entry = entry[:loc] + '\\' + entry[loc:]
                    if literal in key:
                        loc = key.find(literal)
                        key = key[:loc] + '\\' + key[loc:]

                for weird_character in "â€™":
                    if weird_character in entry:
                        loc = entry.find(weird_character)
                        entry = entry[:loc] + entry[loc + 1:]
                    if weird_character in key:
                        loc = key.find(weird_character)
                        key = key[:loc] + key[loc + 1:]

                entry = entry.replace('\n', '\n\n').replace('\n\n\n', '\n\n')

                if not entry:
                    continue

                if key == "Timestamp":
                    continue

                if len(entry) > 1 and entry[1] == ')':  # multiple choice
                    question = multiple_choice.setdefault(key, {})
                    question[entry] = question.get(entry, 0) + 1
                    continue

                if key == "Any pictures you'd like to share?":
                    entry = "%\\includegraphics[width=1.5in]{{{}}}".format(name)  # will need to uncomment this and add the picture name in latex

                if key == "And Now: How was your week?  (bonus points if your word count is a palindrome or multiple of 11) (gentle reminder for third person responses, please!)":
                    key = "And Now: How was your week?  (bonus points if your word count is a palindrome or multiple of 11)"
                    word_count = len(entry.split())
                    entry = "Word Count: {}\n\n".format(word_count) + entry

                person_responses.append("\n \\noindent \\textbf{{{}}}:\n\n {}\n".format(key, entry))

            responses.append("\n".join(person_responses))

    responses.append("\n \\columnbreak \n")

    for i, (question, answers) in enumerate(multiple_choice.items()):
        fname = "MultipleChoice{}.jpg".format(i)
        choices, nums = answers.keys(), answers.values()
        choices = [splitword(choice, 50) for choice in choices]

        fig1, ax1 = plt.subplots()
        wedges, _, _ = ax1.pie(list(nums), autopct='%1.0f%%', shadow=True, startangle=90)
        ax1.legend(wedges, choices)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.savefig(fname)

        multiple_responses = []
        multiple_responses.append("\n\n \\noindent \\textbf{{{}}}:\n".format(question))
        multiple_responses.append("\\includegraphics[width=\columnwidth]{{{}}} \n".format(fname))
        responses.append("".join(multiple_responses))

    responses.append("")  # final \closearticle
    body = "\\closearticle".join(responses)
    f = open("body.tex", "a")
    f.write(body)
    f.close()

# print(format_week("JTech Week 17 - The 3 Weeks  (Responses) - Form Responses 1"))



'''
Allows you to specify a list of questions that you would like the answers to for grouped by person

Use column names from the responses csv

formatting isn't really anything beyond separate headlines - feel free to change to something nicer
Inputs: 
    filename - csv file name string with responses - the file must be in the same directory
    col_names - list of string string of the columns/questions you'd like to pull out by person

output:
    latex file called by_person.tex of format
        - as headline
        ...questions
'''
def get_questions_by_person(filename, col_names):
    person_data = []
    with open('{}.csv'.format(filename), newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            person_data.append("\n \n".join(map(lambda col_name: row[col_name], col_names)))
    body = " \\headline{-} ".join(person_data)
    f = open("by_person.tex", "a")
    f.write(body)
    f.close() 
    
# get_questions_by_person('summary', ['Name', 'one', 'summary'])


'''
Lets you get a body.tex file that can serve as peoples' weeks. 
NOTE you'll probably want to go in the latex file and manually make sure all newlines are actually newlines

Inputs: 
    filename - csv file name string with responses - the file must be in the same directory
    name_col - string of the column/question asking for peoples' names- must be exact
    summary_col - string of the column/question asking for peoples' weeks - must be exact

output:
    latex file called body.tex of format
        Name as headline
        Word count

        week summary

'''
def get_weeks(filename, name_col, summary_col):
    with open('{}.csv'.format(filename), newline='') as csvfile:
        summaries = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            summary = row[summary_col]
            summary_len = len(summary.split(' '))
            name = row[name_col]
            
            summaries.append("\\headline{%s} \n \n \\textbf{Word Count:} %d \n \n  \\vspace{5mm}  %s \n \\closearticle" % (name, summary_len, summary))
    body = "\n".join(summaries)
    f = open("body.tex", "a")
    f.write(body)
    f.close()

# get_weeks('summary', 'Name', 'summary')

'''
Gets everyone's answers for a specific question
NOTE - ignores unansswered questions

Inputs:
    filename - csv file name string with responses - the file must be in the same directory 
    headline - string, your desired header
    question_col - column name of the question you'd like to format
    name_col -string of the column/question asking for peoples' names- must be exact 
'''
def get_question(filename, headline, question_col, name_col):
    with open('{}.csv'.format(filename), newline='') as csvfile:
        answers = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            answer = row[question_col]
            name = row[name_col]

            if answer:
                answers.append('\\item %s - (%s)' % (answer, name)) 
            
    body = '\\headline{%s} \\begin{itemize}' % headline + "\n".join(answers) + '\\end{itemize} \\closearticle' 
    f = open(question_col+".tex", "a")
    f.write(body)
    f.close() 

# get_question('summary','Hours', 'How many hours did you sleep last night? ', 'Name')
