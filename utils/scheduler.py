def days_until_exam(exam_date):
    from datetime import datetime
    today = datetime.today()
    delta = (exam_date - today).days
    return max(delta, 1)
