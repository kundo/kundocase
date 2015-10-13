import requests

def spamcheck_question(question):
    is_spam = long_texts_are_spam(question)

    if not is_spam:
        is_spam = long_titles_are_spam(question)
    if not is_spam:
        is_spam = all_users_from_domain_are_spam(question)
    if not is_spam:
        is_spam = some_usernames_are_spam(question)
    if not is_spam:
        is_spam = words_in_text_are_spam(question)
    if not is_spam:
        is_spam = known_spammers_are_spam(question)

    return is_spam

def spamcheck_answer(answer):
    is_spam = long_texts_are_spam(answer)

    if not is_spam:
        is_spam = all_users_from_domain_are_spam(answer)
    if not is_spam:
        is_spam = some_usernames_are_spam(answer)
    if not is_spam:
        is_spam = words_in_text_are_spam(answer)
    if not is_spam:
        is_spam = known_spammers_are_spam(answer)

    return is_spam

# Different ways to check for spam
def long_texts_are_spam(question_or_comment):
    if len(question_or_comment.content) > 200:
        return True

    return False

# Different ways to check for spam
def long_titles_are_spam(question_or_comment):
    if len(question_or_comment.title) > 200:
        return True

    return False

def all_users_from_domain_are_spam(question_or_comment):
    bad_domains = ["spam.com", "universitydiploma.com"]
    domain = question_or_comment.user_email.split("@")[1]
    if domain in bad_domains:
        return True

    return False

def some_usernames_are_spam(question_or_comment):
    bad_names = ["thord", "curt", "madicken"]
    name = question_or_comment.user_name
    for bad_name in bad_names:
        if name in bad_name:
            return True

    return False

def words_in_text_are_spam(question_or_comment):
    bad_words = ["spam", "universitydiploma"]
    text = question_or_comment.content
    for word in bad_words:
        if word in text:
            return True

    return False

def known_spammers_are_spam(question_or_comment):
    email = question_or_comment.user_email
    url = "https://www.stopforumspam.com/api?f=json&email=" + email
    response = requests.get(url, timeout=2)
    data = response.json()

    if data and data["success"] and data["email"]["appears"]:
        return True

    return False
