import discord
from Weather import Weather
from discord.ext import commands, tasks

# Stores the weather objects
weatherObjects = []

# Creates the client variable and sets a prefix to !
client = commands.Bot(command_prefix='!', status="Weatherman")


@client.command()
async def display(ctx, *args):
    """
    Receives arguments for the time and temperature and displays it through a graph
    The graph it saved as an image and sent to the discord channel
    """
    # By default adds time 0:00 so if theres a single temperature it shows a line rather than a point
    times = ["0:00"]
    times.extend(args[0].split(","))

    # Converts temperatures into floats
    temperature = args[1].split(",")
    temperature.insert(0, temperature[0])
    temperature = list(map(float, temperature))

    # Creates a weather object to store the graph
    weather = Weather(times, temperature, " ".join(args[2:]))
    weatherObjects.append(weather)

    # Sends the graph to the channel
    message = await ctx.send(file=discord.File(f"{weather.name}.png"))
    weather.set_msg_id(message.id)


@client.command()
async def update(ctx, *args):
    """
    Adds points to a pre-existing graph
    """

    # Takes in arguments for time, temperature and the name
    time = args[0]
    temperature = float(args[1])
    name = " ".join(args[2:])

    # Checks if the name matches any of the given objects
    for obj in weatherObjects:
        if name == obj.name:
            # Updates the plot and sends it to the channel
            obj.update_plot(time, temperature)

            # Gets the previous graph and deletes it
            message = await ctx.channel.fetch_message(obj.msgId)
            await message.delete()

            # Sends the updated graph
            updated_msg = await ctx.send(file=discord.File(f"{obj.name}.png"))
            obj.set_msg_id(updated_msg.id)
            break

# Runs the bot with the given token
client.run("OTMzMTU0NTQ3OTE0OTI0MDQy.YedZ5Q.ZSyjfjon8zaA75QUFDAZvkHvW-0")
