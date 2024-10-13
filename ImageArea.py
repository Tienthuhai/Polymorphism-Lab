class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        """Return the area of the image."""
        return self.width * self.height

    def __gt__(self, other):
        """Check if the area of the current image is greater than the other."""
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        """Check if the area of the current image is greater than or equal to the other."""
        return self.get_area() >= other.get_area()

    def __lt__(self, other):
        """Check if the area of the current image is less than the other."""
        return self.get_area() < other.get_area()

    def __le__(self, other):
        """Check if the area of the current image is less than or equal to the other."""
        return self.get_area() <= other.get_area()

    def __eq__(self, other):
        """Check if the area of the current image is equal to the other."""
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        """Check if the area of the current image is not equal to the other."""
        return self.get_area() != other.get_area()

# Example usage:
image1 = ImageArea(4, 5)
image2 = ImageArea(3, 7)

print("Area of Image 1:", image1.get_area())  # Output: 20
print("Area of Image 2:", image2.get_area())  # Output: 21

# Comparison
print(image1 < image2)  # Output: True
print(image1 > image2)  # Output: False
print(image1 == image2)  # Output: False
