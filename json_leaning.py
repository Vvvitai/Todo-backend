import json

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

print(type(filesystem))
print(type(json.dumps(filesystem)))
print(filesystem)
j_filesystem = json.dumps(filesystem)
print(j_filesystem)
print(type(json.loads(j_filesystem)))  # Выгрузить из json

