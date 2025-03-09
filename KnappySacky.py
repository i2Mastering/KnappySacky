from collections import Counter

class KnappySacky:
    """
    Represents a collection of objects with volume and value attributes and implements a knapsack algorithm
    to determine the best combination of items to maximize overall value while staying within capacity constraints.
    """
    def __init__(self, name, value, h, w, d, cap):
        """
        Initializes the KnappySacky object with item attributes and knapsack capacity.

        Args:
            name (list): List of object names.
            value (list): List of object values.
            h (list): List of object heights.
            w (list): List of object widths.
            d (list): List of object depths.
            cap (int): Maximum capacity of the knapsack in cubic inches.
        """
        self.name = name
        self.value = value
        self.height = h
        self.width = w
        self.depth = d
        self.cap = cap
        self.LV = []
        self.cubicInches = []
        self.ans = []
        self.totalvalue = 0
        self.tw = 0

    def findCubicInches(self):
        """
        Calculates the volume of each object and stores it in a list.
        """
        for i in range(len(self.height)):
            vol = self.height[i] * self.width[i] * self.depth[i]
            self.cubicInches.append(vol)

    def linkValues(self):
        """
        Creates a list linking each object's name, cubic inches, and value.

        Returns:
            list: A list of tuples containing (name, cubic inches, value) for each object.
        """
        for i in range(len(self.height)):
            nested = (self.name[i], self.cubicInches[i], self.value[i])
            self.LV.append(nested)
        return self.LV

    def knapsack(self):
        """
        Determines the best objects to include in the knapsack based on maximum total value.

        Returns:
            list: A list of objects selected for the knapsack.
        """
        rwv = []
        for i in range(len(self.value)):
            rwv.append([self.value[i] / self.cubicInches[i], self.cubicInches[i], self.value[i], self.name[i]])
        rwv.sort(reverse=True, key=lambda x: x[0])
        found = True

        while found:
            found = False
            for t in rwv:
                if (t[1] + self.tw) <= self.cap:
                    self.ans.append(t[3])
                    self.totalvalue += t[2]
                    self.tw += t[1]
                    found = True
                    break
        return self.ans

    def printKS(self):
        """
        Displays the items currently in the knapsack, their total value, and remaining capacity.
        """
        ksCounter = Counter(self.ans)
        aPrint = [f"{count} {name}" for name, count in ksCounter.items()]
        print(f"The suggested items are {', '.join(aPrint)} with total value of ${self.totalvalue:.2f} dollars. The space left in cubic inches is {self.cap - self.tw:.2f}")

def main():
    """
    Main function that reads input data, initializes the KnappySacky object, and executes the knapsack algorithm.
    """
    name = []
    value = []
    height = []
    width = []
    depth = []

    def read_file(file_name):
        """
        Reads a CSV file and returns its lines.

        Args:
            file_name (str): The name of the file to read.

        Returns:
            list: A list of lines from the file.
        """
        with open(file_name, 'r') as f:
            return f.readlines()

    def parse_file(lines):
        """
        Parses the lines of the file and populates the object lists.

        Args:
            lines (list): The lines read from the file.
        """
        for line in lines:
            line = line.strip()
            if line:
                parts = line.split(',')
                name.append(parts[0])
                value.append(float(parts[1]))
                height.append(float(parts[2]))
                width.append(float(parts[3]))
                depth.append(float(parts[4]))

    while True:
        try:
            userCAP = int(input("Please enter the capacity of your knapsack: "))
            break
        except ValueError:
            print("Please use the correct value: ")
    
    lines = read_file('IKEpacks.csv')
    parse_file(lines)
    KS = KnappySacky(name, value, height, width, depth, userCAP)
    KS.findCubicInches()
    KS.knapsack()
    KS.printKS()

if __name__ == "__main__":
    main()
