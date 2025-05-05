class FunctionDocumentPrinter():
    def _take_input_from_user(self):
        x = str(input("Enter the function name for which you wanted to see the document: "))
        return x
        

    def _function_document_printer(self):
        x = self._take_input_from_user()
        func_name = eval(x)
        doc = help(func_name)
        return doc


if __name__ == "__main__":
    obj = FunctionDocumentPrinter()
    abc = obj._function_document_printer()