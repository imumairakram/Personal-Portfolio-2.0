# Umair Akram - Portfolio

A complete modern portfolio website for **Umair Akram**.

All interactive features, animations (GSAP, Lenis Smooth Scroll, dynamic ticker marquee), styles, responsive layouts, resume downloads, modal views, and dynamic API content are preserved.

---

## 📁 Project Structure

```text
├── index.html              # Main HTML entry point
├── favicon.svg             # Website favicon
├── Umair_Akram_Resume.pdf  # Downloadable Resume PDF
├── api_content.json        # Dynamic portfolio data (Profile, Experience, Projects, Skills, etc.)
├── api/
│   └── content             # Static API fallback
├── assets/
│   ├── index-CtTLdPUf.js   # Main JavaScript entry module
│   ├── index-CjgW5SaR.css  # Core styling
│   ├── App-BIMeU_XJ.js     # React application logic and components
│   ├── App-Bc1U_rYp.css    # Full application styling & animations
│   ├── Admin-CmRhcYXO.js   # Admin bundle
│   ├── Admin-fI_-rnaT.css  # Admin styling
│   └── Icon-CLz2lwdt.js    # Lucide icons bundle
├── vercel.json             # Vercel deployment & routing config
├── _redirects              # Netlify / static redirects
└── README.md
```

---

## 🚀 How to Run Locally

You can preview the website locally using any static server:

### Option 1: Using Node / NPX (Recommended)
```bash
npx serve .
```

### Option 2: Using Python's built-in HTTP server
```bash
python -m http.server 8000
```
Then open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 🌐 Deployment
This project is configured for automated deployment on **Vercel** via `vercel.json` and Netlify via `_redirects`.
