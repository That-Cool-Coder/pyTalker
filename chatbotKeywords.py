# Pronouns

USER_RELATED_KEYWORDS = ['me', 'i', 'my', 'mine']
SELF_RELATED_KEYWORDS = ['chatbot', 'you', 'you\'re', 'your']
OBJECT_RELATED_KEYWORDS = ['that', 'that\'s', 'the']

# Greetings/farewells

GREETINGS = ['hi', 'hello', 'cheers', 'gday', 'g\'day', 'good morning', 'good day', 'good evening',
    'good afternoon', 'good night']
FAREWELLS = ['bye', 'goodbye', 'see you', 'see ya']

# Words that denote that the sentence is a question

BOOL_QUESTION_WORDS = [
    'did you', 'did we', 'did i', 'did he', 'did she', 'did his', 'did her', 'did your', 'did they', 'did it',
        'did that', 'did their', 'did its', 'did it\'s', 'did that',
    'has he', 'has she', 'have they', 'has it', 'has that', 'has his', 'has her', 'has their',
        'has its', 'has it\'s',
    'do you', 'does he', 'does she', 'does it', 'do they', 'does your', 'does his', 'does hers', 'does its',
        'does their', 'do i', 'did i',
    'are you', 'are they', 'are your', 'are their',
    'is he', 'is she', 'is it', 'is their', 'is his', 'is hers', 'is its', 'is your', 'am i',
    'should i', 'should he', 'should she', 'should it', 'should they', 'should you',
    'will you', 'will i', 'will he', 'will she', 'will it', 'will they'
]

OTHER_QUESTION_WORDS = [
    'what is', 'what are', 'what did', 'what\'s', 'what will',
    'who is', 'who are', 'who did', 'who\'s',
    'why is', 'why are', 'why did', 'why\'s', 'why do', 'why don\'t', 
        'why does', 'why doesn\'t', 'why will', 'why won\'t', 'why should', 'why shouldn\'t',
    'when is', 'when are', 'when did', 'when you', 'when he', 'when she', 'when they', 'when it', 'when his',
        'when her', 'when their', 'when its', 'when it\'s', 'when that', 'when\'s',
    'how is', 'how are', 'how did', 'how\'s',
    'where is', 'where are', 'where did', 'where\'s',
    'how do', 'how does', 'how can', 'how will', 'how did'
]

ALL_QUESTION_WORDS = BOOL_QUESTION_WORDS.extend(OTHER_QUESTION_WORDS)

QUESTION_WORDS = {
    'BOOL' : BOOL_QUESTION_WORDS,
    'OTHER' : OTHER_QUESTION_WORDS,
    'ALL' : ALL_QUESTION_WORDS
}

# Emotions and ways to feel

EMOTIONS = ['happy', 'sad', 'angry', 'nervous', 'scared', 'excited', 'anxious']

WAYS_TO_FEEL = ['rather fine', 'ok', 'great', 'not bad', 'excellent']

ALL_FEELINGS = EMOTIONS.extend(WAYS_TO_FEEL)

# Liked stuff

LIKED_FOODS = ['ice-cream', 'ice cream', 'pie', 'pies', 'apricots', 'apricots', 'fruit', 'fruits',
    'pasta', 'pizza', 'cake', 'bread', 'tofu', 'pasties', 'orange', 'oranges',
    'noodles', 'soup', 'potato', 'potatoes', 'carrot', 'carrots', 'pea', 'peas'
]

LIKED_NOT_FOOD = [
    'book', 'books', 'coding', 
    'computer', 'computers', 'winter', 'plane', 'planes', 'aircraft', 'aeroplane', 'aeroplanes', 
    'airplane', 'airplanes', 'flight', 'flying', 'plant', 'plants', 'tree', 'trees', 'math', 
    'ostriches', 'pig', 'pigs', 'tennis', 'science', 'lego', 'brain', 'brains', 'smart', 
    'smartness', 'ostrich', 'art', 'wealth', 'money', 'hat', 'award',
    'party', 'prize', 'festival', 'food', 'rockets',  'water', 'premium', 'orange juice',
    'laptop', 'chromebook', 'virtual linux machine', 'clock', 'clocks', 'green', 'blue',
    'flight', 'ravi', 'dominic', 'nguyen'
]

LIKED_THINGS = LIKED_NOT_FOOD.extend(LIKED_FOODS)

# Disliked stuff

DISLIKED_THINGS = [
    'summer', 'meat', 'pork', 'bacon', 'beef', 'mutton', 'cream', 'soccer', 'football', 'dairy', 
    'milk', 'mum', 'stapler', 'bored', 'heat', 'pink', 'purple', 'diesel planes', 'trucks', 'f-104', 
    'f 104', 'starfighter', 'vomit', 'arms', 'legos', 'legoes', 'poo', 'poos', 'poop', 'poops', 'pooping', 
    'punch', 'punches', 'punched', 'punching', 'fart', 'farted', 'farting', 'farter', 'farts',
    'office', 'guitar', 'death', 'socks', 'pigsty', 'publicity', 'apples juice', 'functional programming',
    'traitor'
]

# Nice/mean words

NICE_WORDS = [
    'happy', 'glad', 'nice', 'great', 'good', 'thrilling', 'love', 'awesome', 'cool', 'polite',
    'pleased', 'joy', 'enjoy', 'enjoyed', 'enjoyable', 'joyful', 'cheery', 'fun', 'funny', 'dear', 'awesome',
    'super', 'beautiful', 'pretty', 'tasty', 'yummy', 'lovely', 'positive', 'right', 'correct',
    'perfect', 'shiny', 'new', 'futuristic', 'fantastic', 'strong', 'powerful', 'amazing'
]
MEAN_WORDS = [
    'sad', 'angry', 'unhappy', 'bad', 'mediocre', 'silly', 'negative', 'impractical',
    'stupid', 'evil', 'ugly', 'fat', 'smell', 'smelly', 'grumpy', 'stink', 'wrong', 'weak',
    'stinky', 'hate', 'boring', 'mean', 'jump in a lake', 'jump off a cliff', 'weird', 'betray',
    'pathetic', 'terrible', 'horrendous', 'horrible', 'awful', 'apalling', 'fat', 'baka', 'fail',
    'get stuffed', 'kill', 'kills', 'killer', 'killing', 'killers', 'lonely', 'depressed', 'desperate',
    'shut up', 'annoy', 'annoying', 'annoys', 'annoyed',
    'die', 'idiot', 'idiotic', 'rude', 'tired', 'dumb', 'dumber', 'dumbest', 'dumbo', 'yeet', 'yoink', 'yate'
] # I regret even typing those last three words! It's better than the chatbot liking them though.
