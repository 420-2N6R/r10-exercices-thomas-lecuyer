__all__ = ["converter", "fakestore_rq"]




def reverse(msg: str):  # <-- this name shadows the 'reverse.py' submodule
    return msg[::-1]