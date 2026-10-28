import re
import subprocess
import unittest
from html.parser import HTMLParser

from package_site import ROOT, ResourceCheck


class Elements(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.guide_minutes = []
        self.logos = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if "data-minutes" in attrs:
            self.guide_minutes.append(int(attrs["data-minutes"]))
        if tag == "img" and attrs.get("alt") == "Microsoft":
            self.logos.append(attrs.get("src", ""))


class WorkshopTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.elements = Elements()
        cls.elements.feed(cls.html)

    def test_resources_are_embedded(self):
        ResourceCheck().feed(self.html)
        self.assertNotRegex(self.html, r'@import\b|url\(\s*["\']?https?://')
        self.assertEqual(len(self.elements.logos), 2)
        self.assertTrue(all(src.startswith("data:image/png;base64,") for src in self.elements.logos))

    def test_unique_ids(self):
        self.assertEqual(len(self.elements.ids), len(set(self.elements.ids)))

    def test_timing_includes_opening_and_conclusion(self):
        self.assertEqual(self.elements.guide_minutes, [2, 5, 3, 4, 5, 4, 9, 4, 6, 3])
        self.assertEqual(sum(self.elements.guide_minutes), 45)
        self.assertEqual(
            re.findall(r'Acte \d{2} · (\d+) min', self.html),
            ["4", "3", "5", "4", "9", "6", "5", "4"],
        )

    def test_javascript_syntax(self):
        scripts = re.findall(r"<script[^>]*>(.*?)</script>", self.html, re.S)
        self.assertEqual(len(scripts), 3)
        for script in scripts:
            result = subprocess.run(
                ["node", "--check", "--input-type=commonjs"],
                input=script, text=True, encoding="utf-8", capture_output=True, timeout=15,
            )
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_student_prompts_and_print_representation(self):
        self.assertEqual(len(re.findall(r'data-copy-prompt="', self.html)), 3)
        self.assertIn("printable.textContent = field.value", self.html)
        self.assertIn("dialog.showModal()", self.html)
        self.assertNotIn("buildFake();", self.html)
        self.assertNotRegex(self.html, r'class="quiz-card"[^>]+onclick=')


if __name__ == "__main__":
    unittest.main()
