import bleach

# Allowed values for validation
ALLOWED_STYLES = {"academic", "casual", "business", "technical"}
ALLOWED_LANGUAGES = {"english", "spanish", "french", "german", "chinese"}

def sanitize_input(text: str) -> str:
    """Sanitize user input by removing unwanted characters and tags."""
    return bleach.clean(text.strip(), tags=[], attributes={}, protocols=[], strip=True)

def validate_style(style: str) -> str:
    """Validate the writing style, return default if invalid."""
    return style.lower() if style.lower() in ALLOWED_STYLES else "academic"

def validate_language(language: str) -> str:
    """Validate the language choice, return default if invalid."""
    return language.lower() if language.lower() in ALLOWED_LANGUAGES else "english"
