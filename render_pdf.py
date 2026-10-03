import os
import subprocess

html_path = os.path.abspath("generate_portfolio_doc.html")
pdf_path = os.path.abspath(os.path.join("public", "Portofolio_Muhamad_Nizar_Nurfalah.pdf"))

chrome_paths = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
]

browser_exe = None
for p in chrome_paths:
    if os.path.exists(p):
        browser_exe = p
        break

print("Using browser:", browser_exe)
print("HTML path:", html_path)
print("PDF target:", pdf_path)

cmd = [
    browser_exe,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    f"file:///{html_path.replace(os.sep, '/')}"
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", res.returncode)
print("Stdout:", res.stdout)
print("Stderr:", res.stderr)

if os.path.exists(pdf_path):
    print("SUCCESS: PDF created! Size:", os.path.getsize(pdf_path), "bytes")
else:
    print("FAILED to create PDF")
