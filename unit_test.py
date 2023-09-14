class utils:
    def __init__(self) -> None:
        pass

    def reversed(self, x: int) -> int:
        if not isinstance(x, int) or x < 0:
            return -1

        return int(str(x)[::-1])
    
    def formatter(self, x: int) -> tuple[bin, oct]:
        if not isinstance(x, int):
            return -1, -1

        return bin(x), oct(x)
    