import ast,unittest
from pathlib import Path
class SourceTests(unittest.TestCase):
 def test_python_sources_parse(self):
  for path in Path("src").glob("*.py"):ast.parse(path.read_text(encoding="utf-8"),filename=str(path))
 def test_project_has_implementation(self):self.assertTrue(any(Path("src").glob("*.py")))
if __name__=="__main__":unittest.main()