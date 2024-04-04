# Violi Lab Website

## Instructions for updating the website

Most pages are in markdown, which should be relatively easy to edit.
Some more advanced formatting will be in HTML or [Liquid](https://github.com/Shopify/liquid), but it should rarely be necessary to edit this content.

### Download the code for the website

Open the terminal, move to a directory that you want to use for the website files, and run the command `git clone git@github.com:violilab/violilab.github.io.git`.
This will pull the code from GitHub.

### Images

Images can be added to the `assets/img/` directory under the correct subdirectory.
- `headshots` is for images of lab members' faces
- `news` is for images that will be used in our news posts
- `outreach` is for images that will be on the "outreach" page
- `publication_preview` is for interesting images or graphical abstracts that are associated with a paper. These are usually only referenced through the `_bibliography/papers.bib` file.

### News

1. Copy a file from the `_news/` directory and give it a unique name.
1. Leave the `layout`, `inline`, and `related_posts` fields unchanged.
1. Update the `date` field to the date that you want to be displayed next to the news. This should not be in the future, or it will not show up on the website.
1. Change the `title` to the text that you want to display in the "news" section of the home page.
1. Update the `img` field to the name of a file in the `assets/img/news/` directory. You can either reference an existing image or upload a new one.
1. Underneath the second `---`, you can add the main body of your post. This will only be displayed if a user clicks on the news title. You can add images using the typical `![]()` syntax from markdown or the nested `<div/>` tags. For an example of the latter, see the file `_news/16th_cong_combustion.md`.

### Pages

Most of the pages can be edited by modifying the files in the `_pages/` directory.
You should not modify the `blog.md`, `cv.md`, `news.md`, or `publications.md` files unless you are comfortable with [Liquid](https://github.com/Shopify/liquid).

#### `members.md`

This file allows navigation to the pages of different lab members.
The formatting should be pretty easy to copy, but note that if you add members you will also have to add an associated file in the `_data/people/` directory.

### People

Each person has a file called `_data/people/uniquename.yml` which is referenced from `members.md`.
This file contains information that will be automatically displayed on their personal page.
For the most part, it should be straightforward to create files for new members by copying and pasting from the existing files.

### Publications

Publications can be added by adding a bibtex entry to the `_bibliography/papers.bib` file.
If you want to sort the files, you can run `python3 scripts/sort_bibtex.py`.
This is necessary if you place the bibtex entries out of chronological order, as Jekyll cannot easily sort them.

### Previewing the changes

You can either save the changes and push them to GitHub where they will be rendered and displayed for everyone, or you can use a local preview using Jekyll.
To preview locally using Jekyll, you can type `bundle exec jekyll serve` and then open the [`http://127.0.0.1:4000`](http://127.0.0.1:4000) url that is provided.
This assumes that you have Ruby and Jekyll installed.

### Push changes to GitHub

You can use `git commit -am "your message here"` to save all of your changes, and `git push` to send all of your changes to GitHub.

### Pull the latest version from GitHub

You can pull the latest version of the website from GitHub using `git pull`.