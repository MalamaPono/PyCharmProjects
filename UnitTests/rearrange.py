import re

def rearrange_name(name):
    assert type(name) == str, "the input name must be a string"

    result = re.search(r"^([\w .]*), ([\w .]*)$",name)
    if result is None:
        return name
    return "{} {}".format(result[2],result[1])