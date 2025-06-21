class MyManager:
    def __init__(self):
        self.in_manager = False

    def __enter__(self):
        self.in_manager = True
        print('в менеджере')
        return self # Обязательно возвращать, так как передается в as

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.in_manager = False
        print('вышли из менегера')

with MyManager() as manager:
    print('Kaif')
