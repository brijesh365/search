import abc


class AbstractSearchEngine(abc.ABC):
    def __init__(self, query):
        self.query = query
        super().__init__()

    @abc.abstractmethod
    def __repr__(self):
        pass

    @abc.abstractmethod
    def search(self):
        pass

    @abc.abstractmethod
    def process_result(self, result):
        pass
