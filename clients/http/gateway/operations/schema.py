from datetime import date
from enum import StrEnum
from pydantic import BaseModel, Field, ConfigDict, HttpUrl

from tools.fakers import fake


class OperationType(StrEnum):
    FEE="FEE"
    TOP_UP="TOP_UP"
    PURCHASE="PURCHASE"
    CASHBACK="CASHBACK"
    TRANSFER="TRANSFER"
    BILL_PAYMENT="BILL_PAYMENT"
    CASH_WITHDRAWAL="CASH_WITHDRAWAL"

class OperationStatus(StrEnum):
    FAILED="FAILED"
    COMPLETED="COMPLETED"
    IN_PROGRESS="IN_PROGRESS"


class OperationSchema(BaseModel):
    """
    Описание структуры операции.
    """

    operation_id: str = Field(alias="id")
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class OperationSummarySchema(BaseModel):
    """
    Описание структуры статистики операции.
    """

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")

class OperationReceiptSchema(BaseModel):
    """
    Описание структуры чека по операции.
    """
    url: HttpUrl
    document: str

class GetOperationsQuerySchema(BaseModel):
    """
    Структура данных для получения списка операций.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")

class GetOperationsResponseSchema(BaseModel):
    """
    Описание структуры ответа для получения списка операций.
    """
    operations: list[OperationSchema]

class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура данных для получения статистики операций.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")

class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Описание структуры ответа для получения статистики операций.
    """
    summary: OperationSummarySchema

class GetOperationReceiptResponseSchema(BaseModel):
    """
    Описание структуры ответа для получения чека операции.
    """
    receipt: OperationReceiptSchema

class GetOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа для получения операции.
    """
    operation: OperationSchema

class MakeOperationRequestSchema(BaseModel):
    """
    Структура данных для общих полей операции.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для операции комиссии.
    """
    pass

class MakeFeeOperationResponseSchema(BaseModel):
    """
    Структура ответа для операции комиссии.
    """
    operation: OperationSchema

class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для операции пополнения.
    """
    pass

class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Структура ответа для операции пополнения.
    """
    operation: OperationSchema

class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для операции кешбека.
    """
    pass

class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Структура ответа для операции кешбека.
    """
    operation: OperationSchema

class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для операции перевода.
    """
    pass

class MakeTransferOperationResponseSchema(BaseModel):
    """
    Структура ответа для операции перевода.
    """
    operation: OperationSchema

class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для операции покупки.
    """
    category: str = Field(default_factory=fake.category)

class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Структура ответа для операции покупки.
    """
    operation: OperationSchema

class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для операции оплаты по счету.
    """
    pass

class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Структура ответа для операции оплаты по счету.
    """
    operation: OperationSchema

class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для операции снятия наличных.
    """
    pass

class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Структура ответа для операции снятия наличных.
    """
    operation: OperationSchema