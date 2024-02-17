import conjugation
nouns = {"I": ["rej", "j", "s1"], "me": ["reb", "b", "s1"], "you": ["ut", "u", "s2"], "day": ["jur", "dǎ", "s3"], "person": ["irpon", "irp", "s3"]}
verbs  = {
    "yope": [conjugation.RegularEConj, "be", conjugation.EnglishToBe], 
    "ora": [conjugation.RegularAConj, "have", conjugation.EnglishToHave], 
    "eme": [conjugation.RegularEConj, "like", conjugation.EnglishEndsInE]
}
adjs = {"happy": "ipas", "two": "kir"}
prps = {"over": "leno", "and": "te"}
