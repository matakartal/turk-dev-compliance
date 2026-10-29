#!/usr/bin/env python3
"""Her evals/<örnek>/ için audit.py çıktısındaki bulgu türlerini expected.json ile karşılaştırır."""
import json, os, subprocess, sys
here = os.path.dirname(os.path.abspath(__file__))
audit = os.path.join(here, "..", "skills", "turk-dev-compliance", "scripts", "audit.py")
fail = 0
for name in sorted(os.listdir(here)):
    d = os.path.join(here, name)
    if not os.path.isdir(d):
        continue
    exp = set(json.load(open(os.path.join(d, "expected.json"))))
    out = subprocess.run([sys.executable, "-I", audit, d, "--json"], capture_output=True, text=True, check=True).stdout
    got = {f["tur"] for f in json.loads(out)}
    ok = got == exp
    fail += not ok
    print(("OK  " if ok else "FAIL"), name, "" if ok else f"eksik={sorted(exp-got)} fazla={sorted(got-exp)}")
sys.exit(1 if fail else 0)
