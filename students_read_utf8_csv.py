import codecs
"""
      Read Studends.Unique and convert para utf-8
"""


blks = 1048576  # Block Size

with codecs.open('Students_Unique.csv', "r", "iso-8859-1") as sourceFile:
    with codecs.open("Students_Unique_OK.csv", "w", "utf-8") as targetFile:
        while True:
            contents = sourceFile.read(blks)
            if not contents:
                break
            targetFile.write(contents)


