"""Embed the official logo and export the same standalone HTML as GitHub Pages."""

import argparse
import base64
from html.parser import HTMLParser
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent


class ResourceCheck(HTMLParser):
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        resource = attrs.get("src")
        if tag == "link" and attrs.get("rel") == "stylesheet":
            resource = attrs.get("href")
        if resource and not resource.startswith("data:"):
            raise ValueError(f"Non-embedded resource in <{tag}>: {resource}")


def package():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--export", type=Path, help="New destination file; never overwritten")
    args = parser.parse_args()
    if args.export and args.export.exists():
        parser.error(f"Export already exists: {args.export}")

    html = (ROOT / "index.html").read_text(encoding="utf-8")
    logo = base64.b64encode((ROOT / "microsoft-logo.png").read_bytes()).decode("ascii")
    html, count = re.subn(
        r'(<img src=")(?:microsoft-logo\.png|data:image/png;base64,[^"]+)(" alt="Microsoft")',
        lambda match: match[1] + "data:image/png;base64," + logo + match[2],
        html,
    )
    if count != 2:
        raise ValueError(f"Expected two Microsoft signatures, found {count}")
    ResourceCheck().feed(html)
    if re.search(r'@import\b|url\(\s*["\']?https?://', html):
        raise ValueError("External CSS resource found")
    (ROOT / "index.html").write_text(html, encoding="utf-8", newline="\n")
    if args.export:
        args.export.write_text(html, encoding="utf-8", newline="\n")
        print(f"Standalone HTML: {args.export.resolve()}")
    print(f"Packaged {len(html.encode('utf-8')):,} bytes; all resources embedded.")


if __name__ == "__main__":
    package()
