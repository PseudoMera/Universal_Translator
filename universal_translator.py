class UnitsTranslator:
    def __init__(self, file_route):
        self.file_route = file_route
        self.lines = []
        self.length_units = {     
            'm': 1,
            'km': 1000,
            'cm': 0.01,
            'mm': 0.001,
            'um': 0.000001,
            'nm': 0.000000001
        }

    def read_file(self):
        with open(self.file_route, 'r') as reader:
            for line in reader:
                self.lines.append(line)

    def convert_unit(self, num, from_unit, to_unit):
        num_in_meters = num * self.length_units[from_unit]
        if to_unit is not 'm':
            num_in_meters = num_in_meters / self.length_units[to_unit]
        return num_in_meters

    def write_to_file(self, file_content):
        file_name = input("Introduce the result file name: ") + '.txt'
        with open(file_name, "w+") as writer:
            for text in file_content:
                if(text[0] == 'v'):
                    writer.writelines(text[0] + ', ' + text[1] +  ', ' + text[2] + ', ' + 'result' + '\n')
                else:
                    res = self.convert_unit(float(text[0]), text[1], text[2])
                    writer.writelines(text[0] + ', ' + text[1] + ', ' + text[2] + ', ' + str(res) + '\n')
        

if __name__ == "__main__":
    file_route = input('Enter your file route: ') 
    trans = UnitsTranslator(file_route)
    trans.read_file()


    file_elements = []
    for line in trans.lines:
        file_elements.append(line.replace('\n', '').replace(' ', '').split(','))

    trans.write_to_file(file_elements)


