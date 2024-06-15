import telebot
import random
from telebot.types import InlineQuery, InputTextMessageContent, InlineQueryResultVideo

bot = telebot.TeleBot("6374431039:AAEvnN3HTw8T7oWe7qYB6-sDQMJYmF6zgEk")
e = 0
plus_icon = "https://pp.vk.me/c627626/v627626512/2a627/7dlh4RRhd24.jpg"
minus_icon = "https://pp.vk.me/c627626/v627626512/2a635/ILYe7N2n8Zo.jpg"
divide_icon = "https://pp.vk.me/c627626/v627626512/2a620/oAvUk7Awps0.jpg"
multiply_icon = "https://pp.vk.me/c627626/v627626512/2a62e/xqnPMigaP5c.jpg"
error_icon = "https://pp.vk.me/c627626/v627626512/2a67a/ZvTeGq6Mf88.jpg"
root_icon = "https://avatars.dzeninfra.ru/get-zen_doc/173924/pub_5bf9424e06d7e800ab306a50_5bf9cf20dde28b00aaccc04b/scale_1200"

@bot.message_handler(commands=["start"])
def start(msg: telebot.types.Message):
    list = ["Hi, user!", "Hello there!", "Welcome!"]
    bot.send_message(msg.chat.id, random.choice(list))

@bot.message_handler(content_types=["text"])
def maths(msg: telebot.types.Message):
    if msg.text.lower().startswith("math"):
        bot.send_message(msg.chat.id, "How can I help you?")
        bot.register_next_step_handler(msg,inline)

def mathanswer(msg: telebot.types.Message):
    try:
        result = eval(msg.text)
        bot.send_message(msg.chat.id, f"The answer is: {result}")
    except Exception as e:
        bot.send_message(msg.chat.id, f"Error: {e}")




@bot.inline_handler(func=lambda query: len(query.query) > 1)
def inline(query: InlineQuery):
    global e
    print(query.query)
    nums = query.query.split(" ")
    if nums[1] == "+":
        e = nums[4] + " - " + nums[2]
    if nums[1] == "-":
        e = nums[4] + " + " + nums[2]
    if nums[1] == "*":
        e = nums[4] + " / " + nums[2]
    if nums[1] == "/":
        e = nums[4] + " * " + nums[2]
    e = eval(e)

    # r = telebot.types.InlineQueryResultVideo('1',
    #                                          'https://github.com/eternnoir/pyTelegramBotAPI/blob/master/tests/test_data'
    #                                          '/test_video.mp4?raw=true',
    #                                          'video/mp4',
    #                                          'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master'
    #                                          '/examples/detailed_example/rooster.jpg',
    #                                          'Title'
    #                                          )

    # if query.query == "cat":
    #     cat = telebot.types.InlineQueryResultPhoto("1",
    #                                                "https://th-thumbnailer.cdn-si-edu.com/ii_ZQzqzZgBKT6z9DVNhfPhZe5g=/fit-in/1600x0/filters:focal(1061x707:1062x708)/https://tf-cmsv2-smithsonianmag-media.s3.amazonaws.com/filer_public/55/95/55958815-3a8a-4032-ac7a-ff8c8ec8898a/gettyimages-1067956982.jpg",
    #                                                "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/1200px-Cat03.jpg")
    #     input_message_content=telebot.types.InputTextMessageContent("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/1200px-Cat03.jpg")
    # print(nums)
    # nums = tuple(map(float, nums))
    # print(nums)
    # summ = sum(nums)
    # dif = nums[0]
    # for i in nums[1:]:
    #     dif -= i
    # mult = nums[0]
    # for i in nums[1:]:
    #     mult *= i
    # quo = nums[0]
    # for i in nums[1:]:
    #     quo /= i
    # sqrt = nums[0] ** 0.5
    # answer1 = telebot.types.InlineQueryResultArticle("1", "Summ", description=f"Result = {summ}",
    #                                            input_message_content=InputTextMessageContent(
    #                                                f"{nums[0]} {''.join([f' + {i}' for i in nums[1:]])} = {summ}"), thumbnail_url=plus_icon)
    # answer2 = telebot.types.InlineQueryResultArticle("2", "Subtraction", description=f"Result = {dif}",
    #                                            input_message_content=InputTextMessageContent(
    #                                                f"{nums[0]} {' - '.join([str(i) for i in nums[1:]])} = {dif}"), thumbnail_url=minus_icon
    #                                            )
    #
    # answer3 = telebot.types.InlineQueryResultArticle("3", "Multiplication", description=f"Result = {mult}",
    #                                            input_message_content=InputTextMessageContent(
    #                                                f"{nums[0]} {' * '.join([str(i) for i in nums[1:]])} = {mult}"), thumbnail_url=multiply_icon
    #                                            )
    #
    # answer4 = telebot.types.InlineQueryResultArticle("4", "Division", description=f"Result = {quo}",
    #                                            input_message_content=InputTextMessageContent(
    #                                                f"{nums[0]} {' / '.join([str(i) for i in nums[1:]])} = {quo}"), thumbnail_url=divide_icon
    #                                            )
    #
    # answer5 = telebot.types.InlineQueryResultArticle("5", "Square Root", description=f"Result = {sqrt}",
    #                                            input_message_content=InputTextMessageContent(f"√{nums[0]} = {sqrt}"), thumbnail_url=root_icon
    #                                            )
    urav = telebot.types.InlineQueryResultArticle("6", "equations", description=f"Result = {e}",
                                                  input_message_content=InputTextMessageContent(f"x = {e}"))
    # bot.answer_inline_query(query.id,[answer1,answer2, answer3, answer4, answer5, urav])
    bot.answer_inline_query(query.id,[urav])



    # if query.query=="video":
    #     r = telebot.types.InlineQueryResultVideo('1',
    #                             'https://github.com/eternnoir/pyTelegramBotAPI/blob/master/tests/test_data'
    #                             '/test_video.mp4?raw=true',
    #                             'video/mp4',
    #                             'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master'
    #                             '/examples/detailed_example/rooster.jpg',
    #                             'Title'
    #                             )
    #     bot.answer_inline_query(query.id, [r])


bot.infinity_polling()
