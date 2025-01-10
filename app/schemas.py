from pydantic import BaseModel ,Field ,field_validator


class ProductBase (BaseModel):
    nombre: str = Field(... , min_length=1 )
    categoria: str = Field(... , min_length=1 )
    precio: float = Field(... , gt=0)
    stock: int = Field(... , ge=0)

    @field_validator('precio')
    def validate_price(cls, value):
        if value < 0:
            raise ValueError('Price must be greater than zero')
        return value
    @field_validator('stock')
    def validate_stock(cls, value):
        if value < 0:
            raise ValueError('Stock must be greater than zero')
        return value



class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    nombre : str | None = None
    categoria : str | None = None
    precio : float | None = None
    stock : int | None = None

class Product (ProductBase):
    id : int
    class Config:
        from_attributes = True