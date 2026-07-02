from httpx import Response, QueryParams

from clients.http.client import HTTPClient

from typing import TypedDict

from clients.http.gateway.client import build_gateway_http_client

class OperationDict(TypedDict):
    """
    Описание структуры операции.
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationSummaryDict(TypedDict):
    """
    Описание структуры статистики операции.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float

class OperationReceiptDict(TypedDict):
    """
    Описание структуры чека по операции.
    """
    url: str
    document: str

class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения списка операций.
    """
    accountId: str

class GetOperationsResponseDict(TypedDict):
    """
    Описание структуры ответа для получения списка операций.
    """
    operations: list[OperationDict]

class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура данных для получения статистики операций.
    """
    accountId: str

class GetOperationsSummaryResponseDict(TypedDict):
    """
    Описание структуры ответа для получения статистики операций.
    """
    summary: OperationSummaryDict

class GetOperationReceiptResponseDict(TypedDict):
    """
    Описание структуры ответа для получения чека операции.
    """
    receipt: OperationReceiptDict

class GetOperationResponseDict(TypedDict):
    """
    Описание структуры ответа для получения операции.
    """
    operation: OperationDict

class MakeOperationRequestDict(TypedDict):
    """
    Структура данных для общих полей операции.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для операции комиссии.
    """
    pass

class MakeFeeOperationResponseDict(TypedDict):
    """
    Структура ответа для операции комиссии.
    """
    operation: OperationDict

class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для операции пополнения.
    """
    pass

class MakeTopUpOperationResponseDict(TypedDict):
    """
    Структура ответа для операции пополнения.
    """
    operation: OperationDict

class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для операции кешбека.
    """
    pass

class MakeCashbackOperationResponseDict(TypedDict):
    """
    Структура ответа для операции кешбека.
    """
    operation: OperationDict

class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для операции перевода.
    """
    pass

class MakeTransferOperationResponseDict(TypedDict):
    """
    Структура ответа для операции перевода.
    """
    operation: OperationDict

class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для операции покупки.
    """
    category: str

class MakePurchaseOperationResponseDict(TypedDict):
    """
    Структура ответа для операции покупки.
    """
    operation: OperationDict

class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для операции оплаты по счету.
    """
    pass

class MakeBillPaymentOperationResponseDict(TypedDict):
    """
    Структура ответа для операции оплаты по счету.
    """
    operation: OperationDict

class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для операции снятия наличных.
    """
    pass

class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """
    Структура ответа для операции снятия наличных.
    """
    operation: OperationDict


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получить информацию об операции.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получить чек по операции.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operation-receipt{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получить список операций.

        :param query: Словарь с параметрами запроса
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Получить статистику операций.

        :param query: Словарь с параметрами запроса
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Создание операции комиссии.

        :param request: Словарь с status, amount, cardId, accountId
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Создание операции пополнения.

        :param request: Словарь с status, amount, cardId, accountId
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Создание операции кешбека.

        :param request: Словарь с status, amount, cardId, accountId
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cashback-operation",json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Создание операции перевода.

        :param request: Словарь с status, amount, cardId, accountId
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Создание операции покупки.

        :param request: Словарь с status, amount, cardId, accountId, category
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Создание операции оплаты по счету.

        :param request: Словарь с status, amount, cardId, accountId
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Создание операции снятия наличных.

        :param request: Словарь с status, amount, cardId, accountId
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)



    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=100.5,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=100.5,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=100.5,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=100.5,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=100.5,
            cardId=card_id,
            accountId=account_id,
            category="taxi",
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=100.5,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=100.5,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())



