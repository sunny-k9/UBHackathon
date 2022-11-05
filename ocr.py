# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests

def get_text():
    # View complete code at: https://github.com/Asprise/receipt-ocr/tree/main/python-receipt-ocr

    print("=== Python Receipt OCR ===")

    receiptOcrEndpoint = 'https://ocr.asprise.com/api/v1/receipt'  # Receipt OCR API endpoint
    imageFile = "walmart_receipt.png"  # // Modify it to use your own file
    r = requests.post(receiptOcrEndpoint, data={
        'api_key': 'TEST',  # Use 'TEST' for testing purpose \
        'recognizer': 'US',  # can be 'US', 'CA', 'JP', 'SG' or 'auto' \
        'ref_no': 'ocr_python_123',  # optional caller provided ref code \
    },
                      files={"file": open(imageFile, "rb")})

    print(r.text)  # result in JSON

if __name__ == '__main__':
    get_text()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
