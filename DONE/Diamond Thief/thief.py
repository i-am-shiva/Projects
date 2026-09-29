# Clue 1 → The thief wore a red shirt.
# Clue 2 → The thief was seen between 9:30 and 10:00.

from datetime import datetime

suspects = {
    "Arjun": ["red shirt", "9:35 PM"],
    "Rahul": ["black shirt", "10:15 PM"],
    "Vikram": ["red shirt", "9:45 PM"],
    "Kiran": ["blue shirt", "9:30 PM"]
}
c1 = "red shirt"
lst = []
t1 = datetime.strptime("9:30 pm", "%I:%M %p").time()
t2 = datetime.strptime("10:00 pm", "%I:%M %p").time()
for name, clues in suspects.items():
    cluetime = datetime.strptime(clues[1], "%I:%M %p").time()
    if clues[0] == c1 and (t1 <= cluetime <= t2):
        lst.append(name)

print(lst)
