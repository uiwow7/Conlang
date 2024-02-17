import words, istr, conjugation
english = input("What to translate?  ")
wordstotranslate = english.split(" ")

def translate(sentence: list[str]) -> str:
    translated = []
    for word in sentence:
        print(word in words.adjs, words.adjs, word)
        if word in words.nouns:
            translated.append({"noun": words.nouns[word]})
        elif word in words.adjs:
            translated.append({"adj": words.adjs[word]})
        elif word in words.prps:
            translated.append({"prp": words.prps[word]})
        else: # verbs (this is really slow -.-)
            for infinitive, verb in words.verbs.items():
                langconj = verb[0]
                englishinfinitive = verb[1]
                englishconj = verb[2]
                tense = "if"
                try:
                    for conj in englishconj['allPr']:
                        conj = conj.replace("*", englishinfinitive)
                        if word == conj:
                            tense = "pr"
                            raise ValueError
                    for conj in englishconj['allPs']:
                        conj = conj.replace("*", englishinfinitive)
                        if word == conj:
                            tense = "ps"
                            raise ValueError
                except:
                    pass
                else: #unknown word
                    print('UNKNOWN WORD, IGNORING')
                translated.append({"verb": [langconj, infinitive, tense]})
                
    print("EARLY STAGE:", translated)
    # conjugate verbs
    translated2 = []
    for i, word in enumerate(translated):
        typ = word.keys()[0]
        info = word[typ] #langconj, infinitive, tense (all info needed to conjugate)
        if typ == "verb":
            if i == 0: continue
            if translated[i-1].keys()[0] == "noun":
                nounType = translated[i-1].keys()[0]
                translated2.append({"conjverb": f"{info[1][:-info[0]['endl']]}{info[0][f"{tense}_"]}"})
    
translate(wordstotranslate)