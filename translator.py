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
            try:
                for infinitive, verb in words.verbs.items():
                    langconj = verb[0]
                    englishinfinitive = verb[1]
                    englishconj = verb[2]
                    tense = "if"
                    print("ej", englishconj)
                    try:
                        print("NEW1")
                        for conj in englishconj['allPr']:
                            conj = conj.replace("*", englishinfinitive)
                            print("cj", conj, word, word==conj)
                            if word == conj:
                                tense = "pr"
                                print("DONE")
                                raise ValueError
                        print("NEW2")
                        for conj in englishconj['allPs']:
                            conj = conj.replace("*", englishinfinitive)
                            if word == conj:
                                tense = "ps"
                                raise ValueError
                    except:
                        print("appending")
                        translated.append({"verb": [langconj, infinitive, tense]})
                        raise ValueError
            except:
                pass
            else:
                print('UNKOWN WORD')
                exit(1)
                
    print("EARLY STAGE:", translated)
    # conjugate verbs
    translated2 = []
    for i, word in enumerate(translated):
        typ = list(word.keys())[0]
        info = word[typ] #langconj, infinitive, tense (all info needed to conjugate)
        if typ == "verb":
            if i == 0: continue
            if list(translated[i-1].keys())[0] == "noun":
                nounType = list(translated[i-1].values())[0][2]
                translated2.append({"conjverb": f"{info[1][:-info[0]['endl']]}{info[0][f"{tense}_{nounType}"]}"})
        else:
            translated2.append(word)
    
    print('CONJUGATED:', translated2)
    
    #agglutiante connected nouns (with the word "te")
    
translate(wordstotranslate)