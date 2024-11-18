import asyncio
from aiogram import types, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from database import get_notes as gn, add_note, delete_note


router = Router()

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Добавить заметку")],
        [KeyboardButton(text="Посмотреть заметки")],
        [KeyboardButton(text="Удалить заметку")],
    ],
    resize_keyboard=True
)


class NoteState(StatesGroup):
    waiting_for_note = State()


@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привет! Я помогу сохранить твои заметки. Используй команду /add, чтобы добавить заметку.", reply_markup=keyboard)


@router.message(lambda message: message.text == "Добавить заметку")
async def add(message: types.Message, state: FSMContext):
    await message.answer('Пожалуйста введите заметку')
    await state.set_state(NoteState.waiting_for_note)


@router.message(NoteState.waiting_for_note)
async def write_note(message: types.Message, state: FSMContext):
    text = message.text
    chat_id = message.chat.id
    add_note(user_id=chat_id, note=text)
    await message.answer("Запись добавлена успешно!")
    await state.clear()


@router.message(lambda message: message.text == "Посмотреть заметки")
async def get_notes(message: types.Message):
    notes = gn(message.chat.id)

    if notes:
        await message.answer("Ваши заметки: ")
        for note in notes:
            await message.answer(f"- {note[-1]}")    
    else:
        await message.answer("У вас на данный момент нет заметок.")


async def generate_keyboard(user_id):
    notes = gn(user_id)  # Здесь функция для получения заметок из базы
    if notes:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=note[-1], callback_data=f"delete:{note[0]}")]
                for note in notes
            ]
        )
    return None


@router.message(lambda message: message.text == "Удалить заметку")
async def delete_note_start(message: types.Message):
    keyboard = await generate_keyboard(message.chat.id)
    if keyboard:
        await message.answer("Выберите заметку для удаления:", reply_markup=keyboard)
    else:
        await message.answer("У вас нет заметок для удаления.")


@router.callback_query(lambda call: call.data.startswith("delete:"))
async def process_delete(callback_query: types.CallbackQuery):
    note_id = int(callback_query.data.split(":")[1])
    delete_note(note_id)  # Удаляем заметку из базы
    await callback_query.message.edit_text("Заметка удалена!")

