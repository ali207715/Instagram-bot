from filter import MyFilter

filter = MyFilter()
filter.train("corpus/training")
filter.test("corpus/testing")

for lines in open("corpus/testing/!prediction.txt", "r").readlines():
    print(lines)
