from httpx import Response

from clients.http.client import HTTPClient

from typing import TypedDict

class CreateVirtualCardRequestDict(TypedDict):
    """
    Структура данных для создания новой виртуальной карты.
    """
    userId: str
    accountId: str

class CreatePhysicalCardRequestDict(TypedDict):
    """
    Структура данных для создания новой физической карты.
    """
    userId: str
    accountId: str

class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def issue_virtual_card_api(self, request: CreateVirtualCardRequestDict) -> Response:
        """
        Создание новой виртуальной карты.

        :param request: Словарь с данными новой карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: CreatePhysicalCardRequestDict) -> Response:
        """
        Создание новой физической карты.

        :param request: Словарь с данными новой карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)
