import discord
client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    await client.change_presence(status=discord.Status.online, activity=discord.Game('관리'))

@client.event
async def on_message(message):
    if message.content.startswith("/출근"):
        try:
            if message.author.guild_permissions.manage_messages:
                embed = discord.Embed(color=0x80E12A)
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 출퇴근 알림', value='관리자가 출근하였습니다.')
                await client.get_channel(853505093952995336).send(embed=embed)
        except:
            pass
    if message.content.startswith("/퇴근"):
        try:
            if message.author.guild_permissions.manage_messages:
                embed = discord.Embed(color=0xFF0000)
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 출퇴근 알림', value='관리자가 퇴근하였습니다.')
                await client.get_channel(853505093952995336).send(embed=embed)
        except:
            pass

client.run('ODUzNTUwOTQzODk5NzQ2MzI0.YMXBQw.GtRYADlF3XYYCdhso93HzuWZ4Tc')
