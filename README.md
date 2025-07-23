# M-layer Website

This repository contains the source for the **M-layer** project website built with [Jekyll](https://jekyllrb.com/).

## Project Purpose

The site documents how the M-layer uses digital identifiers to annotate numerical data. These identifiers remove the ambiguity found in traditional unit notation and are registered so that systems can reliably transform data between different expressions. The project is coordinated by the NCSLI Measurement Information Infrastructure (MII) technical committee and is led by the Measurement Standards Laboratory of New Zealand (MSL) with technical support from Fluke Calibration.

## Prerequisites

You can preview the site using either Docker or a local Ruby environment with Bundler.

- **Docker** – requires Docker and `docker-compose`.
- **Ruby/Bundler** – requires Ruby with Bundler installed.

## Local Preview

Run one of the following options from the repository root:

```bash
docker-compose up
```

or

```bash
bundle install
bundle exec jekyll serve
```

The site will be served on <http://localhost:4000>.

## Repository Structure

- `_posts/` – blog posts and project news.
- `pages/` – main site content such as documentation and licenses.
- `_data/` – YAML files for glossary terms, navigation and other data.
- `_includes/` – reusable snippets included in pages.
- `_layouts/` – layout templates used by Jekyll.
- `css/`, `js/`, `fonts/`, `images/` – static assets for the site.

## Editing Content

Edit an existing page under `pages/` or create new posts in `_posts/`. After modifying files, commit the changes and rebuild the site using one of the preview methods above to verify your updates.

### Creating Tags

Use the provided `createtag` script from the project root to create tag pages and update `_data/tags.yml`:

```bash
./createtag mytag
```

The script will prompt for a title and generate `pages/tags/tag_mytag.md` while appending the tag to `_data/tags.yml`.

## License

This project is licensed under the [Apache License 2.0](LICENSE). The sidebar navigation includes components covered by `LICENSE-BSD-NAVGOCO.txt`.

