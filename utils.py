def get_result(score):
    if score <= 3:
        return "Dom"
    elif score <= 5:
        return "Goed, maar kan beter"
    elif score <= 8:
        return "Super"
    else:
        return "Genie"
