import ast
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
METADATA_PATH = ROOT / "metadata" / "submissions.json"
SOLUTIONS_DIR = ROOT / "solutions"


def load_submissions():
    return json.loads(METADATA_PATH.read_text(encoding="utf-8"))


def test_manifest_contains_fourteen_unique_full_score_python_submissions():
    submissions = load_submissions()

    assert len(submissions) == 14
    assert len({item["problem_id"] for item in submissions}) == 14
    assert all(item["score"] == 100 for item in submissions)
    assert all(item["language"] == "Python 3" for item in submissions)


def test_each_manifest_entry_has_one_matching_solution_file():
    submissions = load_submissions()
    expected = {ROOT / item["source_file"] for item in submissions}
    actual = set(SOLUTIONS_DIR.glob("*.py"))

    assert actual == expected
    assert all(path.is_file() and path.stat().st_size > 0 for path in expected)


def test_solution_hashes_match_the_export_manifest():
    for item in load_submissions():
        source = (ROOT / item["source_file"]).read_bytes()
        assert hashlib.sha256(source).hexdigest() == item["sha256"]


def test_all_solutions_have_valid_python_syntax():
    for item in load_submissions():
        path = ROOT / item["source_file"]
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def test_readme_indexes_every_solution():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    for item in load_submissions():
        assert item["title"] in readme
        assert item["orac_url"] in readme
        assert item["source_file"] in readme


def test_repository_does_not_contain_common_secret_markers():
    forbidden = (
        "session" + "id=",
        "gh" + "p_",
        "github" + "_pat_",
        "BEGIN PRIVATE" + " KEY",
    )
    ignored_parts = {".git", ".pytest_cache", "__pycache__"}
    inspected = [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and not ignored_parts.intersection(path.parts)
    ]

    for path in inspected:
        text = path.read_text(encoding="utf-8")
        assert not any(marker in text for marker in forbidden)
        assert re.search(r"(?i)password\s*=\s*['\"][^'\"]+", text) is None
