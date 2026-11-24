// Add a permalink to individual option paragraphs (targets labelled "opt_*").
// The theme's "headerlink" class provides the styling and the show-on-hover behaviour.
// The icon text is copied from an existing heading permalink so it always matches the theme.
document.addEventListener('DOMContentLoaded', function () {
  var heading = document.querySelector('h1 > a.headerlink, h2 > a.headerlink');
  var icon = heading ? heading.textContent : '\u00b6';
  document.querySelectorAll('p[id^="opt-"]').forEach(function (el) {
    var link = document.createElement('a');
    link.className = 'headerlink';
    link.href = '#' + el.id;
    link.title = 'Link to this option';
    link.textContent = icon;
    el.appendChild(link);
  });
});
