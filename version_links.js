const default_language = 'en';
const versions = ['v2.3.2', 'v2.4', 'v2.4.1', 'v2.4.2', 'v2.4.4', 'v2.5', 'v2.5.1', 'v2.5.2'];
var vcount = versions.length;
var i, text;
var serv = window.location.protocol + '//' + window.location.hostname

function list_versions(url_root) {
    text = "\n";
    for (i = 0; i < vcount; i++) {
        text += '<dd><a href="/' + versions[i] + '/index.html" class="__ptNoRemap">' + versions[i] + "</a></dd>\n";
    }
    text += '<dd><a href="/index.html" class="__ptNoRemap">latest' + "</a></dd>\n";
    document.getElementById("select_version").innerHTML += text;
}
