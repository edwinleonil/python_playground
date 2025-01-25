import logging

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


# Example usage
divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, 'a')
