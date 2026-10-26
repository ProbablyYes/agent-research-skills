from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

class SkillContracts(unittest.TestCase):
    def test_frontmatter_and_unique_names(self):
        names = []
        for path in SKILLS.glob("*/SKILL.md"):
            content = path.read_text(encoding="utf-8")
            self.assertTrue(content.startswith("---\n"), path)
            self.assertRegex(content, r"(?m)^name: [a-z][a-z0-9-]+$")
            self.assertRegex(content, r"(?m)^description: .{25,}$")
            names.append(re.search(r"(?m)^name: (.+)$", content).group(1))
        self.assertEqual(len(names), 3)
        self.assertEqual(len(names), len(set(names)))

    def test_no_unapproved_paid_experiment(self):
        for path in SKILLS.glob("*/SKILL.md"):
            content = path.read_text(encoding="utf-8").lower()
            self.assertTrue("paid" in content and ("approval" in content or "authorization" in content), path)

if __name__ == "__main__":
    unittest.main()
