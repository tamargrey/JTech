import csv


def format_week(jtech_data):
    summaries = []

    # Note: need to have renamed columns to summary, one, and name
    with open('jtech.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            summary = row["summary"]
            summary_len = len(summary.split(' '))
            one_word = row["one"]
            name = row["name"]

            # couldnt remember how to put strings on separate lines
            summaries.append("\\headline{%s} \n \n  One word summary: %s \n \n Word Count: %d \n \n %s \n \\closearticle" % (name, one_word, summary_len, summary))
    return summaries
print ("".join(format_week("")))







    