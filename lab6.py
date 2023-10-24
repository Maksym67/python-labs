import datetime

log_history = []

def save_to_file(log_entry):
    with open("log.txt", "a") as file:
        file.write(log_entry + "\n")

def logger(log_type=""):
    def decorator(func):
        def wrapped(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_entry = f"Timestamp: {datetime.datetime.now()} - Function: {func.__name__}, Args: {args}, Result: {result}, Log Type: {log_type}"
            except ValueError:
                log_entry = f"{datetime.datetime.now()} - Function: {func.__name__}, Args: {args}, Result: calculation error, Log Type: {log_type}"
                print(f"WARNING! Calculation error!")
            log_history.append(log_entry)
            save_to_file(log_entry)
            return result if 'result' in locals() else None
        return wrapped
    return decorator

def get_logs():
    for log_entry in log_history:
        yield log_entry

@logger(log_type="console_message")
def msg_to_console(msg):
    print(msg)
@logger(log_type="calculation")
def multiply(a, b):
    return a * b
@logger(log_type="calculation")
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed!")
    return a / b
@logger(log_type="calculation")
def add(a, b):
    return a + b
@logger(log_type="calculation")
def subtract(a, b):
    return a - b

msg_to_console("|| LOG STARTED ||")
subtract(10, 5)
add(3, 7)
multiply(3, 4)
divide(10, 2)

log = get_logs()

for entry in log:
    print(entry)

msg_to_console("|| LOG CLOSED ||")