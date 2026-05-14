zeeguu/core/llm_services/simplification_service.py [270:326]:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        language_names = {
            "ro": "Romanian",
            "en": "English",
            "fr": "French",
            "es": "Spanish",
            "de": "German",
            "da": "Danish",
            "nl": "Dutch",
            "it": "Italian",
            "pt": "Portuguese",
            "sv": "Swedish",
            "no": "Norwegian",
            "fi": "Finnish",
        }

        language_name = language_names.get(language_code, "Romanian")

        prompt = f"""Assess the CEFR level and identify the main topic of this {language_name} article.

Title: {title}
Content: {content[:2000]}...

Consider for CEFR level:
- Vocabulary level (basic vs advanced words)
- Sentence complexity (length, subordinate clauses)
- Abstract concepts vs concrete topics
- Technical terminology usage

Topics to choose from (select the most appropriate one):
- Sports
- Culture & Art
- Technology & Science
- Travel & Tourism
- Health & Society
- Business
- Politics
- Satire

Respond in this exact format:
CEFR: [level]
TOPIC: [topic]

Example response:
CEFR: B2
TOPIC: Business"""

        try:
            response = requests.post(
                "https://api.anthropic.com/v1/messages",
                headers={
                    "x-api-key": self.anthropic_api_key,
                    "anthropic-version": "2023-06-01",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "claude-3-haiku-20240307",
                    "messages": [{"role": "user", "content": prompt}],
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



zeeguu/core/llm_services/simplification_service.py [720:784]:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        language_names = {
            "ro": "Romanian",
            "en": "English",
            "fr": "French",
            "es": "Spanish",
            "de": "German",
            "da": "Danish",
            "nl": "Dutch",
            "it": "Italian",
            "pt": "Portuguese",
            "sv": "Swedish",
            "no": "Norwegian",
            "fi": "Finnish",
        }

        language_name = language_names.get(language_code, "Romanian")

        # Ultra-strict A2-level constraints with paragraph and language preservation
        prompt = f"""You are an expert {language_name} language teacher. Create a simplified version of this {language_name} article at EXACTLY {target_level} level for beginner students.

CRITICAL LANGUAGE REQUIREMENT:
🚨 WRITE EVERYTHING IN {language_name.upper()} ONLY! 🚨
- The original article is in {language_name}
- Your simplified version MUST be in {language_name}  
- DO NOT translate to English, Romanian, or any other language
- Keep ALL words in {language_name}
- This is simplification, NOT translation

ULTRA-STRICT {target_level} REQUIREMENTS FOR {language_name.upper()}:
- Use ONLY the 1500 most basic {language_name} words (like in children's books)
- Maximum 12 words per sentence (count carefully!)
- Use ONLY simple sentences (subject + verb + object)
- Present tense ONLY - avoid past tense when possible
- Replace ALL difficult words with simpler {language_name} words
- Break long ideas into multiple short sentences
- Write like you're explaining to a 10-year-old {language_name} learner

PARAGRAPH STRUCTURE RULES:
- PRESERVE PARAGRAPH STRUCTURE: If the original has 4 paragraphs, your simplified version must have 4 paragraphs
- Transform each paragraph of the original into a paragraph in the simplified version
- MAINTAIN CONTENT DEPTH: Include all main ideas from each paragraph, just in simpler {language_name}
- DO NOT SUMMARIZE: This is simplification (easier language), not summarization (shorter content)
- Work paragraph-by-paragraph to preserve all information and structure

🚨 REMEMBER: Write your response in {language_name.upper()}, not English or any other language! 🚨

Original {language_name} Title: {title}
Original {language_name} Content: {content}

Format your response EXACTLY like this (in {language_name.upper()}):
SIMPLIFIED_TITLE: [your simplified title in {language_name}]
SIMPLIFIED_SUMMARY: [a concise plain-text summary in {language_name}, maximum 25 words, NO Markdown or HTML]
SIMPLIFIED_CONTENT: [your simplified content in {language_name} using Markdown formatting - preserve paragraph breaks with double newlines, use **bold**, *italics*, ## for headings, - for lists]"""

        try:
            response = requests.post(
                "https://api.anthropic.com/v1/messages",
                headers={
                    "x-api-key": self.anthropic_api_key,
                    "anthropic-version": "2023-06-01",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "claude-3-haiku-20240307",
                    "messages": [{"role": "user", "content": prompt}],
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



