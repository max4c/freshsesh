class FormulaManager:
    def __init__(self):
        self.formulas = set()

    def add_formula(self, formula):
        self.formulas.add(formula)

    def remove_formula(self, formula):
        self.formulas.discard(formula)

    def list_formulas(self):
        return list(self.formulas)
