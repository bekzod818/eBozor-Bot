from aiogram import types
from aiogram.types import LabeledPrice
from loader import db
from utils.misc.product import Product

python_book = Product(
    title="Biror bir mahsulot bo'lishi garak adi",
    description="Mahsulotga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="USD",
    prices=[
        LabeledPrice(
            label='Kitob',
            amount=500,  # 5.00$
        ),
        LabeledPrice(
            label='Yetkazib berish (7 kun)',
            amount=100,  # 1.00$
        ),
    ],
    start_parameter="create_invoice_python_book",
    photo_url='https://www.ferra.ru/thumb/1720x0/filters:quality(75):no_upscale()/imgs/2021/10/28/14/4989939/40e77b7bc45b7657f2b458a243c3052cd77ece32.png',
    photo_width=1280,
    photo_height=800,
    # photo_size=800,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,  # foydalanuvchi manzilini kiritishi shart
    is_flexible=True,
)

REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title="Pochta (3 kun)",
    prices=[
        LabeledPrice(
            'Maxsus quti', 100),
        LabeledPrice(
            '3 ish kunida yetkazish', 100),
    ]
)
FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Express pochta (1 kun)',
    prices=[
        LabeledPrice(
            '1 kunda yetkazish', 100),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(id='pickup',
                                       title="Do'kondan olib ketish",
                                       prices=[
                                           LabeledPrice("Yetkazib berishsiz", -100)
                                       ])
