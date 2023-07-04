from django.core.cache import cache
from django.conf import settings


def delete_cache(key_prefix: str):
    """Delete all cache keys with the given prefix."""
    key_pattern = f"views.decorators.cache.cache_*.{key_prefix}.*.{settings.LANGUAGE_CODE}.{settings.TIME_ZONE}"
    cache.delete_pattern(key_pattern)
