import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# 1️⃣ 대전일보 기사 가져오기
url = "https://www.daejonilbo.com/"  # 예제 URL
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 기사 제목과 링크 크롤링
articles = soup.select(".list-title a")  # 실제 선택자는 변경 필요
article_list = [{"title": a.text.strip(), "link": a["href"]} for a in articles]

# 2️⃣ 기사 본문 가져오기 (예제: 첫 번째 기사)
article_url = article_list[0]["link"]
article_response = requests.get(article_url)
article_soup = BeautifulSoup(article_response.text, "html.parser")
content = article_soup.select_one(".article-content").text.strip()  # 실제 선택자 변경 필요

# 3️⃣ AI 요약 (Hugging Face 사용)
summarizer = pipeline("summarization", model="google/pegasus-xsum")
summary = summarizer(content, max_length=100, min_length=30, do_sample=False)

print(f"📌 제목: {article_list[0]['title']}")
print(f"📖 원문: {content[:500]}...")  # 일부만 출력
print(f"📝 요약: {summary[0]['summary_text']}")
