def generate_report(file_activity):
    """
    Generate a report for the detected ransomware activity.
    
    Args:
        file_activity (list): List of file activity features.

    Returns:
        None
    """
    with open('data/reports/report.txt', 'a') as report_file:
        report_file.write(f"Ransomware detected: {file_activity}\n")
