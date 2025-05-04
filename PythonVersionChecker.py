import sys
class VersionChecker():
    @classmethod
    def python_version_checker(cls):
        return (
            sys.version
        )

if __name__ == "__main__":
    a=VersionChecker.python_version_checker()
    print(a)