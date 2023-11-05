def favorite_color(d1: dict[str, str]) -> str:
    count : int = 0
    max_color : str = ""
    currentcolor_count : int = 0
    previouscolor_count: int = 0 
    for i in d1:
        color = d1[i]
        for j in d1:
            if color == d1[j]:
                count += 1
        currentcolor_count = count
        if currentcolor_count > previouscolor_count: 
            max_color = color
        previouscolor_count = count
    return max_color  

print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))