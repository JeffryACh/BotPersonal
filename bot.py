"""
Autor: Jeffry Araya Ch
Creación: 03/08/2024 17:30
Modificación: 

Descripción:
    'Este es mi primer bot de Discord!'
"""

import discord
from discord.ext import commands
import openai
import os
from dotenv import load_dotenv

load_dotenv()


DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

"""
    Evento que se ejecuta cuando el bot está listo para recibir eventos.

    No se requieren argumentos.

    No devuelve nada.
"""
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}#{bot.user.discriminator}')

"""
    Un comando que utiliza la API de OpenAI para generar una respuesta basada en la pregunta proporcionada.

    Args:
        ctx (discord.ext.commands.Context): El contexto de la invocación del comando.
        question (str, opcional): La pregunta para generar una respuesta. Por defecto, None.

    Returns:
        None: Este comando no devuelve nada.

    Raises:
        None: Este comando no lanza ninguna excepción.

    Uso:
        ->Jarvis <pregunta>

    Ejemplo:
        ->Jarvis ¿Cuál es la capital de Italia?
"""
@bot.command(name='Jarvis')
async def jarvis(ctx, *, question: str = None):
    if question is None:
        await ctx.send("Por favor, proporciona una pregunta después del comando.")
        return
    
    try:
        openai.api_key = OPENAI_API_KEY
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Puedes usar otro modelo si prefieres
            messages=[
                {"role": "user", "content": question}
            ]
        )
        await ctx.send(response.choices[0].message['content'].strip()) # Mostrar la respuesta
    except Exception as e:
        await ctx.send(f'Ocurrió un error al interactuar con OpenAI: {str(e)}')

bot.run(DISCORD_TOKEN)
