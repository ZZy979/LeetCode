import re
import unittest
from collections import defaultdict
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
PROBLEM_START_PATTERN = re.compile(r'\| [\w\-\.]+ \| \[')
PROBLEM_PATTERN = re.compile(r'\| ([\w\-\.]+) \| (.+) \| (简单|中等|困难) \| (.+) \|')


def parse_link(link):
    m = re.fullmatch(LINK_PATTERN, link)
    if not m:
        raise ValueError('链接格式错误：', link)
    return m.group(1), m.group(2)


def parse_solution_file(filename):
    problems = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            if re.match(PROBLEM_START_PATTERN, line):
                m = re.fullmatch(PROBLEM_PATTERN, line.strip())
                if m is None:
                    raise ValueError('题目格式错误，文件：', filename, '题目：', line)
                num, title, difficulty, solutions = m.group(1), m.group(2), m.group(3), m.group(4)
                title, url = parse_link(title)
                solutions = [Solution(sol[0], Path(sol[1])) for s in solutions.split(', ') if (sol := parse_link(s))]
                problems.append(Problem(num, title, url, difficulty, solutions))
    return problems


class SolutionFileTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.problems = defaultdict(list)
        for f in Path('.').glob('*/solutions*.md'):
            cls.problems[f.parent].extend(parse_solution_file(f))
        print('题目数量：', {str(p): len(cls.problems[p]) for p in cls.problems})

    def test_file_consistent_with_readme(self):
        for problem_set_dir, problems in self.problems.items():
            for p in problems:
                self.assertTrue(
                    len(set(s.file.parent for s in p.solutions)) == 1,
                    f'题目“{p}”的解答不在同一个目录下'
                )
                self.assertEqual(
                    p.num, p.solutions[0].file.parent.name,
                    f'题目“{p}”的解答所在目录与题号不一致'
                )
                problem_dir = problem_set_dir / p.solutions[0].file.parent
                self.assertSetEqual(
                    set(problem_dir.iterdir()), set(problem_set_dir / s.file for s in p.solutions),
                    f'题目“{p}”的解答与文件不一致'
                )

    def test_right_link(self):
        for problems in self.problems.values():
            for p in problems:
                self.assertFalse(p.url.endswith('submissions/'), f'题目“{p}”的链接不正确')


if __name__ == '__main__':
    unittest.main()
