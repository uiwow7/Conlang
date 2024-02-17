from dataclasses import dataclass

ConjType_regular = 0
ConjType_irregular = 1

# Convert RegularEConj class to dictionary
RegularEConj = {
    'typ': ConjType_regular,
    'endl': 1,
    'pr_s1': "",
    'pr_s2': "i",
    'pr_s3': "a",
    'pr_p1': "s",
    'pr_p2': "si",
    'pr_p3': "sa",
    'ps_s1': "ÿ",
    'ps_s2': "it",
    'ps_s3': "at",
    'ps_p1': "z",
    'ps_p2': "is",
    'ps_p3': "as"
}

# Convert RegularAConj class to dictionary
RegularAConj = {
    'typ': ConjType_regular,
    'endl': 1,
    'pr_s1': "i",
    'pr_s2': "e",
    'pr_s3': "i",
    'pr_p1': "z",
    'pr_p2': "za",
    'pr_p3': "z",
    'ps_s1': "ad",
    'ps_s2': "it",
    'ps_s3': "at",
    'ps_p1': "z",
    'ps_p2': "is",
    'ps_p3': "as"
}

# Convert EnglishToBe class to dictionary
EnglishToBe = {
    'pr_s1': "am",
    'pr_s2': "are",
    'pr_s3': "is",
    'pr_p1': "are",
    'pr_p2': "are",
    'pr_p3': "are",
    'ps_s1': "was",
    'ps_s2': "were",
    'ps_s3': "was",
    'ps_p1': "were",
    'ps_p2': "were",
    'ps_p3': "were",
    'all': ["am", "are", "is", "was", "were"]
}

# Convert EnglishToHave class to dictionary
EnglishToHave = {
    'pr_s1': "have",
    'pr_s2': "have",
    'pr_s3': "has",
    'pr_p1': "have",
    'pr_p2': "have",
    'pr_p3': "have",
    'ps_s1': "had",
    'ps_s2': "had",
    'ps_s3': "had",
    'ps_p1': "had",
    'ps_p2': "had",
    'ps_p3': "had",
    'all': ["have", "has", "had"]
}

EnglishBase = {
    'pr_s1': "*",
    'pr_s2': "*",
    'pr_s3': "*s",
    'pr_p1': "*",
    'pr_p2': "*",
    'pr_p3': "*",
    'ps_s1': "*ed",
    'ps_s2': "*ed",
    'ps_s3': "*ed",
    'ps_p1': "*ed",
    'ps_p2': "*ed",
    'ps_p3': "*ed",
    'allPr': ["*", "*s"],
    'allPs': ["*ed"]
}

EnglishAlternate = {
    'pr_s1': "*",
    'pr_s2': "*",
    'pr_s3': "*es",
    'pr_p1': "*",
    'pr_p2': "*",
    'pr_p3': "*",
    'ps_s1': "*ed",
    'ps_s2': "*ed",
    'ps_s3': "*ed",
    'ps_p1': "*ed",
    'ps_p2': "*ed",
    'ps_p3': "*ed",
    'allPr': ["*", "*es"],
    'allPs': ["*ed"]
}

EnglishEndsInE = {
    'pr_s1': "*",
    'pr_s2': "*",
    'pr_s3': "*s",
    'pr_p1': "*",
    'pr_p2': "*",
    'pr_p3': "*",
    'ps_s1': "*d",
    'ps_s2': "*d",
    'ps_s3': "*d",
    'ps_p1': "*d",
    'ps_p2': "*d",
    'ps_p3': "*d",
    'allPr': ["*", "*s"],
    'allPs': ["*d"]
}