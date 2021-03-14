import discord , asyncio , random , time , os

client = discord.Client()

gat = ['뽑기','ㅃㄱ']
rd = ['확률','ㅎㄹ']
va = ['버전','ㅂㅈ']
Slang = ['야발','씨발','개세끼','좃같네','꼴받게 하네','ㅆ']
goalbage = ['나올때까지 한다' , '이제 나와라','...']


@client.event
async def on_ready():

    print(client.user.name)
    print("봇 시작됨")
    await client.change_presence(status=discord.Status.online)

@client.event
async def on_message(message):
    if message.content == "방법":
        await message.channel.send("체팅창에 '뽑기' 또는 'ㅃㄱ'를 입력하면 자동으로 뽑기의 참여됩니다.")
        await message.channel.send("체팅창에 '확률' 또는 'ㅎㄹ' 이라고 치면 상세 확률을 알 수 있습니다.")
        await message.channel.send("체팅창에 '버전' 또는 'ㅂㅈ' 이라고 치면 이 봇의 버전 밎 개발자를 알 수 있습니다.")
        await message.channel.send("당첨 상품의 경우 고정 메시지를 확인하세요")
    if message.content in rd:
        await message.channel.send("1등 : 1000000000 분의 1 입니다.")
        await message.channel.send("2등 : 100000000 분의 1 입니다.")
        await message.channel.send("3등 : 1000000 분의 1 입니다.")
        await message.channel.send("4등 : 100 분의 1 입니다.")
    if message.content in va:
        await message.channel.send("현재 버전은 배타 0.24 입니다.")
        await message.channel.send("개발자 : NOKCHA (이 디스코드 봇의 모든 저작권은 NOKCHA에게 있으며 무단 복제 밎 배포는 처벌의 대상이 될 수 있습니다.)")
    if message.content in goalbage:
        await message.channel.send("아잉 절대 안나오고 ㅋㅋㅋ")
    if message.content in Slang:
        await message.channel.send("비속어는 나쁜거예요")
    if message.content in gat:
        rnum = random.randint(0,1000000000)
        if rnum == 0 :
            await message.channel.send("1등 당첨")
            await message.channel.send("서버장에게 개인디코로 상품을 요구하세요")
            await message.channel.send("상품의 경우 고정 메시지를 확인하세요")
            time.sleep(0.5)
        if  10 >= rnum > 0 :
            await message.channel.send("2등 당첨")
            await message.channel.send("서버장에게 개인디코로 상품을 요구하세요")
            await message.channel.send("상품의 경우 고정 메시지를 확인하세요")
            time.sleep(0.5)
        if  1010 >= rnum > 10 :
            await message.channel.send("3등 당첨")
            await message.channel.send("서버장에게 개인디코로 상품을 요구하세요")
            await message.channel.send("상품의 경우 고정 메시지를 확인하세요")
            time.sleep(0.5)
        if 10001010 >= rnum > 1010:
            await message.channel.send("4등 당첨")
            await message.channel.send("서버장에게 개인디코로 상품을 요구하세요")
            await message.channel.send("상품의 경우 고정 메시지를 확인하세요")
            time.sleep(0.5)
        if rnum > 10001010 :
            await message.channel.send("꽝")
            time.sleep(1)
            
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
