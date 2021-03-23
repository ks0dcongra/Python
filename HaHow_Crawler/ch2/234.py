from datetime import date
import types
def main():
    def foo():
        return 'bar'
    print(foo)
    print(foo())

if __name__ == '__main__':
    main()

