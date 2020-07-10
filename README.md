# JTech

This repo contains some code to help automate some of the JTech process!

The files produced will be `.tex` files that can be uploaded into an existing overleaf project as well as some `.jpg` files for various charts.

Here's what currently exists in `jtech.py` to help:
* `get_questions_by_person`
* `get_week_summaries`
* `get_short_answer_question_with_names`
* `get_multiple_choice_question_pie`

There's a bit of documentation by each of those functions.

Here's what you need to get things running (this is kind of assuming you're working with a Mac, but it shouldn't be that different. You only really need to be able to run a python script. If you dont want to worry about git, then just ignore it! Lmk if you need help!):
1. Clone the repo if you want to be able to contribute - `git clone <repo url>` - or download the files as a zip if you just want the code
2. Make sure you have a csv with the jtech responses and put it in the JTech directory (it'll be ignored by git)
3. go into the `jtech.py` file and directly call any functions you want to run
4. run `python jtech.py' in your terminal
5. The corresponding files should now be in your directory (and will also be ignored by git)

If you're unfamiliar/intimidated by git or latex but want to learn a bit about it, this is a suuuper easy and low stakes way, so let me know if you want a tutorial! Git is great, and I'm always happy to teach and answer questions. I, uhh, probably shouldn't be the one you go to for latex help. Honestly, writing latex code through Python strings is probably super sketchy, but it works for this purpose! 