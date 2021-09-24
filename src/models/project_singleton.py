class ProjectSingleton(object):

    __instance = None
    file_machine = None
    file_simulation = None
    machine = None
    simulation = None

    def __new__(cls):
        if ProjectSingleton.__instance is None:
            ProjectSingleton.__instance = object.__new__(cls)
        return ProjectSingleton.__instance