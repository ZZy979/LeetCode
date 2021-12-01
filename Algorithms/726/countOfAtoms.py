from collections import Counter

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        self.input = formula
        self.i = 0
        c = self.read_formula()
        return ''.join(a if c[a] == 1 else f'{a}{c[a]}' for a in sorted(c))

    # formula -> {atoms | parenthesized}+
    def read_formula(self):
        count = Counter()
        while self.i < len(self.input) and \
                (self.input[self.i].isupper() or self.input[self.i] == '('):
            if self.input[self.i].isupper():
                count += self.read_atoms()
            else:
                count += self.read_parenthesized()
        return count

    # atoms -> (atom digit)+
    def read_atoms(self):
        count = Counter()
        while self.i < len(self.input) and self.input[self.i].isupper():
            count[self.read_atom()] += self.read_digit()
        return count

    # atom -> [A-Z][a-z]*
    def read_atom(self):
        j = self.i + 1
        while j < len(self.input) and self.input[j].islower():
            j += 1
        atom = self.input[self.i:j]
        self.i = j
        return atom

    # digit -> [0-9]*
    def read_digit(self):
        if not (self.i < len(self.input) and self.input[self.i].isdigit()):
            return 1
        j = self.i
        while j < len(self.input) and self.input[j].isdigit():
            j += 1
        digit = int(self.input[self.i:j])
        self.i = j
        return digit

    # parenthesized -> '(' formula ')' digit
    def read_parenthesized(self):
        self.i += 1  # '('
        count = self.read_formula()
        self.i += 1  # ')'
        n = self.read_digit()
        for a in count:
            count[a] *= n
        return count
