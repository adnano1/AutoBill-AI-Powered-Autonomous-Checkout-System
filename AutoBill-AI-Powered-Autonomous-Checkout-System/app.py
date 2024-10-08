import cv2
from inventory_manager import InventoryManager
from checkout_system import CheckoutSystem

# Initialize systems
inventory = InventoryManager()
checkout = CheckoutSystem()

# Start capturing from camera
cap = cv2.VideoCapture(0)

print("AutoBill System Initialized. Begin shopping...")

while True:
    ret, frame = cap.read()

    # Detect items using computer vision (assuming inventory detection is done in InventoryManager)
    detected_items = inventory.detect_items(frame)

    # Update cart and show items on the virtual cart
    checkout.update_cart(detected_items)

    # Display the frame
    cv2.imshow('AutoBill Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Process final payment
checkout.process_payment()

cap.release()
cv2.destroyAllWindows()
