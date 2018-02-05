def create_sequences():
    sequences = {'updown': {}, 'leftright': {}}
    for i in range(10):
        row = input().strip()
        for j in range(10):
            if row[j] == '-':
                updownfound, leftrightfound = False, False
                for start, sequence in sequences['leftright'].items():
                    if start[0] == i and start[1] + sequence['length'] == j:
                        sequence['length'] += 1
                        leftrightfound = True
                        break
                if not leftrightfound:
                    new_sequence = {'length': 1}
                    sequences['leftright'][(i, j)] = new_sequence
                for start, sequence in sequences['updown'].items():
                    if start[1] == j and start[0] + sequence['length'] == i:
                        sequence['length'] += 1
                        updownfound = True
                        break
                if not updownfound:
                    new_sequence = {'length': 1}
                    sequences['updown'][(i, j)] = new_sequence
    updown_sequences = {start: {'length': sequence['length']} for start, sequence in sequences['updown'].items() if
                        sequence['length'] > 1}
    leftright_sequences = {start: {'length': sequence['length']} for start, sequence in sequences['leftright'].items()
                           if sequence['length'] > 1}
    sequences = {'updown': updown_sequences, 'leftright': leftright_sequences}

    return sequences


spaces = create_sequences()
print(spaces)
words = input().split(';')
len_to_words = {}
for word in words:
    if len(word) in len_to_words.keys():
        len_to_words[len(word)].append(word)
    else:
        len_to_words[len(word)] = [word]


