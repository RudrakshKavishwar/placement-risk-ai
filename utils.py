def generate_summary(data, risk):
    cgpa, internships, skills, tier, placement_rate, job_demand = data

    reasons = []

    if internships == 0:
        reasons.append("no internship experience")

    if skills < 5:
        reasons.append("low skill score")

    if job_demand < 0.5:
        reasons.append("weak job market demand")

    if cgpa < 7:
        reasons.append("low academic performance")

    if not reasons:
        reasons.append("strong overall profile")

    return f"This student has {risk} placement risk due to " + ", ".join(reasons) + "."


def recommendations(data):
    cgpa, internships, skills, tier, placement_rate, job_demand = data

    recs = []

    if internships == 0:
        recs.append("Apply for internships immediately")

    if skills < 6:
        recs.append("Improve technical skills (DSA / projects)")

    if cgpa < 7:
        recs.append("Focus on academics")

    if job_demand < 0.5:
        recs.append("Explore alternative domains with higher demand")

    if not recs:
        recs.append("Continue current strategy and apply to top companies")

    return recs