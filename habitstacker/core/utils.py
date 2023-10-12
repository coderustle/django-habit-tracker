from typing import Any, Self

from django.http import HttpResponseRedirect


class HtmxResponseRedirect(HttpResponseRedirect):
    """
    This is a utility class to add HX-Redirect to response header
    Thus, will let the htmx to redirect to a specific location.
    """

    def __init__(self, redirect_to: str, *args: Any, **kwargs: Any) -> Self:
        super().__init__(redirect_to, *args, **kwargs)
        self["HX-Redirect"] = self["Location"]
