story = "Katherine went to the concert to see 'Catheryn and the Catheryns'. She ran into her friend Katharine, who introduced Katherine to her friend Catherine. Together they enjoyed the concert while texting inaudible snippets to their mutual friend, Kathrin. Their mercurial friend, katharine, felt left out."
In [15]:

import re
attempt1 = re.compile('\w+ath\w+')
match1 = re.findall(attempt1,story)
print(match1)
print(len(match1))
​
['Katherine', 'Catheryn', 'Catheryns', 'Katharine', 'Katherine', 'Catherine', 'Kathrin', 'katharine']
8
In [17]:

attempt2 = re.compile('[ck]+ath[aey]?r[eiy]ne*\w*', re.I)
match2 = re.findall(attempt1,story)
print(match2)
print(len(match2))
['Katherine', 'Catheryn', 'Catheryns', 'Katharine', 'Katherine', 'Catherine', 'Kathrin', 'katharine']
8
