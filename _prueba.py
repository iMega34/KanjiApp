
from jamdict import Jamdict

jam = Jamdict()

# result = jam.lookup('水曜%')
result = jam.lookup('帰%る')

for entry in result.entries:
    print(entry)
