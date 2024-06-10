from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

router = Router()


# Хэндлер для сообщений, которые не попали в другие хэндлеры
# При декорировании хэндлера, мы не устанавливаем никакие фильтры, то есть этот
# хэндлер будет срабатывать на любые сообщения от пользователя. Это означает,
# что его нужно регистрировать последним, среди зарегистрированных хэндлеров
@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])
