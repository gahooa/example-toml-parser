# vim:fileencoding=utf-8:ts=4:sw=4:sts=4:expandtab


import toml
import rich.pretty


with open('data.toml', 'rt') as f:
    data = f.read()

rich.pretty.pprint(toml.loads(data))



