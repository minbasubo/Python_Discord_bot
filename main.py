import discord
from discord.ext import commands
import calendar
from datetime import datetime


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("--- 연결 성공 ---")
    print(f"봇 이름 : {bot.user.name}")
    print(f"ID : {bot.user.id}")
    await bot.change_presence(activity=discord.Game("명령어 가이드 = !도움"))

@bot.command()
async def 디데이(ctx, sty, stm, std, edy, edm, edd):
    try:
        mon_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        st_year = int(sty)
        st_month = int(stm)
        st_day = int(std)
        ed_year = int(edy)
        ed_month = int(edm)
        ed_day = int(edd)
        if st_year % 4 == 0 and (st_year % 100 != 0 or st_year % 400 == 0):  # 윤년
            mon_day[1] = 29
        if ed_year % 4 == 0 and (ed_year % 100 != 0 or ed_year % 400 == 0):  # 윤년
            mon_day[1] = 29

        def day(month, day):
            monthday_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            total = 0
            for i in range(month - 1):
                total += monthday_list[i]
            total += day
            return total - 1

        def solution(st_month, st_day, ed_month, ed_day):
            start_total = day(st_month, st_day)
            end_total = day(ed_month, ed_day)
            return end_total - start_total

        y = (ed_year * 365) - (st_year * 365)
        result = solution(st_month, st_day, ed_month, ed_day) + y

        if result > 0:
            D_Day = discord.Embed(title=f"D-Day : {result}일", color=0xEF746F)
            await ctx.send(embed=D_Day)
        else:
            D_Day = discord.Embed(title=f"D-Day : {-result}일", color=0xEF746F)
            await ctx.send(embed=D_Day)
    except:
        Title = discord.Embed(title="잘못된 형식을 입력했습니다. 다시 입력해 주세요.", color=0xEF746F)
        await ctx.send(embed=Title)

@bot.command(name="달력") #달력 기능
async def 달력(ctx, year):
    if year.isdigit():
        Title = discord.Embed(title=f"{year}달력을 출력합니다.", color=0xEF746F)
        Des = discord.Embed(description="", color=0xEF746F)
        for month in range(1, 13):
            Des.add_field(name=f"{year}년의 {month}월의 달력", value=calendar.month(int(year), int(month)), inline=True)
        await ctx.send(embed=Title)
        await ctx.send(embed=Des)
    elif not year.isdigit():
        Title = discord.Embed(title="잘못된 년도입니다. 다시 입력해 주세요.", color=0xEF746F)
        await ctx.send(embed=Title)

@bot.command(name="메모") #메모장 기능
async def 메모(ctx, *args):
    embed = discord.Embed(title="메모를 시작합니다.", color=0xEF746F)
    written_text = discord.Embed(title=f"{datetime.today().month}월 {datetime.today().day}일",
                                 description=f"{' '.join(args)}", color=0xEF746F)
    channel = bot.get_channel(778616267912773662)
    await ctx.send(embed=embed)
    await channel.send(embed=written_text)

@bot.command()
async def 날짜(ctx, year, month):
    if year.isdigit() and month.isdigit():
        Title = discord.Embed(title=f"{year}년 {month}월의 달력을 출력합니다.", color=0xEF746F)
        print_month = discord.Embed(description="", color=0xEF746F)
        print_month.add_field(name=f"{year}년의 {month}월의 달력", value=calendar.month(int(year), int(month)), inline=True)
        await ctx.send(embed=Title)
        await ctx.send(embed=print_month)
    elif not year.isdigit():
        Title = discord.Embed(title="잘못된 년도입니다. 다시 입력해 주세요.", color=0xEF746F)
        await ctx.send(embed=Title)
    elif not month.isdigit():
        Title = discord.Embed(title="잘못된 월입니다. 다시 입력해 주세요.", color=0xEF746F)
        await ctx.send(embed=Title)

@bot.command()
async def 도움(ctx):
    Title = discord.Embed(title="봇 사용법", color=0xEF746F)
    Des = discord.Embed(description="디데이 : ex) !디데이 2020 3 1 2020 4 21\n"
                                    "달력 : ex) !달력 2020\n"
                                    "메모 : ex) !메모 내용(띄어쓰기도 포함 가능)\n"
                                    "날짜 : ex) !날짜 2020 3", color=0xEF746F)
    await ctx.send(embed=Title)
    await ctx.send(embed=Des)




bot.run("")


