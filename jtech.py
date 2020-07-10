# import csv with jtech data 
import csv


def format_week(jtech_data):
    summaries = []

    # Note: need to have renames columns to summary, one, and name
    with open('jtech.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # do thing to pull out info 
            summary = row["summary"]
            summary_len = len(summary.split(' '))
            one_word = row["one"]
            name = row["name"]

            summaries.append("\\headline{%s} \n \n  One word summary: %s \n \n Word Count: %d \n \n %s \n \\closearticle" % (name, one_word, summary_len, summary))
    return summaries
print ("".join(format_week("")))







    