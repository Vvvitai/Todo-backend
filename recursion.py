def print_recursively1(file: dict):
    print(file['path'])
    for d in file['content']:
        print_recursively1(d)


def print_recursively(list_of_lists: list, depth=0):
    for item in list_of_lists:
        if isinstance(item, list):
            print_recursively(item, depth + 1)
        else:
            print(depth, item)


list_of_lists = [10, [[1, [2, 3, [1]]], [1, [2]]]]
print_recursively(list_of_lists)


filesystem = {
    'path': 'C:',
    'content': [
        {
            'path': 'documents',
            'content': [
                {
                    'path': 'pictures',
                    'content': [
                        {
                            'path': 'me.png',
                            'content': [],
                        },
                        {
                            'path': 'keks.png',
                            'content': [],
                        }
                    ]
                }
            ]
        }
    ]
}


