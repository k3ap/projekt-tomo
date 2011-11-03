import json

class Check:
    @staticmethod
    def initialize(parts):
        Check.parts = parts
        Check.current = None
        Check.part_counter = None

    @staticmethod
    def part():
        if Check.part_counter is None:
            Check.part_counter = 0
        else:
            Check.part_counter += 1
        Check.current = Check.parts[Check.part_counter]
        return Check.current.get('solution', '') != ''

    @staticmethod
    def error(msg):
        if 'errors' not in Check.current:
            Check.current['errors'] = []
        Check.current['errors'].append(msg)

    @staticmethod
    def challenge(x, k=None):
        if 'challenge' not in Check.current:
            Check.current['challenge'] = []
        Check.current['challenge'].append((str(k),str(Check.canonize(x))))

    @staticmethod
    def run(example, state, message=None, env={}, clean=lambda x: x):
        code = "\n".join(example)
        example = "\n".join(["    " + line for line in example])
        s = {}
        s.update(env)
        exec (code, globals(), s)
        for (x,v) in state.items():
            if x not in s:
                Check.error('Ukazi\n\n{0}\n\nne nestavijo spremenljivke {1}, a bi jo morali.'.format(example, x))
            elif clean(s[x]) != clean(v):
                Check.error('Ukazi\n\n{0}\n\nbi morali nastaviti {1} na {2},\na nastavijo {1} na {3}'.format(example, x, v, s[x]))

    @staticmethod
    def canonize(x, digits=6):
        if   type(x) is float: return round(x, digits)
        elif type(x) is complex: return complex(round(x.real, digits), round(x.imag, digits))
        elif type(x) is list: return list([Check.canonize(y) for y in x])
        elif type(x) is tuple: return tuple([Check.canonize(y) for y in x])
        elif type(x) is dict: return sorted([(Check.canonize(k), Check.canonize(v)) for (k,v) in x.items()])
        elif type(x) is set: return sorted([Check.canonize(y) for y in x])
        else: return x

    @staticmethod
    def compare(example, expected,
                message="Izraz {0} vrne {1!r} namesto {2!r} ({3}).",
                clean=(lambda x: x), env={},
                precision=1.0e-6, strict_float=False, strict_list=True):
        def comp(x,y):
            if x == y: return None
            elif (type(x) != type(y) and
                 (strict_float or not (type(y) is float and type(x) in [int,float])) and
                 (strict_list or not (type(y) in [list, tuple] and type(x) in [list, tuple]))):
                return "različna tipa"
            elif type(y) in [float,complex]:
                return ("numerična napaka" if abs(x-y) > precision else None)
            elif type(y) in [tuple,list]:
                if len(y) != len(x): return "napačna dolžina seznama"
                else:
                    for (u,v) in zip(x,y):
                        msg = comp(u,v)
                        if msg: return msg
                    return None
            elif type(y) is dict:
                if len(y) != len(x): return "napačna dolžina slovarja"
                else:
                    for (k,v) in y.items():
                        if k not in x: return "manjkajoči ključ v slovarju"
                        msg = comp(x[k], v)
                        if msg: return msg
                    return None
            else: return "različni vrednosti"

        local = locals()
        local.update(env)
        answer = eval(example, globals(), local)
        reason = comp(clean(answer), clean(expected))
        if reason: Check.error(message.format(example, answer, expected, reason))

    @staticmethod
    def equal(example, expected, message=None, clean=None, digits=6, env={}):
        if not message:
            message = 'Ukaz {0} vrne {1!r} namesto {2!r}.'
        local = locals()
        local.update(env)
        answer = eval(example, globals(), local)
        if not clean: clean = lambda x: Check.canonize(x,digits)
        if clean(answer) != clean(expected):
            Check.error(message.format(example, answer, expected))

    @staticmethod
    def num_equal(example, expected, digits=6):
        local = locals()
        local.update(env)
        answer = eval(example, globals(), local)
        if abs(answer - expected) > 10 ** (-digits):
            Check.error(message.format(example, answer, expected))

    @staticmethod
    def summarize():
        for i, part in enumerate(Check.parts):
            if not part['solution']:
                print('Podnaloga {0} je brez rešitve.'.format(i + 1))
            elif 'errors' in part:
                print('Podaloga {0} ni prestala vseh testov:'.format(i + 1))
                for e in part['errors']:
                    print("- {0}\n".format("\n  ".join(e.splitlines())))
            else:
                print('Podnaloga {0} je prestala vse teste.'.format(i + 1))

    @staticmethod
    def dump():
        return json.dumps(Check.parts)
