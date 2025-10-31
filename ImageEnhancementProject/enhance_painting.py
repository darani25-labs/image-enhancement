import cv2
import numpy as np

# ----------- STEP 1: Load Image -----------
# Change the file name to your image
img = cv2.imread("image_file/faded_painting.jpg")

if img is None:
    print("❌ Error: Image not found. Please check the file path.")
    exit()

# ----------- STEP 2: Convert to RGB -----------
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# ----------- STEP 3: Contrast Stretching Function -----------
def contrast_stretch(image):
    # Calculate min and max for each channel
    min_val = np.min(image, axis=(0, 1))
    max_val = np.max(image, axis=(0, 1))

    # Apply formula: (pixel - min) / (max - min) * 255
    stretched = (image - min_val) / (max_val - min_val) * 255
    stretched = np.clip(stretched, 0, 255).astype(np.uint8)

    return stretched

# ----------- STEP 4: Apply Enhancement -----------
enhanced = contrast_stretch(img_rgb)

# ----------- STEP 5: Convert back to BGR for OpenCV display -----------
original_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
enhanced_bgr = cv2.cvtColor(enhanced, cv2.COLOR_RGB2BGR)

# ----------- STEP 6: Show and Save Result -----------
cv2.imshow("Original Faded Painting", original_bgr)
cv2.imshow("Enhanced Painting (Contrast Stretched)", enhanced_bgr)

# Save the enhanced image
cv2.imwrite("enhanced_painting.jpg", enhanced_bgr)
print("✅ Enhanced image saved as 'enhanced_painting.jpg'")

cv2.waitKey(0)
cv2.destroyAllWindows()
