RULES = [
    {
        "category": "Threat to share private content",
        "keywords": [
            "share private", "share photo", "leak video", "expose nudes", 
            "post private", "send your friends", "send your family"
        ],
        "points": 35,
        "warning": "The message appears to threaten exposure or distribution of private content."
    },
    {
        "category": "Payment demand",
        "keywords": [
            "pay", "payment", "transfer money", "send money", 
            "rupees", "dollars", "₹"
        ],
        "points": 25,
        "warning": "The message appears to demand money or payment."
    },
    {
        "category": "Time pressure",
        "keywords": [
            "within hours", "right now", "immediately", 
            "today only", "last chance", "hurry", "deadline"
        ],
        "points": 15,
        "warning": "The sender appears to impose a deadline or urgency."
    },
    {
        "category": "Threat / intimidation",
        "keywords": [
            "or else", "otherwise", "you will regret", 
            "i will ruin", "i will expose", "blackmail", "extort"
        ],
        "points": 20,
        "warning": "The message includes language commonly associated with intimidation or coercion."
    },
    {
        "category": "Contacting friends / family",
        "keywords": [
            "your friends", "your family", "your parents", 
            "your classmates", "everyone you know"
        ],
        "points": 10,
        "warning": "The sender may be threatening to contact people around the recipient."
    }
]

def analyse_message(message):
    text=(message).strip().lower()

    score=0
    indicators=[]
    reasons=[]

    for rule in RULES:
        matched = False
        for keyword in rule["keywords"]:
            if keyword in text:
                matched = True
                break 
        
        if matched:
            indicators.append(rule["category"])
            reasons.append(rule["warning"])
            score += rule["points"]

    score=min(score,100)

    if score>=60:
        risk="High"
    elif score >= 30:
        risk = "Medium"
    else:
        risk = "Low"   # 0 to 30 low, 31-59 medium >59 high
        
    if not text:
        risk = "Low"
        score = 0
        
    guidance = [
        "Preserve the original message and relevant screenshots if it is safe to do so.",
        "Do not pay or send additional private content in response to a threat.",
        "Consider submitting a complaint and speaking with a trusted person or designated support staff.",
    ]
    
    return {
        "score": score,
        "risk_level": risk,
        "indicators": indicators,
        "reasons": reasons or ["No configured warning keywords were detected in the provided text."],
        "guidance": guidance,
    }