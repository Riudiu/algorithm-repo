while True:
    try: 
        x, y, width, height = map(int, input().split())

        widthOfEscape = width - x if width - x < x else x
        heightOfEscape = height - y if height - y < y else y

        if(widthOfEscape <= 0 or heightOfEscape <= 0): break

        if (widthOfEscape > heightOfEscape):
            print(heightOfEscape)
        else: 
            print(widthOfEscape)
        break

    except ValueError:
        print("다시 입력하세요")
        break
