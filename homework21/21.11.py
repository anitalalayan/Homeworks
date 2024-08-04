def make_logger(level):
    def log(message):
        print(f"[{level}] {message}")
    return log

make_logger("ERROR")("This is an error message.")       
make_logger("WARNING")("This is a warning message.")
