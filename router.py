import asyncio
from aiogram import types, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()


class NoteState(StatesGroup):
    waiting_for_note = State()

@router.message(CommandStart())
async def start(message: types.Message):
    print(message)
    await message.answer("Привет! Я помогу сохранить твои заметки. Используй команду /add, чтобы добавить заметку.")


@router.message(Command('add'))
async def add(message: types.Message, state: FSMContext):
    await message.answer('Пожалуйста введите заметку')
    await state.set_state(NoteState.waiting_for_note)


@router.message(NoteState.waiting_for_note)
async def write_note(message: types.Message, state: FSMContext):
    await message.answer(message.text)
    await state.clear()
    
