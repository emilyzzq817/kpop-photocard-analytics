"""
K-pop group and member taxonomy for NLP-based entity extraction.
Maps group names to keyword patterns and member aliases.
"""

GROUP_KEYWORDS = {
    "SEVENTEEN": ["seventeen", "svt", "henggarae", "sector 17", "seventeenth heaven",
                   "spill the feels", "mini12", "mini11", "face the sun", "fts", "nana tour bnb"],
    "TXT": ["txt ", " txt", "tomorrow x together", "ppulbatu", "sanctuary", "minisode",
            "the star chapter", "act: promise", "act: sweet mirage", "act: tomorrow",
            "good boy gone bad", "midsummer"],
    "ENHYPEN": ["enhypen", "dimension", "manifesto", "dark blood", "romance:"],
    "IVE": ["ive ", " ive", "i've mine", "love dive", "i am ", "switch", "eleven"],
    "aespa": ["aespa", "savage", "my world", "drama ", "armageddon", "supernova",
              "whiplash", "come to my illusion", "rich man rich bag"],
    "BOYNEXTDOOR": ["boynextdoor", "bnd ", "19.99", "how?", "the action"],
    "ITZY": ["itzy", "cheshire", "kill my doubt", "born to be", "gold"],
    "ILLIT": ["illit", "super real me", "i'll like you", "not cute anymore"],
    "TWS": ["tws ", " tws", "lastbell", "last bell", "sparkling blue", "summer beat", "play hard"],
    "NMIXX": ["nmixx", "fe3o4", "dash", "expergo"],
    "RIIZE": ["riize", "ever riize", "get a guitar", "talk saxy"],
    "NCT": ["nct ", " nct", "nct127", "nct dream", "wayv", "nct wish"],
    "NewJeans": ["newjeans"],
    "Stray Kids": ["stray kids", "straykids", "skz"],
    "LE SSERAFIM": ["le sserafim", "lesserafim", "sserafim", "fearless", "unforgiven"],
    "Kickflip": ["kickflip"],
    "MEOVV": ["meovv"],
    "CORTIS": ["cortis", "color outside the lines"],
    "Hearts2Hearts": ["hearts2hearts"],
    "KiiiKiii": ["kiiikiii", "kiikiii", "kiii"],
    "SayMyName": ["saymyname", "say my name"],
    "TREASURE": ["treasure"],
    "iFeye": ["ifeye"],
    "The Boyz": ["the boyz", "theboyz", "tbz"],
}

MEMBER_MAP = {
    "SEVENTEEN": {
        "S.Coups": ["scoups", "s.coups", "seungcheol"],
        "Jeonghan": ["jeonghan"],
        "Joshua": ["joshua", "jisoo"],
        "Jun": ["jun "],
        "Hoshi": ["hoshi", "soonyoung"],
        "Wonwoo": ["wonwoo"],
        "Woozi": ["woozi"],
        "DK": [" dk ", " dk,", "dokyeom", "seokmin"],
        "Mingyu": ["mingyu"],
        "The8": ["the8", "minghao"],
        "Seungkwan": ["seungkwan"],
        "Vernon": ["vernon", "hansol"],
        "Dino": ["dino"],
    },
    "TXT": {
        "Yeonjun": ["yeonjun"],
        "Soobin": ["soobin", "choi yong"],
        "Beomgyu": ["beomgyu"],
        "Taehyun": ["taehyun"],
        "Hueningkai": ["hueningkai", "huening kai", "huening"],
    },
    "ENHYPEN": {
        "Heeseung": ["heeseung"],
        "Jay": ["jay "],
        "Jake": ["jake"],
        "Sunghoon": ["sunghoon"],
        "Sunoo": ["sunoo"],
        "Jungwon": ["jungwon"],
        "Ni-ki": ["ni-ki", "niki", "nishimura"],
    },
    "IVE": {
        "Yujin": ["yujin"],
        "Gaeul": ["gaeul"],
        "Rei": [" rei ", " rei,"],
        "Wonyoung": ["wonyoung"],
        "Liz": [" liz ", " liz,"],
        "Leeseo": ["leeseo"],
    },
    "aespa": {
        "Karina": ["karina"],
        "Giselle": ["giselle"],
        "Winter": ["winter"],
        "NingNing": ["ningning"],
    },
    "BOYNEXTDOOR": {
        "Sungho": ["sungho"],
        "Riwoo": ["riwoo"],
        "Jaehyun": ["jaehyun"],
        "Taesan": ["taesan"],
        "Leehan": ["leehan"],
        "Woonhak": ["woonhak"],
    },
    "ITZY": {
        "Yeji": ["yeji"],
        "Lia": ["lia "],
        "Ryujin": ["ryujin"],
        "Chaeryeong": ["chaeryeong"],
        "Yuna": ["yuna"],
    },
    "ILLIT": {
        "Yunah": ["yunah"],
        "Minju": ["minju"],
        "Moka": ["moka"],
        "Wonhee": ["wonhee"],
        "Iroha": ["iroha"],
    },
    "TWS": {
        "Shinyu": ["shinyu"],
        "Dohoon": ["dohoon"],
        "Youngjae": ["youngjae"],
        "Hanjin": ["hanjin"],
        "Jihoon": ["jihoon"],
        "Kyungmin": ["kyungmin"],
    },
    "NMIXX": {
        "Lily": ["lily"],
        "Haewon": ["haewon"],
        "Sullyoon": ["sullyoon"],
        "Bae": [" bae "],
        "Jiwoo": ["jiwoo"],
        "Kyujin": ["kyujin"],
    },
    "RIIZE": {
        "Shotaro": ["shotaro"],
        "Eunseok": ["eunseok"],
        "Sungchan": ["sungchan"],
        "Wonbin": ["wonbin"],
        "Seunghan": ["seunghan"],
        "Sohee": ["sohee"],
        "Anton": ["anton"],
    },
}

# Generation/wave categorization
GROUP_GENERATION = {
    "3rd Gen": ["SEVENTEEN", "NCT", "TWICE", "Red Velvet", "The Boyz", "Stray Kids", "ITZY", "TREASURE"],
    "4th Gen": ["TXT", "ENHYPEN", "aespa", "IVE", "LE SSERAFIM", "NewJeans", "NMIXX", "ILLIT"],
    "5th Gen": ["BOYNEXTDOOR", "TWS", "RIIZE", "Kickflip", "MEOVV", "CORTIS", "Hearts2Hearts",
                "KiiiKiii", "SayMyName", "iFeye"],
}

# Company mapping
GROUP_COMPANY = {
    "HYBE": ["SEVENTEEN", "TXT", "ENHYPEN", "BOYNEXTDOOR", "ILLIT", "TWS", "Kickflip", "Hearts2Hearts", "MEOVV", "KiiiKiii"],
    "SM": ["aespa", "NCT", "RIIZE", "Red Velvet"],
    "JYP": ["ITZY", "NMIXX", "Stray Kids"],
    "Starship": ["IVE"],
    "YG": ["TREASURE"],
    "Other": ["NewJeans", "LE SSERAFIM", "SayMyName", "iFeye", "CORTIS", "The Boyz", "XG"],
}
