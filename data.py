"""
EduMate AI — Content Data
Subjects, lessons, quizzes, and the chatbot knowledge base.
"""

SUBJECTS = {
    "Mathematics": {
        "icon": "📐",
        "topics": {
            "Understanding Fractions": {
                "grade": "Grade 5-6",
                "summary": "Learn what fractions are and how to compare them.",
                "lesson": [
                    "A fraction represents a part of a whole. It is written as a numerator (top number) over a denominator (bottom number), like 3/4.",
                    "The denominator tells you how many equal parts the whole is divided into. The numerator tells you how many of those parts you have.",
                    "Example: If a pizza is cut into 8 slices and you eat 3, you ate 3/8 of the pizza.",
                    "To compare fractions with the same denominator, just compare the numerators: 5/8 is bigger than 3/8.",
                    "To compare fractions with different denominators, convert them to a common denominator first.",
                ],
                "quiz": [
                    {
                        "q": "What does the bottom number of a fraction represent?",
                        "options": ["The number of parts you have", "The total number of equal parts", "The remainder", "The whole number"],
                        "answer": 1,
                    },
                    {
                        "q": "Which fraction is larger: 3/5 or 4/5?",
                        "options": ["3/5", "4/5", "They are equal", "Cannot be determined"],
                        "answer": 1,
                    },
                    {
                        "q": "A cake is cut into 6 equal slices. You eat 2. What fraction did you eat?",
                        "options": ["2/6", "6/2", "2/8", "4/6"],
                        "answer": 0,
                    },
                ],
            },
            "Introduction to Algebra": {
                "grade": "Grade 7-8",
                "summary": "Understand variables, expressions, and simple equations.",
                "lesson": [
                    "In algebra, letters like x or y are used to represent unknown numbers. These letters are called variables.",
                    "An expression combines numbers, variables, and operations, e.g. 2x + 5.",
                    "An equation states that two expressions are equal, e.g. 2x + 5 = 11.",
                    "To solve an equation, isolate the variable by performing the same operation on both sides.",
                    "Example: 2x + 5 = 11 → subtract 5 from both sides → 2x = 6 → divide both sides by 2 → x = 3.",
                ],
                "quiz": [
                    {
                        "q": "What is a variable?",
                        "options": ["A fixed number", "A letter representing an unknown number", "An operation like + or -", "A type of equation"],
                        "answer": 1,
                    },
                    {
                        "q": "Solve for x: x + 4 = 10",
                        "options": ["x = 4", "x = 6", "x = 14", "x = 2"],
                        "answer": 1,
                    },
                    {
                        "q": "Solve for x: 3x = 12",
                        "options": ["x = 3", "x = 9", "x = 4", "x = 15"],
                        "answer": 2,
                    },
                ],
            },
        },
    },
    "Science": {
        "icon": "🔬",
        "topics": {
            "Photosynthesis": {
                "grade": "Grade 6-8",
                "summary": "How plants make their own food using sunlight.",
                "lesson": [
                    "Photosynthesis is the process by which green plants make their own food using sunlight, water, and carbon dioxide.",
                    "It takes place mainly in the leaves, inside structures called chloroplasts, which contain a green pigment called chlorophyll.",
                    "The simple word equation is: Carbon dioxide + Water + Sunlight → Glucose + Oxygen.",
                    "Plants release oxygen as a by-product, which is essential for humans and animals to breathe.",
                    "Photosynthesis mostly happens during the day when sunlight is available.",
                ],
                "quiz": [
                    {
                        "q": "Which pigment absorbs sunlight for photosynthesis?",
                        "options": ["Melanin", "Chlorophyll", "Hemoglobin", "Keratin"],
                        "answer": 1,
                    },
                    {
                        "q": "What gas do plants release during photosynthesis?",
                        "options": ["Carbon dioxide", "Nitrogen", "Oxygen", "Hydrogen"],
                        "answer": 2,
                    },
                    {
                        "q": "Where does photosynthesis mainly occur in a plant?",
                        "options": ["Roots", "Stem", "Leaves", "Flowers"],
                        "answer": 2,
                    },
                ],
            },
            "States of Matter": {
                "grade": "Grade 5-6",
                "summary": "Solids, liquids, and gases and how they change.",
                "lesson": [
                    "Matter exists in three common states: solid, liquid, and gas.",
                    "Solids have a fixed shape and volume because their particles are tightly packed.",
                    "Liquids have a fixed volume but take the shape of their container; particles are close but can move around.",
                    "Gases have no fixed shape or volume; particles are far apart and move freely.",
                    "Matter can change state through heating or cooling: melting, freezing, evaporation, and condensation.",
                ],
                "quiz": [
                    {
                        "q": "Which state of matter has a fixed shape and volume?",
                        "options": ["Gas", "Liquid", "Solid", "Plasma"],
                        "answer": 2,
                    },
                    {
                        "q": "The process of a liquid turning into a gas is called:",
                        "options": ["Freezing", "Condensation", "Evaporation", "Melting"],
                        "answer": 2,
                    },
                    {
                        "q": "In a gas, the particles are:",
                        "options": ["Tightly packed", "Far apart and free-moving", "Fixed in place", "Arranged in a grid"],
                        "answer": 1,
                    },
                ],
            },
        },
    },
    "English": {
        "icon": "📚",
        "topics": {
            "Parts of Speech": {
                "grade": "Grade 5-7",
                "summary": "Nouns, verbs, adjectives, and how they build sentences.",
                "lesson": [
                    "A noun names a person, place, thing, or idea (e.g. teacher, city, book, happiness).",
                    "A verb shows an action or a state of being (e.g. run, is, think).",
                    "An adjective describes or modifies a noun (e.g. tall, blue, happy).",
                    "An adverb describes or modifies a verb, adjective, or another adverb, often ending in -ly (e.g. quickly, very).",
                    "A simple sentence needs at least a subject (noun) and a verb, e.g. 'The dog barks.'",
                ],
                "quiz": [
                    {
                        "q": "Which word is a verb in the sentence: 'She sings beautifully'?",
                        "options": ["She", "sings", "beautifully", "None"],
                        "answer": 1,
                    },
                    {
                        "q": "Which word is an adjective in: 'The tall boy jumped'?",
                        "options": ["The", "tall", "boy", "jumped"],
                        "answer": 1,
                    },
                    {
                        "q": "A noun names a:",
                        "options": ["Person, place, thing or idea", "Action only", "Description only", "Connector word"],
                        "answer": 0,
                    },
                ],
            },
            "Verb Tenses": {
                "grade": "Grade 6-8",
                "summary": "Past, present, and future tense basics.",
                "lesson": [
                    "Verb tense tells us when an action happens: past, present, or future.",
                    "Present tense describes actions happening now, e.g. 'I play cricket.'",
                    "Past tense describes actions that already happened, e.g. 'I played cricket yesterday.'",
                    "Future tense describes actions that will happen, e.g. 'I will play cricket tomorrow.'",
                    "Regular verbs usually add '-ed' for past tense, but irregular verbs change form completely (go → went).",
                ],
                "quiz": [
                    {
                        "q": "Which sentence is in the past tense?",
                        "options": ["I eat lunch.", "I ate lunch.", "I will eat lunch.", "I am eating lunch."],
                        "answer": 1,
                    },
                    {
                        "q": "What is the past tense of 'go'?",
                        "options": ["Goed", "Going", "Went", "Goes"],
                        "answer": 2,
                    },
                    {
                        "q": "'I will study tomorrow' is an example of which tense?",
                        "options": ["Past", "Present", "Future", "None"],
                        "answer": 2,
                    },
                ],
            },
        },
    },
}

# ------------------------------------------------------------
# Chatbot knowledge base — keyword-matched NLP responses
# ------------------------------------------------------------
CHAT_KB = [
    {
        "keywords": ["fraction", "numerator", "denominator"],
        "response": "A fraction shows a part of a whole, written as numerator/denominator. For example, 3/4 means 3 parts out of 4 equal parts. Want to try a quick quiz on fractions?",
    },
    {
        "keywords": ["photosynthesis", "chlorophyll"],
        "response": "Photosynthesis is how plants make food using sunlight, water and carbon dioxide, producing glucose and oxygen. It happens in the chloroplasts inside leaves.",
    },
    {
        "keywords": ["algebra", "variable", "equation"],
        "response": "In algebra, a variable (like x) stands for an unknown number. To solve an equation like 2x + 5 = 11, isolate x step by step using inverse operations.",
    },
    {
        "keywords": ["angle", "acute", "obtuse", "right angle"],
        "response": "Angles are measured in degrees. Acute < 90°, right = 90°, obtuse is between 90° and 180°, and straight = 180°.",
    },
    {
        "keywords": ["solar system", "planet", "sun", "orbit"],
        "response": "Our Solar System has 8 planets orbiting the Sun, in order: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune.",
    },
    {
        "keywords": ["states of matter", "solid", "liquid", "gas"],
        "response": "Matter exists mainly as solids (fixed shape/volume), liquids (fixed volume, changing shape), and gases (no fixed shape or volume).",
    },
    {
        "keywords": ["noun", "verb", "adjective", "adverb", "parts of speech"],
        "response": "Nouns name people/places/things, verbs show actions, adjectives describe nouns, and adverbs describe verbs — usually ending in -ly.",
    },
    {
        "keywords": ["tense", "past tense", "future tense", "present tense"],
        "response": "Tense tells us when something happens: present (I play), past (I played), or future (I will play).",
    },
    {
        "keywords": ["hello", "hi", "hey"],
        "response": "Hello! I'm your AI tutor. Ask me about any topic in Math, Science, or English, or pick a subject from the sidebar to start a structured lesson.",
    },
    {
        "keywords": ["help", "what can you do"],
        "response": "I can explain topics in Math, Science and English, answer your questions, and quiz you to check your understanding. Try asking about fractions, photosynthesis, or verb tenses!",
    },
    {
        "keywords": ["thank", "thanks"],
        "response": "You're welcome! Keep learning — consistent practice is the key to mastering any subject. 🌟",
    },
]

FALLBACK_RESPONSES = [
    "That's an interesting question! Try rephrasing it, or pick a topic from the sidebar so I can guide you through it step by step.",
    "I'm still learning about that specific topic. Could you ask about Math, Science, or English basics? For example: 'What is a fraction?' or 'Explain photosynthesis.'",
    "Let's break this down together — could you tell me which subject this relates to: Math, Science, or English?",
]
