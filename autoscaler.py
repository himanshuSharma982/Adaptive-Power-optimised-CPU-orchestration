def scale_resources(predicted_cpu):
    if predicted_cpu > 70:
        return 3
    elif predicted_cpu > 40:
        return 2
    else:
        return 1