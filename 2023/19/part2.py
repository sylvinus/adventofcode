import re
defs = open("input.txt").read().split("\n\n")[0]
defs = re.sub(r"([a-z]+)\{(.*?)\,([a-zRA]+)\}", "def _\\1(p):\n\tr=0\n\t\\2\n\treturn r+_\\3(p)", defs)
defs = re.sub(r"([a-z]+)([<>])([0-9]+)\:([RAa-z]+)", "p2=dict(p)\n\tp2['\\1']=[x for x in p2['\\1'] if x\\2\\3]\n\tr+=_\\4(p2)\n\tp['\\1']=[x for x in p['\\1'] if not x\\2\\3]", defs.replace(",", "\n\t"))
code = "import math\n_I=lambda:set(range(1, 4001))\n_R = lambda p: 0\n_A = lambda p: math.prod(map(len,p.values()))\n"+defs+"\nprint(_in({'x':_I(), 'm':_I(), 'a':_I(), 's':_I()}))"
exec(code)