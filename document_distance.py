import math

first = dict()
second = dict()


def read(dictionary, content):
    data = content.split()
    for i in range(len(data)):
        word = data[i].lower()
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    print(dictionary)


def dot_product(f_dict, s_dict):
    sum = 0
    for key, value in f_dict.items():
        if key in s_dict:
            sum += value * s_dict[key]
    return sum


def norm(dict):
    return sqrt(product(dict))


def product(dict):
    sum = 0
    for key in dict:
        sum += dict[key] ** 2
    return sum


def sqrt(number):
    return number ** (1.0 / 2)


def offset_angle(f_dict, s_dict):
    numerator = dot_product(f_dict, s_dict)
    denominator = norm(f_dict) * norm(s_dict)

    if denominator == 0:
        if len(f_dict) == 0 and len(s_dict) == 0:
            return 0
        else:
            return math.pi / 2
    offset = math.acos(numerator / denominator)
    return angle_to_percentage(offset)


def angle_to_percentage(angle):
    return int((1.0 - angle / (math.pi / 2)) * 100)


read(first,
     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's "
     "standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to "
     "make a type specimen book. It has survived not only five centuries, but also the leap into electronic "
     "typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset "
     "sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker "
     "including versions of Lorem Ipsum.")

read(second,
     "It is a long established fact that a reader will be distracted by the readable content of a page when looking "
     "at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, "
     "as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing "
     "packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' "
     "will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by "
     "accident, sometimes on purpose (injected humour and the like).")

result = offset_angle(first, second)
print("The percentage 2 documents are the same is : " + str(result) + "%")
