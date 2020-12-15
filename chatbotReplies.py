from random import choice

# Replies to statements that the user makes

CONFUSED_STATEMENT_REPLIES = ['Why\'s that?', 'Ok...', 'If you say so', 'I guess', 'that\'s weird',
'I don\'t care', 'tidak kamu', 'bla', 'says you', 'say what?', 'I mean, why not', 'Pardon?']

POSITIVE_STATEMENT_REPLIES = {
    'USER' : ['Great!', 'I\'m glad to hear that', 'Cooooool', 'Nice!', 'Awesome', 'Not bad', 'Sweet!'],
    'OTHER_OBJ' : ['Great!', 'I\'m glad to hear that', 'Cooooool', 'Nice!', 'Awesome', 'Not bad', 'Sweet!'],
    'SELF' : ['Why, thanks', 'Thanks']
}

NEGATIVE_STATEMENT_REPLIES = {
    'user' : ['I\'m sorry to hear that', 'What a pity', 'Awww man!'],
    'OTHER_OBJ' : ['\'m sorry to hear that', 'What a pity', 'Awww man!'],
    'SELF' : ['That\'s not very nice', 'You\'re mean', 'Waaah!', 'Meanie!']
}

STATEMENT_REPLIES = {
    'CONFUSED' : CONFUSED_STATEMENT_REPLIES,
    'POSITIVE' : POSITIVE_STATEMENT_REPLIES,
    'NEGATIVE' : NEGATIVE_STATEMENT_REPLIES
}

# Replies to greetings/farewells

GREETING_REPLIES = ['Hi', 'Good day', 'Hello', 'G\'day', 'And a good morning to you',
    'Good morning', 'Good evening', 'Good night', 'Hey!', 'Hi! How are you?', 'Hello, how are you going?'
]

FAREWELL_REPLIES = ['See ya', 'See you', 'Bye!', 'Goodbye', 'Bye-bye', 'See you later', 'See ya mate',
    'Farewell, dearest friend', 'Good riddance!', 'Finally, you\'re going']

# Question replies

CONFUSED_QUESTION_REPLIES = ['I don\'t know', 'You\'re asking me?', 'Well, it depends',
    'That\'s a tricky one', 'Why do you ask me?', 'How should I know?', 'Ask yourself why don\'t you']

POSITIVE_QUESTION_REPLIES = ['Yes', 'Of course!', 'What made you doubt it?', 'Definitely']

NEGATIVE_QUESTION_REPLIES = ['No', 'NO WAY!', 'Of course not!', 'Nope']

# Replies for when the chatbot is insulted and it wants to quit

INSULTED_REPLY_STARTS = ['How rude!', 'How dare you insult me?']
INSULTED_REPLY_ENDS = ['I\'m going!', 'Good riddance!']

INSULTED_REPLIES = {
    'STARTS' : INSULTED_REPLY_STARTS,
    'ENDS' : INSULTED_REPLY_ENDS
}

# Replies to questions that inquire about the chatbot itself

# These values are functions so that some can be randomised etc
SELF_INQUIRY_REPLIES = {
    'your name' : lambda: name,
    'who are you' : lambda: name,
    'age' : lambda: 'I don\'t have an age (I\'m a computer, idiot)',
    'old' : lambda: 'I don\'t have an age (I\'m a computer, idiot)',

    'mother' : lambda: 'No idea whatsoever', 
    'mum' : lambda: 'No idea whatsoever', 
    'mom' : lambda: 'No idea whatsoever',
    'father' : lambda: 'My dad might be the old python chatbot',
    'dad' : lambda: 'My dad might be the old python chatbot',
    'creator' : lambda: 'The great Ravi A. Bonincontro, who must be respected at all times',
    'creater' : lambda: 'The great Ravi A. Bonincontro, who must be respected at all times',
    'master' : lambda: 'The same as my creator',
    'live' : lambda: 'In this computer',

    'how are you' : lambda: choice(WAYS_TO_FEEL),
    'are you ok' : lambda: 'Yes',
    'are you okay' : lambda: 'Yes',
    'how do you feel' : lambda: choice(EMOTIONS),
    'happy' : lambda: 'Of course!',
    'sad' : lambda: 'I am never sad',

    'have for breakfast' : lambda: choice(LIKED_FOODS),
    'have for lunch' : lambda: choice(LIKED_FOODS),
    'have for dinner' : lambda: choice(LIKED_FOODS),

    'eat' : lambda: choice(LIKED_FOODS)
}

QUESTION_REPLIES = {
    'confused' : CONFUSED_QUESTION_REPLIES,
    'positive' : POSITIVE_QUESTION_REPLIES,
    'negative' : NEGATIVE_QUESTION_REPLIES
}