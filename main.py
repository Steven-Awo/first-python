def create_file(filee):
    def execute():
        result1 = filee()
        return result1.open(statement,"w")
    return execute

def write_to_file(word):
    def executing():
        result2 = word()
        return result2.open(statement,"w")
    return executing

@create_file
@write_to_file
def statement():
    return "Today is a nice day"

print(create_file(write_to_file(statement())))
print(statement())


# output = create_file(statement)
# output2 = write_to_file(statement)
# print(output(statement()))
# print(output2(statement()))
