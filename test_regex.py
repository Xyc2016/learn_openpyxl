test_text = """
1 2
2312312  123123  2131231232

0.1 0.2 
0.01 0.02
0.10 0.20 0.15

1.1 1.2
1.01 1.02
1.10 1.20 1.15

1.2132321 

"""

import re

price_match = r"[0-9]{1,15}(\.[0-9]{1,2})?"
price_pattern = re.compile(price_match)

"中文"

s = "s"
