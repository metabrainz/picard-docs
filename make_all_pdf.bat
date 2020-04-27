@ECHO OFF
setlocal
for %%i in (en de fr es) do (
	set SPHINXOPTS=
	if NOT '%%i' == 'en' sphinx-intl update -p _build\gettext -l %%i
 	set SPHINXOPTS=-D language=%%i
	rd /S /Q _build\latex
	echo | set /p=Removing old _build\latex directory
	timeout /T 2
	.\make.bat latexpdf
	xcopy /Y _build\latex\*.pdf docs\%%i\MusicBrainz_Picard[%%i].pdf
	set SPHINXOPTS=
)
set SPHINXOPTS=
