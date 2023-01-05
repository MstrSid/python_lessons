# Create class Image.
# Add 3 fields for class: resolution, title, extension.
# Add method resize() for class. It must change resolution field.
# Add attribute for class like counter

class Image:
    counter = 0

    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension
        Image.counter += 1

    def resize(self, new_size):
        self.resolution = new_size

    def __repr__(self) -> str:
        return f"Class {self.__class__.__name__}: {{\n" \
               f"resolution: {self.resolution},\n" \
               f"title:{self.title},\n" \
               f"extension={self.extension}\n}}\n"


image_one = Image('1300x1200', 'img1', 'jpeg')
image_two = Image('1920x1080', 'img2', 'png')
print(f"Created class objects: {Image.counter}")
print(image_one)
print(image_two)
image_one.resize('1400x1500')
image_one.resize('2048x1900')
print(image_one)
print(image_two)
