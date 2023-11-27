from discord.ext import commands
from discord.commands import Option
from config import TOKEN, PREFIX

import discord
import tracemalloc
import g4f

tracemalloc.start(999)

intents = discord.Intents.default()
intents.message_content = True  # Включаем обработку контента сообщений

bot = commands.Bot(command_prefix=PREFIX, intents=intents)


@bot.event
async def on_ready():
    print(f"Мы успешно вошли как {bot.user}")


@bot.slash_command(name='bing', description='Тестовая команда для проверки аргументов')
async def bing(ctx, message: Option(str, 'Задайте любой вопрос Bing', required=True)):
    await ctx.respond('Генерация ответа...')
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": message}],
            provider=g4f.Provider.Bing,
            proxy="http://172.245.159.177:80",
        )
        await ctx.respond(str(response))
    except Exception as e:
        await ctx.respond(f"Ошибка: {e}")
        await print(e)


bot.run(TOKEN)
