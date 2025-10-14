import argparse
from pathlib import Path
from collections import Counter
import re

# الگوی پیدا کردن کلمات فارسی و انگلیسی
WORD_RE = re.compile(r"[A-Za-z\u0600-\u06FF]+")

def analyze_text(text: str):
    lines = text.splitlines()
    words = WORD_RE.findall(text)
    chars = len(text)
    counts = Counter([w.lower() for w in words])
    top10 = counts.most_common(10)

    return {
        "lines": len(lines),
        "words": len(words),
        "chars": chars,
        "top10": top10
    }

def main():
    parser = argparse.ArgumentParser(description="📊 ابزار تحلیل متن ساده")
    parser.add_argument("--file", "-f", required=True, help="مسیر فایل متنی")
    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"❌ فایل '{file_path}' پیدا نشد")
        return

    text = file_path.read_text(encoding="utf-8", errors="ignore")
    result = analyze_text(text)

    print("📊 نتیجه‌ی تحلیل:")
    print(f"- تعداد خطوط: {result['lines']}")
    print(f"- تعداد کلمات: {result['words']}")
    print(f"- تعداد حروف: {result['chars']}")
    print("- ۱۰ واژه پرتکرار:")
    for i, (w, c) in enumerate(result['top10'], start=1):
        print(f"  {i}. {w} ({c})")

if __name__ == "__main__":
    main()
