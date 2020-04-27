@ECHO OFF
setlocal
for %%i in (en fr de es) do (
	set SPHINXOPTS=
	if NOT '%%i' == 'en' sphinx-intl update -p _build\gettext -l %%i
 	set SPHINXOPTS=-D language=%%i
	rd /S /Q -build\html
	echo | set /p=Removing old _build\html directory
	timeout /T 2
	.\make.bat html
	del /F docs\%%i\MusicBrainz_Picard_HTML[%%i].zip
	cd _build
	7za a -r ..\docs\%%i\MusicBrainz_Picard_HTML[%%i].zip html
	cd ..
	rd /S /Q docs\%%i\html
	echo | set /p=Removing old docs\%%i\html directory
	timeout /T 2
	md docs\%%i\html
	echo | set /p=Creating new docs\%%i\html directory
	timeout /T 2
	xcopy /E _build\html docs\%%i\html
	set SPHINXOPTS=
)
set SPHINXOPTS=
