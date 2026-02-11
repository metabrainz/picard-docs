#! /usr/bin/bash
BASEDOC=MusicBrainzPicardUserGuide
if [ -z "$READTHEDOCS_LANGUAGE" ]; then
    READTHEDOCS_LANGUAGE=en
fi

echo "Environment:"
printenv

echo ""
echo "Build LaTeX files"
sphinx-build -M latex . _build -D language=$READTHEDOCS_LANGUAGE

echo ""
echo "List output files"
cd _build/latex
ls -l

echo ""
echo "Building PDF from LaTeX (Pass 1)"
lualatex $BASEDOC

echo ""
echo "Building PDF index"
makeindex -s python.ist $BASEDOC

echo ""
echo "Building PDF from LaTeX (Pass 2)"
lualatex $BASEDOC
