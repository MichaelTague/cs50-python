file = input("File name: ").strip().lower()
if file.find(".") == -1:
    print("application/octet-stream")
else:
    match file.rsplit(".", 1)[1]:
        case "gif":
            print("image/gif")
        case "jpeg" | "jpg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")
