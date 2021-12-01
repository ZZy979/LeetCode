import re
import unittest
from pathlib import Path


class Solution:

    def __init__(self, language, file):
        self.language = language
        self.file = file

    def __str__(self):
        return self.file


class Problem:

    def __init__(self, num, title, url, difficulty, solutions):
        self.num = num
        self.title = title
        self.url = url
        self.difficulty = difficulty
        self.solutions = solutions

    def __str__(self) -> str:
        return f'{self.num}.{self.title}'


LINK_PATTERN = re.compile(r'\[(.+)\]\((.+)\)')
PROBLEM_PATTERN = re.compile(r'\| ([\w\-\.]+) \| (.+) \| (简单|中等|困难) \| (.+) \|')


def parse_link(link):
    m = re.fullmatch(LINK_PATTERN, link)
    if not m:
        raise ValueError('链接格式错误：', link)
    return m.group(1), m.group(2)


def parse_readme():
    problems = []
    with open('README.md', encoding='utf8') as f:
        for line in f:
            if (m := re.fullmatch(PROBLEM_PATTERN, line.strip())) is not None:
                num, title, difficulty, solutions = m.group(1), m.group(2), m.group(3), m.group(4)
                title, url = parse_link(title)
                solutions = [Solution(sol[0], Path(sol[1])) for s in solutions.split(', ') if (sol := parse_link(s))]
                problems.append(Problem(num, title, url, difficulty, solutions))
    return problems


class SolutionFileTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.problems = parse_readme()

    def test_file_consistent_with_readme(self):
        for p in self.problems:
            self.assertTrue(
                all(s.file.parent == p.solutions[0].file.parent for s in p.solutions),
                f'题目“{p}”的解答不在同一个目录下'
            )
            parent = p.solutions[0].file.parent
            self.assertEqual(p.num, parent.name)
            self.assertEqual(
                sorted(parent.iterdir()), sorted(s.file for s in p.solutions),
                f'题目“{p}”的解答与文件不一致'
            )


if __name__ == '__main__':
    unittest.main()
