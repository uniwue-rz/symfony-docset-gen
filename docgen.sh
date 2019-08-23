#!/usr/bin/env bash

DIR="$1"
VERSION="$2"
RUN_DIR=`pwd`


rm -rf ${DIR}-${VERSION}
rm -rf venv

virtualenv --python=python3 venv
git clone https://github.com/symfony/symfony-docs.git "${DIR}-${VERSION}"
cp index_gen.py "${DIR}-${VERSION}/_build"
cd ${DIR}-${VERSION}
git checkout ${VERSION}
source "${RUN_DIR}/venv/bin/activate"
patch -p1 < "${RUN_DIR}/theme.patch"
cd _build
pip install -r .requirements.txt
pip install bs4
make html
mkdir -p symfony-docs.docset/Contents/Resources/Documents/
cp -r html/* symfony-docs.docset/Contents/Resources/Documents/
cp "${RUN_DIR}/Info.plist" symfony-docs.docset/Contents
sqlite3 "symfony-docs.docset/Contents/Resources/docSet.dsidx" ""
python index_gen.py

