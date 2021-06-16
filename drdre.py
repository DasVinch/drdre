def choukrounCrap(n: int, a: str = "Dr. André", b: str = "Young, Ph.D.", c: str = "Dr. Dre"):
    if n == 0:
        return a + " " + b
    
    return a + f" \"Please don't call me \"{choukrounCrap(n-1)}\", just call me {c}\" " + b


if __name__ == "__main__":
    print(choukrounCrap(13))