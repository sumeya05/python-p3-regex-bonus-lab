import re

# Matches only the 3 required sentences inside a larger multi-line block
my_regex = re.compile(r"[A-Z][A-Za-z\s',]+day[A-Za-z\s',]*[.?]")
