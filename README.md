# googlesites2github

Move Google Sites HTML to GitHub Wiki Markdown.

This tool was written in order to transfer content from https://sites.google.com/a/puredarwin.org/puredarwin/ to https://github.com/PureDarwin/PureDarwin/wiki

Unfortunately the [google-sites-liberation tool](https://code.google.com/p/google-sites-liberation/) seems broken (cannot log into Google Apps domains anymore) so that using https://github.com/foursquare/sites-to-markdown was not an option.

## Usage

* Download the whole content form Google Sites, e.g., using `wget --mirror --convert-links --adjust-extension 
    --page-requisites --no-parent http://www.somesite.org`
* On each downloaded HTML file, run `googlesites2markdown <file>`. You can automate that by running `find . -name *html -exec ../googlesites2markdown \{\} \;`
* Finally, the images need to be downloaded in full resolution using something like `grep -o -r -e "_/rsrc/.*.jpg" . | cut -d "%" -f 1 | cut -d ")" -f 1 | sort  | sort | uniq | cut -d ":" -f 2 > urls` and downloading the resulting URLs using wget
* The result is a good starting point but definitely needs manual fine-tuning
