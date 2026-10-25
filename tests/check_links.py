"""Build the docs like Read the Docs does and fail on broken relative links in
docs/about.md.

Run with: uv run python tests/check_links.py
"""

import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

LINK_ATTRS = {"href", "src", "data"}


class LinkCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in LINK_ATTRS and value:
                self.links.append(value)


def broken_links(page):
    collector = LinkCollector()
    collector.feed(page.read_text(encoding="utf-8"))
    broken = []
    for link in collector.links:
        url = urlparse(link)
        if url.scheme or url.netloc or not url.path:
            continue
        target = (page.parent / unquote(url.path)).resolve()
        if target.is_dir():
            target = target / "index.html"
        if not target.exists():
            broken.append(link)
    return broken


def main():
    with tempfile.TemporaryDirectory() as tmp:
        out_dir = Path(tmp)
        subprocess.run(
            ["sphinx-build", "-q", "-W", "-b", "dirhtml", "docs", str(out_dir)],
            check=True,
        )
        broken = broken_links(out_dir / "about" / "index.html")
    for link in broken:
        print(f"Broken link in docs/about.md: {link}")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
