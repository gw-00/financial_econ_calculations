
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#function to look through a list of numbers and return the largest number
def largest_number(list):
    largest = list[0]
    for i in list:
        if i > largest:
            largest = i
    return largest

#function to look through a list of numbers and return the smallest number
def smallest_number(list):
    smallest = list[0]
    for i in list:
        if i < smallest:
            smallest = i
    return smallest

#function to look through a list of numbers and return the sum of the numbers
def sum_of_numbers(list):
    sum = 0
    for i in list:
        sum += i
    return sum

#function to look through a list of numbers and return the average of the numbers
def average_of_numbers(list):
    sum = 0
    for i in list:
        sum += i
    return sum / len(list)

#function to look through a list of numbers and return the median of the numbers
def median_of_numbers(list):
    list.sort()
    if len(list) % 2 == 0:
        return (list[int(len(list) / 2)] + list[int(len(list) / 2 - 1)]) / 2
    else:
        return list[int(len(list) / 2)]

#function to look through a list of numbers and return the mode of the numbers
def mode_of_numbers(list):
    list.sort()
    mode = 0
    mode_count = 0
    for i in list:
        if list.count(i) > mode_count:
            mode = i
            mode_count = list.count(i)
    return mode

#function to look through a list of numbers and return the range of the numbers
def range_of_numbers(list):
    return largest_number(list) - smallest_number(list)

#function to look through a list of numbers and return the variance of the numbers
def variance_of_numbers(list):
    sum = 0
    for i in list:
        sum += (i - average_of_numbers(list)) ** 2
    return sum / len(list)

#function to look through a list of numbers and return the standard deviation of the numbers
def standard_deviation_of_numbers(list):
    return variance_of_numbers(list) ** 0.5

#function to look through a list of numbers and return the coefficient of variation of the numbers
def coefficient_of_variation_of_numbers(list):
    return standard_deviation_of_numbers(list) / average_of_numbers(list)

#function to look through a list of numbers and return the z-score of the numbers
def z_score_of_numbers(list):
    z_score = []
    for i in list:
        z_score.append((i - average_of_numbers(list)) / standard_deviation_of_numbers(list))
    return z_score

#function to look through a list of numbers and return the percentile of the numbers
def percentile_of_numbers(list):
    list.sort()
    percentile = []
    for i in list:
        percentile.append((list.index(i) + 1) / len(list) * 100)
    return percentile

#function to look through a list of numbers and return the quartiles of the numbers
def quartiles_of_numbers(list):
    list.sort()
    quartiles = []
    if len(list) % 2 == 0:
        quartiles.append(median_of_numbers(list[:int(len(list) / 2)]))
        quartiles.append(median_of_numbers(list))
        quartiles.append(median_of_numbers(list[int(len(list) / 2):]))
    else:
        quartiles.append(median_of_numbers(list[:int(len(list) / 2)]))
        quartiles.append(median_of_numbers(list))
        quartiles.append(median_of_numbers(list[int(len(list) / 2 + 1):]))
    return quartiles

print("Largest number: " + str(largest_number(list)), "Smallest number: " + str(smallest_number(list)), "Sum of numbers: " + str(sum_of_numbers(list)), "Average of numbers: " + str(average_of_numbers(list)), "Median of numbers: " + str(median_of_numbers(list)), "Mode of numbers: " + str(mode_of_numbers(list)), "Range of numbers: " + str(range_of_numbers(list)), "Variance of numbers: " + str(variance_of_numbers(list)), "Standard deviation of numbers: " + str(standard_deviation_of_numbers(list)), "Coefficient of variation of numbers: " + str(coefficient_of_variation_of_numbers(list)), "Z-score of numbers: " + str(z_score_of_numbers(list)), "Percentile of numbers: " + str(percentile_of_numbers(list)), "Quartiles of numbers: " + str(quartiles_of_numbers(list)))
