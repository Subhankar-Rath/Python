color=input("enter the color")

match color:
    case "green":
        print("go")
    case "red":
        print("stop")
    case "yellow":
        print("look")
    case _:
        print("invalid color ")