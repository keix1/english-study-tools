import random

conjunction = ['although / though / even though', 'while / whereas', 'because / since', 'while', 'if / when / provided that', 'unless', 'even if', 'once', 'unless']

preposition = ['despite / in spite of', 'because of', 'due to', 'during', 'according to', 'in addition to / besides, moreover / furthermore', 'instead of']

adverb = ['nevertheless', 'therefore', 'even', 'instead']

conjunction_dict = { v: 'c' for v in conjunction}
preposition_dict = { v: 'p' for v in preposition}
adverb_dict = { v: 'a' for v in adverb}

question_dict = {}
question_dict.update(conjunction_dict)
question_dict.update(preposition_dict)
question_dict.update(adverb_dict)

while True:
    print()
    print('##############')
    print()
    print('Choose from options:')
    print('    "c": conjunction（接続詞）')
    print('    "p": preposition（前置詞）')
    print('    "a": adverb（副詞）')
    print()

    question_key = random.choice(list(question_dict.keys()))
    print(f'-----------{question_key}')
    print()
    word_class = input('この品詞は？> ')
    if word_class == question_dict.get(question_key):
        print('○ Correct!')
    else:
        print('☓ Incorrect')
        print()
        print(f'Correct Answer is {word_class}')
    print()

    input('Input any key...')

