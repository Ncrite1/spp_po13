import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timezone
from collections import Counter

# ====== 1. Ввод темы ======
topic = input("Введите тему для анализа: ")
print(f'Анализируем 100 популярных репозиториев по теме "{topic}"...')

# ====== 2. GitHub API ======
url = "https://api.github.com/search/repositories"
params = {
    "q": topic,
    "sort": "stars",
    "order": "desc",
    "per_page": 100
}

response = requests.get(url, params=params)

if response.status_code != 200:
    print("Ошибка запроса к GitHub API")
    exit()

data = response.json()["items"]

# ====== 3. Сбор данных ======
repos = []

for repo in data:
    repos.append({
        "name": repo["full_name"],
        "language": repo["language"] if repo["language"] else "Unknown",
        "stars": repo["stargazers_count"],
        "forks": repo["forks_count"],
        "issues": repo["open_issues_count"],
        "updated_at": repo["updated_at"]
    })

df = pd.DataFrame(repos)

# ====== 4. Анализ ======

# --- Популярность языков ---
language_counts = Counter(df["language"])
total = sum(language_counts.values())

language_percent = {
    lang: round(count / total * 100, 2)
    for lang, count in language_counts.items()
}

sorted_languages = sorted(language_percent.items(), key=lambda x: x[1], reverse=True)

print("\nСамые популярные языки:")
for lang, percent in sorted_languages[:5]:
    print(f"- {lang} ({percent}%)")

# --- Самый популярный репозиторий ---
top_repo = df.loc[df["stars"].idxmax()]
print(f'\nСамый звёздный репозиторий: "{top_repo["name"]}" ({top_repo["stars"]} звёзд)')

# --- Средние форки ---
avg_forks = df["forks"].mean()
print(f"Среднее количество форков: {round(avg_forks, 1)}")

# --- Анализ "старения" ---
df["updated_at"] = pd.to_datetime(df["updated_at"])
now = datetime.now(timezone.utc)

df["days_since_update"] = (now - df["updated_at"]).dt.days

old_repos = df[df["days_since_update"] > 365]
percent_old = len(old_repos) / len(df) * 100

print(f"{round(percent_old)}% репозиториев не обновлялись больше года!")

# ====== 5. Визуализация ======
sns.set(style="whitegrid")

# --- Диаграмма языков ---
plt.figure(figsize=(10, 6))
top_langs = dict(sorted_languages[:10])

sns.barplot(
    x=list(top_langs.values()),
    y=list(top_langs.keys())
)

plt.title(f"Популярные языки ({topic})")
plt.xlabel("Процент")
plt.ylabel("Язык")
plt.tight_layout()
plt.savefig("languages.png")

# --- Популярность (звезды vs форки) ---
plt.figure(figsize=(8, 6))

plt.scatter(df["stars"], df["forks"])

plt.title("Популярность репозиториев")
plt.xlabel("Звезды")
plt.ylabel("Форки")
plt.tight_layout()
plt.savefig("popularity.png")

# --- Старение репозиториев ---
plt.figure(figsize=(8, 6))

sns.histplot(df["days_since_update"], bins=20)

plt.title("Возраст последнего обновления (в днях)")
plt.xlabel("Дни")
plt.ylabel("Количество репозиториев")
plt.tight_layout()
plt.savefig("aging.png")

print('\nГрафики сохранены: languages.png, popularity.png, aging.png')