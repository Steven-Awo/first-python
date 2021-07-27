def create_file(filee):
    def execute():
        result1 = filee()
        with open(result1,"w+") as my_file:
            print(my_file.write(result1))
    return execute

def write_to_file(word):
    def executing():
        result2 = word()
        with open(result2, "w+") as my_file:
            print("Filw was just created")
        return result2
    return executing

@create_file
@write_to_file
def statement():
    return "Today is a nice day"
statement()

# output = create_file(statement)
# output2 = write_to_file(statement)
# print(output(statement()))
# print(output2(statement()))
