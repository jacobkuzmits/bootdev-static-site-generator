# Static Site Generator

A Python-based static site generator that converts Markdown to HTML. Built following the [Boot.dev static site generator course](https://www.boot.dev/courses/build-static-site-generator-python).

Takes Markdown files from `content/` and generates a static website in `docs/`. Supports all the usual Markdown stuff: headings, links, images, code blocks, lists, and blockquotes.

## Setup

Clone the repo and run:

```bash
./setup.sh
```

This installs a git hook that automatically builds the site for production before each commit.

## Configuration

Edit `config.json` to set your basepaths:

```json
{
  "basepath": {
    "local": "/",
    "production": "/bootdev-static-site-generator/"
  }
}
```

Change `production` to match your GitHub Pages URL (e.g., `/your-repo-name/` or just `/` for custom domains).

## Local Development

```bash
./main.sh
```

Builds the site and starts a server at `http://localhost:8888`.

Or build manually: `python3 src/main.py local`

## Production Build

The git hook handles this automatically, but you can manually build with:

```bash
./build.sh
```

Or: `python3 src/main.py production`

## Tests

```bash
./test.sh
```

## Structure

- `content/` - Markdown files
- `static/` - CSS and images
- `docs/` - Generated HTML (what GitHub Pages serves)
- `config.json` - Basepath settings
- `src/` - Python source
- `template.html` - HTML template

## Deployment

GitHub Pages serves the `docs/` directory. Push to main and it goes live.
