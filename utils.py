import functools
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

def safe_tool(func):
    """Decorator to catch errors in tool functions and return structured responses."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            logging.info(f"Tool {func.__name__} executed successfully.")
            return result
        except Exception as e:
            logging.error(f"Error in tool {func.__name__}: {str(e)}", exc_info=True)
            return {"error": f"Tool {func.__name__} failed: {str(e)}"}
    return wrapper
