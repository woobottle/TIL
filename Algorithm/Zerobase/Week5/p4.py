def binary_search(data, search):
  if len(data) == 1 and search == data[0] :
    return True
  if len(data) == 1 and search != data[0] :
    return False
  if len(data) == 0 :
    return False

  medium = len(data) // 2 
  if search == data[medium] :
    return True
  else :
    if search > data[medium]:
      return binary_search(data[medium:], search)
    else :
      return binaray_search(data[:medium], search)