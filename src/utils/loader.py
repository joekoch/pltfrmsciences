class Loader:
    pass


class FileLoader(Loader):
    @staticmethod
    def load_from_file(file_path):
        for rec in open(file_path):
            yield rec
