import math


def calculate_area(shape, dimensions):
    match shape:
        case "rectangle":
            return dimensions[0] * dimensions[1]
        case "triangle":
            return 0.5 * dimensions[0] * dimensions[1]
        case "circle":
            return math.pi * dimensions[0] ** 2
        case _:
            raise ValueError("Invalid shape. Supported shapes are 'rectangle', 'triangle', and 'circle'.")


# Get user input for shape and dimensions
shape = input("Enter the shape ('rectangle', 'triangle', or 'circle'): ").lower()

if shape in ["rectangle", "triangle", "circle"]:
    # Get user input for dimensions based on the shape
    dimensions = [float(input(f"Enter the {dim} of the {shape}: ")) for dim in ["length", "width"] if
                  shape == "rectangle" or dim != "width"]

    # Calculate and print the area
    print(f"Area of {shape}: {calculate_area(shape, dimensions)}")
else:
    print("Invalid shape. Please enter 'rectangle', 'triangle', or 'circle'.")