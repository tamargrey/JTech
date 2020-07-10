import csv


def format_week(filename):
    summaries = []

    # Note: need to have renamed columns to summary, one, and name
    with open('{}.csv'.format(filename), newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            person_responses = []
            for key, entry in row.items():
                if not entry:
                    continue
                if key == "Timestamp":
                    continue
                if len(entry) > 1 and entry[1] == ')':  # multiple choice
                    continue
                if key == "Name, please!":
                    person_responses.append("\\headline{%s} \n" % entry)
                    continue
                if key == "Any pictures you'd like to share?":
                    entry = "%\\begin{{window}}[1, r, \\includegraphics[width=1.5in]{{{}}}]".format(entry)
                if key == "And Now: How was your week?  (bonus points if your word count is a palindrome or multiple of 11) (gentle reminder for third person responses, please!)":
                    key = "And Now: How was your week?  (bonus points if your word count is a palindrome or multiple of 11)"
                    word_count = len(entry.split())
                    entry = "Word Count: {}\n\n".format(word_count) + entry

                for literal in '&#':
                    if literal in entry:
                        loc = entry.find(literal)
                        entry = entry[:loc] + '\\' + entry[loc:]

                person_responses.append("\\noindent \\textbf{{{}}}:\n\n {}\n\n".format(key, entry))
            summaries.append("\n".join(person_responses))

    summaries.append("") # final \closearticle
    body = "\\closearticle".join(summaries)
            # summary = row["summary"]
            # summary_len = len(summary.split(' '))
            # one_word = row["one"]
            # name = row["name"]
            #
            # # couldnt remember how to put strings on separate lines
            # summaries.append("\\headline{%s} \n \n  One word summary: %s \n \n Word Count: %d \n \n %s \n \\closearticle" % (name, one_word, summary_len, summary))
    # return summaries
    f = open("body.tex", "a")
    f.write(body)
    f.close()

print(format_week("JTech Week 17 - The 3 Weeks  (Responses) - Form Responses 1"))







    