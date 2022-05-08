from z3 import Int
from z3 import Optimize
from z3 import sat

# 898 pokemon
# 197: umbreon (index 198)

for length in range(5, 15):
    opt = Optimize()

    ints = []

    for i in range(length):
        int_i = Int(f'X_{i}')
        opt.add(int_i >= ord('a'))
        opt.add(int_i <= ord('z'))
        ints.append(int_i)

    sum_v = Int('sum')
    opt.add(sum_v == sum(ints))
    opt.add(((sum_v + 244) % 898 + 1) == 197)

    if opt.check() == sat:
        print('found an answer!')
        model = opt.model()
        print(''.join(chr(model[t].as_long()) for t in ints))
