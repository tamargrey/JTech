import csv
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


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
NOTE - ignores unansswered questions and will work well with short answer-style qs

Inputs:
    filename - csv file name string with responses - the file must be in the same directory 
    headline - string, your desired header
    question_col - column name of the question you'd like to format
    name_col -string of the column/question asking for peoples' names- must be exact 

Output:
    latex file called <question_col>.tex - this might be kind of long and unweidly
'''
def get_short_answer_question_with_names(filename, headline, question_col, name_col):
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

def splitword(sentence, max_line):
    count = 0
    for word in sentence.split():
        count += len(word) + 1
        if count > max_line:
            return sentence[:count] + "\n" + sentence[count:]
    return sentence


'''
Allows you to plot pie chart with legend

Inputs:
    filename - csv file name string with responses - the file must be in the same directory 
    headline - string, your desired header
    question_col - column name of the question you'd like to format
Output:
    <question_col>.jpg
'''
def get_multiple_choice_question_pie(filename, headline, question_col):
    answers = []
    with open('{}.csv'.format(filename), newline='') as csvfile:
        answers = []
        reader = csv.DictReader(csvfile)
        for row in reader:
           
           answers.append(row[question_col])
        #    want to grab answer
    answers_hist = Counter(answers)
    
    choices = [splitword(choice, 50) for choice in list(answers_hist.keys())]
    # build plot
    fname = question_col + ".jpg"
    fig1, ax1 = plt.subplots()
    wedges, _, _ = ax1.pie(list(answers_hist.values()), autopct='%1.0f%%', shadow=True, startangle=90)
    ax1.legend(wedges, list(choices), loc = 'lower right') #the legend is over the pie
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig(fname)

get_multiple_choice_question_pie('summary', "Q", 'How did MIT *actually* decide who got to return?')




