class FileExtensionExtractor():
    def __init__(self, a="abc.java"):
        self.a = a
    
    def file_extension_extractor(self):
        file_name = self.a.split('.')
        return file_name[-1]
    
if __name__ == "__main__":
    z = FileExtensionExtractor("abc.java")
    print(z)
    x = z.file_extension_extractor()
    print(x)