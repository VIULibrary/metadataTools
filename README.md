# metadataTools #

## some tools for processing metadata ##

 **extract_metadata.py**

1. Extracts the contents of `<mods:title>`, `<mods:subject>`, and `<mods:genre>`, from an OAI harvest XML file, and writes them to a new output file.

2. `<mods:subject>`, and `<mods:genre>` are filtered to output only the unique values.

3. Set input/output file and run `python extract_metadata.py`

- with a nod to Mark Jordan's [metadata_reporter](https://github.com/mjordan/metadata_reporter)




