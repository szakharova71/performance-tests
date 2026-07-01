from httpx import Response, QueryParams

from clients.http.client import HTTPClient

from typing import TypedDict

class GetOperationsQueryDict(TypedDict):
    accountId: str

class GetOperationsSummaryQueryDict(TypedDict):
    accountId: str

class MakeOperationRequestDict(TypedDict):
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    pass

class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    pass

class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    pass

class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    pass

class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    category: str

class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    pass

class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    pass

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



