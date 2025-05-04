class ExamSchedulerFormatter():
    def __init__(self, exam_st_date):
        self.exam_st_date = exam_st_date

    def Formatter(self):
        formatted_date = "/".join(map(str, self.exam_st_date))
        return formatted_date

if __name__ == "__main__":
    exam_st_date = (11, 12, 2014)
    obj = ExamSchedulerFormatter(exam_st_date)
    result = obj.Formatter()
    print(result)
 