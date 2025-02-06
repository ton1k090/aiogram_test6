from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from keyboards.builders import profile
from keyboards.reply import rmk
from utils.states import Form

router = Router()


@router.message(Command('profile'))
async def fill_profile(message: Message, state: FSMContext):
    '''Задаем начало стейтов'''
    await state.set_state(Form.name) # Запрашиваем поле имя
    await message.answer(
        'input your name',
        reply_markup=profile(message.from_user.first_name)
    )


@router.message(Form.name)
async def form_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)  # Устанавливаем поле имя
    await state.set_state(Form.age) # Запрашиваем поле возвраст
    await message.answer('Input your age', reply_markup=rmk) # Убираем клавиатуру


@router.message(Form.age)
async def form_age(message: Message, state: FSMContext):
    if message.text.isdigit(): #nЕсли введено число то
        await state.update_data(age=message.text) # Устанавливаем поле возврасс
        await state.set_state(Form.sex) # Запрашиваем поле пол
        await message.answer('Input your sex', reply_markup=profile(['male', 'female'])) # Lj,fdkztv rkfdbfnehe
    else:
        await message.answer('input digit!')


@router.message(Form.sex, F.text.casefold().in_(['male', 'female']))
async def form_sex(message: Message, state: FSMContext):
    await state.update_data(sex=message.text) # Устанавливаем поле пол
    await state.set_state(Form.about) # Запрашиваем поле о себе
    await message.answer('tell me about yourself', reply_markup=rmk)


@router.message(Form.sex)
async def incorrect_form_sex(message: Message, state: FSMContext):
    '''Если пол введен не верно'''
    await message.answer('button!!!')


@router.message(Form.about)
async def form_about(message: Message, state: FSMContext):
    if len(message.text) < 5: # Если текст меньше 5 символов
        await message.answer('enter something more interesting')
    else:
        await state.update_data(about=message.text) # Добавляем поле о себе
        await state.set_state(Form.photo) # Запрашиваем поле фото
        await message.answer('now send a photo about')


@router.message(Form.photo, F.photo)
async def form_photo(message: Message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id # получаем поле фото с лучшим качеством -1
    data = await state.get_data() # Все данные
    await state.clear() # завершить стейт

    formatted_text = []
    [
        formatted_text.append(f'{key}: {value}')
        for key, value in data.items()
    ]
    await message.answer_photo(
        photo_file_id,
        '\n'.join(formatted_text)
                               )


@router.message(Form.photo, ~F.photo)
async def incorrect_form_photo(message: Message, state: FSMContext):
    await message.answer('This is noy photo! Send photo')