import os
from datetime import datetime

easy = medium = hard = total = 0
rows = []

for folder in sorted(os.listdir(".")):
    if not os.path.isdir(folder):
        continue

    if folder.startswith(".") or folder == "scripts":
        continue

    readme = os.path.join(folder, "README.md")

    difficulty = ""

    if os.path.exists(readme):
        text = open(readme, encoding="utf8").read().lower()

        if "easy" in text:
            easy += 1
            difficulty = "🟢 Easy"

        elif "medium" in text:
            medium += 1
            difficulty = "🟡 Medium"

        elif "hard" in text:
            hard += 1
            difficulty = "🔴 Hard"

    total += 1

    rows.append(f"- {folder} ({difficulty})")

template = open("README.template.md", encoding="utf8").read()

template = template.replace("{{TOTAL}}", str(total))
template = template.replace("{{EASY}}", str(easy))
template = template.replace("{{MEDIUM}}", str(medium))
template = template.replace("{{HARD}}", str(hard))

template = template.replace(
    "{{PROBLEMS}}",
    "\n".join(rows[::-1][:10])
)

template = template.replace(
    "{{DATE}}",
    datetime.now().strftime("%d %B %Y %H:%M UTC")
)

open("README.md","w",encoding="utf8").write(template)
