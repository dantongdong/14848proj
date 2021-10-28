def displayPrompt():
    print("Welcome to Big Data Processing Application")
    print("Please type the number that corresponds")
    print("1. Apache Hadoop")
    print("2. Apache Spark")
    print("3. Jupyter Notebook")
    print("4. SonarQube and SonarScanner")

def askUserInput():
    return input("Type the number here > ")

def processUserInput(cmd):
    pass

while True:
    displayPrompt()
    cmd = askUserInput()
    processUserInput(cmd)