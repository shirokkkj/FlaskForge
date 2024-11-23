import os

def create_directory(paths):
    try:
        for path in paths:
            if not os.path.exists(path):
                os.makedirs(path)
        return 'Success'
    except os.error as error:
        print(error)
        return 'Fail'

def create_file_in_directory(directory_path, files):
    if not os.path.exists(directory_path):
        return 'Directory not found.'
    
    results = {}
    
    for file_info in files:
        try:
            filename = file_info[0]
            
            file_content = file_info[1] if len(file_info) > 1 else ''
            
            file_path = os.path.join(directory_path, filename)
            
            
            with open(file_path, 'w') as file:
                file.write(file_content)
                
            results[filename] = 'success'
        except Exception as e:
            results[filename] = e
            
    return results
        
            
            
            