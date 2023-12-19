import re
defs, parts = open("input.txt").read().split("\n\n")
defs = re.sub(r"([a-z]+)\{(.*?)\,([a-zRA]+)\}", "def _\\1(p):\n\t\\2\n\treturn _\\3(p)", defs)
defs = re.sub(r"([a-z]+)([<>])([0-9]+)\:([RAa-z]+)", "if p['\\1']\\2\\3:\n\t\treturn _\\4(p)", defs.replace(",", "\n\t"))
parts = re.sub(r"([a-z]+)\=", "'\\1':", parts.replace("\n", ","))
code = "_R = lambda p: 0\n_A = lambda p: sum(p.values())\n"+defs+"\nprint(sum(map(_in,["+parts+"])))"
exec(code)