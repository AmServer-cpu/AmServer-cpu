import discord
client = discord.Client()

@client.event
async def on_ready():
    print("���� ���������� ����Ǿ����ϴ�.")
    await client.change_presence(status=discord.Status.online, activity=discord.Game('����'))

@client.event
async def on_message(message):
    if message.content.startswith("/���"):
        try:
            if message.author.guild_permissions.manage_messages:
                embed = discord.Embed(color=0x80E12A)
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                embed.add_field(name='������ ����� �˸�', value='�����ڰ� ����Ͽ����ϴ�.')
                await client.get_channel(853505093952995336).send(embed=embed)
        except:
            pass
    if message.content.startswith("/���"):
        try:
            if message.author.guild_permissions.manage_messages:
                embed = discord.Embed(color=0xFF0000)
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                embed.add_field(name='������ ����� �˸�', value='�����ڰ� ����Ͽ����ϴ�.')
                await client.get_channel(853505093952995336).send(embed=embed)
        except:
            pass

client.run('ODUzNTUwOTQzODk5NzQ2MzI0.YMXBQw.GtRYADlF3XYYCdhso93HzuWZ4Tc')
