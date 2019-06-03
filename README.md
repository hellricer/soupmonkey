# soupmonkey

Userscript manager for ELinks powered by BeautifulSoup library.

## Prerequisites

Your ELinks needs to be compiled with Python scripting support. To check, see `elinks --version`.

## Installation

1. Clone this repository into your `~/.elinks/` directory.

2. Create `~/.elinks/hooks.py` with following contents:

```python
    import soupmonkey

    def pre_format_html_hook(url, html):
        return soupmonkey.infect(url, html)
```
