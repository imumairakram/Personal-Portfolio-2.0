#!/usr/bin/env python3
"""
Complete Portfolio Scraper & Extractor
Target: https://firojynr.sentlas.in/
Extracts complete UI, scripts, stylesheets, fonts, assets, and API content.
"""

import os
import re
import json
import urllib.request
import urllib.parse

BASE_URL = "https://firojynr.sentlas.in"
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

def download(url_path, local_rel_path):
    full_url = urllib.parse.urljoin(BASE_URL, url_path)
    local_path = os.path.join(OUTPUT_DIR, local_rel_path)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    try:
        req = urllib.request.Request(full_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read()
            with open(local_path, "wb") as f:
                f.write(content)
        print(f"[SUCCESS] {url_path} -> {local_rel_path} ({len(content):,} bytes)")
        return content
    except Exception as e:
        print(f"[FAILED]  {url_path} -> {e}")
        return None

def main():
    print(f"[*] Starting extraction from {BASE_URL}...")
    
    # 1. Download index.html
    html_content = download("/", "index.html")
    if not html_content:
        print("[!] Failed to fetch index.html")
        return
    
    html_text = html_content.decode('utf-8', errors='ignore')
    
    # 2. Extract referenced scripts and links from HTML
    script_srcs = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html_text)
    link_hrefs = re.findall(r'<link[^>]+href=["\']([^"\']+)["\']', html_text)
    
    assets_to_fetch = set()
    for s in script_srcs:
        if not s.startswith("http"):
            assets_to_fetch.add(s)
    for l in link_hrefs:
        if not l.startswith("http"):
            assets_to_fetch.add(l)
            
    # 3. Fetch primary assets
    for asset in sorted(assets_to_fetch):
        download(asset, asset.lstrip("/"))
        
    # 4. Fetch dynamic API content
    api_content = download("/api/content", "api_content.json")
    
    # 5. Extract all dynamic chunks and static resources from JS files
    all_js_files = [f for f in os.listdir(os.path.join(OUTPUT_DIR, "assets")) if f.endswith(".js")]
    discovered_chunks = set()
    
    for js_file in all_js_files:
        js_path = os.path.join(OUTPUT_DIR, "assets", js_file)
        with open(js_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            
        # Find imports and map deps
        chunks = re.findall(r'[\'"`]([a-zA-Z0-9_\-]+\.(?:js|css))[\'"`]', content)
        chunks += re.findall(r'import\([\'"`]\./([^\'"`]+)[\'"`]\)', content)
        chunks += re.findall(r'assets/[a-zA-Z0-9_\-]+\.(?:js|css)', content)
        
        for c in chunks:
            if not c.startswith("/assets/"):
                c = "/assets/" + c if not c.startswith("assets/") else "/" + c
            discovered_chunks.add(c)
            
    for chunk in sorted(discovered_chunks):
        download(chunk, chunk.lstrip("/"))
        
    # 6. Fetch downloadable files like Resume
    download("/Firoj_Resume.pdf", "Firoj_Resume.pdf")
    download("/favicon.svg", "favicon.svg")
    
    print("\n[+] Scraping & Extraction Completed Successfully!")
    print(f"[+] All files saved to {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
