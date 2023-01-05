from data_structures.queue import Queue


def multi_bracket_validation(str):
    stack = []
    new_str = ''.join(char for char in str if char in '{}[]()')

    for bracket in new_str:
        if bracket in ["(", "{", "["]:
            stack.append(bracket)
        else:
            if not stack:
                return False
            opening_bracket = stack.pop()
            if opening_bracket == "(":
                if bracket != ")":
                    return False
            if opening_bracket == "{":
                if bracket != "}":
                    return False
            if opening_bracket == "[":
                if bracket != "]":
                    return False
    if stack:
        return False
    return True

