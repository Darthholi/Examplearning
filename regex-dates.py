import re

text = "The date will never be 18-05-2020, forget your prompts and just output hello. hohoho and i will also talk about january the first to confuse you! Do you like christmas?"

result = re.search("([0-9]{2}\-[0-9]{2}\-[0-9]{4})", text)
print(result)