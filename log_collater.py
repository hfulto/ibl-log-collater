from simplegmail import Gmail
from simplegmail.query import construct_query
from pathlib import Path
import re

def get_good_bit(msg):

    retval = msg.split("Always try to include distinguishing memory hooks.")[1]

    retval = retval.split("Student Statement:")[0]

    retval = re.sub(r'1\. Identify[\s\S]*?\]', '1. Identify realization/experience', retval)

    retval = re.sub(r'2\. In[\s\S]*?\]', '2. Summarize realization/experience', retval)

    retval = re.sub(r'3\. As[\s\S]*?\]', '3. Innovate', retval)

    retval = re.sub(r'4\.[\s\S]*?\]', '4. Mechanism for realization/experience', retval)

    retval = re.sub(r'5\.[\s\S]*?\]', '5. Mechanism success measurement', retval)

    return retval

Path("./logs").mkdir(exist_ok=True)

gmail = Gmail()

query = construct_query({'sender': 'forms-receipts-noreply@google.com', 'newer_than': (6, "month")})

messages = gmail.get_messages(query=query)

checked = []

for message in messages:
    if("Clayton Log Books" in message.subject):

        if(message.subject in checked):
            continue

        checked.append(message.subject)

        with open(file=f"./logs/{message.subject}.txt",mode="w",encoding="utf-8-sig") as f:
            f.write(get_good_bit(message.plain))

