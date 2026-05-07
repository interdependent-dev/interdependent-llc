# interdependent.llc

Static governance site for INTERDEPENDENT LLC, deployed via GitHub Pages.

- **Live:** https://interdependent.llc
- **Hosting:** GitHub Pages (main branch, root)

## Edit the website copy

**You only ever need to touch one file:**

> [`content.md`](./content.md)

Open it. Edit any value. Commit and push. The site rebuilds and deploys automatically (~60 seconds).

The file has two halves:
1. **YAML frontmatter** at the top (everything between the `---` markers): all short fields, labels, navigation links, lists. Indentation matters — keep the existing spacing.
2. **Markdown body** below the second `---`: long-form prose paragraphs (about, leadership bio).

If you only edit prose, you'll never need to touch the YAML.

### Editing locally

```sh
cd /Users/camell/Documents/interdependent-llc
open content.md            # or open in any editor
git add content.md
git commit -m "update copy"
git push
```

### Editing on GitHub.com

Navigate to [`content.md` on GitHub](https://github.com/interdependent-dev/interdependent-llc/edit/main/content.md), edit in the browser, and click **Commit changes**. Works from a phone too.

## Recover a stable version

The first stable version is tagged `v1.0`. To restore:

```sh
git -C /Users/camell/Documents/interdependent-llc reset --hard v1.0
git -C /Users/camell/Documents/interdependent-llc push --force-with-lease
```

Or browse the frozen snapshot: <https://github.com/interdependent-dev/interdependent-llc/releases/tag/v1.0>

## How the build works (for reference)

You don't need to know this to edit copy — but in case you're curious:

- `content.md` is the source of truth for all editable text.
- `_template/index.html.j2` is a Jinja2 template; it knows about styling and structure.
- `build.py` reads `content.md`, renders the template, writes `index.html`.
- `.github/workflows/build.yml` runs `build.py` on every push to `main` (when `content.md` or the template changes) and commits the rebuilt `index.html` automatically.

The result is committed to the repo so GitHub Pages can serve plain static HTML — no client-side rendering, fast load, accessible without JS.

## Legal pages

`privacy.html` and `terms.html` are plain static HTML — edit those files directly when needed.

## Local build

```sh
python3 -m venv .venv
.venv/bin/pip install pyyaml jinja2
.venv/bin/python build.py
```

## License

© 2026 INTERDEPENDENT LLC. All rights reserved.
