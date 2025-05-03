from datetime import datetime

def days_between(date1, date2):
    """
    Returns the number of days between two dates in 'YYYY-MM-DD' format.

    """
    try:
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        return abs((d2 - d1).days)
    except ValueError:
        return "Error: Dates must be in 'YYYY-MM-DD' format."

# Example usage
print(days_between("2025-05-01", "2025-05-03"))  # 2
print(days_between("2025-05-03", "2025-05-01"))  # 2
print(days_between("2025/05/01", "2025-05-03"))  # Error message