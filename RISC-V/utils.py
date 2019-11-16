def to_bytes_lst(string, arr_length=10):
    if arr_length < len(string) + 1:
        arr_length = len(string) + 1
    return [ord(string[i]) if i < len(string) and type(string[i]) == str else 0 for i in range(arr_length)]
