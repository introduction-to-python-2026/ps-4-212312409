def split_before_each_uppercases(formula):
    split_formula = []
    start = 0
    end = 0   
    
    if formula == "":
      return split_formula

    for i in range(1, len(formula)):
        if formula[i].isupper():
            end = i
            split_formula.append(formula[start:end])
        start = end
    
    split_formula.append(formula[start:])
    return split_formula

def split_at_first_digit(formula):
    for i in range(len(formula)):
        if formula[i].isdigit():
            return formula[:i], int(formula[i:])
    
    return formula, 1
