import json

LANGUAGE_MAP = {
    "日本語": "ja",
    "中文": "zh",
    "English": "en",
}

def load_prompt(src_lang,dst_lang):
    """Load the translation prompt from a JSON file based on the target language."""
    lang_code = LANGUAGE_MAP.get(dst_lang, "en")
    prompt_path = f"prompts/{lang_code}.json"
    
    with open(prompt_path, "r", encoding="utf-8") as file:
        prompt_data = json.load(file)
        
        # Extract prompts
        system_prompt = prompt_data.get("system_prompt", "")
        user_prompt = prompt_data.get("user_prompt", "Translate the following text:")
        previous_prompt = prompt_data.get("previous_prompt", "This is the contextual content of the previous paragraph:")
        previous_text_default = prompt_data.get("previous_text_default", {})
        
        # Replace placeholders with src_lang and dst_lang
        system_prompt = system_prompt.format(Text_Target_Language=dst_lang, Text_Source_Language=src_lang)
        
        return system_prompt, user_prompt, previous_prompt, previous_text_default