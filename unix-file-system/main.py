from abc import ABC, abstractmethod
import typing


class IEntry(ABC):
    """Interface for Entry class."""

    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

    
    @abstractmethod
    def is_directory(self):
        pass



class File(IEntry):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def is_directory(self):
        return False
    

class Directory(IEntry):
    def __init__(self, name):
        self.name = name
        self.entries:typing.List[IEntry] = []

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_size(self):
        size = 0
        for entry in self.entries:
            size += entry.get_size()
        return size

    def is_directory(self):
        return True

    def add_entry(self, entry: IEntry):
        self.entries.append(entry)

    def remove_entry(self, entry):
        self.entries.remove(entry)
        
    def get_entries(self):
        return self.entries

    def get_entry(self, name):
        for entry in self.entries:
            if entry.get_name() == name:
                return entry
        return None

    def __str__(self):
        return self.name


class SearchParms:
    def __init__(self):
        self.name = ""
        self.min_size = 0
        self.max_size = 0
        self.extension = ""

    def set_name(self, name):
        self.name = name
    
    def set_min_size(self, min_size):
        self.min_size = min_size
    
    def set_max_size(self, max_size):
        self.max_size = max_size
    
    def set_extension(self, extension):
        self.extension = extension
    
    def get_name(self):
        return self.name
    
    def get_min_size(self):
        return self.min_size

    def get_max_size(self):
        return self.max_size
    
    def get_extension(self):
        return self.extension
    

class IFilter(ABC):
    @abstractmethod
    def apply(self, entry: IEntry, search_parms: SearchParms):
        pass

class NameFilter(IFilter):
    def apply(self, entry: IEntry, search_parms: SearchParms):
        return search_parms.get_name() == entry.get_name()


class SizeFilter(IFilter):
    def apply(self, entry: IEntry, search_parms: SearchParms):
        return search_parms.get_min_size() <= entry.get_size() <= search_parms.get_max_size()


class ExtensionFilter(IFilter):
    def apply(self, entry: IEntry, search_parms: SearchParms):
        return entry.get_name().endswith(search_parms.get_extension())



class FileSystem:
    def __init__(self):
        self.root = Directory("root")

    def add_entry(self, path, entry):

        if entry.is_directory():
            self._add_directory(path, entry)
        else:
            self._add_file(path, entry)
    
    def _add_directory(self, path, directory):
        parts = path.split("/")
        current = self.root
        for part in parts:
            if part == "":
                continue
            child = current.get_entry(part)
            if child is None:
                child = Directory(part)
                current.add_entry(child)
            current = child
        current.add_entry(directory)
    
    def _add_file(self, path, file):
        parts = path.split("/")
        current = self.root
        for part in parts:
            if part == "":
                continue
            child = current.get_entry(part)
            if child is None:
                child = Directory(part)
                current.add_entry(child)
            current = child
        current.add_entry(file)

    def search(self, search_parms: SearchParms):
        results = []
        self._search(self.root, search_parms, results)
        return results

    def _search(self, entry, search_parms, results):
        if entry.is_directory():
            for child in entry.get_entries():
                self._search(child, search_parms, results)
        else:
            if self._apply_filters(entry, search_parms):
                results.append(entry)

    def _apply_filters(self, entry, search_parms):
        filters : typing.List[IFilter] = [NameFilter(), SizeFilter(), ExtensionFilter()]
        for filter in filters:
            if not filter.apply(entry, search_parms):
                return False
        return True