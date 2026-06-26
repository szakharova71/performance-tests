import time

import httpx

create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

print("Create user response:", create_user_response_data)
print("Create user response status code:", create_user_response.status_code)


open_credit_card_account_payload = {
    "userId": create_user_response_data['user']['id']
}


open_credit_card_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-credit-card-account",
                                             json=open_credit_card_account_payload)
open_credit_card_account_response_data = open_credit_card_account_response.json()

print("Create credit card account response:", open_credit_card_account_response_data)
print("Create credit card account status code:", open_credit_card_account_response.status_code)


make_purchase_operation_payload = {
  "status": "IN_PROGRESS",
  "amount": 77.99,
  "cardId": open_credit_card_account_response_data["account"]["cards"][0]["id"],
  "accountId": open_credit_card_account_response_data["account"]["id"],
  "category": "taxi"
}

make_purchase_operation_response = httpx.post(
    "http://localhost:8003/api/v1/operations/make-purchase-operation",
    json=make_purchase_operation_payload
)
make_purchase_operation_response_data = make_purchase_operation_response.json()

print("Make purchase operation response:", make_purchase_operation_response_data)
print("Make purchase operation status code:", make_purchase_operation_response.status_code)

get_receipt_document_response = httpx.get(
    f"http://localhost:8003/api/v1/operations/operation-receipt/"
    f"{make_purchase_operation_response_data['operation']['id']}"
    )

get_receipt_document_response_data = get_receipt_document_response.json()

print("Get receipt document response:", get_receipt_document_response_data)
print("Get receipt document status code:", get_receipt_document_response.status_code)