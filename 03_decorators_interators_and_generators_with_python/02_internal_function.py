def main():
    print("Executing main function")

    def internal():
        print("Executing internal function")

    def internal2():
        print("Executing internal2 function")

    internal()
    internal2()

main()
