# Symfony Docs Docset Generator

This simple shell/python application is used to create Dash docsets
from Symfony documentations.

## Requirements

You need to have `virutalenv` installed on your machine. This application
only support python 3.

## Running

To run the Symfony docset generator simply run the following command:

```bash
chmod +x docgen.sh
./docgen.sh symfony-docs 4.3 #symfony-docs-folder symfony-version
```

This will create a symfony-docs.docset` folder in `_build` folder of the
Symfony documentation. This can be imported directly to Dash/Zeal.