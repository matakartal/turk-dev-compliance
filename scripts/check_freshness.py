#!/usr/bin/env python3
"""guncellik.md'deki 'Son toplu doğrulama' tarihi 6 aydan eskiyse hata verir."""
import datetime
import pathlib
import re
import sys

p = pathlib.Path(__file__).resolve().parent.parent / "skills/turk-dev-compliance/references/guncellik.md"
m = re.search(r"Son toplu doğrulama: \*\*(\d{4}-\d{2}-\d{2})\*\*", p.read_text(encoding="utf-8"))
if not m:
    sys.exit("guncellik.md içinde 'Son toplu doğrulama' tarihi bulunamadı")
age = (datetime.date.today() - datetime.date.fromisoformat(m.group(1))).days
print(f"Son doğrulama: {m.group(1)} ({age} gün önce)")
if age > 183:
    sys.exit("Doğrulama 6 aydan eski: referansları birincil kaynakta yeniden kontrol edin.")
