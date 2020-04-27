@ECHO OFF
setlocal
set SPHINXOPTS=-D language=en
.\make.bat gettext
set SPHINXOPTS=
