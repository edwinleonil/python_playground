import logging
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        logging.error(f"Error: Cannot divide by zero. {e}")
        raise
    except TypeError as e:
        logging.error(f"Error: Invalid input type. {e}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None
    else:
        logging.info(f"The result is {result}")
        return result
    finally:
        logging.info("Execution completed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Divide two numbers.")
    parser.add_argument("a", type=float, help="The dividend")
    parser.add_argument("b", type=float, help="The divisor")
    args = parser.parse_args()

    divide_numbers(args.a, args.b)
