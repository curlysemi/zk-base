def sz(n, s, o = 0):
    return ', '.join([n + str(i + o) for i in range(s)])

def var(name, offset = 0):
    try:
        i = name.index('X')
        clean_name = name[0:i]
    except:
        clean_name = name
    return '    ' + sz(clean_name, 128, offset) + ' = unpack128(' + name + ')\n'

def call(func, arg = [], res = None, res_size = None):
    line = '    '
    if res:
        if res_size:
            line = line + sz(res, res_size) + ' = '
        else:
            line = line + res + ' = '
    line = line + func + '(' + (', '.join(arg)) + ')\n'
    return line

def args(name, size):
    return [name + str(i) for i in range(size)]

def assert_(left, right, size):
    return '\n'.join(['    ' + left + str(i) + ' == ' + right + str(i) for i in range(size)]) + '\n'

def return_(vals):
    return '    return ' + ','.join(vals) + '\n'

HEAD = """import "PACKING/unpack128"
import "LIBSNARK/sha256compression"

def main(private field pX0, private field pX1, private field pX2, private field pX3, field hX0, field hX1) -> (field):
"""

lines = [
    HEAD,
    var('pX0'),
    var('pX1', 128),
    var('pX2', 256),
    var('pX3', 384),
    var('hX0'),
    var('hX1', 128),
    call('sha256compression', args('p', 512), 'c', 256),
    assert_('h', 'c', 256),
    return_(['1'])
]

print(''.join(lines))