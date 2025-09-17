from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import logging
import config

logging.basicConfig(level=config.LOG_LEVEL)

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

CATEGORIES = {
    "Электроника": [
    {"name": "Смартфон", "desc": "Современный смартфон с отличной камерой.", "photo": "Photos/Example.JPG"},
    {"name": "Ноутбук", "desc": "Мощный ноутбук для работы и игр.", "photo": "Photos/Example.JPG"},
    {"name": "Планшет", "desc": "Удобный планшет для учебы и развлечений.", "photo": "Photos/Example.JPG"},
    {"name": "Наушники", "desc": "Беспроводные наушники с шумоподавлением.", "photo": "Photos/Example.JPG"},
    {"name": "Умные часы", "desc": "Фитнес-трекер и часы в одном устройстве.", "photo": "Photos/Example.JPG"},
    {"name": "Телевизор", "desc": "4K Smart TV с поддержкой Wi-Fi.", "photo": "Photos/Example.JPG"}
    ],
    "Одежда": [
    {"name": "Футболка", "desc": "Стильная футболка из хлопка.", "photo": "Photos/Example.JPG"},
    {"name": "Кроссовки", "desc": "Удобные кроссовки для спорта.", "photo": "Photos/Example.JPG"},
    {"name": "Джинсы", "desc": "Классические джинсы синего цвета.", "photo": "Photos/Example.JPG"},
    {"name": "Куртка", "desc": "Теплая зимняя куртка.", "photo": "Photos/Example.JPG"},
    {"name": "Платье", "desc": "Летнее платье с цветочным принтом.", "photo": "Photos/Example.JPG"},
    {"name": "Шорты", "desc": "Удобные спортивные шорты.", "photo": "Photos/Example.JPG"}
    ],
    "Бытовая техника": [
    {"name": "Пылесос", "desc": "Мощный пылесос для дома.", "photo": "Photos/Example.JPG"},
    {"name": "Микроволновка", "desc": "Компактная микроволновая печь.", "photo": "Photos/Example.JPG"},
    {"name": "Холодильник", "desc": "Энергоэффективный холодильник.", "photo": "Photos/Example.JPG"},
    {"name": "Стиральная машина", "desc": "Автоматическая стиральная машина.", "photo": "Photos/Example.JPG"},
    {"name": "Кофемашина", "desc": "Эспрессо кофемашина для дома.", "photo": "Photos/Example.JPG"}
    ],
    "Книги": [
    {"name": "Роман", "desc": "Захватывающий современный роман.", "photo": "Photos/Example.JPG"},
    {"name": "Научная литература", "desc": "Книга для расширения кругозора.", "photo": "Photos/Example.JPG"},
    {"name": "Детектив", "desc": "Остросюжетный детектив.", "photo": "Photos/Example.JPG"},
    {"name": "Фантастика", "desc": "Книга в жанре научной фантастики.", "photo": "Photos/Example.JPG"},
    {"name": "Сказки", "desc": "Сборник детских сказок.", "photo": "Photos/Example.JPG"}
    ],
    "Игрушки": [
    {"name": "Конструктор", "desc": "Развивающий конструктор для детей.", "photo": "Photos/Example.JPG"},
    {"name": "Плюшевый медведь", "desc": "Мягкая игрушка для малышей.", "photo": "Photos/Example.JPG"},
    {"name": "Машинка", "desc": "Игрушечная машинка.", "photo": "Photos/Example.JPG"},
    {"name": "Кукла", "desc": "Красивая кукла для девочек.", "photo": "Photos/Example.JPG"},
    {"name": "Настольная игра", "desc": "Веселая настольная игра для всей семьи.", "photo": "Photos/Example.JPG"}
    ],
    "Косметика": [
    {"name": "Шампунь", "desc": "Питательный шампунь для волос.", "photo": "Photos/Example.JPG"},
    {"name": "Крем для лица", "desc": "Увлажняющий крем для лица.", "photo": "Photos/Example.JPG"},
    {"name": "Тушь для ресниц", "desc": "Объемная тушь для ресниц.", "photo": "Photos/Example.JPG"},
    {"name": "Гель для душа", "desc": "Освежающий гель для душа.", "photo": "Photos/Example.JPG"},
    {"name": "Парфюм", "desc": "Ароматный парфюм.", "photo": "Photos/Example.JPG"}
    ],
    "Спорт": [
    {"name": "Гантели", "desc": "Набор гантелей для тренировок.", "photo": "Photos/Example.JPG"},
    {"name": "Скакалка", "desc": "Спортивная скакалка.", "photo": "Photos/Example.JPG"},
    {"name": "Тренажер", "desc": "Домашний тренажер для фитнеса.", "photo": "Photos/Example.JPG"},
    {"name": "Мяч", "desc": "Футбольный мяч.", "photo": "Photos/Example.JPG"}
    ],
    "Авто": [
    {"name": "Масло моторное", "desc": "Синтетическое моторное масло.", "photo": "Photos/Example.JPG"},
    {"name": "Автомагнитола", "desc": "Современная автомагнитола.", "photo": "Photos/Example.JPG"},
    {"name": "GPS-навигатор", "desc": "Автомобильный GPS-навигатор.", "photo": "Photos/Example.JPG"}
    ],
    "Мебель": [
    {"name": "Диван", "desc": "Удобный диван для гостиной.", "photo": "Photos/Example.JPG"},
    {"name": "Стол", "desc": "Обеденный стол из массива.", "photo": "Photos/Example.JPG"},
    {"name": "Кресло", "desc": "Мягкое кресло для отдыха.", "photo": "Photos/Example.JPG"}
    ]
}
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(KeyboardButton("Категории"))

@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer("Добро пожаловать в каталог товаров!", reply_markup=main_menu)

@dp.message_handler(lambda m: m.text == "Категории")
async def show_categories(message: types.Message):
    markup = InlineKeyboardMarkup()
    for cat in CATEGORIES:
        markup.add(InlineKeyboardButton(cat, callback_data=f"cat_{cat}"))
    await message.answer("Выберите категорию:", reply_markup=markup)

@dp.callback_query_handler(lambda c: c.data.startswith("cat_"))
async def show_products(callback: types.CallbackQuery):
    cat = callback.data[4:]
    products = CATEGORIES.get(cat, [])
    markup = InlineKeyboardMarkup()
    for idx, prod in enumerate(products):
        markup.add(InlineKeyboardButton(prod["name"], callback_data=f"prod_{cat}_{idx}"))
    await callback.message.edit_text(f"Товары в категории '{cat}':", reply_markup=markup)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data.startswith("prod_"))
async def show_product(callback: types.CallbackQuery):
    _, cat, idx = callback.data.split("_", 2)
    prod = CATEGORIES[cat][int(idx)]
    photo = prod["photo"]
    if photo.startswith("http"):
        await bot.send_photo(callback.from_user.id, photo, caption=f"{prod['name']}\n\n{prod['desc']}")
    else:
        from aiogram.types import InputFile
        await bot.send_photo(callback.from_user.id, InputFile(photo), caption=f"{prod['name']}\n\n{prod['desc']}")
    await callback.answer()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
