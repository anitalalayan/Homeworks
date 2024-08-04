def make_logger(level):
    def logger(message):
        print(f"[{level}] {message}")
    return logger

make_logger("INFO")("This is an info message.")
make_logger("ERROR")("This is an error message.")
