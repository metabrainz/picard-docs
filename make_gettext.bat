@ECHO OFF
setlocal
set SPHINXOPTS=-D language=en
call .\make.bat gettext
set SPHINXOPTS=
sphinx-intl update -p _build\gettext -l fr -l de -l es
