def add(a, b):
    return a + b
def classify_score(score):
    if score < 0 or score > 100:
        raise ValueError("score out of range")
    if score >= 80:
        return "excellent"
    if score >= 50:
        return "pass"
    return "fail"
def shipping_cost(total, priority=False):
    if total < 0:
        raise ValueError("negative total")
    if priority:
        return 15
    if total >= 100:
        return 0
    return 8