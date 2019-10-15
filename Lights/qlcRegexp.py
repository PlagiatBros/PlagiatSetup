# encoding: utf-8
import re

def osc_to_regexp_transliteration(match):
    s = match.group(0)
    s = s.replace("{","(")
    s = s.replace("}",")")
    s = s.replace(",","|")
    return s

osc_to_regexp_re = re.compile(r"\{[^\}]*\}")

osc_to_regexp_patterns = {
    r"\?": ".",
    r"\*": ".*",
    r"\[!([^\]]*)\]": r"[^\1]",
    r"\$": r"\$",
    r"\^": r"\^",
    r"\\": r"\\"
}

def osc_to_regexp(address):
    """
    Convert OSC 1.1 compliant address to regexp pattern standards
    Escape ^, $ (start/end of string delimiters) and \ (escape char)
    ?           -> .?
    [!a-Z]      -> [^a-Z]
    {foo,bar}   -> (foo|bar)

    Params:
    address : str

    Borrowed from pyoChainsaw @ https://framagit.org/groolot-association/pyoChainsaw
    Copyleft Gregory David & JE Doucet (GNU GPLv3)
    """

    for pattern, repl in osc_to_regexp_patterns.items():
        address = re.sub(pattern, repl, address)

    return re.compile("^" + re.sub(osc_to_regexp_re, osc_to_regexp_transliteration, address) + "$")
