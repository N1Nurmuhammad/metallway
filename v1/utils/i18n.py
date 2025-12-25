from django.utils import translation

SUPPORTED_LANGS = {"uz", "ru", "en", "kz"}


def activate_request_language(request):
    """
    Activate translation based on ?lang= query param if provided and supported.
    Falls back to middleware/Accept-Language if not provided or invalid.
    """
    lang = (request.GET.get("lang") or request.headers.get("X-Language") or "").lower()
    if lang in SUPPORTED_LANGS:
        translation.activate(lang)
        request.LANGUAGE_CODE = lang
    # else: leave the language as selected by LocaleMiddleware
