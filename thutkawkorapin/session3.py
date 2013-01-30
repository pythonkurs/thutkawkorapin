import untangle
import os


class CourseRepo(object):


    def __init__(self, surname):
        self.required = []
        self.surname  = surname

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        del self.required[:]
        self.required.append(".git")
        self.required.append("setup.py")
        self.required.append("README.md")
        self.required.append("scripts/getting_data.py")
        self.required.append("scripts/check_repo.py")
        self.required.append(value + "/__init__.py")
        self.required.append(value + "/session3.py")
        self.__surname = value

    def check(self):
        for item in self.required:
            if not os.path.exists(item):
                return False
        return True


class RepoDir:


    def __init__(self, path):
        self.current_path = os.getcwd()
        self.working_path = path

    def __enter__(self):
        os.chdir(self.working_path)

    def __exit__(self, type, value, tb):
        os.chdir(self.current_path)

