import numpy


class Chrome:
    chromeCount = 0

    def __init__(self):
        self.name = "GENE" + Chrome.geneCount
        self.gene_list = []
        Chrome.chromeCount += 1
