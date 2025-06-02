import cv2

def process_image(img, standard_width=480):
    height = int(img.shape[0] * (standard_width / img.shape[1]))
    img = cv2.resize(img, (standard_width, height))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (9, 9), 0)
    edges = cv2.Canny(blurred, 90, 255)
    return edges, img  # also returns resized image


def calculate_crack_metrics(contours, min_area=15):
    total_area = 0
    total_length = 0
    filtered_contours = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        length = cv2.arcLength(cnt, closed=False)
        if area > min_area:
            total_area += area
            total_length += length
            filtered_contours.append(cnt)

    return total_area, total_length, filtered_contours


def classify_crack(area, length):
    if area > 2000 or length > 1500:
        return "RISK OF COLLAPSE", (0, 0, 255)  # Red
    elif area > 1000 or length > 700:
        return "WARNING", (0, 255, 255)  # Yellow
    else:
        return "STABLE", (0, 255, 0)  # Green


def draw_results(img, contours, area, length, status, text_color):
    output = img.copy()
    for cnt in contours:
        cv2.drawContours(output, [cnt], -1, text_color, 2)
    return output


def analyze_crack(image_path, output_path):
    img = cv2.imread(image_path)
    edges, img = process_image(img)
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    area, length, filtered_contours = calculate_crack_metrics(contours)
    status, color = classify_crack(area, length)
    result_img = draw_results(img, filtered_contours, area, length, status, color)

    # Save result image
    cv2.imwrite(output_path, result_img)

    return output_path, status, int(area), int(length)
