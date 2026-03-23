<!-- # Website 404 Redirection -->

The standard path format for requesting a documentation page from the website is `https://picard-docs.musicbrainz.org/{language}/{version}/{page}` where:

- `{language}` is the code for the desired language. Note that only a select few languages are currently supported.
- `{version}` is the `v{major}.{minor}` form of the desired version number. For example, if you are requesting documentation for release version 2.13.1 (part of the 2.13 family of releases), `v2.13` would be entered as the version in the requested URL. If `{version}` is omitted, the latest version will be displayed.
- `{page}` is the name of the HTML file to display including the topic path, such as `about_picard/contributing.html`.

If the requested file is not found on the server, a file not found (404) condition will be triggered resulting in the display of an appropriate message. Additional redirection logic has been built into the 404 processing to try to identify and display the requested page before displaying the file not found message. The redirection logic will also try to accommodate some missing information by using default values, or information placed in the wrong order.
