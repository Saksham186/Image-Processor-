import cv2
import numpy as np

# Load an image using OpenCV
image_path = '/Users/anand/Documents/University/SummerProjects/Image_processor/Image1.png'
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not read image. Check file path or image integrity.")
else:
    # Prompt the user for what they want to do
    print("Choose an option:")
    print("1: Resize the image")
    print("2: Sharpen the image")
    print("3: Convert to grayscale and blur")
    print("4: Edge detection")
    print("5: Enhance contrast")
    print("6: Brighten the image")
    
    choice = input("Enter the number of the operation you'd like to perform: ")

    if choice == '1':
        # Resize the image
        width = int(input("Enter the new width: "))
        height = int(input("Enter the new height: "))
        resized_image = cv2.resize(image, (width, height))
        cv2.imwrite('Resized_Image.jpg', resized_image)
        print("Image resized and saved as 'Resized_Image.jpg'.")

    elif choice == '2':
        # Apply a sharpening filter
        kernel = np.array([[0, -1, 0], 
                           [-1, 5, -1],
                           [0, -1, 0]])
        sharpened_image = cv2.filter2D(image, -1, kernel)
        cv2.imwrite('sharpened_image.jpg', sharpened_image)
        print("Image sharpened and saved as 'sharpened_image.jpg'.")

    elif choice == '3':
        # Convert to grayscale and apply GaussianBlur
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
        cv2.imwrite('processed_image.jpg', blurred_image)
        print("Image converted to grayscale, blurred, and saved as 'processed_image.jpg'.")

    elif choice == '4':
        # Edge detection
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image, 100, 200)
        cv2.imwrite('edges_image.jpg', edges)
        print("Edge detection applied and saved as 'edges_image.jpg'.")

    elif choice == '5':
        # Enhance contrast using CLAHE
        lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab_image)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        cl = clahe.apply(l)
        limg = cv2.merge((cl, a, b))
        contrast_image = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
        cv2.imwrite('contrast_image.jpg', contrast_image)
        print("Contrast enhanced and saved as 'contrast_image.jpg'.")

    elif choice == '6':
        # Brighten the image
        bright_image = cv2.convertScaleAbs(image, alpha=1.0, beta=50)  # Increase beta for higher brightness
        cv2.imwrite('bright_image.jpg', bright_image)
        print("Image brightened and saved as 'bright_image.jpg'.")

    else:
        print("Invalid choice. Please select a valid option.")
