from __future__ import with_statement


class BaseAsset(object):

    def __init__(self, attributes):
        self.attributes = attributes

    def get_source(self):
        raise NotImplementedError()

    def __str__(self):
        return self.get_source()


class Asset(BaseAsset):

    def get_source(self):
        with open(self.attributes.absolute_path, 'rb') as f:
            source = f.read()
        for processor in self.attributes.get_processors():
            source = processor.process(source)
        return source


class StaticAsset(BaseAsset):

    def get_source(self):
        with open(self.attributes.absolute_path, 'rb') as f:
            return f.read()
