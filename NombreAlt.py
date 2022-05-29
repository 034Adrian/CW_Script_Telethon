# -*- coding: utf-8 -*-
from telethon import TelegramClient, events
import random, asyncio, time, aiocron, pytz

loop1 = asyncio.get_event_loop()

api_id = 12345678
api_hash = ""
phone= "Nombre_session"

CHAT_WARS = 408101137
BOTNIATO3 = 1561523253
target = "/ga_def"

set_order_cron = '57 6,14,22 * * *' # sin Hacer aiming

client1=TelegramClient(phone,api_id,api_hash)

async def noisy_sleep(t_max, t_min=0):
    rand_seconds = random.randrange(t_min, t_max)
    await asyncio.sleep(rand_seconds)

async def clic_intervene(event):
    buttons = await event.get_buttons()
    for bline in buttons:
        for button in bline:
            if 'Intervene' in button.button.text:
                await button.click()

async def clic_forest(event):
    buttons = await event.get_buttons()
    for bline in buttons:
        for button in bline:
            if 'Forest' in button.button.text:
                await button.click()

async def clic_swamp(event):
    buttons = await event.get_buttons()
    for bline in buttons:
        for button in bline:
            if 'Swamp' in button.button.text:
                await button.click()

async def clic_valley(event):
    buttons = await event.get_buttons()
    for bline in buttons:
        for button in bline:
            if 'Valley' in button.button.text:
                await button.click()
## bucle de arenas 
async def arenas():
    await client1.send_message('chtwrsbot', '▶️Fast fight')

async def reporte():
    await client1.send_message('chtwrsbot', '/report')

async def menu_quest():
    await client1.send_message('chtwrsbot', '🗺Quests')
## batallas
async def defend():
    await client1.send_message('chtwrsbot', '🛡Defend')

async def a_hignt():
    await client1.send_message('chtwrsbot', '⚔️Attack')
    time.sleep(2)
    await client1.send_message('chtwrsbot', '🦅')

async def a_deern():
    await client1.send_message('chtwrsbot', '⚔️Attack')
    time.sleep(2)
    await client1.send_message('chtwrsbot', '🦌')

async def a_moon():
    await client1.send_message('chtwrsbot', '⚔️Attack')
    time.sleep(2)
    await client1.send_message('chtwrsbot', '🌑')

async def a_pott():
    await client1.send_message('chtwrsbot', '⚔️Attack')
    time.sleep(2)
    await client1.send_message('chtwrsbot', '🥔')

async def a_drag():
    await client1.send_message('chtwrsbot', '⚔️Attack')
    time.sleep(2)
    await client1.send_message('chtwrsbot', '🐉')

async def a_shark():
    await client1.send_message('chtwrsbot', '⚔️Attack')
    time.sleep(2)
    await client1.send_message('chtwrsbot', '🦈')
## reenviar a lycaon
async def reenviar_lycaon(event):
    await event.forward_to('LycaonBot')

@client1.on(events.NewMessage(chats=('chtwrsbot'), incoming = True))
async def my_event_handler(event):
    
#go y pledges
    if 'You were strolling around on your horse when you noticed' in event.raw_text:
        time.sleep(random.randint(1, 2))
        await clic_intervene(event)

    if '/pledge' in event.raw_text:
        time.sleep(random.randint(1, 2))
        await client1.send_message('chtwrsbot', '/pledge')

#bichos
    if 'You met some hostile creatures' in event.raw_text:
        async with client1.conversation('chtwrsbot'):
            await reenviar_lycaon(event)

    if 'Your result on the battlefield:' in event.raw_text:
        async with client1.conversation('chtwrsbot'):
            await reenviar_lycaon(event)
            time.sleep(random.randint(1, 2))
            await menu_quest()
           
##abriendo menu de quests               
    if 'Stamina restored' in event.raw_text:
        time.sleep(random.randint(1, 10))
        await menu_quest()

    if 'You received:' in event.raw_text:
        time.sleep(random.randint(1, 10))
        await menu_quest()

    if 'Not enough stamina.' in event.raw_text:
        time.sleep(random.randint(1, 10))
        await defend()

##quests normales 
    if '🌲Forest' in event.raw_text:
        time.sleep(random.randint(1, 3))

        if not '🔒' in event.raw_text:
            await arenas()   

        if '🌲Forest' and '🔥' in event.raw_text:

            if '🌲Forest 3min 🔥' in event.raw_text:
                await clic_forest(event)

            elif '🍄Swamp 4min 🔥' in event.raw_text:
                await clic_swamp(event)

            elif '🏔Mountain Valley 4min 🔥' in event.raw_text:
                await clic_valley(event)

            elif '🌲Forest 5min 🔥' in event.raw_text:
                await clic_forest(event)

            elif '🍄Swamp 6min 🔥' in event.raw_text:
                await clic_swamp(event)

            elif '🏔Mountain Valley 6min 🔥' in event.raw_text:
                await clic_valley(event)

        else:
            await clic_valley(event) 

    if 'You found hidden' in event.raw_text:
        await client1.forward_messages(BOTNIATO3, event.message)       

@client1.on(events.NewMessage(chats=(-1001510356585), incoming = True))
async def my_event_handler(event):
    if 'Battle results:' in event.raw_text:
        async with client1.conversation(-1001510356585):
            time.sleep(random.randint(600, 610))
            await reporte()

@client1.on(events.NewMessage(chats=('LycaonBot'), incoming = False))
async def my_event_handler(event):
    if 'Your arrows are getting low.' in event.raw_text:
        if 'Bodkin arrow' in event.raw_text:
            await client1.send_message('chtwrsbot', '/use_523')

@client1.on(events.NewMessage(chats=(-1237607365), incoming = False))
async def my_event_handler(event):

    if 'Battle results:' in event.raw_text:
        async with client1.conversation(-1237607365):
            time.sleep(random.randint(600, 610))
            await reporte()

    if '⚔️Attack' in event.raw_text:

        if '⚔️Attack 🦈SHARKS' in event.raw_text:
            time.sleep(1)
            await a_shark()

        #elif '🦅' in event.raw_text:
            #time.sleep(1)
            #await a_hignt()

        elif '⚔️Attack 🐉DRAGONS' in event.raw_text:
            time.sleep(1)
            await a_drag()

        #elif '🥔' in event.raw_text:
            #time.sleep(1)
            #await a_pott()

        #elif '🌑' in event.raw_text:
            #time.sleep(1)
            #await a_moon()

        #elif '🦌' in event.raw_text:
            #time.sleep(1)
            #await a_deern()

@client1.on(events.NewMessage(chats=BOTNIATO3, incoming = True))
async def my_event_handler(event):
    if 'Órdenes para la próxima batalla' in event.raw_text:
        global target
        target = '/ga_' + \
            event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]
    
    if 'Por motivos de seguridad' in event.raw_text:
        command = '/' + event.message.text.split('/')[-1]
        await client1.send_message(BOTNIATO3, command)
    
    if 'Buzzing Tailor just set the orders' in event.raw_text:
        await client1.send_message(BOTNIATO3, '/order')

async def order_setter():
    await noisy_sleep(60)
    await client1.send_message(CHAT_WARS, target)
    print('order_set')

    # Sets the order automatically
@aiocron.crontab(set_order_cron, tz=pytz.utc)
async def set_order():
    await order_setter()
    global target
    target = '/ga_def'