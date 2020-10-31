import app

def test():
    try:
        n = int(input("Provide an integer 'n' to run 'n' times the pasword generator app: "))
    except ValueError:
        print('An integer must be provided')
    finally:
        for _ in range(n):
            app.app()

test()