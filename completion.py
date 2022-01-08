import anybadge
import os

os.remove('completion_badge.svg')
completion = round(100*len(os.listdir("masks")) / len(os.listdir("imgs")))

# Define thresholds: <2=red, <4=orange <8=yellow <10=green
thresholds = {25: 'orange',
             50: 'yellow',
             75: 'green',
             100: 'yellow'}

badge = anybadge.Badge('completed', str(completion) + "%", thresholds=thresholds)
badge.write_badge('completion_badge.svg')
