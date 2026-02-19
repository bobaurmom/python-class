#5. Handling Different Types of Data
#1. Create a Data class that will be the base class
class Data:
    def __init__(self, data):
        self.data = data
    def display(self):
        print(f"data: {self.data}")

#. Use encapsulation to keep the data private and provide methods to access and process it
class Encapsulation(Data):
    def __init__(self, data):
        super().__init__(data)
        self.__data = data
    def get_data(self):
        return self.__data
    def process_data(self):
        if isinstance(self.__data, list):
            return [x * 2 for x in self.__data]
        elif isinstance(self.__data, dict):
            return {k: v * 2 for k, v in self.__data.items()}
#- NumericalData → Stores a list of numbers and calculates the mean.
class NumericalData(Encapsulation):
    def __init__(self, data):
        super().__init__(data)
    def calculate_mean(self):
        if isinstance(self.get_data(), list):
            return sum(self.get_data()) / len(self.get_data())
        else:
            return "Data is not a list"
#- CategoricalData → Stores a dictionary of categories and their count the frequency of each category.
class CategoricalData(Encapsulation):
    def __init__(self, data):
        super().__init__(data)
    def calculate_frequency(self):
        if isinstance(self.get_data(), dict):
            return dict(self.get_data())
        else:
            return "Data is not a dictionary"
#- TextData → Stores a string and counts the number of words.
class TextData(Encapsulation):
    def __init__(self, data):
        super().__init__(data)
    def count_words(self):
        if isinstance(self.get_data(), str):
            return len(self.get_data().split())
        else:
            return "Data is not a string"
    
#4. Each class should have a process_data() method.

#case 1
print("\n=== Case Study 1: Numerical Data ===")
num_data = NumericalData([10, 20, 30, 40, 50])
print("Mean of all numbers: {}".format(num_data.calculate_mean()))

print("\n=== Case Study 2: Text Data ===")
text_data = TextData("Data science is fun and easy to learn")
print("Number of words: {}".format(text_data.count_words()))

print("\n=== Case Study 3: Categorical Data ===")
cat_data = CategoricalData({"cat": 3, "dog": 2, "bird": 1})
print("Frequency of 'dog': {}".format(cat_data.get_data()["dog"]))