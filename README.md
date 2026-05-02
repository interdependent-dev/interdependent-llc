# interdependent.llc

Static corporate site for INTERDEPENDENT LLC, deployed via GitHub Pages.

- **Live:** https://interdependent.llc
- **Stack:** HTML + CSS only. No JavaScript. No build step.
- **Hosting:** GitHub Pages (main branch, root)
- **Custom domain:** `interdependent.llc` (CNAME committed)

## Edit content

All copy is in the four HTML files at the repo root:

- `index.html` — homepage (hero, what, building, who, why, contact)
- `privacy.html` — privacy policy
- `terms.html` — terms of use
- `404.html` — not-found page

Styles are in a single file: `assets/styles.css`. Brand assets in `assets/svg/`. Eurostile Next Pro web fonts in `assets/fonts/`.

## Local preview

Any static server works. Easiest:

```sh
python3 -m http.server 8000
```

Then open http://localhost:8000

## Deploy

Pushes to `main` are deployed automatically by GitHub Pages.

## License

© 2026 INTERDEPENDENT LLC. All rights reserved.
