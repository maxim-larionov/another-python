from sys import argv
from json import load as load_f

def m_replace(text, to_replace: dict):
  for key in to_replace.keys():
    text = text.replace(key, to_replace[key])
  return text

script_f, lang_f = files = [open(n) for n in argv[1:]]

lang_dict = load_f(lang_f)
script_text = script_f.read()

en_script_text = m_replace(script_text, lang_dict)
print(en_script_text)
exec(en_script_text)
