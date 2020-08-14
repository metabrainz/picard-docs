const default_language = 'en';
const versions = ['v2.3.2', 'v2.4'];
var vcount = versions.length;
var i, text;
var serv = window.location.protocol + '//' + window.location.hostname

function list_versions(url_root) {
    text = "\n";
    for (i = 0; i < vcount; i++) {
        text += '<dd><a href="' + serv + '/' + versions[i] + '/' + default_language + '/index.html" class="__ptNoRemap">' + versions[i] + "</a></dd>\n";
    }
    text += '<dd><a href="' + serv + '/' + default_language + '/index.html" class="__ptNoRemap">latest' + "</a></dd>\n";
    document.getElementById("select_version").innerHTML += text;
}
