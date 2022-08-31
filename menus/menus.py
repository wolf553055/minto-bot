from discord.ext import commands
from discord import Embed
from discord_components import DiscordComponents, Button, ButtonStyle
import settings
import discord


class MyWelcomeMenu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def welcome_menu(self, ctx):
        embed = Embed(title = 'Welcome to <:minto_logo:1007563227837780108> Minto Discord!', 
                      description=settings.WELCOME_MENU_DESCRIPTION, color=0x2f3137)
        components = [[
                Button(style = ButtonStyle.URL, url = 'https://t.me/btcmtofficial', label='Telegram', emoji=self.client.get_emoji(1007563235861467166)),
                Button(style = ButtonStyle.URL, url = 'https://twitter.com/BTCMTOfficial', label='Twitter', emoji=self.client.get_emoji(1007563233936293899)),
                Button(style = ButtonStyle.URL, url = 'https://minto.finance/', label='Website', emoji=self.client.get_emoji(1007563230849290400)),
        ]]
        await ctx.send(embed=embed, components=components)

    @commands.command()
    async def welcome_img(self, ctx):
        await ctx.send(file = discord.File("minto_main.png"))

class MyInfoMenu(commands.Cog):
    def __init__(self, client):
        self.client = client

    def roles_info_menu(self):
        embed = discord.Embed(title="<:minto_person:1007563246351437854> Special roles", 
                      description=settings.CONTENT_ROLES, 
                      color=0x54dac1)
        embed.add_field(name="\u200b", value=settings.FIRST_LVL, inline=True)
        embed.add_field(name="\u200b", value=settings.FIFTH_LVL, inline=True)
        embed.add_field(name="\u200b", value=settings.TENTH_LVL, inline=True)
        embed.add_field(name="\u200b", value=settings.TWENTY_FIFTH_LVL, inline=True)
        embed.add_field(name="\u200b", value=settings.FIFTY_FIFTH_LVL, inline=True)
        return embed
    
    def chats_info_menu(self):
        embed = discord.Embed(title="<:minto_star:1007563229150588979> Chats", 
                      description=settings.CONTENT_CHATS, 
                      color=0x54dac1)
        embed.add_field(name="Community", value=settings.COMMUNITY_CHATS, inline=True)
        embed.add_field(name="Information", value=settings.INFORMATION_CHATS, inline=True)
        return embed

    def rules_info_menu(self):
        embed = discord.Embed(title="<:minto_book:1007563226143264858> RULES", 
                      description=settings.RULES_INFO, 
                      color=0x54dac1)
        return embed
        

    @commands.command()
    async def info_menu(self, ctx):
        embed = Embed(title = '', 
                      url='https://minto.finance/about', 
                      description=settings.INFO_MENU_DESCRIPTION, color=0x54dac1)
        embed.add_field(name="Quick Links", value=settings.INFO_MENU_LINKS, inline=True)
        embed.add_field(name="Information", value=settings.INFO_MENU_INFORMATION, inline=True)
        embed.add_field(name="To Buy BTCMT", value="Follow this [link](https://minto.finance/purchase) to our website or purchase on [PancakeSwap](https://pancakeswap.finance/swap?inputCurrency=0x55d398326f99059ff775485246999027b3197955&outputCurrency=0x410a56541bD912F9B60943fcB344f1E3D6F09567) exchange.", inline=False,)
        components = [[
                Button(style = ButtonStyle.grey, label = 'Roles info', custom_id="bth_roles_info", emoji=self.client.get_emoji(1007563246351437854)),
                Button(style = ButtonStyle.grey, label = 'Chats', custom_id="chats", emoji=self.client.get_emoji(1007563229150588979)),
                Button(style = ButtonStyle.grey, label = 'Server rules', custom_id="bth_server_rules", emoji=self.client.get_emoji(1007563226143264858)),
        ]]
        await ctx.send(embed = embed, components = components)
        while True:
            response = await self.client.wait_for('button_click')
            if response.message.id == 891587821368905728:
                await response.respond(type=6)
            elif response.component.custom_id == 'bth_roles_info':
                await response.respond(embed=self.roles_info_menu(), ephemeral=True)
            elif response.component.custom_id == 'chats':
                await response.respond(embed=self.chats_info_menu(), ephemeral=True)
            elif response.component.custom_id == 'bth_server_rules':
                await response.respond(embed=self.rules_info_menu(), ephemeral=True)


class MySelectMenu(commands.Cog):
    def __init__(self, client):
        self.client = client

    def select_info_menu(self, title, description):
        embed = discord.Embed(title=title, 
                      description=description, 
                      color=0x54dac1)
        return embed

    @commands.command()
    async def select_menu(self, ctx):
        embed = Embed(title = 'Frequently Asked Questions', description="Select your question from the dropdown below to get an answer to! If your question isn't listed here, feel free to ask <@981596992478269442>", color=0x2f3137)
        components = [
            settings.OPTIONS
        ]
        await ctx.send(embed=embed, components=components)
        while True:
            response = await self.client.wait_for("select_option")
            if response.message.id == 891587821368905728: #Message id(not obligatory)
                await response.respond(type=6)
            try:
                await response.respond(embed=self.select_info_menu(title=response.values[0], description=settings.FAQ[response.values[0]]), ephemeral=True)
            except:
                print("this question doesn't exist")


def setup(client):
    DiscordComponents(client)
    client.add_cog(MyInfoMenu(client))
    client.add_cog(MyWelcomeMenu(client))
    client.add_cog(MySelectMenu(client))
