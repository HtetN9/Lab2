def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    # Calculate BMI
    bmi = weight / (height * height)

    # Display BMI
    print("BMI = " + str(round(bmi, 2)))

    # Determine weight classification
    if bmi < 18.5:
        classification = "-1"
  
    elif bmi <= 25.0:
        classification = "0"
  
    else:
        classification = "1"
    # Display classification
    print("Weight Classification = " + classification)
    return round(bmi, 2), classification
# Example usage
calculate_bmi(weight=57, height=1.73)

