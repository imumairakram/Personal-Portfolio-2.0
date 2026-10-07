# Umair Akram - Portfolio

A 1:1 complete portfolio website for **Umair Akram**.

All interactive features, animations (GSAP, Lenis Smooth Scroll, dynamic ticker marquee), styles, responsive layouts, resume downloads, modal views, and dynamic API content are preserved.

---

## 📁 Project Structure

```text
├── index.html              # Main HTML entry point
├── favicon.svg             # Website favicon
├── Firoj_Resume.pdf        # Downloadable Resume PDF
├── api_content.json        # Dynamic portfolio data (Profile, Experience, Projects, Skills, etc.)
├── api/
│   └── content             # Static API fallback for non-python hosts
├── assets/
│   ├── index-CtTLdPUf.js   # Main JavaScript entry module
│   ├── index-CjgW5SaR.css  # Core styling
│   ├── App-BIMeU_XJ.js     # React application logic and components
│   ├── App-Bc1U_rYp.css    # Full application styling & animations
│   ├── Admin-CmRhcYXO.js   # Admin bundle
│   ├── Admin-fI_-rnaT.css  # Admin styling
│   └── Icon-CLz2lwdt.js    # Lucide icons bundle
├── scrape_portfolio.py     # Python scraper script to re-extract or update assets
├── server.py               # Multi-threaded local Python web server
└── README.md
```

---

## 🚀 How to Run Locally

### Option 1: Using Python Server (Recommended)
Run the provided threaded server:
```bash
python server.py
```
Then open [http://localhost:8000](http://localhost:8000) in your browser.

---

### Option 2: Using Any Static Server
You can also use Node / NPX:
```bash
npx serve .
```
or Python's built-in module:
```bash
python -m http.server 8000
```

---

## 🔄 How to Re-Scrape / Update
To re-run the Python scraper and update all assets directly from the live URL:
```bash
python scrape_portfolio.py
```
