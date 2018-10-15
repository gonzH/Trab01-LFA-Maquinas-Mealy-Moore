'''
    CONVERSAO DE S-EXPRESSION EM LISTA
    FONTE: https://rosettacode.org/wiki/S-Expressions#Python

'''

import re

dbg = False

term_regex = r'''(?mx)
    \s*(?:
        (?P<brackl>\()|
        (?P<brackr>\))|
        (?P<num>\-?\d+\.\d+|\-?\d+)|
        (?P<sq>"[^"]*")|
        (?P<s>[^(^)\s]+)
       )'''


def parse_sexp(sexp):
    stack = []
    out = []
    if dbg: print("%-6s %-14s %-44s %-s" % tuple("term value out stack".split()))
    for termtypes in re.finditer(term_regex, sexp):
        term, value = [(t, v) for t, v in termtypes.groupdict().items() if v][0]
        if dbg: print("%-7s %-14s %-44r %-r" % (term, value, out, stack))
        if term == 'brackl':
            stack.append(out)
            out = []
        elif term == 'brackr':
            assert stack, "Trouble with nesting of brackets"
            tmpout, out = out, stack.pop(-1)
            out.append(tmpout)
        elif term == 'num':
            v = float(value)
            if v.is_integer(): v = int(v)
            out.append(v)
        elif term == 'sq':
            out.append(value[1:-1])
        elif term == 's':
            out.append(value)
        else:
            raise NotImplementedError("Error: %r" % (term, value))
    assert not stack, "Trouble with nesting of brackets"
    return out[0]


def print_sexp(exp):
    out = ''
    if type(exp) == type([]):
        out += '(' + ' '.join(print_sexp(x) for x in exp) + ')'
    elif type(exp) == type('') and re.search(r'[\s()]', exp):
        out += '"%s"' % repr(exp)[1:-1].replace('"', '\"')
    else:
        out += '%s' % exp
    return out


if __name__ == '__main__':

    #TESTE
    sexp1 = ''' (mealy
                (symbols-in c d)
                (symbols-out 0 1)
                (states q0 q1 q2 q3)
                (start q0)
                (finals q2)
                (trans
                (q0 q2 c 1) 
                (q0 q3 d 0) 
                (q1 q0 c 0) 
                (q1 q1 d 1)  
                (q2 q1 c 1) 
                (q2 q2 d 0) 
                (q3 q2 c 0) 
                (q3 q0 d 1)))'''


    print('Input S-expression: %r' % (sexp1,))
    parsed = parse_sexp(sexp1)
    print("\nParsed to Python:", parsed)

    print("\nThen back to: '%s'" % print_sexp(parsed))

    sexp2 = ''' (moore
                (symbols-in A B)
                (symbols-out S A B O)
                (states q0 q1 q2 q3 q4)
                (start q0)
                (finals q4)
                (trans
                 (q0 q1 A)
                 (q1 q2 B)
                 (q2 q3 A)
                 (q3 q2 B)
                 (q2 q4 B))
                (out-fn
                 (q0 ())
                 (q1 S)
                 (q2 A)
                 (q3 B)
                 (q4 O)))'''
    print('\n\nInput S-expression: %r' % (sexp2,))
    parsed = parse_sexp(sexp2)
    print("\nParsed to Python:", parsed)
    print("\n", parsed[6][1])
    print("\nThen back to: '%s'" % print_sexp(parsed))
